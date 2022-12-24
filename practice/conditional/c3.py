import random
target_num,ges_num=random.randint(1,10),0

while target_num!=ges_num:
      ges_num=int(input("Guess a number between 0 and 10 until you get it right : "))

print("well guessed")