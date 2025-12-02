#1-misol
text = str(input('Matn kirit: '))

funk = lambda x: len(x)
print(funk(text))

#2-misol
son = int(input("Son kiriting: "))

funk = lambda x: "Musbat" if x > 0 else ("Manfiy" if x < 0 else "Nol")
print(funk(son))

#3-misol
son = int(input("Son kirit: "))
son2 = int(input('Son kirit: '))

funk = lambda x, y: 0.5 * son * son2
print(funk(son, son2))

#4-misol
son = int(input("Son kirit: "))

funk = lambda x: son % 2 == 0
print(funk(son))

#5-misol
son = int(input("Son kirit: "))

funk = lambda x: son > 10
print(funk(son))
