import tkinter
from tkinter import ttk
from tkinter import colorchooser as cc
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

        self.lang_frame = ttk.LabelFrame(self.mainframe, text="What language does your Website has?", padding=5)
        self.lang_frame.grid(column=0, row=2, pady=10, padx=10)
        self.lang_selector = ttk.Combobox(self.lang_frame, values=["English-en", "German-de"], width=30,
                                          state="readonly")
        self.lang_selector.grid()

        self.css_frame = ttk.Labelframe(self.mainframe, text="Do you want to integrate a CSS Stylesheet?", padding=5)
        self.css_frame.grid(column=1, row=2, pady=10, padx=10)
        self.YesNo_variable = tkinter.IntVar()
        self.radio_css_yes = ttk.Radiobutton(self.css_frame, text="Yes", variable=self.YesNo_variable, value=1)
        self.radio_css_yes.grid(column=0, row=0, sticky="e")
        self.radio_css_no = ttk.Radiobutton(self.css_frame, text="No", variable=self.YesNo_variable, value=0)
        self.radio_css_no.grid(column=1, row=0, sticky="w")

        self.title_labelframe = ttk.LabelFrame(self.mainframe, text="Title (shown in browser tab):", padding=5)
        self.title_labelframe.grid(column=0, row=3, pady=10, padx=10)
        self.title_entry = ttk.Entry(self.title_labelframe, width=40)
        self.title_entry.grid()

        self.headline_labelframe = ttk.LabelFrame(self.mainframe, text="The Headline for your Website:", padding=5)
        self.headline_labelframe.grid(column=1, row=3)
        self.headline_entry = ttk.Entry(self.headline_labelframe, width=40)
        self.headline_entry.grid()

        self.text_frame = ttk.LabelFrame(self.mainframe, text="Here goes your main Website content.", relief="sunken",
                                         padding=5)
        self.text_frame.grid(column=0, row=4)
        self.content_text = ttk.Label(self.text_frame, wraplength=250,
                                      text="For better results, it is highly encouraged to write your content "
                                           "externally and copy the written text in an 'Editor'-File (.txt). "
                                           "Then place the file in the same folder as this program and write the "
                                           "name of the file in here (e.g. 'example.txt').")
        self.content_text.grid()
        self.content_entry = ttk.Entry(self.text_frame)
        self.content_entry.grid(pady=5)

        self.submit_button = ttk.Button(self.mainframe, text="Submit",
                                        command=self.invoke_scripts)
        self.submit_button.grid(column=int(self.mainframe.grid_size()[0] / 2), row=self.mainframe.grid_size()[1] + 1)

    def invoke_scripts(self):
        if self.YesNo_variable.get():
            CSSWindow()
        try:
            create_html(cut_lang(self.lang_selector.get()), self.title_entry.get(), css=self.YesNo_variable.get(),
                        headline=self.headline_entry.get(),
                        content=self.content_entry.get())
        except ValueError:
            WarningWindow(0)


class CSSWindow:
    def __init__(self):
        self.root = tkinter.Tk()

        self.root.geometry("600x600+100+100")
        self.root.title("Simple-Website-Creator: CSS")
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

        self.headline_frame = ttk.LabelFrame(self.mainframe, text="Configure your Headline:", padding=5)
        self.headline_frame.grid(column=0, row=2, columnspan=2)
        self.headline_align = tkinter.IntVar()
        self.headline_align.set(1)
        self.headline_align_str = "center"
        self.headline_left = ttk.Radiobutton(self.headline_frame, text="Left", variable=self.headline_align,
                                             value=0, command=lambda: self.get_headline_align("left"))
        self.headline_left.grid(column=0, row=0)
        self.headline_center = ttk.Radiobutton(self.headline_frame, text="Center", variable=self.headline_align,
                                               value=1, command=lambda: self.get_headline_align("center"))
        self.headline_center.grid(column=1, row=0)
        self.headline_right = ttk.Radiobutton(self.headline_frame, text="Right", variable=self.headline_align,
                                              value=2, command=lambda: self.get_headline_align("right"))
        self.headline_right.grid(column=2, row=0)

        self.color = ""
        self.headline_colorchooser = ttk.Button(self.headline_frame, text="Color of the headline",
                                                command=self.choose_color)
        self.headline_colorchooser.grid(column=3, row=0)
        self.color_display = tkinter.Canvas(self.headline_frame, background="white", height=20, width=20,
                                            relief="sunken", borderwidth=3)
        self.color_display.grid(column=4, row=0)

        self.submit_button = ttk.Button(self.mainframe, text="Submit",
                                        command=self.invoke_scripts)
        self.submit_button.grid(column=int(self.mainframe.grid_size()[0] / 2), row=self.mainframe.grid_size()[1] + 1)

    def invoke_scripts(self):
        create_css(headline_align=self.headline_align_str, headline_color=self.color)

    def get_headline_align(self, align):
        self.headline_align_str = align

    def choose_color(self):
        self.color = cc.askcolor()[1]
        self.color_display.configure(background=self.color)


class WarningWindow:
    def __init__(self, what):
        root = tkinter.Tk()
        root.geometry("300x75+600+400")
        root.title("Error")

        if what == 0:
            label = ttk.Label(root, text="You need to choose a language and title.", padding=5)
            label.pack()

        button = ttk.Button(root, text="OK", command=root.destroy, padding=5)
        button.pack()
