
from sample import *

def get_calc(product_list,location):
    return Calculate(product_list,location).get_total()

def test_answer1(): # different products, prices, weight and tax
    item1 = Product("Apple", 20, 0.1, 10,0.11)
    item2 = Product("Banana",50, 0.2, 5,0.11)
    item3 = Product("Zipper",2, 0.01, 100,0.24)
    item4 = Product("Clock", 1500, 1, 3,0.24)
    product_list = [item1,item2,item3,item4]
    location = 101
    assert get_calc(product_list,location) == 5177.5

def test_answer2(): # increase in price and weight
    item1 = Product("iPad", 50000, 1, 50,0.24)
    item2 = Product("iPhone",100000, 0.5, 40,0.24)
    item3 = Product("MacBook",300000, 2, 100,0.24)
    product_list = [item1,item2,item3]
    location = 300
    assert get_calc(product_list,location) == 8760000.0

def test_answer3(): # empty product list
    product_list = []
    location = 0
    assert get_calc(product_list,location) == 0

def test_answer4(): # product list containing only one item
    item1 = Product("Christmas tree", 7500, 8, 2, 0.5)
    product_list = [item1]
    location = 10000
    assert get_calc(product_list,location) == 9500.0

def test_answer5(): 
    item1 = Product("Basketball", 4000,0.5,5)
    item2 = Product("Basketball jersey", 14500,0.01,20,0.12)
    item3 = Product("Energy drinks",250,0.33,24,0.11)
    item4 = Product("Mirrors",3450,3,43,0.57)
    item5 = Product("Lip balms",140,0.0001,232,0.09)
    product_list = [item1,item2,item3,item4,item5]
    location = 500
    assert get_calc(product_list,location) == 132942.7
    
def test_answer6(): #no taxes
    item1 = Product("Blanket", 1000, 0.1,10,0)
    item2 = Product("TV",40000,4,100,0)
    product_list = [item1,item2]
    location = 0
    assert get_calc(product_list,location) == 4012000


