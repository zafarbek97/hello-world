uyqu = False
yuv = False
kiyingan = False
eslatma = False
iye = 0
ism = input("Meni nima deb chaqirmoqchisiz? ").capitalize()
print(f"Xo'p bo'ladi. Endi mening ismim {ism}")
while True:

	command = input(" >").lower()
	
	if command == "hey":
		print("Eshitaman")

	elif command == "isming nima":
		print(f"Ismim {ism}")	

	elif command == "yuvindingmi":
		if not yuv:
			print("Yo'q hali")
		else:
			print("Ha yuvinganman")


	elif command == ism.lower():
		print("Xoooov !!!!!!!!!!!!!!!!")		

	elif command == "ismni almashtiramiz":
		print("Xo'p bo'ladi. Qanday ism qo'yasiz: ")
		ism = input(" >").capitalize()
		print(f"Endi mening ismim {ism}")

	elif command == "iye":
		iye += 1
		if iye > 3:
			print("Iyalorami xadeb Zafar aka")
		else:
			print("Iyeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

	elif command == "yaramas":
		print("O'ziz yaramassiz")

	elif command == "meni ismim nima":
		print("Sizning ismingiz Zafar")

	elif command == "qalesan":
		print("Chidasa bo'ladi")
	
	elif command == "uxla":
		if not uyqu:
					print("Mana yotdim")
					uyqu = True
					kiyingan = False
					yuv = False
		else:
			print("Uxlayappanu uyg'otvordiz endi")

	elif command == "nima qilyapsan":
		if not uyqu:
					print("Siz bilan gaplashyapmanuuu")
		else:
			print("Uxlayappanu")		

	elif command == "save":
		eslatma = input("""Eslab turishim kerak bo'gan gapni ayting:
	>""")

	elif command == "eslatma":
		if not eslatma:
			print("Xali beri aytmadizuu")
			eslatma = True
			eslatma = input("Ayting endi eslab qolaman: ")
		else:
				print(eslatma)

	elif command == "nima":
		print("nima nima nimalaaaaaaaaaaaaaaaaaaaaaaaar bo'pti, axir senga yetmadi qo'lim....... ")

	elif command == "kiyin":
		if uyqu:
			print("Uxlayotgandayam kiyinorami silar tarafda")
		elif kiyingan:
			print("Kiyimlarim qayerda. Ha mana topdim")
			kiyingan = True
		else:
			print("Kiyinib bo'ganman")		

	elif command == "tur":
		if not uyqu:
			print("Uyg'oqmanu iplos")
		else:
			kiyingan = True
			uyqu = False
			print("Mana mana turdim")

	elif command == "yuvin":
		if not uyqu and not yuv:
			print("Suv quyib ber")
			yuv = True
		elif yuv is True:
				print("Yuvinib bo'dimuuu")
		else:
			print("Avval uyg'onish keremasmikin? ")

	elif command == "hisoblashni bilasanmi":
		print("Xa albatta")
		print("Ayting nimani hisoblash kerak ?")
		a = input()
		print("Natija: ", a, ":) xa xaaa xaaa :)")

	elif command == "q":
		print("O'yin tugadi")
		break

	else:
		print("Odamga o'xshab gapir tushunmadim")	