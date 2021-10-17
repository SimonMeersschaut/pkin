from tkinter import *
import pkin
import matplotlib.pyplot as plt


def start_graph(info):
    root = Tk()

    # Basically Links Any Radiobutton With The Variable=i.
    selected_radio = IntVar()
    r1 = Radiobutton(root, text="Element1", value=0, variable=selected_radio)
    r2 = Radiobutton(root, text="Element2", value=1, variable=selected_radio)
    r3 = Radiobutton(root, text="Theta", value=2, variable=selected_radio)
    r4 = Radiobutton(root, text="energy", value=3, variable=selected_radio)

    def plot():
        graph_data = []
        i = 0
        while i < 1000:
            i += 1
            try:
                data[selected_radio.get()] = i
                response = list(
                    pkin.pkin(data[0], data[1], data[2], data[3]).values())
                if type(response) != list:
                    response = [response]
                graph_data.append(response)
            except:
                break
        lines = [[] for i in range(max([len(vert) for vert in graph_data]))]
        for vertical in graph_data:
            for i, point in enumerate(vertical):
                if type(point) == tuple:
                    point = point[0]
                lines[i].append(point)
        for line in lines:

            plt.plot(range(len(line)), line)
        plt.show()

    button = Button(root, command=plot, text="plot")

    r1.pack(anchor=W)
    r2.pack(anchor=W)
    r3.pack(anchor=W)
    r4.pack(anchor=W)
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    import sys
    from json import loads
    data = sys.argv[1:]
    start_graph(data)
