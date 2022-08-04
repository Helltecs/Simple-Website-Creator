from tkinter import ttk
import scripts as s


class GUI:
    def __init__(self, root):
        self.root = root

        self.root.geometry("920x600")
        self.root.title("Simple-Website-Creator")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky="nesw")
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.title = ttk.Label(self.mainframe, text="Please fill out the following to create your file.",
                               relief="solid", anchor="center", padding=5)
        self.title.grid(column=0, row=0, sticky="n", pady=10)
        self.title.grid_anchor("center")
        self.placeholder = ttk.Label(self.mainframe, text="Placeholder, delete text", background="red")
        self.placeholder.grid(column=0, row=1, columnspan=3, pady=5, sticky="n")

        self.css_frame = ttk.LabelFrame(self.mainframe, text="Do you want to integrate a CSS Stylesheet?")
        self.css_frame.grid(column=0, row=2)
        self.radio_css_yes = ttk.Radiobutton(self.css_frame, text="Yes")
        self.radio_css_yes.grid(column=0, row=0, sticky="nw")
        self.radio_css_no = ttk.Radiobutton(self.css_frame, text="No")
        self.radio_css_no.grid(column=1, row=0, sticky="nw")
