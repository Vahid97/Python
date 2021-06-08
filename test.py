import math
import random


#1

a = "Big brother is watching you"
print(a)

#2 

ad = "Vahid"
soyad = "Afandiyev"
tam_ad = ad.capitalize() + " " + soyad.capitalize()
print(f"Salam, {tam_ad}") 
print(f"Salam, {tam_ad}")  

#3

print("Baku", "Lissabon", "Roma", "Munchen", sep= "*")


#4 

m = "Macaristan"
print(m[::-1])

#5 ????


#6

print('\"Forever for now\" is one of the best movie replicas' )

#7

h = "O, ümumi PFA və FWA mükafatını alan ilk futbolçu oldu. 2008,2013,2014,2016-cü illərdə Qızıl top mükafatını qazandı."
z = int(len(h)/2)

print(h[:z])

#8

a = 7
b = 4

e = math.pow(a, b)
z = math.pow(b, a)

print(f"7 ustu 8 {int(e)}, 8 ustu 7 ise {int(z)} edir")


#9

x = 10
y = 55

print(x > y and 55 > 10)
print(x < y and 55 > 10)


#10

text = 'Nineteet Eighty-Four does not present "art_as-culture" but "art-as-function". Orwell like Marcel Proust fears that the habit of conforming to the force benumbs sensations and erases the perception of the world. Technological totalitarianism alienates senses, controls human behaviour and leads to linguistic degradation.'

split = text.split()
word = "force"

if word in split:
    print(f"{word} sozu metnde var")
else:
    print("Not found")


#11



x = 15

if x > 10 and x%2 == 0:
    print("okay")
elif x >10 or x%2 == 0:
    print("not okay")
else:
    print("bad")













