import math

# import random


# #1

# a = "Big brother is watching you"
# print(a)

# #2 

# ad = "Vahid"
# soyad = "Afandiyev"
# tam_ad = ad.capitalize() + " " + soyad.capitalize()
# print(f"Salam, {tam_ad}")  

# #3

# print("Baku", "Lissabon", "Roma", "Munchen", sep= "*")


# #4 

# m = "Macaristan"
# print(m[::-1])

# #5 ????


# #6

# print('\"Forever for now\" is one of the best movie replicas' )

# #7

# h = "O, ümumi PFA və FWA mükafatını alan ilk futbolçu oldu. 2008,2013,2014,2016-cü illərdə Qızıl top mükafatını qazandı."
# z = int(len(h)/2)

# print(h[:z])

# #8

# a = 7
# b = 4

# e = math.pow(a, b)
# z = math.pow(b, a)

# print(f"7 ustu 8 {int(e)}, 8 ustu 7 ise {int(z)} edir")


# #9

# x = 10
# y = 55

# print(x > y and 55 > 10)
# print(x < y and 55 > 10)


# #10

# text = 'Nineteet Eighty-Four does not present "art_as-culture" but "art-as-function". Orwell like Marcel Proust fears that the habit of conforming to the force benumbs sensations and erases the perception of the world. Technological totalitarianism alienates senses, controls human behaviour and leads to linguistic degradation.'

# split = text.split()
# word = "force"

# if word in split:
#     print(f"{word} sozu metnde var")
# else:
#     print("Not found")


# #11



# x = 15

# if x > 10 and x%2 == 0:
#     print("okay")
# elif x >10 or x%2 == 0:
#     print("not okay")
# else:
#     print("bad")


# DAY 02 //////////////


# QUIZ1

# x = int(input("Enter a value: "))

# k = x*x

# print(f"Kvadratin sahesi: {k}-dir")


#QUIZ2

# x = [int(x) for x in input("Enter four value: ").split()]

# x.sort()

# print("Largest number is: ", x[-1])


#QUIZ3

# foods = {
#     "portagal":"3 manat",
#     "armud":"2 manat",
#     "gilas":"4 manat",
#     "nar":"5 manat",
# }


# for key in foods.keys():
#     print(key, end=" ")


# x = input("\nIstediyiniz meyveni secin: ")

# if x in foods.keys():
#     print(foods[x])
# else:
#     print("Meyve menyuda yoxdur")





#QUIZ4

# istifadeci_adi = input("Adinizi daxil edin: ")

# if 3 < len(istifadeci_adi) <11:
#     istifadeci_soyadi = input("Soyadinizi daxil edin: ")
#     if 5 < len(istifadeci_soyadi) < 15:
#         istifadecinin_dogum_ili = input("Dogum ilinizi daxil edin: ")
#         if len(istifadecinin_dogum_ili) == 4:
#             istifadecinin_email_adresi = input("Email adresinizi daxil edin: ")
#             if 10 < len(istifadecinin_email_adresi) < 22:
#                 istifadecinin_parolu = input("Parolunuzudaxil edin: ")
#                 if 6 < len(istifadecinin_parolu) < 13:
#                     istifadecinin_parolu_tekrar = input("Parolunuzu yeniden yigin: ")
#                     if istifadecinin_parolu_tekrar == istifadecinin_parolu:
#                         qeydiyyat_detali_sorush = input("Qeydiyyat tamamlandi! Detalara baxmaq siteyirsinizmi? ")
#                         if qeydiyyat_detali_sorush == "beli":
#                             print(f"Ad {istifadeci_adi}, Soyad {istifadeci_soyadi}, Yash {istifadecinin_dogum_ili}")
#                         elif qeydiyyat_detali_sorush == "xeyr":
#                             print(f"{istifadeci_adi} {istifadeci_soyadi} Ugurlar!")
#                     else:
#                         print("Tekrar parolu dogru qeyd edin")
#                 else:
#                     print("Parolunuz dogru qeeyd edin")
#             else:
#                 istifadecinin_email_adresi = input("Email adresinizi daxil edin: ")
                
#         else:
#             print("Dogum ilinizi dogru qeyd edin")
#     else:
#         print("Soyadinizi dogru qeyd edin")
# else:
#     print("Adinizin uzunlugu 3 ve 11 arasinda olmalidir")


#QUIZ5


# list = [10, 5, 6, 1]

# a = 0
# b = 0
# if a < len(list):
#     for i in list:
#         b += i
#         a+1
#         print(b)


#QUIZ6 //////////////////

# numbers = [4,2,10,14,11]
# a = 0
# b = 0
# for i in numbers:
#     if  < :
#         b = i
#         a+1
#         print("dfasd")
#     else:
#         print("Eded")





#QUIZ9



# a = ["Vahid", "Murad", "Vusal"]

# if len(a) == 0:
#     print("List boshdur")
# else:
#     print("List bosh deyil")


#QUIZ10

# a = [9, 7,10]
# b = 0
# if a[b] %2:
#     print(f"{a[b]} is odd")
# else:
#     print(f"{a[b]} is odd")







#DAY03 ///////////////


#QUIZ01


# def sum(*args):
#     cem = 0
#     for i in args:
#         cem += i
#     return cem


# print(sum(5,4,3,2))



#QUIZ02


# def multiply(*args):
#     z = 1
#     for i in args:
#         z *= i
#     return z

# print(multiply(3,7,2,8))


#QUIZ03


# def returnDay(a):
#     days = {
#         1: "Monday",
#         2: "Thursday",
#         3: "Wednsday",
#         4: "Tuesday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }  

#     if 1 <= a < 8:
#         z = f"{a} is {days[a]}"
#     else:
#         z = None
#     return z

# print(returnDay(7))


#QUIZ04


# def lastElement(a):
#     result = 0
#     for i in a:
#         result = i
#     return result



# a = [1,4,6,8,9]
# print(lastElement(a))


#QUIZ05



# def even(a):
#     evenList = []
#     for i in a:
#         if i%2 == 0:
#             evenList.append(i)
#         else:
#             None
#     return evenList




# a = [1,2,3,4,5,6,7,8]
# print(even(a))