from os import system, name

s = 0
cont = 0
for c in range(3, 501, 2):
  if c % 3 == 0:
      s += c
      cont += 1      
print (f' A soma de todos os {cont} Valores é: {s}')
