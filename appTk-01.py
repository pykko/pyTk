#!/usr/bin/python3
# coding: utf-8


from tkinter import *


def quitterApplication() :
	print( "Quitter" )
	fenetre.destroy()


if __name__ == "__main__" :

	fenetre = Tk()
	
	fenetre.title( 'appTk' )
	fenetre.geometry( '400x300' )
	fenetre['bg'] = 'lightgreen'

	barreMenus = Menu( fenetre )
	fenetre.config( menu = barreMenus )

	menuFichier = Menu( barreMenus , tearoff = 0 )
	barreMenus.add_cascade( label = "Fichier" , menu = menuFichier )

	menuEdition = Menu( barreMenus , tearoff = 0 )
	barreMenus.add_cascade( label = "Edition" , menu = menuEdition )

	menuFichier.add_command( label = "Ouvrir" )
	menuFichier.add_command( label = "Fermer" )
	menuFichier.add_separator()
	menuFichier.add_command( label = "Quitter" , command = quitterApplication )
	
	
	message = Label( fenetre )
	message['text'] = 'Application SLAM'
	message.pack( padx = 2 , pady = 2 )
	
	saisie = Entry( fenetre )
	saisie.pack( padx = 2 , pady = 2 )
	
	bouton = Button( fenetre )
	bouton['text'] = 'Quitter'
	bouton['command'] = quitterApplication
	bouton.pack( padx = 2 , pady = 2 , side = RIGHT )


	fenetre.mainloop()
