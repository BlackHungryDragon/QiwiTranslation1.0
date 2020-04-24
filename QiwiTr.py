import  pyqiwi,os
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
    wallet =pyqiwi.Wallet(token,number)
    menu()
def menu ():
    Mdoings= """\n  Выбери действиe :

  [1] - Проверить баланс
  [2] - Выполнить перевод на другой киви кошелек
  [3] - Узнать id  провайдера (телефона)
"""
    print(Mdoings)
    doings=int(input(" Действие : "))
    if doings == 1:
   balance = wallet.balance()
   print(' На балансе :',balance)
elif doings ==2:
    print("\n Введите номер киви кошелька")
    account=input(" Номер : ")
    print("\n Введите сумму платежа ")
    amount= input("  Сумма :")
    print("\n Введите комментай . Если не нужен , то омтаьте поле пустым")
    comment=input(' Коммент :')
    transfer=wallet.qiwi_transfer(account, amount, comment)
    print(" Платеж успешно отправлен",trasfer)
elif doings ==3:
    print ( "\n  Напиши номер у которого хочешь узнать айди ")
    phone =input(' Номер : ')
    deteck= pyqiwi.detect_mobile(phone)
    print (deteck)

