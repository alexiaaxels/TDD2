class Product():
    def __init__(self,item,price,weight,quantity,tax = 0.25):  # afh stendur að það eigi að taka in location til að finna út hvað skatturinn er mikill
        # en svo er beðið um tax input????? ?? ? ? ?? ? ? ?? ? ? ? ?? ? ? ?? ?? ? ? ? ? ? ? ?? ? ??
        self.item = item
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.tax = tax


class Calculate():
    def __init__(self,product_list,location=0):
        self.product_list = product_list
        self.location = location
    
    def get_shipping(self):
        #postcodes
        city = range(300,400)
        near_city = range(200,500)
        outskirts = range(0,700)
        if self.location in city: 
            shipping = 0
        elif self.location in near_city:
            shipping = 500
        elif self.location in outskirts:
            shipping = 1000
        else:
            shipping = 2000 
        return shipping
    
    def get_total(self):
        total_sum = 0
        shipping = self.get_shipping()
        for i in self.product_list:
            #weight in KG
            small = range(0,2)
            medium = range(2,3)
            large = range(3,5)
            if i.weight in small:
                shipping *= 1.1
            elif i.weight in medium:
                shipping *= 1.2
            elif i.weight in large:
                shipping *= 1.3
            else:
                shipping *= 1.5
            total_sum += (i.price*i.quantity*i.tax) + self.get_shipping()
        return total_sum

