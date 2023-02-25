
from sample import *

def get_calc(product_list,location):
    return Calculate(product_list,location).get_total()

def test_answer1():
    item1 = Product("Apple", 20, 0.1, 10,0.11)
    item2 = Product("Banana",50, 0.2, 5,0.11)
    item3 = Product("Zipper",2, 0.01, 100,0.24)
    item4 = Product("Clock", 1500, 1, 3,0.24)
    product_list = [item1,item2,item3,item4]
    location = 101
    assert get_calc(product_list,location) == 5177.5

def test_answer2():
    item1 = Product("iPad", 50000, 1, 50,0.24)
    item2 = Product("iPhone",100000, 0.5, 40,0.24)
    item3 = Product("MacBook",300000, 2, 100,0.24)
    product_list = [item1,item2,item3]
    location = 300
    assert get_calc(product_list,location) == 8760000.0

