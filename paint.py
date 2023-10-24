import tkinter as tk
from tkinter import ttk, colorchooser, messagebox


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Program")
        self.root.geometry("800x600")

        self.pen_color = "black"
        self.pen_size = 5
        self.shape = "line"

        self.create_menu()
        self.create_canvas()
        self.create_toolbar()

        self.canvas.bind("<B1-Motion>", self.draw)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_canvas)
        file_menu.add_command(label="Save", command=self.save_canvas)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menu_bar)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(expand=True, fill="both")

    def create_toolbar(self):
        self.toolbar = ttk.Frame(self.root)
        self.toolbar.pack(side="top", fill="x")

        color_button = ttk.Button(self.toolbar, text="Color", command=self.choose_color)
        color_button.pack(side="left", padx=5, pady=5)

        size_label = ttk.Label(self.toolbar, text="Size:")
        size_label.pack(side="left", padx=5, pady=5)

        self.size_spinbox = tk.Spinbox(self.toolbar, from_=1, to=10, width=2)
        self.size_spinbox.pack(side="left", padx=5, pady=5)

        shape_label = ttk.Label(self.toolbar, text="Shape:")
        shape_label.pack(side="left", padx=5, pady=5)

        self.shape_combo = ttk.Combobox(
            self.toolbar,
            values=["Line", "Rectangle", "Circle"],
            state="readonly",
            width=10,
        )
        self.shape_combo.pack(side="left", padx=5, pady=5)
        self.shape_combo.current(0)  # Select the first shape by default

        clear_button = ttk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side="left", padx=5, pady=5)

    def draw(self, event):
        x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
        x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)

        if self.shape == "line":
            self.canvas.create_line(x1, y1, x2, y2, fill=self.pen_color, width=self.pen_size)
        elif self.shape == "rectangle":
            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill=self.pen_color, outline="", width=self.pen_size
            )
        elif self.shape == "circle":
            self.canvas.create_oval(
                x1, y1, x2, y2, fill=self.pen_color, outline="", width=self.pen_size
            )

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose color")
        if color:
            self.pen_color = color[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def new_canvas(self):
        result = messagebox.askyesno("New Canvas", "Are you sure you want to start a new canvas?")
        if result == tk.YES:
            self.clear_canvas()

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.canvas.postscript(file=file_path, colormode="color")


root = tk.Tk()
paint_app = PaintApp(root)
root.mainloop()
