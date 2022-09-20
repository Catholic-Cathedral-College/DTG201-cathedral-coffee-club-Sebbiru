#Make function for a introduction
def title():
  print("                ----%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%----")
  print("                          ♥ Welcome to the Cafe ♥")
  print("                ----%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%----")

#_______________________________main
title()

#make function to print menu
def coffee():
  print("-------------")
  print("1.Flat white $3.00")
  print("2.Cappuccino $3.00")
  print("3.Latte $3.50")
  print("4.Decaf $3.00")
  print("5.Hot Choccolate $4.00")
  print("-------------")

#Coffee prices in a list 
prices = ["3.00","3.00","3.50","3.00","4.00",]

#Make function to ask customer for their name and menu
def username(name):
  print("Welcome " + name)

#_____________________________main
username(input("(っ◔◡◔)っWhat may I call you dear customer? "))

#Make a function for an option to show the Cafe's menu
def menu():
  ask_menu = input("Would you like to see the menu? [Yes/No]".lower())
  while True:
    if ask_menu == 'y' or ask_menu == 'yes':
      coffee()
      break
    elif ask_menu == 'n' or ask_menu == 'no':
      print("Do you not want to order?")
      menu()
      break
      
    else:
      print("Please answer either yes or no")
      menu()
      break

#___________________________main
menu()

def order():
  
#Make function that asks for customer's order