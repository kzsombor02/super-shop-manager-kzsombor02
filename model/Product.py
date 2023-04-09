class Product():
    def __init__(self,product_id, name,serial_num, expiry, category,price ):
        self.product_id = product_id
        self.name = name
        self.serial_num = serial_num
        self.expiry = expiry
        self.category = category
        self.quantity = 0
        self.price =  price

    # def new_product(self,product_id,name,serial_num,expiry_date,category,quantity):
    #     new_product ={
    #         "product_id":product_id,
    #         "name": name,
    #         "serial_num": serial_num,
    #         "expiry_date": expiry_date,
    #         "category": category,
    #         "quantity": quantity
    #     }

        # self.products.append(new_product)
        # return "The product was added succesfully!"

    def delete_product(self,product_id):
        for product in self.products:
            if product["product_id"] == product_id:
                self.products.remove(product_id)
                return "Product was deleted!"
        return "Product does not exist!"

#     def change_stock(self,product_id,quantity):
#         for product in self.products:
#             if product["product_id"] == product_id:
#                 product["quantity"] = quantity
#                 return "Stock was changed!"
# #No else bc if the first product doesnt match the given id it will immediateky return the product does not exist message without checking the other products
#         return "Product does not exist!"

    # def get_products(self):
    #     return self.products


    # def get_product_by_id(self,product_id):
    #     for product in self.products:
    #         if product["product_id"] == product_id:
    #             return product
    #     return "The product does not exits!"


    # def sell_product(self,customer_id, product_id,quantity):
    #     for product in self.products:
    #         if product["product_id"] == product_id: # checking if the id is the same as the one in the arguments
    #             if product["quantity"] >= quantity: #checking if there is enough quantity
    #                 product["quantity"] -= quantity#substracting the quantity of the product
    #                 purchase_history={
    #                     "customer_id": customer_id,
    #                     "product_id":product_id,
    #                     "quantity": quantity
    #
    #                 }
    #                 self.customer_purchase_history[customer_id].append(purchase_history)
    #                 return "Product sold successfully!"
    #             else:
    #                 return "Not enough quantity in inventory!"
    #     return "Product does not exist!"


    def removeStock(self):
        self.quantity = 0

    # def reorder_product(self,product_id,quantity):
    #     for product in self.products:
    #         if product.product_id == product_id:
    #             product.quantity += quantity
    #             return True
    #     return False



