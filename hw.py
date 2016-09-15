# Вариант 6
# Конъюкция
# Штрих Шеффера

a =  1
b = 0
print("*"*33)
print("*   A   *   B  * A & B *  A | B *")
print("*"*33)


for i in range(4):
  a = i // 2
  b = i % 2
  if a and b:
   k = "True"
  else:
   k = "False"
  if not (a and b):
   sh = "True"
  else:
   sh = "False"
  print("*  ", a, "  *  ", b, " *", k, "* ", sh, " *  ")
  print("*"*33)

print("")

# №13
print("*"*45)
print("*   A   *   B  *  C  *  (A&B<=>B&C)|(-C->A) *")
print("*"*45)
for i in range(8):
  a = i//4
  b = (i%4)//2
  c = (i%4)%2
  if (c or a) or ((a and b) == (b and c )):
    res = "True"
  else:
    res = "False"
  print("*  ", a, "  *  ", b, " * ", c, " *        ",res, "        *")
  print("*"*45)
print("")


# Минимальный элемент, стоящий на нечетной  позиции
# среди элементов первой  половины    списка
a = [0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	144,	233,	377,	
610,	987,	1597,	2584,	4181,	6765,	10]

print(min(a[1:(len(a)//2):2]))

# Найти сумму всех чисел с плавающей точкой

b = ("name",	"	DeLorean	DMC-12",	"motor_pos",	"rear",	"n_of_wheels",	4,
"n_of_passengers",	2,	"weight",	1.230,	"height",	1.140,	"length",	4.216,
 "width", 1.857, "max_speed", 177)

print(sum(b[9:16:2]))


