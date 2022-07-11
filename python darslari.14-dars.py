# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:46:17 2022

@author: Ogabek
"""

                #PYTHON. 14-DARS
                #MAVZU:Dictionary (lug'a)
#car_0 = {'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
#print([car_0])
#en_uz = {'apple':'olma','apricot':"o'rik",'banana':'banan'}
#mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
#print(f"Olma narhi {mevalar['olma']} so'm")
#talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba_0['ism'].title()},\
#      {talaba_0['t_yil']}-yilda tug'ilgan,\
#      {talaba_0['yosh']} yoshda")    
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = 'informatika'
#talaba_1 = {}
#talaba_1['ism'] = "Og'abek Boltaev"
#talaba_1['kurs'] = 2
#talaba_1['yosh'] = 21
#print(talaba_1)
#talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")
#talaba_0 = {'ism': 'murod olimov','yosh':20,'t_yil':2000}
#del talaba_0['yosh']
#print(talaba_0)
#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'nokia 3310',
#    'anvar':'pixel'}
#get() metodi
#phone = en_uz.get('pineapple','Bunday ism mavjud emas')
#phone = telefonlar.get('hasan')
#print(phone)

#print(phone)    
                          #AMALIYOT.
#oyim = {'ismi':'Polvonova Klara', 't_yil':1976, 'viloyat':'Xorazm'}
#t_yil = oyim['t_yil']
#vil = oyim['viloyat']
#print(f"Oyimning ismi {oyim['ismi'].title()}, {t_yil}-yilda, {vil.title()} viloyatida tug'ilgan")
#taomlar = {
#    'otam':'osh',
#    'onam':'manti',
#    'opam':'gumma',
#    'akam':'shrgururch',
#    'singlim':"sho'rva",
#    'men':'barak'}
#taom = taomlar['otam']
#print(f"Otamning sevimli taomi {taom}")
python_izohli_lugati = {
    'integr':'Butun son',
    'float':"O'nlik son",
    'string':'matn',
    'if':'agar',
    'else':'yoki',
    'and':'va'}
#lugat = input("Kalit so'z kiriting\n>>>>:")
#print(python_izohli_lugati.get(lugat,"Bunday so'z mavjud emas"))
  

lugat = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(lugat)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{lugat.title()} so'z {tarjima} deb tarjima qilindi")

















    



                