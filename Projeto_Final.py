# -*- coding: cp1252 -*-
## -*- coding: UTF-8 -*-
#from __future__ import unicode_literals

from Tkinter import *

class App:
	def __init__(self, j):

		main.resizable(0,0)
		j.title("Digitando Palavras - v. 0.1")

		self.lbl1 = Label(j, text="Sejam bem vindos!", fg="black", font=('Times','35', 'bold')).pack()
		self.lbl2 = Label(j, text="Vamos aprender a utilizar o teclado.", fg="black", font=('Times','35', 'bold')).pack()
		self.btn = Button(j, text="Clique aqui para começar", command=self.nivel1, bg="gray", fg="black", font=('Times','25', 'bold')).pack()
		self.lbl3 = Label(j, text="Desendolvido por Rogério Silva - Versão 0.1", bd=1, relief=SUNKEN, anchor=W, width=39).pack(side=BOTTOM)

	def nivel1(self):
		import nivel1

if __name__ == '__main__':
	main = Tk()
	main.geometry('825x300+50+50')
	App(main)
	main.mainloop()