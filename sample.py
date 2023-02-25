class Product():
    def __init__(self,item,price,weight,quantity,tax = None):  # afh stendur að það eigi að taka in location til að finna út hvað skatturinn er mikill
        # en svo er beðið um tax input????? ?? ? ? ?? ? ? ?? ? ? ? ?? ? ? ?? ?? ? ? ? ? ? ? ?? ? ??
        self.item = item
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.tax = tax


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
        
        #weight in KG
        small = range(0,1.5)
        medium = range(1.5,3)
        large = range(3,5)
        if self.weight in small:
            shipping *= 1.1
        elif self.weight in medium:
            shipping *= 1.2
        elif self.weight in large:
            shipping *= 1.3
        else:
            shipping *= 1.5
        return shipping


    def get_price(self):
        shipping = self.get_shipping()
        return (self.price + self.tax + shipping)*self.quantity
    
    