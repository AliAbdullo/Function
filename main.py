
#Tug'ilgan yilini aniqlovchi funksya tuzish 
def t_yil(ism, yosh, j_yil=2022):
  """Foydalanuvchidan ismi va yoshini so'rab tug'ilgan yilini aniqlovchi funksiya """
  print(f"{ism.title()}, siz {j_yil-yosh}-yilda tug'ilgansiz")
  
t_yil('ali',25)

#kvadrat va kub hisoblash funksiya  
def kvkub(son):
  """Kiritilgan son kv va kub xisoblash"""
  print(f"{son} kvadrati: {son**2},\n"
        f"{son} kubi: {son**3}")
  
  kvkub(15)

  #Sonning juf yoki toq ekanligini topish
def  jufttoq(son):
  """Sonning Juft yoki Toq ekanligini topish dasturi"""
  if son%2==0:
    print(f"{son} Juft" )
  else:
    print(f"{son} Toq")
jufttoq(8)

#Sonlar kattasini aniqlash 
def kattason(son1,son2):
  """Kiritilgan sonlarning kattasini aniqlash"""
  if son1>son2:
    print(f'{son1} soni katta ')
  elif son1<son2:
    print(F'{son2} soni katta')
  else:
    print(f"SONLAR TENG!!!")

kattason(15, 15)

#Darajani aniqlash funksiyasi
def daraja(son, daraja=2):
  """Darajani xisoblash funksiyasi"""
  print(son**daraja)

daraja(2, 3)

#Foydalanuvchi kiritgan sonni sonnlarga bo'linishini aniqlash funksiyasi
def qoldiqsiz(son):
  for n in range(2,11):
    if not son%n:
      print(f"{son} {n} ga qoldiqsiz bo'linadi")
      
qoldiqsiz(20)