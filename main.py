
#Make list of menu
menu = ["1.Flat white $3.00", "2.Cappuccino $3.00", "3.Latte $3.50", "4.Decaf $3.50", "5.Hot Chocolate $4.00"]

#Make introduction
def intro(name):
  print("Welcome " + name)
  yes = True
  while yes:
    show_menu = input("Would you like to see the menu?:")
    if show_menu.lower() == 'y' or show_menu.lower() == 'yes':
      print(*menu, sep = "\n")
      yes = False
    elif show_menu.lower() == 'n' or show_menu.lower() == 'no':
      print("Do you not want to order?")
    
    else:
      print("Please answer either yes or no")
      
#Make list for order
Coffee = [0, 0, 0, 0, 0]

#Function for asking the customer for their choice & show customer their order
def order():
  yes = True
  while yes:
    choice = input("Please Choose from the menu [1-5]: ")
    if choice == "1":
      print("")
      print("you orderd a Flat white")
      Coffee[0] += 1
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4]) 
      print("")
      print("Would you like to order anything else? (If not say no) ")
    elif choice == "2":
      print("")
      print("you orderd a Cappuccino")
      Coffee[1] += 1 
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4])
      print("")
      print("Would you like to order anything else? (If not say no) ")
    elif choice == "3":
      print("")
      print("you orderd a Latte")
      Coffee[2] += 1
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4])
      print("")
      print("Would you like to order anything else? (If not say no) ")
    elif choice == "4":
      print("")
      print("you orderd a Decaf")
      Coffee[3] += 1
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4])
      print("")
      print("Would you like to order anything else? (If not say no) ")
    elif choice == "5":
      print("")
      print("you orderd a Hot Chocolate")
      Coffee[4] += 1
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4])
      print("")
      print("Would you like to order anything else? (If not say no) ")
    elif choice == 'n' or choice == 'no':
      print("")
      print("[Your order]\nFlat white:", Coffee[0], "\nCappuccino:", Coffee[1], "\nLatte:", Coffee[2], "\nDecaf:", Coffee[3], "\nHot Chocolate:", Coffee[4])
      yes = False
    else:
      print("")
      print("Please answer between 1-5")

#Execute all functions
intro(input("Name:"))
order() 

#Add up Everything and show total
pay = 0

if Coffee[0] >= 1:
  pay += 3 * Coffee[0]
if Coffee[1] >= 1:
  pay += 3 * Coffee[1]

if Coffee[2] >= 1:
  pay += 3.5 * Coffee[2]
  
if Coffee[3] >= 1:
  pay += 3.5 * Coffee[3]
  
if Coffee[4] >= 1:
  pay += 4 * Coffee[4]

print("")
print("Payment Total: $",pay, )




