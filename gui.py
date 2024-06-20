import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000

class Root_Wrapper():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.screens = {}
        self.current_screen = None
        self.root.protocol("WM_DELETE_WINDOW", self.on_close) 
    
    def add_screen(self, screen_key):
        self.screens[screen_key] = Screen(self)
    
    def switch_screen(self, screen_key):
        if self.current_screen:
            self.screens[self.current_screen].frame.pack_forget()
        self.screens[screen_key].frame.pack(fill="both", expand=1)
        self.current_screen = screen_key
    
    def on_close(self):
        # self.root.destroy() 
        sys.exit() 

class Screen():
    def __init__(self, rootw):
        self.rootw = rootw
        self.frame = tk.Frame(self.rootw.root)
        self.buttons = {}
        self.graphs = {}
    
    def add_button(self, **options):
        x = options.pop("x")
        y = options.pop("y")
        button = tk.Button(self.frame, **options)
        button.place(x=x, y=y)
        self.buttons[options["name"]] = button
    
    def add_graph(self, **options):
        fig, ax = plt.subplots(figsize=(options["width"], options["height"]))
        ax.plot(options["datax"], options["datay"])
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=options["x"], y=options["y"])
        self.graphs[options["name"]] = canvas

rootw = Root_Wrapper()
rootw.add_screen("screen1")
rootw.add_screen("screen2")

rootw.screens["screen1"].add_button(name="button1", text="Click me!", bg="blue", fg="white", font=("Arial", 12), width=2, height=2, x=175, y=370)
rootw.screens["screen1"].add_graph(name="graph1", datax=[1, 2, 3, 4, 5], datay=[1, 2, 3, 4, 5], width=2, height=2, x=50, y=50)
rootw.screens["screen1"].buttons["button1"].config(command=lambda: rootw.switch_screen("screen2"))

rootw.screens["screen2"].add_button(name="button2", text="yaya", bg="blue", fg="white", font=("Arial", 12), width=2, height=2, x=175, y=370)

rootw.switch_screen("screen1")
rootw.root.mainloop()




