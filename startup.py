from OwlveyGateway import OwlveyGateway
from datetime import datetime, timedelta
import  pandas as pd
import random
import math

if __name__ == "__main__":
    client_id = "CF4A9ED44148438A99919FF285D8B48D"
    secret_key = "0da45603-282a-4fa6-a20b-2d4c3f2a2127"

    owlvey = OwlveyGateway("http://localhost:50001","http://localhost:47002", client_id, secret_key)
    customers = owlvey.get_customers_lite()
    customer = next(filter(lambda c: c['name'] == "EShopping", customers))    
    products = owlvey.get_products_lite(customer_id = customer["id"])
    product = next(filter(lambda c: c['name'] == "Amazing Product", products))    
    sources = owlvey.get_sources(product_id=product["id"])

    
    data = list()
    for item in sources:                
        for i in range(365):            
            start = datetime(2020, 1, 1, 0, 0, 0) + timedelta(days=i)            
            for j in range(24):                                
                end = start + timedelta( minutes=59, seconds=59)

                total = math.floor(random.uniform(100,1000))

                if item["name"]  in ["LoginController:PreLogin", "LoginController::Login", 
                                    "CatalogController::LoadSilders", "CatalogController::LoadBanners", 
                                    "CatalogController::LoadProducts", "CatalogController::LoadAwards", 
                                    "CatalogController::LoadNotifications", "CatalogController::LoadCategories"]:                
                    ava_prop = random.normalvariate(0.99, 0.01)                    
                    exp_prop = random.normalvariate(0.98, 0.01)
                    lat =  round(random.normalvariate(1000, 200), 3)
                    #random.choices([0.65, 0.95, 0.98, 0.989, 0.99, 0.999], [0.1, 0.1 , 0.2 ,0.2 , 0.2 , 0.2],  24)                    
                else:
                    ava_prop = random.normalvariate(0.95, 0.4)                    
                    exp_prop = random.normalvariate(0.97, 0.4)
                    lat =  round(random.normalvariate(1000, 200), 3)

                ava_prop = ava_prop if ava_prop <= 1 else 1
                exp_prop = exp_prop if exp_prop <= 1 else 1  
                good = math.floor(total * ava_prop)
                experience = math.floor(total * exp_prop)

                experience = experience if experience >= 0 else 0
                good = good if good >= 0 else 0
                lat = lat if lat >= 0 else 0
                
                data.append("{};{};{};{};{};{};{}\n".format(item["name"], start, end, total, 
                                                good, experience, lat))                
                start = end + timedelta(seconds=1)
                
    with open('data.csv', 'w+') as f:
        f.writelines(data)  
    
    
    



        

        
        



    

