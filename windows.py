import tkinter
from tkinter import ttk
from scripts import *


class GUI:
    def __init__(self, root):
        self.root = root

        self.root.geometry("600x600+500+300")
        self.root.title("Simple-Website-Creator")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky="nesw")

        for n in range(0, self.mainframe.grid_size()[0]):
            self.mainframe.columnconfigure(n, weight=1)
        for n in range(0, self.mainframe.grid_size()[1]):
            self.mainframe.rowconfigure(n, weight=1)

        self.gui_title = ttk.Label(self.mainframe, text="Please fill out the following to create your file.",
                                   relief="solid", anchor="center", padding=5)
        self.gui_title.grid(column=0, row=0, sticky="new", pady=10, padx=10, columnspan=3)
        self.gui_title.grid_anchor("center")
        self.placeholder = ttk.Label(self.mainframe, text="Placeholder, delete text and background", background="red")
        self.placeholder.grid(column=0, row=1, columnspan=3, pady=5, sticky="n")

        self.css_frame = ttk.Labelframe(self.mainframe, text="Do you want to integrate a CSS Stylesheet?", padding=5)
        self.css_frame.grid(column=0, row=2, pady=10, padx=10)
        self.radio_css_yes = ttk.Radiobutton(self.css_frame, text="Yes")
        self.radio_css_yes.grid(column=0, row=0, sticky="e")
        self.radio_css_no = ttk.Radiobutton(self.css_frame, text="No")
        self.radio_css_no.grid(column=1, row=0, sticky="w")

        self.title_labelframe = ttk.LabelFrame(self.mainframe, text="Title (shown in browser tab):", padding=5)
        self.title_labelframe.grid(column=1, row=2, pady=10, padx=10)
        self.title_entry = ttk.Entry(self.title_labelframe, width=40)
        self.title_entry.grid()

        self.headline_labelframe = ttk.LabelFrame(self.mainframe, text="The Headline for your Website:", padding=5)
        self.headline_labelframe.grid(column=0, row=3, sticky="n")
        self.headline_entry = ttk.Entry(self.headline_labelframe, width=40)
        self.headline_entry.grid()

        self.text_frame = ttk.Frame(self.mainframe, relief="sunken", padding=5)
        self.text_frame.grid(column=1, row=3)
        self.content_text = ttk.Label(self.text_frame, wraplength=250,
                                      text="Here goes your main Website content.\n"
                                           "For better results, it is highly encouraged to write your content "
                                           "externally and copy the written text in an 'Editor'-File (.txt). "
                                           "Then place the file in the same folder as this program and write the "
                                           "name of the file in here (e.g. 'example.txt').")
        self.content_text.grid()
        self.content_entry = ttk.Entry(self.text_frame)
        self.content_entry.grid()

        self.submit_button = ttk.Button(self.mainframe, text="Submit",
                                        command=self.invoke_scripts)
        self.submit_button.grid(column=int(self.mainframe.grid_size()[0]/2), row=self.mainframe.grid_size()[1]+1)

    def invoke_scripts(self):
        create_html(self.title_entry.get(), self.headline_entry.get(), self.content_entry.get())
