import uuid


class Customer:
    def __init__(self, name, email, address, dob):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.email = email
        self.bonus_points = 0
        self.status = "unverified"
        self.verification_token = str(uuid.uuid4())[:5]
        self.dob = dob
        self.password = None
        self.temppw = None
        self.shopping_cart = {}
        self.returnable = 14

    def verify(self, token):
        if self.verification_token == token:
            self.status = "verified"
            self.verification_token = None
        return self.status == "verified"

    def update(self, name, address, dob):
        if not name: # if the name is empty return False
            return False
        self.name = name
        self.address = address
        self.dob = dob
        return True

    def generate_temporary_password(self):
        self.temppw= str(uuid.uuid4())[:5] # generate a random password of 5 characters
        return self.temppw

    def reset_password(self,temporary_password,new_password):
        if self.temppw != temporary_password: #if the passowrd doesnt match the tp it gives an error message instead of just returning false
            return False
        else:
            self.password = new_password # if the password matches the tp it changes the password
            return True

    def addToShoppingCart(self, product_id, quantity,my_shop):#my_shop bc thats how i can access my_shops functions
        if not my_shop.getProductById(product_id): # if the product does not exist return false
            return False
        stock = my_shop.getProductById(product_id).quantity # if the product exists get the quantity of the product
        if stock >= int(quantity): # if the quantity is less than the stock
            if int(quantity) == -1:  # if the quantity is -1 it means that the user wants to delete the product from the shopping cart
                if product_id in self.shopping_cart:
                    self.shopping_cart.pop(product_id) # deleting the product from the shopping cart
                    return True
                return False
            elif int(quantity) > 0: # if the quantity is greater than 0 it means that the user wants to add the product to the shopping cart
                self.shopping_cart[product_id] = int(quantity) # adding the product to the shopping cart
                return True
        return False



    def returnBonusPoints(self):
        return self.bonus_points # returning the bonus points



    def addBonusPoints(self,bonus_points):
        self.bonus_points += int(bonus_points) # adding bonus points to the customer


















