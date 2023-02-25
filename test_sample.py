from sample import *

def get_calc(product_list,location):
    return Calculation(product_list,location).get_price()

def test_answer():
    item1 = Product("Apple", 20, 0.1, 10, 0.11)
    item2 = Product("Banana",50, 0.2, 5, 0.11)
    item3 = Product("Zipper",2, 0.01, 100, 0.24)
    item4 = Product("Clock", 1500, 1, 3, 0.32)
    product_list1 = [item1,item2,item3,item4]
    location = 101
    assert get_calc(product_list1, location) == 3437.5
