import tkinter as tk
from tkinter import ttk
import tkinterweb as tkweb
import webbrowser

class DocumentationPageCTRL:
    def __init__(self, master, doc_path:str):
        self.view = DocumentationPage(master, self, doc_path)

    def show(self):
        self.view.tkraise()
    
    def link_clicked_handler(self, url):
        webbrowser.open(url)

        
class DocumentationPage(tkweb.HtmlFrame):
    def __init__(self, master, controller, doc_path:str):
        tkweb.HtmlFrame.__init__(self, master, messages_enabled = False)
        self.controller = controller
        self.on_link_click(self.controller.link_clicked_handler)
        
        with open(doc_path, 'r') as f:
            html = f.read()
        
        self.load_html(html)

        self.grid(row=0, column=0, sticky="nesw")
