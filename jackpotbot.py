import random as rd
import time as t

money = 10000

def inform():
   
    print("현재 잔액:", money)
    bet = int(input("배팅할 금액을 적어주세요."))
    
    if (bet.isdigit() == True):
       
        if(bet <= money):
            jackpot()
            return
        else:
            print("잔액 부족.")
            return
    else:
        print("숫자만 입력하세요")
        return

def jackpot(bet1):
    num1 = rd.randint(1,99)

    print("배팅 금액 :", bet1)
    print("성공 확률 :", num1 + "%")

    t.sleep(3)

    num2 = rd.radint(1,100)

    if(num2 <= num1):
        money += bet1
        print("성공했습니다. 나온 숫자:", num2, "/ +" + bet1)
    else:
        money -= bet1
        print("실패했습니다. 나온 숫자:", num2, "/ -" + bet1)

    return

while True:
    inform()

    







