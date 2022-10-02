#Make function for a introduction
def title():
  print("                ----%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%----")
  print("                          ♥ Welcome to the Cafe ♥")
  print("                ----%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%----")

#_______________________________main
title()

#make list of menu
menu = ["1.Flat white $3.00", "2.Cappuccino $3.00", "3.Latte $3.50", "4.Decaf $3.50", "5.Hot Chocolate $4.00"]
#Make function to ask customer for their name and menu
def username(name):
  print("Welcome " + name)

#_____________________________main
username(input("(っ◔◡◔)っWhat may I call you dear customer?:"))

#Make a function for an option to show the Cafe's menu
def ask_menu():
  ask_menu = input("Would you like to see the menu? [Yes/No]:").lower()
  while True:
    if ask_menu == 'y' or ask_menu == 'yes':
      print(menu[0])
      print(menu[1])
      print(menu[2])
      print(menu[3])
      print(menu[4])
      break
    elif ask_menu == 'n' or ask_menu == 'no':
      print("Do you not want to order?")
      ask_menu()
      break
      
    else:
      print("Please answer either yes or no")
      menu()
      break

#___________________________main
ask_menu()


#_________main (Values of the coffees)
Coffee1 = 0
Coffee2 = 0
Coffee3 = 0
Coffee4 = 0
Coffee5 = 0

#Make function that asks for customer's order
def order():
  order = input("What would you like to order? [1-5]:")
  while True:
    if order == "1":
      print("you orderd 1")
      Coffee1 += 1
      break
    elif order == "2":
      print("you orderd 2")
      Coffee2 += 1
      break
    elif order == "3":
      print("you orderd 3")
      Coffee3 += 1
      break
    elif order == "4":
      print("you orderd 4")
      Coffee4 += 1
      break
    elif order == "5":
      print("you orderd 5")
      Coffee5 += 1
      break
    elif order == "6":
      break
    else:
      print("Please answer between 1-5")

      
order()

#How many of each
while True:
  if Coffee1 == 1:
    Coffee1_num = input("How many Flat whites would you like to order?:")
    break

  if Coffee2 == 2:
    Coffee2_num = input("How many Cappuccinos would you like to order?:")
    break

  if Coffee3 == 3:
    Coffee3_num = input("How many Lattes would you like to order?:")
    break

  if Coffee4 == 4:
    Coffee4_num = input("How many Decafs would you like to order?:")
    break

  if Coffee5 == 5:
    Coffee5_num = input("How many Hot Chocolates would you like to order?:")
    break



  
    
  