# this program asks will determine if you will go the Mana Concert
name = input("Hello there, What is your Name? ")
user_age = input(" Hey {} ,How old are you? ".format(name))
if (user_age > 18):
  print("Alrighty! {} you can enter the concert and watch Mana".format(name))
else:
  print("Sorry Bro, you are too young and can't attend the concert")
print("Have a nice day!")
  
#elif Example of this program

if (age<18):
  print("you can go to the show")
elif(age==18):
  print("go see Pink Floyd. You are allowed to attend this Concert")
else:
  print("You can go to see Meatloaf")
print("Have an awesome day")
