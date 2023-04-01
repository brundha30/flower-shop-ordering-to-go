import json
import re
import random
class User:
    
    bouquet_list = {"1":"Orchid Hand Bunch - Rs.300",
                    "2":"Roses - Rs.350",
                    "3":"Bunch of mixed roses - Rs.375",
                    "4":"Double Layered Gerbera - Rs.400",
                    "5":"Yellow rose hunch - Rs.510",
                    "6":"Rose vase - Rs.540",
                    "7":"Roses and Gerberas - Rs.765",
                    "8":"Red and yellow roses - Rs.1190",
                    "9":"White Lily - Rs.550",
                    "10":"Pink Gerbera - Rs.550"}
    
    order_history = []
    
    
    def __init__(self):
    
        self.user_detail = {}
        
        
    def registration(self):
        
        self.user_id=random.randint(1,1001)
        self.fullname =input("Enter your full name:")
        while True:
            self.phonenumber =input("Enter your phonenumber:")
            pattern = re.findall("[6-9[0-9]{9}",self.phonenumber)
            if pattern:
                print("Valid phone number.")
                break
            else:
                print("Invalid phone number.")
        while True:
            self.email =input("Enter your email:")
            regex = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',self.email)
            if regex:
                print("Valid email.")
                break
            else:
                print("Invalid Email")
        self.address=input("Enter your address:")
        while True:
            self.password = input("Create a new password using specified characters (eg:'AbcBe333') :")
            password = re.findall("[a-zA-Z0-9]",self.password)
            if len(password)<8:
                if password:
                    print("Valid Password")
                    break
                else:
                    print("Invalid Password")
            else:
                print("Invalid Password")
        
        self.details = {"Fullname":self.fullname,
                        "Phone Number":self.phonenumber,
                        "Email":self.email,
                        "Address":self.address,
                        "Password":self.password}
        
        self.user_detail[self.user_id] = self.details
        
        with open("User_details.json","w") as f:
            json.dump(self.user_detail,f)
        return self.user_detail
    
    def log_in(self):
        
        email = input("Enter your email:")
        password = input("Enter your password:")
        while True:
            if email==self.email and password==self.password:
                print("Welcome,Login Successfull!")
                break
            else:
                print("Sorry! Please enter your valid email and password.")
                break
        return " "
    
    def selected_order(self,order_id):
        self.order_history.append(self.bouquet_list[order_id])    
        return self.bouquet_list[order_id]
    
    def update_profile(self):
        
        update_profile=int(input("Enter the number:"))
        print("*"*30)
        if update_profile== 1:
            self.fullname =input("Enter your full name:")
            
        elif update_profile == 2:
            while True:
                self.phonenumber =input("Enter your phonenumber:")
                pattern = re.findall("[6-9[0-9]{9}",self.phonenumber)
                if pattern:
                    print("Valid phone number.")
                    break
                else:
                    print("Invalid phone number.")
        
        elif update_profile == 3:
            while True:
                self.email =input("Enter your email:")
                regex = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',self.email)
                if regex:
                    print("Valid email.")
                    break
                else:
                    print("Invalid Email")
                
        elif update_profile == 4:
            self.address=input("Enter your address:")
        
        elif update_profile == 5:
            while True:
                self.password = input("Create a new password using specified characters (eg:'AbcBe333') :")
                password = re.findall("[a-zA-Z0-9]",self.password)
                if len(password)<8:
                    if password:
                        print("Valid Password")
                        break
                    else:
                        print("Invalid Password")
                else:
                    print("Invalid Password")
        
        self.details = {"Fullname":self.fullname,
                        "Phone Number":self.phonenumber,
                        "Email":self.email,
                        "Address":self.address,
                        "Password":self.password}
        
        self.user_detail[self.user_id] = self.details            
        print("Your updated profile is:",self.user_detail)
        
        with open("User_details.json","w") as f:
            json.dump(self.user_detail,f)
        return " "