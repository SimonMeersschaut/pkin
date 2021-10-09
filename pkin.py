from typing import Union
from json import load
from sys import argv
from math import pi, sin, asin, sqrt, cos

INTEGERS = '0123456789'
C_DEG = pi/180.0
P_C = 299792458
P_E = 1.60217733e-19
P_EPS0 = 8.85419e-12
C_U = 1.6605402e-27  # Atomic mass to kilograms
C_EV = P_E           # eV to J
C_BARN = 1.0E-28     # barn
C_MEV = (1.0e6*C_EV)
C_NS = 1.0e-9
C_CM = 1.0e-2
TOFLEN = 0.75541


def pkin(z1: Union[int, str], z2: Union[int, str], Theta_Deg: float, E_MeV: float) -> tuple:
    """
    Calculates energies, time-of-flight and scattering cross section of an elastic scattering

    Parameters:
      element1:  First element described by element name (He), element index (2) or isotope + elementName (6He)
      element2:  Second element described by ''
      Theta_Deg: Angle of collision
      E_MeV:     Energy of collision

    Return:
      {
          'z1':index of element 1,
          'm1':mass of element 1,
          'z2':index of element2,
          'm2':mass of element2,
          'theta':angle in radians,
          'toflen':toflen,
          #TODO all outputs
      }

    example: pkin('He', '13C', 15.0, 6.0) -> {'z1': 2, 'm1': 4.003, 'z2': 6, 'm2': 12.011, 'theta': 0.2617993877991494, 'toflen': 0.75541, 'RBS_E': 5.865011744134161, 'RBS_tof': 44.92576588216547, 'RBS_sigma': 17.857740230704632, 'ERD_E': 4.198207562799662, 'ERD_tof': 91.98028856469045, 'ERD_sigma': 0.040899099172101536}
    """
    z1, m1 = GetMass(z1)
    z2, m2 = GetMass(z2)
    try:
        Theta_Deg = float(Theta_Deg)
        E_MeV = float(E_MeV)
    except ValueError:
        raise ValueError('theta or E_MeV was not given as a float or int')
    m1 *= C_U
    m2 *= C_U
    Theta = Theta_Deg * C_DEG
    E = E_MeV*C_MEV
    Ecm = m2*E/(m1+m2)
    erd = Theta < pi/2
    tcm = cm_angle(Theta, m1/m2)
    n = len(tcm)
    results = {
        'z1': z1,
        'm1': m1/C_U,
        'z2': z2,
        'm2': m2/C_U,
        'theta': Theta,
        'toflen': TOFLEN
    }
    if n == 0:
        print('Scattered projectiles not detectable.\n\n')
    elif n == 1:
        RBS_E = E_MeV*Krbs(m1, m2, Theta, 0)
        RBS_tof = calc_tof(E*Krbs(m1, m2, Theta, 0), m1)/C_NS
        RBS_sigma = mc2lab_scatc(
            Srbs_mc(z1, z2, tcm[0], Ecm), tcm[0], Theta)/C_BARN
        results.update({
            'RBS_E': RBS_E,
            'RBS_tof': RBS_tof,
            'RBS_sigma': RBS_sigma
        })
    else:
        RBS_E = (E*Krbs(m1, m2, Theta, 0)/C_MEV,
                 E*Krbs(m1, m2, Theta, 1)/C_MEV)
        RBS_tof = (calc_tof(E*Krbs(m1, m2, Theta, 0), m1)/C_NS,
                   calc_tof(E*Krbs(m1, m2, Theta, 1), m1)/C_NS)
        RBS_sigma = (mc2lab_scatc(Srbs_mc(z1, z2, tcm[0], Ecm), tcm[0], Theta)/C_BARN, -mc2lab_scatc(
            Srbs_mc(z1, z2, tcm[1], Ecm), tcm[1], Theta)/C_BARN)
        results.update({
            'RBS_E': RBS_E,
            'RBS_tof': RBS_tof,
            'RBS_sigma': RBS_sigma
        })
    if erd:
        ERD_E = E*Kerd(m1, m2, Theta)/C_MEV
        ERD_tof = calc_tof(E*Kerd(m1, m2, Theta), m2)/C_NS
        ERD_sigma = 4*Srbs_mc(z1, z2, pi-2*Theta, Ecm)*cos(Theta)/C_BARN
        results.update({
            'ERD_E': ERD_E,
            'ERD_tof': ERD_tof,
            'ERD_sigma': ERD_sigma
        })
    else:
        results.update({
            "recoiled atoms": 'not detectable'
        })
        print('Recoiled target atoms not detectable')
    #print(n, a, erd, Ecm, Theta)
    # (element1, element1_mass, element2, element2_mass, E_MeV, Theta, RBS_E, RBS_tof, RBS_sigma, ERD_E, ERD_tof, ERD_sigma)
    return results


def mc2lab_scatc(mcs, tcm, t):
    return mcs*((sin(tcm)/sin(t))**2)/cos(tcm-t)


