import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk


class mainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MiniPaint")
        width, height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{width}x{height}+0+0")

        self.buttons_frame = tk.Frame(self, height=height, width=200, borderwidth=5, relief=tk.GROOVE)
        self.main_canvas = tk.Canvas(self, height=height, width=width - 200, bg="white", cursor="top_left_arrow")
        self.buttons_frame.pack(side=tk.LEFT)
        self.buttons_frame.pack_propagate(0)
        self.main_canvas.pack(side=tk.RIGHT)
        self.create_widgets()
        self.line_color = "red"
        self.fill_color = "white"
        self.fill_state = True

    def create_widgets(self):
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", width=200, command=self.clear)
        self.line_button = tk.Button(self.buttons_frame, text="Line", width=200, command=self.line)
        self.rect_button = tk.Button(self.buttons_frame, text="Rect", width=200, command=self.rect)
        self.oval_button = tk.Button(self.buttons_frame, text="Oval", width=200, command=self.oval)
        self.caption_label = tk.Label(self.buttons_frame, text="Caption")
        self.caption_entry = tk.Entry(self.buttons_frame)
        self.fill_button = tk.Button(self.buttons_frame, text="Fill", width=200, command=self.fill)
        self.image_button = tk.Button(self.buttons_frame, text="Image", width=200, command=self.image)
        self.freehand_button = tk.Button(self.buttons_frame, text="Freehand", width=200, command=self.freehand)
        self.eraser_button = tk.Button(self.buttons_frame, text="Eraser", width=200, command=self.eraser)
        self.line_color_button = tk.Button(self.buttons_frame, text="Line Color", width=200, bg="red",
                                           command=self.line_colorcode)
        self.fill_color_button = tk.Button(self.buttons_frame, text="Fill Color", width=200, bg="white",
                                           command=self.fill_colorcode)
        self.line_width_label = tk.Label(self.buttons_frame, text="Line Width")
        self.line_width_slider = tk.Scale(self.buttons_frame, from_=1, to=19, orient=tk.HORIZONTAL, length=200)
        self.text_size_label = tk.Label(self.buttons_frame, text="Text Size")
        self.text_size_slider = tk.Scale(self.buttons_frame, from_=8, to=24, orient=tk.HORIZONTAL, length=200)
        self.quit_button = tk.Button(self.buttons_frame, text="Quit", width=200, command=quit)

        self.clear_button.pack(pady=(50, 3), anchor=tk.W)
        self.line_button.pack(pady=3, anchor=tk.W)
        self.rect_button.pack(pady=3, anchor=tk.W)
        self.oval_button.pack(pady=3, anchor=tk.W)
        self.caption_label.pack(pady=2, anchor=tk.W)
        self.caption_entry.pack(pady=3, anchor=tk.W)
        self.fill_button.pack(pady=3, anchor=tk.W)
        self.image_button.pack(pady=3, anchor=tk.W)
        self.freehand_button.pack(pady=3, anchor=tk.W)
        self.eraser_button.pack(pady=3, anchor=tk.W)
        self.line_color_button.pack(pady=3, anchor=tk.W)
        self.fill_color_button.pack(pady=3, anchor=tk.W)
        self.line_width_label.pack(pady=1, anchor=tk.W)
        self.line_width_slider.pack(pady=3, anchor=tk.W)
        self.text_size_label.pack(pady=1, anchor=tk.W)
        self.text_size_slider.pack(pady=3, anchor=tk.W)
        self.quit_button.pack(pady=3, anchor=tk.W)

    def on_move(self, event):
        component = event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        w, h = self.main_canvas.winfo_width(), self.main_canvas.winfo_height()
        mx, my = component.winfo_width(), component.winfo_height()
        xpos = (locx + event.x) - (15)
        ypos = (locy + event.y) - int(my / 2)
        if xpos >= 0 and ypos >= 0 and w - abs(xpos) >= 0 and h - abs(ypos) >= 0 and xpos + mx <= w and ypos + my <= h:
            component.place(x=xpos, y=ypos)

    def on_button_press(self, event, func=None):
        self.start_x, self.start_y = event.x, event.y
        line_width = self.line_width_slider.get()

        if func == "rect":
            self.rectangle = self.main_canvas.create_rectangle(self.start_x, self.start_y, 1, 1, width=line_width,
                                                               outline=self.line_color, fill=self.fill_color)
        elif func == "line":
            self.line = self.main_canvas.create_line(self.start_x, self.start_y, 1, 1, fill=self.line_color,
                                                     width=line_width)

        elif func == "oval":
            self.oval = self.main_canvas.create_oval(self.start_x, self.start_y, 1, 1, width=line_width,
                                                     outline=self.line_color, fill=self.fill_color)

        elif func == "free":
            self.prev = event

    def on_button_release(self, event):
        pass

    def clear(self):
        self.main_canvas.delete("all")
        if self.image_label:
            self.image_label.place_forget()

    def drawline(self, event):
        current_x, current_y = event.x, event.y
        self.main_canvas.coords(self.line, self.start_x, self.start_y, current_x, current_y)

    def line(self):
        self.main_canvas.configure(cursor="pencil")
        self.main_canvas.bind("<ButtonPress-1>", lambda key: self.on_button_press(key, func="line"))
        self.main_canvas.bind("<B1-Motion>", self.drawline)
        self.main_canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def drawrect(self, event):
        current_x, current_y = event.x, event.y
        self.main_canvas.coords(self.rectangle, self.start_x, self.start_y, current_x, current_y)

    def rect(self):
        self.main_canvas.configure(cursor="plus")
        self.main_canvas.bind("<ButtonPress-1>", lambda key: self.on_button_press(key, func="rect"))
        self.main_canvas.bind("<B1-Motion>", self.drawrect)
        self.main_canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def drawoval(self, event):
        current_x, current_y = event.x, event.y
        self.main_canvas.coords(self.oval, self.start_x, self.start_y, current_x, current_y)

    def oval(self):
        self.main_canvas.configure(cursor="circle")
        self.main_canvas.bind("<ButtonPress-1>", lambda key: self.on_button_press(key, func="oval"))
        self.main_canvas.bind("<B1-Motion>", self.drawoval)
        self.main_canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def caption(self):
        pass

    def fill(self):
        if self.fill_state == True:
            self.ori_fill_color = self.fill_color[:]
            self.fill_color = None
            self.fill_color_button.configure(state=tk.DISABLED)
            self.fill_state = False
        elif self.fill_state == False:
            self.fill_color = self.ori_fill_color
            self.fill_color_button.configure(state=tk.NORMAL)
            self.fill_state = True

    def image(self):
        file = filedialog.askopenfilename(initialdir="/Pictures", title="Select an image",
                                          filetypes=(("JPG Files", "*.jpg"), ("PNG Files", "*.png"),
                                                     ("All Files", "*.*")))
        if file:
            image = ImageTk.PhotoImage(Image.open(file))
            self.image_label = tk.Label(self.main_canvas, image=image)
            self.image_label.image = image
            self.image_label.bind("<B1-Motion>", self.on_move)
            self.main_canvas.create_window(20, 20, anchor=tk.NW, window=self.image_label)

    def drawfree(self, event):
        current_x, current_y = event.x, event.y
        line_width = self.line_width_slider.get()
        self.main_canvas.create_line(self.prev.x, self.prev.y, current_x, current_y, fill=self.line_color,
                                     width=line_width)
        self.prev = event

    def freehand(self):
        self.main_canvas.configure(cursor="dot")
        self.main_canvas.bind("<ButtonPress-1>", lambda key: self.on_button_press(key, func="free"))
        self.main_canvas.bind("<B1-Motion>", self.drawfree)
        self.main_canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def drawerase(self, event):
        current_x, current_y = event.x, event.y
        line_width = self.line_width_slider.get()
        self.main_canvas.create_line(self.prev.x, self.prev.y, current_x, current_y, fill="white",
                                     width=line_width * 2)
        self.prev = event

    def eraser(self):
        self.main_canvas.configure(cursor="spraycan")
        self.main_canvas.bind("<ButtonPress-1>", lambda key: self.on_button_press(key, func="free"))
        self.main_canvas.bind("<B1-Motion>", self.drawerase)
        self.main_canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def line_colorcode(self):
        color = askcolor()[1]
        self.line_color_button.configure(bg=color)
        self.line_color = color

    def fill_colorcode(self):
        color = askcolor()[1]
        self.fill_color_button.configure(bg=color)
        self.fill_color = color


def main():
    app = mainApp()
    app.mainloop()


if __name__ == '__main__':
    main()
