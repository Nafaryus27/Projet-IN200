import tkinter as tk
from tkinter import ttk
import tkinterweb as tkweb
import webbrowser

class DocumentationPageCTRL:
    def __init__(self, master, controller, doc_path:str):
        self.view = DocumentationPage(master, self, doc_path)
        self.controller = controller

        
    def show(self):
        self.old_frame = self.controller.top_frame
        self.controller.set_top_frame(self)
        self.view.tkraise()

        
    def link_clicked_handler(self, url):
        webbrowser.open(url)

        
    def back(self):
        self.old_frame.show()


class DocumentationPage(ttk.Frame):
    def __init__(self, master, controller, doc_path:str):
        ttk.Frame.__init__(self, master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.html_viewer = HtmlViewer(self, controller, doc_path)
        self.html_viewer.grid(row=0, column=0, sticky='nesw')

        self.back_button = ttk.Button(self, text="Back", command=controller.back)
        self.back_button.grid(row=1, column=0)
        self.grid(row=0, column=0, sticky='nesw')
        
    
        
class HtmlViewer(tkweb.HtmlFrame):
    def __init__(self, master, controller, doc_path:str):
        tkweb.HtmlFrame.__init__(self, master, messages_enabled = False)
        self.controller = controller
        self.on_link_click(self.controller.link_clicked_handler)
        
        with open(doc_path, 'r') as f:
            html = f.read()

        self.load_html(html)


