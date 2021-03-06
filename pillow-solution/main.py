import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('1920x1080')

canvas = tk.Canvas(root)
vsb = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
hsb = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
canvas.config(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

canvas.grid(row=0, column=0, sticky='nsew')
vsb.grid(row=0, column=1, sticky='ns')
hsb.grid(row=1, column=0, sticky='ew')

image = Image.open('cours10.png')
image_resized = image.resize((3000, 3000))

img = ImageTk.PhotoImage(image_resized)
bgimg = canvas.create_image(0, 0, image=img, anchor=tk.NW)
print(img.height, img.width)
canvas.config(width=1920, height=1080, scrollregion=(0, 0, img.width(), img.height()))

def scroll_horizontal(dx):
  canvas.xview_scroll(dx, 'units')

def scroll_vertical(dy):
  canvas.yview_scroll(dy, 'units')

canvas.bind('<MouseWheel>', lambda e: scroll_vertical(-e.delta//120))
canvas.bind('<Button-1>', lambda e: canvas.focus_set())

canvas.bind('<Up>', lambda e: scroll_vertical(-1))
canvas.bind('<Down>', lambda e: scroll_vertical(+1))
canvas.bind('<Left>', lambda e: scroll_horizontal(-1))
canvas.bind('<Right>', lambda e: scroll_horizontal(+1))

# if using bind_all, no need to call canvas.focus_set()
canvas.focus_set() # canvas must be focused to receive keyboard events

root.mainloop()