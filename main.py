import tkinter as tk

global main_canvas


def clear():
    main_canvas.delete("all")


def line():
    main_canvas.configure(cursor="pencil")


def rect():
    main_canvas.configure(cursor="plus")


def oval():
    pass


def caption():
    pass


def fill():
    pass


def image():
    pass


def freehand():
    pass


def eraser():
    pass


def line_color():
    pass


def fill_color():
    pass


def quit(root):
    root.quit()


def main():
    global main_canvas
    root = tk.Tk()
    root.title("MiniPaint")
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{width}x{height}+0+0")

    buttons_frame = tk.Frame(root, height=height, width=200, borderwidth=5, relief=tk.GROOVE)
    main_canvas = tk.Canvas(root, height=height, width=width - 200, bg="white", cursor="top_left_arrow")
    buttons_frame.pack(side=tk.LEFT)
    buttons_frame.pack_propagate(0)
    main_canvas.pack(side=tk.RIGHT)

    clear_button = tk.Button(buttons_frame, text="Clear", width=200, command=clear)
    line_button = tk.Button(buttons_frame, text="Line", width=200, command=line)
    rect_button = tk.Button(buttons_frame, text="Rect", width=200, command=rect)
    oval_button = tk.Button(buttons_frame, text="Oval", width=200)
    caption_label = tk.Label(buttons_frame, text="Caption")
    cation_entry = tk.Entry(buttons_frame)
    fill_button = tk.Button(buttons_frame, text="Fill", width=200)
    image_button = tk.Button(buttons_frame, text="Image", width=200)
    freehand_button = tk.Button(buttons_frame, text="Freehand", width=200)
    eraser_button = tk.Button(buttons_frame, text="Eraser", width=200)
    line_color_button = tk.Button(buttons_frame, text="Line Color", width=200, bg="yellow")
    fill_color_button = tk.Button(buttons_frame, text="Fill Color", width=200, bg="red")
    line_width_label = tk.Label(buttons_frame, text="Line Width")
    line_width_slider = tk.Scale(buttons_frame, from_=1, to=19, orient=tk.HORIZONTAL, length=200)
    text_size_label = tk.Label(buttons_frame, text="Text Size")
    text_size_slider = tk.Scale(buttons_frame, from_=8, to=24, orient=tk.HORIZONTAL, length=200)
    quit_button = tk.Button(buttons_frame, text="Quit", width=200, command=lambda: quit(root))

    clear_button.pack(pady=(50, 3), anchor=tk.W)
    line_button.pack(pady=3, anchor=tk.W)
    rect_button.pack(pady=3, anchor=tk.W)
    oval_button.pack(pady=3, anchor=tk.W)
    caption_label.pack(pady=2, anchor=tk.W)
    cation_entry.pack(pady=3, anchor=tk.W)
    fill_button.pack(pady=3, anchor=tk.W)
    image_button.pack(pady=3, anchor=tk.W)
    freehand_button.pack(pady=3, anchor=tk.W)
    eraser_button.pack(pady=3, anchor=tk.W)
    line_color_button.pack(pady=3, anchor=tk.W)
    fill_color_button.pack(pady=3, anchor=tk.W)
    line_width_label.pack(pady=1, anchor=tk.W)
    line_width_slider.pack(pady=3, anchor=tk.W)
    text_size_label.pack(pady=1, anchor=tk.W)
    text_size_slider.pack(pady=3, anchor=tk.W)
    quit_button.pack(pady=3, anchor=tk.W)

    root.mainloop()


if __name__ == '__main__':
    main()
