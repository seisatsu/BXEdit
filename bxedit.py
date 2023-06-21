from tkinter import *
from PIL import ImageTk, Image


# Thanks to https://pythonguis.com/tutorials/create-gui-tkinter/
# Thanks to https://stackoverflow.com/a/55642085


topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
rect_text_display = None


def get_mouse_posn(event):
    global topx, topy

    topx, topy = event.x, event.y


def update_sel_rect(event):
    global rect_id, rect_text_display
    global topx, topy, botx, boty

    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)

    rect_text = "[{0}, {1}, {2}, {3}]".format(topx, topy, botx, boty)
    rect_text_display = Label(left_frame, text=rect_text, relief=SUNKEN, bg="#BBBBBB").grid(row=3, column=1, padx=5, pady=3, sticky=W)


def load_room():
    pass


def save_room():
    pass


def choose_image():
    pass


root = Tk()
root.title("BXEdit")
#root.config(bg='lightgrey')

# Create Left and Right Frames
left_frame = Frame(root, width=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Load an Image
image = ImageTk.PhotoImage(Image.open("room01.jpg"))
canvas = Canvas(right_frame, width=image.width(), height=image.height(), borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=0, padx=5, pady=5)
canvas.img = image
canvas.create_image(0, 0, image=image, anchor=NW)

# Create Selection Rectangle
rect_id = canvas.create_rectangle(topx, topy, topx, topy, dash=(2,2), fill="", outline="white")
canvas.bind("<Button-1>", get_mouse_posn)
canvas.bind("<B1-Motion>", update_sel_rect)

# Display Image in Right Frame
#Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)

# Create Data Entry Frame
load_button = Button(left_frame, text="Load", command=load_room).grid(row=0, column=0, padx=5, pady=3)
save_button = Button(left_frame, text="Save", command=save_room).grid(row=0, column=1, padx=5, pady=3, sticky=W)
title_label = Label(left_frame, text="Title").grid(row=1, column=0, padx=5, pady=3)
title_entry = Entry(left_frame).grid(row=1, column=1, padx=5, pady=3)
image_label = Label(left_frame, text="Image").grid(row=2, column=0, padx=5, pady=3)
image_path = Label(left_frame, text="Image Path", relief=SUNKEN, bg="#BBBBBB").grid(row=2, column=1, padx=5, pady=3, sticky=W)
image_choose_button = Button(left_frame, text="Choose Image", command=choose_image).grid(row=2, column=2, padx=5, pady=3)
rect_label = Label(left_frame, text="Rect").grid(row=3, column=0, padx=5, pady=3)
rect_text_display = Label(left_frame, text="[,,,,]", relief=SUNKEN, bg="#BBBBBB").grid(row=3, column=1, padx=5, pady=3, sticky=W)


root.mainloop()



