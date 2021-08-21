# Izox: y 


from datetime import datetime
from tkinter import *
"""y = datetime.today()
ism = input("Ismingiz nima? ")
print("Salom", ism)
ty = int(input("Tug'ilgan yilingizni kiriting: "))
natija = y.year - int(ty)
print("Sizning yoshingiz: ", natija)
yosh = input("Yoshingiz nechada ? ")
natija2 = y.year - int(yosh)
print("Sizning tug'ilgan yilingiz: ", natija2, ism)"""

oyna = Tk()
oyna.title("MyFirstUI")
oyna.geometry("300x300")

natija = Label(text="Natija", bg="red")
natija.place(x=90, y=123, width=120, height=50)

yil = Entry()
yil.place(x=75, y=60, width=150, height=30)

def farq():
	bugun = datetime.today()
	natija.config(text=bugun.year - int(yil.get()))

tugma = Button(text="Hisoblash", command=farq)
tugma.place(x=90, y=90, width=122, height=34)




oyna.mainloop()