from adminpanel import *
from user import *
import sys
ad=AdminPanel()
us=User()
while True:
    
    print("Press 1 for Admin Login")
    print("Press 2 for User Login")
    print("Press 3 for Exit")
    option = int(input("Enter your option:"))
    if option==1:
        print("***************************Admin Login***************************")
        temp = ad.admin_login()
        if temp:
            print("Press 1 for Add New Bouquet")
            print("Press 2 for View Bouquet List")
            print("Press 3 for Edit Bouquet List")
            print("Press 4 for Remove Bouquet List")
            choose=int(input("Enter your choice:"))
            if choose ==1:
                print(ad.add_new_bouquet())
                print(ad.add_new_bouquet())
                print(ad.add_new_bouquet())
                print("New Bouquet List Added Successfully!")
                print("*"*50)
            elif choose ==2:
                print(ad.view_bouquet_details())
                print("You have viewed your bouquet list!")
                print("*"*50)
            elif choose ==3:
                print(ad.edit_bouquet_details())
                print("You haved edited your bouquet list successfully!")
                print("*"*50)
            elif choose ==4:
                print(ad.remove_bouquet_details())
                print("Bouquet List removed successfully!")
                print("*"*50)
    elif option==2:
        print("***************************User SignUp***************************")
        print("Press R for Registration")       
        print("Press L for Login")               
        print("Press P for Place New Order")
        print("Press O for Order History")
        print("*"*50)
        choice=input("Enter your choice:").upper()
        if choice=="R":
            print(us.registration())
            print("Registration Successfull!")
            print("*"*50)
        elif choice =="L":
            print(us.log_in())
            print("*"*50)
        elif choice=="P":
            print("Choose 1 for Orchid Hand Bunch - Rs.300")
            print("Choose 2 for Roses - Rs.350")
            print("Choose 3 for Bunch of mixed roses - Rs.375")
            print("Choose 4 for Double Layered Gerbera - Rs.400")
            print("Choose 5 for Yellow rose hunch - Rs.510")
            print("Choose 6 for Rose vase - Rs.540")
            print("Choose 7 for Roses and Gerberas - Rs.765")
            print("Choose 8 for Red and yellow roses - Rs.1190")
            print("Choose 9 for White Lily - Rs.550")
            print("Choose 10 for Pink Gerbera - Rs.550")
            print("*"*50)
            order = int(input("Enter your order:"))
            print("Your ordered: ",order)
            print(f"Your selected order is:{list(map(us.selected_order,order))}")
            print("*"*50)
        elif choice == "O":
            print(f"Order history:{list(map(us.selected_order,order))}")
                          
        elif choice == "U":
            print("Choose 1 for Name")
            print("Choose 2 for Phonenumber")
            print("Choose 3 for Email")
            print("Choose 4 for Address")
            print("Choose 5 for Password")
            print("*"*10)
            update=int(input("Enter the number:"))
            print("*"*10)
            print(us.update_profile())
         
    elif option==3:
        print("Your order arrives earlier than you expected.")
        print("Thank you for ordering!")
        sys.exit()   
                
    else:
        print("OOPS! Please choose the valid option.") 