from SimpleQIWI import *
import os,pyqiwi
from  colorama import Fore ,Back ,Style

banner = """

   QQ QQ   II  W        W   II    TT TT TT    R R R
   QQ  Q       W        W            TT       R    R
   Q Q Q   II  W   WW   W   II       TT       R R R
       Q   II  W W    W W   II       TT       R    R
       Q   II  W        W   II       TT       R     R
  
    Qiwi Translation v1.0

""" 

######################################
#    Coder:HungrDragon   #    
 #      Telegram :@HundrDragon #                           #
######################################
# Программа еще не доработана #
 # # # # # # # # # # # # # # # 
def clear ():
        if os.name == 'nt':
                _ = os.system ('cls')
        else:
                _ = os.system ('clear')
clear()

if __name__ == '__main__': 
    print(Fore.YELLOW+banner)
    print("Для того,чтобы воспользоватся функионалом программы ,необходимо авторизироваться")
    print("\n Введите токен :")
    token= input(" Токен : ")
    print( "\n Введитп номер телефона : ")
    number = input("  Номер : ") 
    
Mdoings= """\n  Выбери действиe :

  [1] - Проверить баланс
  [2] - Выполнить перевод на другой киви кошелек
  [3] - Узнать id  провайдера (телефона)
"""
print(Mdoings)
doings=int(input(" Действие : "))
if doings == 1:
   api = QApi(token=token, phone=number)
   print(' На балансе :',api.balance)
elif doings ==2:
    api = QApi(token=token, phone=number)
    print("\n Введите номер получателя (киви кошелек)")
    phone=input(' Номер : ')
    print(Fore.WHITE+' Введите сумму.')
    sum=input(' Сумма :')
    comm=input(' Комментарий :')
    api.pay(account=phone, amountsu=m, comment=comm)
    time.sleep(2)
    print(' Успешно выполнен перевод .Ваш баланс : ', api.balance)
elif doings ==3:
    print ( "\n  Напиши номер у которого хочешь узнать айди ")
    phone =input(' Номер : ')
    deteck= pyqiwi.detect_mobile(phone)
    print (deteck)
