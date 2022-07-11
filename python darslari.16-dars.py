# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:15:12 2022

@author: Ogabek
"""

#                        PYTHON DARSLARI.
#                        16-DARS.MAVZU:NESTING
#                        Lug'atlar ro'yxati.
#car0 = {
#        'model':'lasetti',
#        'rang':'oq',
#        'yil':2018,
#        'narh':13000,
#        'km':50000,
#        'korobka':'avtomat'
#        }

#car1 = {
#        'model':'nexia 3',
#        'rang':'qora',
#        'yil':2015,
#        'narh':9000,
#        'km':89000,
#        'korobka':'mexanika'
#        }

#car2 = {
#        'model':'gentra',
#        'rang':'qizil',
#        'yil': 2019,
#        'narh':13000,
#3        'km':20000,
 #       'korobka':'mexanika'}
#car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']}-yil, {car['narh']} $$")

#cars =[car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang, "
#          f"{car['yil']}-yil, {car['narh']}$$")

#print(cars[1]['model'])

#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")
#malibus = []
#for n in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None,   #rangi noaniq
#        'yil':2020,
#        'narh':None,
#        'km':0,
#        'korobka':'avto'
#        }
#    malibus.append(new_car)
    
#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
    
#    for malibu in malibus:
#        print(malibu)

#for malibu in malibus[6:]:
#    malibu['rang']='qora'

#for malibu in malibus[6:]:
#    malibu['rang']='qora'
#    malibu['korobka']='mexanika'
    
#    for malibu in malibus:
#        if malibu ['korobka']=='avto':
#            malibu['narh']=40000
#        else:
#            malibu['narh']=35000

                      #Lug'atlar ichida ro'yxat
#dasturchilar = {
#    'ali':['python','c++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['c++','c#']
#    }

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(til.upper())

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi tillarni biladi:")
#    for til in tillar:
#        print(f'{til.upper()} ', end='')


#hamkasblar = {
#    'ali':{'familiya':'valiyev',
#           'tyil':1995,
#           'malumot':'oliy',
#           'tillar':['python','c++']
#           },
#    'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta-maxsus",
#            'tillar':['html', 'css', 'js']},
#    'hasan':{'familiya':'husanov',
#             'tyil':1999,
#             'malumot':'maxsus',
#             'tillar':['python','php']}
#    }
    

#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, "
#         f"{info['tyil']}-yilda tug'ilgan. "
#         f"Ma'lumoti: {info['malumot']}. \n"
#         "Quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#      print(til.upper())
          
              #AMALIYOT
#buxoriy = {'ism':'Abu abdulloh Muhmmad ibn Ismoil',
#               'tyil':810,
#               'vyil':870,                             
#               'tjoy':'Buxoro',
#               'asarlar':["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix  al-kabir" , "At-tarix As-sag'ir"]
#            }
#qodiriy = {'ism':'Abdulla Qodiriy',
#               'tyil':1894,
#               'vyil':1938,
#               'tjoy':'Toshkent',
#               "asarlar":["O'tkan kunlar","Mehrobdan chayon",'Obid ketmon']
#                          }
#vohidov = {'ism':'Erkin Vohidov',
#                     'tyil':1936,
#                     'vyil':2016,
#                     'tjoy':"Farg'ona",
 #                    'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim",'Qiziquvchan Matmusa']
 #                    }
#navoiy = {'ism':'Alisher Navoiy',
#                      'tyil':1441,
#                      'vyil':1501,
#                      'tjoy':"Xirot",
#                      'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub","Munojot"]
#                      }

#shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    asarlar = shaxs['asarlar']
#    print(f"\n{ism} ning mashxur asarlari: ")
#    for asar in asarlar:
#        print(asar)
        
kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interestaller'],
    'hasan':['Abdullajon','Bomba','SHaytanat'],
    'husan':['Mahallada duv-duv gap','John Wisk']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)