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
            if c.email == email:
                return c

    def changeStock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = int(quantity)
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
                    purchase_history = {
                        "customer_id": customer_id,
                        "product_id": product_id,
                        "quantity": quantity
                    }
                    self.customer_purchase_history.append(purchase_history)
                    return True
                else:
                    return False


    def removeProduct(self,product_id,reason):
        for product in self.products:
            if product.product_id == product_id:
                product.removeStock()
                return True
        return False

    def reorderProduct(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += int(quantity)
                return True
        return False




    def confirmOrder(self,credit_card_number,customer_id):
        customer = self.getCustomer(customer_id)
        if not luhn.is_valid(credit_card_number):
            print("kuki")
            return False
        deleted = []
        for product_id,qty in customer.shopping_cart.items():
            stock = self.getProductById(product_id).quantity
            if qty < stock: # quantity in this case is the stock of how many items we have
                stock -= qty
                self.changeStock(product_id,stock)
                deleted.append(product_id) # removing from the dictionary
                customer.addBonusPoints(int(qty)*int(self.getProductById(product_id).price)) #depending on what is the amount of quantity for a product id I * the price by that much
                purchase_history = {
                    "customer_id": customer_id,
                    "product_id": product_id,
                    "quantity": qty,
                    "order_date": datetime.today(),
                    "delivery_date": datetime.today() + timedelta(days=1)
                }
                self.customer_purchase_history.append(purchase_history)
        for items in deleted: # cannot delete from dict while in for loop -> append the items i want to delete to an empty list and aftert the for loop i delete it from the dictionary
            customer.shopping_cart.pop(items)
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
                day_since_order = (datetime.today() - order["order_date"])
                if day_since_order.days <= 14:
                    returnable_orders.append(order)
        return returnable_orders



    def recommendation(self,customer_id):
        recommendations = []
        orders = self.getOrder(customer_id)
        if len(orders) < 10:
            return False
        else:
            for order in orders[:10]: # gets the first 10 orders from purchase history
                recommendations.append(self.getProductById(order["product_id"]))
            return recommendations


    def newCoupon(self,number,product_category,validity, discount_percentage):
        new_coupon = Coupons(number,product_category,validity, discount_percentage)
        if number.isnumeric() and len(number) == 10:
            self.coupons.append(new_coupon)
            return True
        else:
            return False

    def getCoupons(self):
        valid_coupons = []
        for coupon in self.coupons:
            if datetime.today().date() < datetime.strptime(coupon.validity, '%Y.%m.%d').date():
                valid_coupons.append(coupon)
                return valid_coupons
        return self.coupons


