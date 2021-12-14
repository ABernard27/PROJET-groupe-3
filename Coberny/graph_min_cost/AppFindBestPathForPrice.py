# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:16:38 2021

@author: olivi
"""

import Coberny as cyb
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
import time
import datetime as dt
#import bestPricePathForUI as best_pp
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def UI():
    
    
    class AppFindBestPathForPrice():
        # Ici on initialise la fenêtre de l'interface
        def __init__(self):
            self.win = tk.Tk()
            self.win.title("Trouver le meilleur trajet au meilleur prix !")
            self.initialize() # Initialise l'interface graphique


        # Ici on initialise les éléments graphiques qui composent l'interface
        # 


        def initialize(self):
            # On renseigne la taille de la fenêtre
            self.win.minsize(width=800, height=500)

            # Ici on initialise les variables internes à l'interface qui prendront
            # leur valeur après l'interaction de l'utilisateur. Ces variables seront
            # parfois utilisées dans les méthodes (callback) liées aux composants
            # graphiques
            self.nameFile = tk.StringVar()
            self.data = None
            self.departureCity = tk.StringVar()
            self.destinationCity = tk.StringVar()
            self.stepsNumber = tk.IntVar()

            ###########################################################
            ###### Frame pour charger le fichier de données ###########
            ###########################################################
            # - Contient un bouton pour récupérer le fichier de données
            # - contient un label affichant le chemin du fichier
            ###########################################################
            loadFile_Frame = ttk.LabelFrame(self.win, text='Fichier de données')
            loadFile_Frame.grid(column=0, row=0, columnspan=10, rowspan=3,
                                padx=10, pady=10)

            self.button_loadFile = ttk.Button(loadFile_Frame,
                                              text="Sélectionner le fichier de données",
                                              command=self.loadDataFile)
            self.button_loadFile.grid(column=0, row=0, rowspan=3, padx=5, pady=5)

            ttk.Label(loadFile_Frame, text="Chemin : ").grid(column=1, row=0, pady=5) 
            ttk.Label(loadFile_Frame, textvariable=self.nameFile).grid(
                column=3,
                row=0,
                pady=5
            )

            self.button_loadDepartCity = ttk.Button(self.win,
                                                    text="Charger les villes de départ",
                                                    command=self.loadDepartCity,
                                                    state='disabled')
            self.button_loadDepartCity.grid(column=4, row=3, rowspan=3, pady=5)

            ############################################################################
            ###############     Frame pour configurer le trajet     ####################
            ############################################################################
            # - Contient un label affichant le texte 'Ville de départ'
            # - Contient une liste déroulante (Combobox) pour choisir la ville de départ
            # - Contient un label affichant le texte 'Ville de destination'
            # - Contient une liste déroulante pour choisir la ville de destination
            # - Contient un buton qui déclenche le calcul du nombre maximum de sorties 
            #   sur le trajet
            # - Contient un label affichant le texte 'Choisir le nombre de sorties'
            # - Contient une liste déroulante pour choisir le nombre de sorties
            ############################################################################
            city_Frame = ttk.LabelFrame(self.win, text='Choix du trajet')
            city_Frame.grid(column=0, row=6, columnspan=10, rowspan=9, padx=10, pady=10)

            ttk.Label(city_Frame, text="Ville de départ: ").grid(column=0, row=0)
            self.cbox_departCity = ttk.Combobox(city_Frame,
                                                width=30,
                                                textvariable=self.departureCity,
                                                state='disabled')
            self.cbox_departCity.grid(column=1, row=0, padx=(5, 40), pady=5)

            # Ici on retire la ville de départ choisie par l'utilisateur dans
            # dans la liste des villes de destination gràce à la méthode
            # loadDestinationCity
            self.cbox_departCity.bind("<<ComboboxSelected>>", self.loadDestinationCity)

            ttk.Label(city_Frame, text="Ville de destination: ").grid(column=3, row=0)
            self.cbox_destinaCity = ttk.Combobox(city_Frame,
                                                 width=30,
                                                 textvariable=self.destinationCity,
                                                 state='disabled')
            self.cbox_destinaCity.grid(column=4, row=0, padx=5, pady=5)

            self.button_stepsOnPath = ttk.Button(
                city_Frame,
                text="Calcul du nombre maximum de sorties sur le trajet",
                command=self.findStepsOnPath,
                state='disabled'
            )
            self.button_stepsOnPath.grid(column=2, row=1, rowspan=3, pady=5)

            ttk.Label(city_Frame, text="Choisir le nombre de sorties: ").grid(column=1,
                                                                              row=4)
            self.cbox_stepsNumber = ttk.Combobox(city_Frame,
                                                 width=10,
                                                 textvariable=self.stepsNumber,
                                                 state='disabled')
            self.cbox_stepsNumber.grid(column=2, row=4, padx=5, pady=5)

            #######################################################################
            ###############     Frame pour les résultats   ########################
            #######################################################################
            # - Contient un buton qui déclenche:
            #   - le calcul du meilleur chemin au meilleur prix
            #   - la génération et l'affichage du graph représentant le trajet
            # - Contient une fenêtre dans laquelle les résultats de l'exécution
            #   du programme s'afficheront
            #######################################################################

            results_Frame = ttk.LabelFrame(self.win, text='Résultats')
            results_Frame.grid(column=0, row=15, columnspan=10, rowspan=4, padx=10, pady=10)

            self.button_bestPathForPrice = ttk.Button(results_Frame,
                                                      text="Trouver le meilleur trajet au meilleur prix",
                                                      command=self.bestPathForPrice,
                                                      state='disabled')
            self.button_bestPathForPrice.grid(column=0, row=0, padx=5, pady=5)

            self.winResult = scrolledtext.ScrolledText(results_Frame,
                                                       width=120,
                                                       height=20,
                                                       wrap=tk.WORD)
            self.winResult.grid(column=0, row=1, pady=10)


        ###########################################################################
        #####################     Méthodes (Callbacks)    #########################
        ###########################################################################




        def loadDataFile(self):
            self.nameFile.set(askopenfilename(title="Choisir le fichier de données",
                                              filetypes=[('csv files', '.csv')]))
            self.data = pd.read_csv(self.nameFile.get())
            self.data = self.data.fillna(0)
            if (not self.data.empty):
                self.button_loadDepartCity.configure(state='normal')


        def loadDepartCity(self):
            departCityList = cyb.GetListOfcolnames(self.data)
            self.cbox_departCity['values'] = tuple(departCityList)
            self.cbox_departCity.current(0)
            self.cbox_departCity.configure(state='readonly')


        def loadDestinationCity(self):
            departCityList = cyb.GetListOfcolnames(self.data)
            destinaCityList = departCityList[:]
            destinaCityList.remove(self.cbox_departCity.get())
            self.cbox_destinaCity['values'] = tuple(destinaCityList)
            self.cbox_destinaCity.current(0)
            self.cbox_destinaCity.configure(state='readonly')
            self.button_stepsOnPath.configure(state='normal')


        def findStepsOnPath(self):
            kMaxConstraint = cyb.GetKMaxConstraint(self.data,
                                                       self.departureCity.get(),
                                                       self.destinationCity.get())
            stepsNb_list = [x for x in range(0, kMaxConstraint + 1)]
            self.cbox_stepsNumber['values'] = tuple(stepsNb_list)
            self.cbox_stepsNumber.current(0)
            self.cbox_stepsNumber.configure(state='readonly')
            self.button_bestPathForPrice.configure(state='normal')


        def bestPathForPrice(self):
            self.winResult.insert(tk.INSERT, '*************************************\n')
            self.winResult.insert(tk.END, '*************************************\n')
            startTime1 = time.time()
            bestPathPriceCouple = cyb.FindBestPathForPrice(self.data,
                                                               self.departureCity.get(),
                                                               self.destinationCity.get(),
                                                               self.stepsNumber.get())
            runTime1 = time.time() - startTime1
            roundRunTime1 = str(dt.timedelta(seconds=runTime1))
            beginStr1 = "Temps d'exécution: "+ str(runTime1) +' secondes.\n cad '
            endStr1 = str(roundRunTime1) + " dans le format heures minutes secondes"
            displayTime1 = beginStr1 + endStr1

            bestPath = bestPathPriceCouple[0]
            bestPrice = bestPathPriceCouple[1]
            self.winResult.insert(tk.END, 'Meilleur trajet: ' + str(bestPath) + '\n')
            self.winResult.insert(tk.END, 'Meilleur prix: ' + str(bestPrice) + '\n')
            self.winResult.insert(tk.END, displayTime1 + '\n')
            self.winResult.insert(tk.END, '-------------------------------------\n')
            self.winResult.insert(tk.END, 'Génération du graph en cours \n')

            f = Figure(figsize=(5,5), dpi=100, facecolor='white')
            ax = f.add_subplot(111)
            plt.axis('off')

            startTime2 = time.time()
            cyb.GraphOfBestPathForPrice_UI(self.data,
                                                  self.departureCity.get(),
                                                  self.destinationCity.get(),
                                                  self.stepsNumber.get(),
                                                  ax)
            runTime2 = time.time() - startTime2
            roundRunTime2 = str(dt.timedelta(seconds=runTime2))
            beginStr2 = "Temps d'exécution: "+ str(runTime2) +' secondes.\n cad '
            endStr2 = str(roundRunTime2) + " dans le format heures minutes secondes"
            displayTime2 = beginStr2 + endStr2
            self.winResult.insert(tk.END, displayTime2 + '\n')
            self.winResult.insert(tk.END, '*************************************\n')
            self.winResult.insert(tk.END, '*************************************\n')
            self.winResult.insert(tk.END, '\n')
            self.winResult.insert(tk.END, '\n')

            winGraph = tk.Toplevel(self.win)

            def destroyWindow():
                winGraph.destroy()

            winGraph.title('Le meilleur trajet au meilleur prix')
            winGraph.minsize(width=100, height=100)
            winGraph.protocol('WM_DELETE_WINDOW', destroyWindow)
            canvas = FigureCanvasTkAgg(f, master=winGraph)
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(canvas, winGraph)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
        app = AppFindBestPathForPrice()
        app.win.mainloop()

  #if __name__ == "__main__":
    
