#format

# name = input("Ismingizni kiriting: ")
# print("Salom {}".format(name))
# ism = input("Ism: ")
# print("Salom", ism)

# truncate long string
# print("{:.5}".format(ism))
# print(ism.capitalize())
# print(ism.casefold())
# print(ism.count("a"))
# s = "salom"
# print(s[:3])

# kiritilgan so'zni teskarisiga o'girish
word = input("so'z kiriting: ")
print(word[::-1].capitalize())

matn1 = input("Birinchi so'z: ")
matn2 = input("Ikkinchi so'z: ")
matn1,matn2 = matn2,matn1
print(matn1,matn2)