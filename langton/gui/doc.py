import tkinter as tk
from tkinter import ttk
import tkinterweb as tkweb
import webbrowser

class DocumentationPageCTRL:
    def __init__(self, master, controller, doc_path:str):
        """
        Initialisation du controlleur de la page de documentation

        :param master: widget parent de la page de documentation
        :param controller: controlleur, racine de l'interface
        graphique contenant la Frame courante
        :param str doc_path: chemin vers la documentation
        """
        self.view = DocumentationPage(master, self, doc_path)
        self.controller = controller

        
    def show(self):
        self.old_frame = self.controller.top_frame
        self.controller.set_top_frame(self)
        self.view.tkraise()
        self.view.focus()

        
    def link_clicked_handler(self, url):
        webbrowser.open(url)

        
    def back_callback(self):
        self.old_frame.show()


class DocumentationPage(ttk.Frame):
    def __init__(self, master, controller, doc_path:str):
        """
        Frame permettant d'afficher une documentation au format html.

        :param master: widget parent
        :param controller: controlleur de la Frame, doit contenir
        l'implémentation de back_callback
        :param str doc_path: chemin vers la documentation
        """
        ttk.Frame.__init__(self, master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.html_viewer = HtmlViewer(self, controller, doc_path)
        self.html_viewer.grid(row=0, column=0, sticky='nesw')

        self.back_button = ttk.Button(self, text="Back", command=controller.back_callback)
        self.back_button.grid(row=1, column=0)
        self.grid(row=0, column=0, sticky='nesw')
        
    
        
class HtmlViewer(tkweb.HtmlFrame):
    def __init__(self, master, controller, html_path:str):
        """Widget permettant d'afficher un fichier html

        :param master: widget parent
        :param controller: controlleur du widget, doit contenir
        l'implémentation de link_clicked_handler
        :param str html_path: chemin vers le fichier html à afficher

        """
        tkweb.HtmlFrame.__init__(self, master, messages_enabled = False)
        self.controller = controller
        self.on_link_click(self.controller.link_clicked_handler)
        
        with open(html_path, 'r') as f:
            html = f.read()

        self.load_html(html)


class AboutPopup:
    def __init__(self, about_msg_path:str):
        self.about_msg_path = about_msg_path


    def popup(self):
        """
        Affiche la popup
        """
        self.window = tk.Toplevel()
        
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.about_msg = HtmlViewer(self.window, self, self.about_msg_path)
        self.about_msg.grid(row=0, column=0, sticky='nesw')

        self.ok_button = ttk.Button(self.window, text="Ok", command=self.window.destroy)
        self.ok_button.grid(row=1, column=0)

        
    def link_clicked_handler(self, url):
        webbrowser.open(url)
