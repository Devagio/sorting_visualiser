from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

from bubble import bubble_sort
from quick import quick_sort
from merge import merge_sort
from insertion import insertion_sort
from selection import selection_sort


# Initializing
root = Tk()
root.title("Sorting Algorithm Visualiser")
root.maxsize(900, 600)
root.config(bg="black")


# Variables
radio_var = IntVar()
data = []
font = "helvetica 10 bold"
algorithm_list = ["Insertion Sort",
                  "Bubble Sort",
                  "Selection Sort",
                  "Merge Sort",
                  "Quick Sort"]


# functions
def draw(array, color_array):
    canvas.delete("all")

    n = len(array)
    c_height = 380
    c_width = 600
    spacing = max(int(c_width/(n+2)/4), 1)
    x_width = (c_width - spacing) / (n + 2)
    offset = x_width

    data_max = max(array)
    norm = [val / data_max for val in array]
    for i, height in enumerate(norm):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height

        # drawing bars
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        # labelling bars if there is enough space
        if n < 50:
            canvas.create_text((x0+x1)/2, y0, anchor=S, text=str(data[i]))

    root.update_idletasks()


def generate():
    global data
    rand_val = radio_var.get()

    min_val = int(minScale.get())
    max_val = int(maxScale.get())

    if min_val > max_val:
        messagebox.showinfo("Range Flip", "The Min Value you entered was greater than the Max Value you entered.\n"
                                          "Flipping those Values to generate data.")
        min_val, max_val = max_val, min_val

    if rand_val == 1:
        size = int(sizeScale.get())
        data = []
        for _ in range(size):
            data.append(random.randrange(min_val, max_val + 1))

    else:
        data = []
        for i in range(min_val, max_val+1):
            data.append(i)
        random.shuffle(data)

    draw(data, ["red" for _ in range(len(data))])


def start_alg():
    global data
    if len(data) == 0:
        messagebox.showwarning("Data Not Found", "You need to generate data before starting the sort.")
        return

    if algMenu.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, draw, speedScale.get())
    elif algMenu.get() == "Bubble Sort":
        bubble_sort(data, draw, speedScale.get())
    elif algMenu.get() == "Merge Sort":
        merge_sort(data, draw, speedScale.get())
    elif algMenu.get() == "Insertion Sort":
        insertion_sort(data, draw, speedScale.get())
    elif algMenu.get() == "Selection Sort":
        selection_sort(data, draw, speedScale.get())

    else:
        messagebox.showwarning("Algorithm Not Found", "Please pick a sorting algorithm from the drop-down menu.")
        return

    draw(data, ["green" for _ in range(len(data))])


# Frame / Base layout
UI_frame = Frame(root, width=600, height=200, bg="#83C8FF")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="#DADADA")
canvas.grid(row=1, column=0, padx=10, pady=5)


# User interface area
# Row[0]
Label(UI_frame, text="Algorithm: ", bg="#83C8FF", font=font).grid(row=3, column=2, padx=5, pady=5, sticky=E)
algMenu = ttk.Combobox(UI_frame, values=algorithm_list, font=font, state='readonly')
algMenu.grid(row=3, column=3, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.01, to=0.50, length=200, digits=2, font=font, bg="#0024E1", fg="white",
                   troughcolor="#001582", resolution=0.01, orient=HORIZONTAL, label="Select Delay [in seconds]")
speedScale.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
Button(UI_frame, text="Start", command=start_alg, bg="green", font=font).grid(row=3, column=4, padx=5, pady=5)


# Row[1] and Row[2]

sizeScale = Scale(UI_frame, from_=1, to=99, resolution=1, orient=HORIZONTAL, label="Data Size", length=200,
                  state="normal", font=font, troughcolor="#A9B30A", bg="#ECF828")
sizeScale.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

notRandom = Radiobutton(UI_frame, text="Uniform Values", variable=radio_var, value=0, font=font, bg="#ECF828",
                        command=lambda: sizeScale.config(state="disabled", label="Data Size (disabled)"))
notRandom.grid(row=1, column=2, padx=5, pady=5)

yesRandom = Radiobutton(UI_frame, text="Random Values", variable=radio_var, value=1, font=font, bg="#ECF828",
                        command=lambda: sizeScale.config(state="normal", label="Data Size"))
yesRandom.grid(row=1, column=3, padx=5, pady=5)

yesRandom.select()

minScale = Scale(UI_frame, from_=1, to=99, resolution=1, orient=HORIZONTAL, label="Data Min", font=font,
                 bg="#FF62F0", fg="white", troughcolor="#8A0A7E")
minScale.grid(row=1, column=0, padx=5, pady=5, rowspan=2)

maxScale = Scale(UI_frame, from_=1, to=99, resolution=1, orient=HORIZONTAL, label="Data Max", font=font,
                 bg="#FF62F0", fg="white", troughcolor="#8A0A7E")
maxScale.grid(row=1, column=1, padx=5, pady=5, rowspan=2)

butt = Button(UI_frame, text="Generate", command=generate, bg="red", font=font)
butt.grid(row=1, column=4, padx=5, pady=5, rowspan=2)


root.mainloop()
