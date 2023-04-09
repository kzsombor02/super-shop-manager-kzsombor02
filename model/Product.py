class Product():
    def __init__(self,product_id, name,serial_num, expiry, category,price ):
        self.product_id = product_id
        self.name = name
        self.serial_num = serial_num
        self.expiry = expiry
        self.category = category
        self.quantity = 0
        self.price = price





    def removeStock(self):
        self.quantity = 0





