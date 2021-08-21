command = ""
started = False
sleeping = False
while True:
		command = input("> ").lower()
	
		if command == "start":
			sleeping = False
			if started:
				print("Already started")
			else:
				started = True
				print("Car started")
	
		elif command == "stop":
			if not started:
				print("Car is already stopped")
			else:
				started = False
				print("Car stopped!")

		elif command == "sleep":
			if not 	sleeping:
				print("Im going to bed")
				sleeping = True
			else:
				print("Heh. I'm dreaming boy....")


	
		elif command == "help":
			print("""
start - to start the car
stop - to stop the car
quit - to quit
help - for help""")
	
		elif command == "quit":
			print("O'yin tugadi. Mashina garajga ketdi!!!")
			break
	
		else:
			print("I don't understand.")