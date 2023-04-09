from cardvalidator import luhn
from datetime import datetime
from datetime import timedelta
from model.Coupons import Coupons



class Shop:
    def __init__(self):
        self.customers = []
        self.products = []
        self.customer_purchase_history = []
        self.coupons = []



    def addProduct(self, p):
        self.products.append(p)


    def deleteProduct(self, product_id):
        product = None
        for p in  self.products:
            if p.product_id == product_id:
                product = p
        if product:
            self.products.remove(product)
            return True
        else:
            return False
    def addCustomer(self, c):
        c1 = self.getCustomerbyEmail(c.email)
        if c1 == None:  # customer does not exist with the given email address
            self.customers.append(c)
            return True
        else:
            return False

    def removeCustomer(self, c):
        self.customers.remove(c)

    def getCustomer(self, cust_id):
        for c in self.customers:
            if c.customer_id == cust_id:
                return c
        return None

    def getCustomerbyEmail(self, email):
        for c in self.customers:
            if c.email == email: # checking if the email is the same as the one in the arguments
                return c # returning the customer

    def changeStock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id: # checking if the id is the same as the one in the arguments
                product.quantity = int(quantity) # changing the quantity of the product
                return True
        # No else bc if the first product doesnt match the given id it will immediateky return the product does not exist message without checking the other products
        return False

    def getProductById(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return False

    def sellProduct(self, customer_id, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id: # checking if the id is the same as the one in the arguments
                if product.quantity >= int(quantity): # checking if there is enough quantity
                    product.quantity -= int(quantity)  # substracting the quantity of the product
                    product.threshold += int(quantity)
                    purchase_history = {
                        "customer_id": customer_id,
                        "product_id": product_id,
                        "quantity": quantity
                    }
                    self.customer_purchase_history.append(purchase_history) # adding the purchase history to the list
                    return True
                else:
                    return False


    def removeProduct(self,product_id,reason):
        for product in self.products:
            if product.product_id == product_id:  # checking if the id is the same as the one in the arguments
                product.removeStock() # calling the removeStock method
                return True
        return False

    def reorderProduct(self, product_id):
        must_reorder = []
        for product in self.products:
            if product.product_id == product_id: # checking if the id is the same as the one in the arguments
                if product.quantity < product.threshold:
                    must_reorder.append(product)
        return must_reorder





    def confirmOrder(self,credit_card_number,customer_id):
        customer = self.getCustomer(customer_id) # getting the customer
        if not luhn.is_valid(credit_card_number): # checking if the credit card number is valid
           # print("test")
            return False
        deleted = []
        for product_id,qty in customer.shopping_cart.items(): # looping through the shopping cart
            stock = self.getProductById(product_id).quantity # getting the quantity of the product
            if qty < stock: # quantity in this case is the stock of how many items we have
                stock -= qty # substracting the quantity from the stock
                self.changeStock(product_id,stock) # changing the stock
                deleted.append(product_id) # removing from the dictionary
                customer.addBonusPoints(int(qty)*int(self.getProductById(product_id).price)) #depending on what is the amount of quantity for a product id I * the price by that much
                purchase_history = {
                    "customer_id": customer_id,
                    "product_id": product_id,
                    "quantity": qty,  # quantity is the amount of items in the shopping cart
                    "order_date": datetime.today(), # setting the order date to the current date
                    "delivery_date": datetime.today() + timedelta(days=1) # setting the delivery date to the next day
                }
                self.customer_purchase_history.append(purchase_history)
        for items in deleted: # cannot delete from dict while in for loop -> append the items i want to delete to an empty list and aftert the for loop i delete it from the dictionary
            customer.shopping_cart.pop(items) # deleting the items from the shopping cart
        return True


    def getOrder(self, customer_id):
        orders = []
        for order in self.customer_purchase_history:
            if order["customer_id"] == customer_id:
                orders.append(order)
        return orders

    def returnOrder(self,customer_id):
        returnable_orders = []
        for order in self.customer_purchase_history:
            if order["customer_id"] == customer_id:
                day_since_order = (datetime.today() - order["order_date"]) # getting the difference between the current date and the order date to calculate how many days have passed since the order
                if day_since_order.days <= 14: # checking if the order is still returnable
                    returnable_orders.append(order) # adding the order to the list
        return returnable_orders



    def recommendation(self,customer_id):
        recommendations = []
        orders = self.getOrder(customer_id) # getting the orders of the customer
        if len(orders) < 10: # checking if the customer has enough orders to get recommendations
            return False
        else:
            for order in orders[:10]: # gets the first 10 orders from purchase history
                recommendations.append(self.getProductById(order["product_id"])) # adding the product to the list
            return recommendations


    def newCoupon(self,number,product_category,validity, discount_percentage):
        new_coupon = Coupons(number,product_category,validity, discount_percentage) # creating a new coupon
        if number.isnumeric() and len(number) == 10: #checking if the length of the couping is appropriate and if it is nan integer
            self.coupons.append(new_coupon) # adding the coupon to the list
            return True
        else:
            return False

    def getCoupons(self):
        valid_coupons = []
        for coupon in self.coupons:    # converting the string to date
            if datetime.today().date() < datetime.strptime(coupon.validity, '%Y.%m.%d').date(): # checking if the coupon is still valid by comparing the current date to the validity date
                valid_coupons.append(coupon)
                return valid_coupons
        return self.coupons


