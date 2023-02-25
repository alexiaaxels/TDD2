class Product():
    def __init__(self,item,price,weight,quantity,tax = None):  # afh stendur að það eigi að taka in location til að finna út hvað skatturinn er mikill
        # en svo er beðið um tax input????? ?? ? ? ?? ? ? ?? ? ? ? ?? ? ? ?? ?? ? ? ? ? ? ? ?? ? ??
        self.item = item
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.tax = tax

    def get_price(self):
        return (self.price + self.tax + self.shipping)*self.quantity