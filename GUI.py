from os import error
import tkinter as tk   
from tkinter import ttk
import tkinter
from typing import Type 
import pkin
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.geometry("%dx%d" % (380, 500))

    def create_widgets(self):
        Label = tkinter.Label(self, text='#Neutrons')
        Label.grid(column=1, row=0)
        Label = tkinter.Label(self, text='ElementName')
        Label.grid(column=2, row=0)
        Label = tkinter.Label(self, text='Z')
        Label.grid(column=3, row=0)
        Label = tkinter.Label(self, text='M')
        Label.grid(column=4, row=0)
        
        #self.z1 = tk.Button(self)
        #self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        #self.z1.pack(side="top")
        self.labels = [('optionmenu', 'element1;He'), ('optionmenu', 'element2;Fe'), ('input', 'theta;170'), ('input', 'energy;1.5'), ('text', 'output:'), ('text', 'output:')]
        self.inputs = []
        self.output = {}
        self.index = 1
        self.outputLabels = []
        OPTIONS = pkin.Data.elements[0:93]
        self.E_info = []
        for index, (type, text) in zip(range(self.index, len(self.labels)),self.labels):
            try:
                text, standard = text.split(';')
            except:
                standard = None
            if type == 'optionmenu':
                
                variable = tk.StringVar(self)
                variable.set(standard)
                variable.trace("w", self.calculate)
                label = tk.Label(self,text=text+':')
                label.grid(row=index,column=0)
                option = ttk.Combobox(self, values=OPTIONS, textvariable=variable, width=5)
                option.grid(row=index, column=2)
                option.bind("<<ComboboxSelected>>", self.calculate)
                entry = tk.Entry(self, width=5)
                entry.bind('<KeyRelease>', self.calculate)
                entry.grid(row=index, column=1)
                self.inputs.append((variable, entry))
                str_var = tkinter.StringVar(self)
                #label = tkinter.Label(self, text=str_var)
                #label.grid(row=index, column=3)
                #self.E_info.append(str_var)
            if type == 'input':
                label = tk.Label(self,text=text+':')
                label.grid(row=index,column=0)
                inputLabel = tk.Entry(self, width=5)#, validate='focusout', validatecommand=self.calculate
                inputLabel.bind("<KeyRelease>", self.calculate)
                inputLabel.insert(0,standard)
                inputLabel.grid(row=index, column=1)
                self.inputs.append(inputLabel)
            else:
                label = tk.Label(self,text=text)
                label.grid(row=index,column=0)
        #self.calc = tk.Button(self, text="calculate",
        #                      command=self.calculate)
        #self.calc.grid(row=index,column=0)
        self.index = index+2
        self.calculate()
    def calculate(self, event=None, event2=None, event3=None):
        NEW_LINE = ['toflen']
        for label in self.outputLabels:
            label.destroy()
        params = []
        for inputLabel in self.inputs:
            try:
                params.append(inputLabel.get())
            except AttributeError:
                if inputLabel[1].get() != '':
                    param = inputLabel[1].get()+inputLabel[0].get()
                else:
                    param = inputLabel[0].get()
                print(param)
                params.append(param)
                
        try:
            output = pkin.pkin(params[0], params[1], params[2], params[3])
        except Exception as e:
            output = {'ERROR':e}
        for key, value in zip(output.keys(), output.values()):
            if key in ['z1', 'm1', 'z2', 'm2']:
                label = tk.Label(self,text=value)
                self.outputLabels.append(label)
                column = {'z1':3, 'm1':4, 'z2':3, 'm2':4}[key]
                label.grid(row=int(key[1]),column=column)
            else:
                print(key)
                try:
                    if len(value) == 2:
                        value = (round(value[0], 4), round(value[1], 4))
                    else:
                        if len(str(value)) > 4:
                            value = round(value, 4)
                except TypeError:
                    pass
                label = tk.Label(self,text=key+':')
                self.outputLabels.append(label)
                label.grid(row=self.index,column=0)
                label = tk.Label(self,text=value)
                self.outputLabels.append(label)
                label.grid(row=self.index,column=1)
                self.index += 1
                if key in NEW_LINE:
                    label = tk.Label(self,text='--')
                    self.outputLabels.append(label)
                    label.grid(row=self.index,column=1)
                    self.index += 1     
root = tk.Tk()
app = Application(master=root)
app.master.title('tkin (V1.5)')
app.mainloop()


#for index, y in enumerate(5,91,10,5,4,56)