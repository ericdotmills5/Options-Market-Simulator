from gui_class import Root_Wrapper

if __name__ == "__main__":
    rootw = Root_Wrapper()
    rootw.add_screen("screen1")
    rootw.add_screen("screen2")

    rootw.screens["screen1"].add_button(name="button1", text="Click me!", bg="blue", fg="white", font=("Arial", 12), width=2, height=2, x=175, y=370)
    rootw.screens["screen1"].add_graph(name="graph1", datax=[1, 2, 3, 4, 5], datay=[1, 2, 3, 4, 5], width=2, height=2, x=50, y=50)
    rootw.screens["screen1"].buttons["button1"].config(command=lambda: rootw.switch_screen("screen2"))

    rootw.screens["screen2"].add_button(name="button2", text="yaya", bg="blue", fg="white", font=("Arial", 12), width=2, height=2, x=175, y=370)

    rootw.switch_screen("screen1")
    rootw.root.mainloop()