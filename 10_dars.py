# son = 1
# while son <= 31:
#	print(son)
#	son = son + 1
# promo code generatsiya
from random import randint
kodlar = [135, 132, 134, 130, 131]
yangi_kod = randint(130, 135)
i = 0
while yangi_kod in kodlar:
	i += 1
	yangi_kod = randint(130, 135)

print("Takrorlanishlar soni: ", i)	
print(yangi_kod)

while True:
	number = input("Butun son please: ")
	if number.isdigit():
		print("raxmat")
		break
	print("xatolik")	
	