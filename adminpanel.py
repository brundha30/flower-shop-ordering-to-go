import json
import random
class AdminPanel:
    
    def __init__(self):
        self.bouquet_list = {}
        
    def admin_login(self,username,password):
        
        if username =="admin" and password == "admin":
            return True
        return False
            
        
    def add_new_bouquet(self):
            self.bouquet_id = random.randint(1,21)
            self.name = input("Bouquet Name:")
            self.size = input("Bouquet Size:")
            self.price =int(input("Bouquet Price:"))
            self.discount = int(input("Bouquet Discount:"))
            self.stock = int(input("Bouquet Stock:"))
            
            self.details ={"Name":self.name,
                           "Size":self.size,
                           "Price":self.price,
                           "Discount":self.discount,
                            "Stock":self.stock}
            self.bouquet_list[self.bouquet_id] = self.details
            
            with open("Bouquet_list.json","w") as f:
                json.dump(self.bouquet_list,f)
            return self.bouquet_list
        
    def view_bouquet_details(self):
        for i,j,k in self.bouquet_list.items():
            print(list((i,j,k)))
        return " "
    
    def edit_bouquet_details(self):
        id_bouquet=int(input("Enter the id you want to edit:"))
        for i in self.bouquet_list[self.bouquet_id]:
            #print(i)
            self.bouquet_list[id_bouquet]["Name"] = "Rose Vase"
            self.bouquet_list[id_bouquet]["Size"] = "Large"
            self.bouquet_list[id_bouquet]["Price"] = "540"
            self.bouquet_list[id_bouquet]["Discount"] = "20"
            self.bouquet_list[id_bouquet]["Stock"] = "5"
            
            with open("Bouquet_list.json","w") as f:
                json.dump(self.bouquet_list,f)
            print("Updated bouquet list:",self.bouquet_list)
            return " "
        
    def remove_bouquet_details(self):
            bouquetid =int(input("Enter the id you want to remove:"))
            del self.bouquet_list[bouquetid]
         
            with open("Bouquet_list.json","w") as f:
                json.dump(self.bouquet_list,f)
            print("Remaining bouquet list:",self.bouquet_list)
            return " "