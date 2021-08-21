kalit_raqam = 20
urinishlar_limiti = 3
urinishlar_soni = 0
while urinishlar_soni < urinishlar_limiti:
	urinish = int(input("top: "))
	urinishlar_soni += 1
	if urinish == kalit_raqam:
		print("Qoyil !!! To'g'ri topdingiz.")
		break
	elif urinishlar_soni == urinishlar_limiti:
		print("Yana urinib ko'rishni xoxlaysizmi?")
		command = input("> yes/no: ")
		if command == "yes":
			urinishlar_soni = 0
		else:
			break	


else:
		print("Afsus. Yutqazdingiz")		 
