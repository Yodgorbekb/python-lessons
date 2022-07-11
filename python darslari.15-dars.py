# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:40:33 2022

@author: Ogabek
"""

                            #15-dars: lug'at bilan ishlash.
           #items() metodi.
talaba_0 = {
    'ism':'alijon',
    'familya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
print(talaba_0.items())
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}\n")
telefonlar = {
    'ali':'iphone 13',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'redmi 10'
    }
for k, q in telefonlar.items():
    print(f"{k.title()} ning telefoni {q}")
    #.keys() metodi
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())
 

print('Do\'konimizdagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())    

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")        
    
for buyum in bozorlik:
    if buyum not in mahsulotlar:    
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        print(mahsulot.title())


# #LUG'AT ELEMENTLARINI TARTIB BILAN CHAQIRISH
print("Do'konimizdagi mahsulotalar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
# #.values metodi

print(telefonlar.values())    
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
telefonlar = {
   'ali':'iphone x',
    'olim':'galaxy s9',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawi',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

#set funksiyasi

print('Foydalanuvchilar quyodagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)    
toys = {"ball","car","lamp","ball","bear","car"}
                        #AMALIYOT
python_izohli_lugati = {
    "Boolen":"Mantiqiy qiymat",
    "float":"O'nlik son",
    "For":"Biror amalni qayta-qayta bajarish tsikli",
    "If":"SHartlarni tekshirish operatori",
    "Integer":"Butun son"
    }    
for kalit, value in sorted(python_izohli_lugati.items()):
    print(f"{kalit.title()} - {value}")

davlatlar = {
    "o'zbekiston":'toshkent',
   'aqsh':'washington',
  'rossiya':'moskva',
 'tojikiston':'dushanbe',
"qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lupur',
    'singapur':'singapur',
    'italiya':'rim'}
print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())
    
    print('\nDunyo davlatlarining poytaxtlari')
    for poytaxt in sorted(davlatlar.values()):
        print(poytaxt.title())
        
country = input("Qaysi davalatlarni poytaxtini bilishni  istaysiz?")
capital = davlatlar.get(country)
if capital==None:
    print("Kechirasiz bizda bu davlat haqida ma\'lumot yo\'q")
else:
    print(f"{country.upper()} ning poytaxti {capital.title()} shahri")
  

      
menu = {
        'osh':3000,
        'manti':20000,
        'somsa':4000,
        'mastava':5000,
        'chuchvara':6000,
        "sho'rva":7000,
        'shashlik':2000,
        'non':3000,
        'choy':1000,
        'sharbat':1000}
print("Salom, 2ta taom-ichimlik buyurtma bering\n")
buyurtmalar = []
hisob = {'100000'}
for n in range(4):
    buyurtmalar.append(str(input(f"{n+1}-taom:").lower()))
    hisob = '100000' - buyurtmalar   
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma}  {menu[buyurtma]} so'm.")
else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")   
print("Hisobingizda {hisob} so'm qoldi")