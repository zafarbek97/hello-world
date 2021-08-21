"""son = 45
print(son)
sonlar = [45, 61, 27, -91]
print("sonlar =", sonlar, type(son))
sonlar = [34, 54, 543]
print(sonlar[2], [3])"""
import pygal

#topshiriq

line_chart = pygal.Line()
line_chart.title = "Yillik hisobot"
line_chart.x_labels = ["1 chorak", "2 chorak", "3 chorak", "4 chorak"]
IT_soni = int(input("IT soni nechta: "))
i = 0
while i < IT_soni:
	i+=1
	name = input("IT nomi: ")
	x = float(input("1 chorak ko'rsatkichi: "))
	y = float(input("2 chorak ko'rsatkichi: "))
	z = float(input("3 chorak ko'rsatkichi: "))
	w = float(input("4 chorak ko'rsatkichi: "))
	line_chart.add(name, [x,y,z,w])
line_chart.render_in_browser()