def Srbs_mc(z1, z2, t, E):
    return ((z1*z2*P_E**2)/(4*pi*P_EPS0))**2*(1/(4*E))**2*(1/sin(t/2))**4


def calc_tof(energy, mass):
    try:
        return TOFLEN/sqrt(2*energy/mass)
    except ZeroDivisionError:
        return float('inf')


def cm_angle(lab_angle, r):
    a = []
    if r > 1 and sin(lab_angle) > 1/r:
        return a
    stmp = asin(r*sin(lab_angle))
    if r > 1:
        a.append(lab_angle + stmp)
        a.append(pi + lab_angle - stmp)
        return a
    else:
        a.append(lab_angle + stmp)
        return a


def Krbs(m1, m2, t, n):
    # print('t',t)
    # print('m1',m1)
    # print('m2',m2)
    sq_tmp = sqrt(m2**2 - (m1*sin(t))**2)
    # print(sq_tmp)
    if m1 > m2:
        if n == 0:
            return ((sq_tmp + m1*cos(t)) / (m1 + m2))**2
        else:
            return ((-sq_tmp + m1*cos(t)) / (m1 + m2))**2
    else:
        return ((sq_tmp + m1*cos(t)) / (m1 + m2))**2


def Kerd(m1, m2, t):
    return 4*m1*m2*(cos(t))**2/(m1+m2)**2


def GetMass(element):
    # check if there's an integer in the description of the element
    if any([(letter in INTEGERS) for letter in str(element)]):
        try:
            # check if the element was written using the index
            element = int(element)
            try:
                return (element, float(Data.natural[element-1]))
            except IndexError:
                raise ValueError('Element was not found')
        except ValueError:  # element was described by the name and the isotope
            elementName = ''.join(
                [letter for letter in str(element) if letter not in INTEGERS])
            isotopeNumber = int(
                ''.join([number for number in str(element) if number in INTEGERS]))
            element = int(getElementIndexByName(elementName))
            isotopes = getIsotopes(elementName)
            for isotope in isotopes:
                if int(isotope[2]) == isotopeNumber:
                    return (element, float(isotope[4])/1e6)
            raise ValueError('the given isotope was not found.')  # ! opgepast
    else:  # element was described by name only
        element = int(getElementIndexByName(element))
        return (element, float(Data.natural[element-1]))


def getIsotopes(name):
    # get all isotopes of element
    return [isotope for isotope in Data.data if isotope[3] == name]


def getElementIndexByName(name):
    for isotope in Data.data:
        if isotope[3] == name:
            return isotope[1]
    raise ValueError('Element was not found')


def print_values(dict):
    new_line = ['toflen', 'RBS_sigma']
    for key, value in zip(dict.keys(), dict.values()):
        x = ''.join([' ' for x in range(12-len(key))])
        if type(value) == tuple:
            print(f'{key}:{x}{value[0]:12.4f}   {value[1]:12.4f}')
        else:
            print(f'{key}:{x}{value:12.4f}')
        if key in new_line:
            print()

# class Files:
#  with open('natural.json', 'r') as f:
#    natural = load(f)
#  with open('data.json', 'r') as f:
#    data = load(f)


def main():
    try:
        _, element1, element2, Theta_Deg, E_MeV = argv
        data = pkin(element1, element2, float(Theta_Deg), float(E_MeV))
        print_values(data)
    except ValueError:
        print
        ('''PARAMETERS:
  -element1
  -element2
  -Theta(deg)
  -E(MeV)''')


class Data:
    natural = [1.008, 4.003, 6.941, 9.012, 10.811, 12.011, 14.007, 15.999, 18.998, 20.18, 22.99, 24.305, 26.982, 28.086, 30.974, 32.066, 35.453, 39.948, 39.098, 40.08, 44.956, 47.9, 50.942, 51.996, 54.938, 55.847, 58.933, 58.69, 63.546, 65.39, 69.72, 72.61, 74.922, 78.96, 79.904, 83.8, 85.47, 87.62, 88.905, 91.22, 92.906, 95.94, 97.0, 101.07, 102.91, 106.4,
               107.87, 112.4, 114.82, 118.71, 121.75, 127.6, 126.9, 131.3, 132.91, 137.327, 138.91, 140.12, 140.91, 144.24, 148.0, 150.36, 151.97, 157.25, 158.93, 162.5, 164.93, 167.26, 168.93, 173.04, 174.97, 178.49, 180.95, 183.85, 186.2, 190.2, 192.2, 195.08, 196.97, 200.59, 204.38, 207.19, 208.98, 210.0, 210.0, 222.0, 223.0, 226.0, 227.0, 232.0, 231.0, 238.03]
    with open('data.json', 'r') as f:
        data = load(f)
    isotopes = {

    }
    elements = []
    for isotope in data:
        if not isotope[3] in elements:
            elements.append(isotope[3])
    print(elements)
    for isotope in data:
        try:
            isotopes[isotope[0]].append(isotope[1])
        except KeyError:
            isotopes.update({isotope[0]: [isotope[1]]})


if __name__ == '__main__':
    main()
