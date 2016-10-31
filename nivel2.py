# -*- coding: cp1252 -*-
# -*- coding: UTF-8 -*-


from Tkinter import *

class Nivel2:
	def __init__(self, j):

		self.s = False
		main.resizable(0,0)
		j.title("Digitando Palavras - v. 0.1")

		self.lbl1 = Label(j, text="Nível 2", fg="blue", font=('Times','20', 'bold'))
		self.lbl2 = Label(j, text="RIO GRANDE DO NORTE", fg="black", font=('Times','20', 'bold'))
		self.lbl3 = Label(j, text="Confira aqui se a palavra foi digitada corretamente:", fg="red", font=('Times','20', 'bold'))
		self.lbl4 = Label(j, text="", font=('Times','20', 'bold'))

		self.btn1 = Button(j, text="Próximo Nível", command=self.proximoNivel, fg="black", font=('Times','15', 'bold'))
		self.btn2 = Button(j, text="Clique aqui para confirmar a palavra", command=self.resposta, fg="black", font=('Times','15', 'bold'))

		self.palavra = StringVar()
		self.txt = Entry(j, textvariable=self.palavra, fg="black", font=('Times','20', 'bold'))

		self.lbl1.pack()
		self.lbl2.pack()
		self.txt.pack(ipadx=25, ipady=10)
		self.lbl3.pack()
		self.lbl4.pack()

		self.btn1.pack(side=LEFT)
		self.btn2.pack(side=RIGHT)

	def resposta(self):
		if self.lbl2["text"] == self.palavra.get():
			self.lbl4["text"] = "A palavra foi digitada corretamente."
			self.s = True
		else:
			self.lbl4["text"]= "Existem um ou mais erros na digitação."
			self.s = False
	def proximoNivel(self):
		if self.s == True:
			main.destroy()
			import nivel3

if __name__ == '__main__':
	main = Tk()
	main.geometry('635x260+50+50')
	Nivel2(main)
	main.mainloop()
