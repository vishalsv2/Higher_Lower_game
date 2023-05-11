import random
from data import data
from art import logo,vs
from replit import clear
count=0
game=True
print(logo)

while game:
    a=random.choice(data)
    b=random.choice(data)
    
    def highlow():
        global result
        global count
        global r
        global game
        if a==b:
            pass
        else:
            a1=(a["follower_count"])
            b1=(b["follower_count"])
            print(f"Compare A :  {a['name']},{a['description']},from {a['country']}.")
            print(vs)
            print(f"Against B : {b['name']},{b['description']},from {b['country']}.")
            result=input("Who has more followers? Type 'A' or 'B' : ").lower()
            if result=="a":
                result=a1
            elif result=="b":
                result=b1
            else:
                print("invalid")
            clear()
            
            if result==a1:
                if a1>b1:
                    r="q"
                    print("Win")
                else:
                    print("Loose")
                    game=False
                    r="f"
            elif result==b1:
                if b1>a1:
                    r="q"
                    print("Win")
                else:
                    print("Loose")
                    game=False
                    r="f"
            if r=="q":
                count+=1
  
                print(f"your current score is {count}")
            
            
            
    highlow()
print(f"Your final Score is {count}")


        
                