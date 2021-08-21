def tarjima(message):

    words = message.split(" ")
    tarjima = {
        "English": "Ingliz",
        "Word": "Dunyo",
        "World": "So'z",
        "Love": "Sevgi"
    }
    output = ""
    for word in words:
        output += tarjima.get(word, word) + " "
    return output


message = input(">")
result = tarjima(message)
print(result)