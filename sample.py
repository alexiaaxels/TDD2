class Product():
    def __init__(self,item,price,weight,quantity,tax = None):  # afh stendur að það eigi að taka in location til að finna út hvað skatturinn er mikill
        # en svo er beðið um tax input????? ?? ? ? ?? ? ? ?? ? ? ? ?? ? ? ?? ?? ? ? ? ? ? ? ?? ? ??
        self.item = item
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.tax = tax

class Calculation():
    def __init__(self,product_list,location=0):
        self.product_list = product_list
        self.location = location
    
    def get_shipping_cost(self):
        print(self.location)
        no_shc = range(101,270) # postcodes for the capital
        shc1 = range(271,400) # postcodes for semi near the capital
        shc2 = range(401,700) # postcodes for rest of Iceland

        shipping_cost = 0

        if int(self.location) in no_shc:
            return shipping_cost
        elif int(self.location) in shc1:
            shipping_cost += 1000
        elif int(self.location) in shc2:
            shipping_cost += 2000 
        else:
            shipping_cost += 4000 # shipping out of Iceland

    def get_price(self):
        final = 0
        shipping_cost = self.get_shipping_cost()
        for i in self.product_list:
            if i.weight*i.quantity <= 2: # total weigth is less than 2 KG
                shipping_cost += 100
            elif i.weight*i.quantity <= 5: # total weight is less than 5 KG 
                shipping_cost += 1000
            elif i.weight*i.quantity <= 10: # total weight is less than 10 KG
                shipping_cost += 2000
            else:
                shipping_cost += 4000 # total weight is greater than 10 KG
            final += shipping_cost + i.price * i.tax * i.quantity
        return float(round(final,2))