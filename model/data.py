# the instance of shop, where all data is stored.
from model.Customer import Customer
from model.Shop import Shop
from model.Product import Product


my_shop = Shop()

# Test data
c1 = Customer("Markus Muelle", "markus.mueller@email.test", "1101 Vienna", "10.09.2001")
my_shop.addCustomer(c1)
p1 = Product("123","Zsombor","5435","tomorrow","diary","10")
my_shop.addProduct(p1)
my_shop.changeStock("123","200")
