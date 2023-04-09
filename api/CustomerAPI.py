from flask import jsonify, request
from flask_restx import Resource, Namespace

from model.Customer import Customer
from model.data import my_shop

CustomerAPI = Namespace('customer',
                        description='Customer Management')


@CustomerAPI.route('/')
class GeneralCustomerOps(Resource):

    @CustomerAPI.doc(description="Get a list of all customers")
    def get(self):
        return jsonify(my_shop.customers)

    @CustomerAPI.doc(
        description="Register a new customer",
        params={'address': 'Customers address',
                'name': 'Customers name',
                'email': 'Customer Email',
                'dob': 'Customer birthday'})
    def post(self):
        # get the post parameters
        args = request.args
        name = args['name']
        email = args['email']
        address = args['address']
        dob = args['dob']
        new_customer = Customer(name, email, address, dob) # create a new customer object
        # add the customer
        if my_shop.addCustomer(new_customer): # add the customer to the shop
            return jsonify(new_customer)
        else:
            return jsonify("Customer with the email address already exists")


@CustomerAPI.route('/<customer_id>')
class SpecificCustomerOps(Resource):
    @CustomerAPI.doc(description="Get data about a particular customer")
    def get(self, customer_id):
        search_result = my_shop.getCustomer(customer_id)
        return jsonify(search_result)  # this is automatically jsonified by flask-restx

    @CustomerAPI.doc(description="Delete an existing customer")
    def delete(self, customer_id):
        c = my_shop.getCustomer(customer_id)
        if not c:
            return jsonify("Customer ID {cust_id} was not found")
        my_shop.removeCustomer(c)
        return jsonify("Customer with ID {cust_id} was removed")

    @CustomerAPI.doc(
        description="Update customer data",
        params={'address': 'Customers address',
                'name': 'Customers name',
                'email': 'Customer Email',
                'dob': 'Customer birthday'})
    def put(self, customer_id):
        args = request.args
        name = args['name']
        address = args['address']
        dob = args['dob']
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found.")
        if customer.update(name, address, dob):
            return jsonify(customer)
        else:
            return jsonify("Customer update failed.")

@CustomerAPI.route('/<customer_id>/add2cart')
class addToCart(Resource):
    @CustomerAPI.doc(description="add or remove a product form cart",
                     params={'product_id':'product id','quantity':'quantity of the product'})
    def put(self,customer_id):
        args = request.args
        product_id = args["product_id"]
        quantity = args["quantity"]
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found")
        if customer.addToShoppingCart(product_id, quantity,my_shop): # if product is added to cart
            return jsonify("Product added to cart")
        else:
            return jsonify("Invalid quantity")


@CustomerAPI.route("/<customer_id>/order")
class confirmOrder(Resource):
    @CustomerAPI.doc(description="confirm an order",
                     params={
                             "credit_card_number":"credit card number","shipping_address":"shipping address"})
    def post(self,customer_id):
        args = request.args
        credit_card_number = args["credit_card_number"]  # get credit card number
        customer = my_shop.getCustomer(customer_id) # get customer
        if customer is None: # if customer is not found
            return jsonify("Customer not found")
        if my_shop.confirmOrder(credit_card_number,customer_id): # if order is confirmed
            return jsonify("Order confirmed")
        else:
            return jsonify("Order failed")





@CustomerAPI.route("/<customer_id>/orders")
class CustomerOrders(Resource):
    @CustomerAPI.doc(description="keeping track of orders")
    def get(self,customer_id):
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found")
        orders = my_shop.getOrder(customer_id) # get orders
        if len(orders) == 0: # if no orders are found
            return jsonify("No orders found")
        else:
            return jsonify(orders) # returning the orders

@CustomerAPI.route("/<customer_id>/returnable")
class CustomerReturns(Resource):
    @CustomerAPI.doc(description="keeping track of returns")
    def get(self,customer_id):
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found")
        orders = my_shop.returnOrder(customer_id)
        if len(orders) == 0: # if no orders are found
            return jsonify("No orders found")
        else:
            return jsonify(orders)


@CustomerAPI.route("/<customer_id>/recommendations")
class recommendations(Resource):
    @CustomerAPI.doc(description="Showing recommended items")
    def get(self,customer_id):
        customer = my_shop.getCustomer(customer_id)
        if customer is None:
            return jsonify("Customer not found")
        recommendations = my_shop.recommendation(customer_id) # get recommendations
        if recommendations != False: # if recommendations are found
            return jsonify(recommendations)
        else:
            return jsonify("Not enough orders for recommendations")




@CustomerAPI.route("/<customer_id>/points")
class CustomerPoints(Resource):
    @CustomerAPI.doc(description="keeping track of points")
    def get(self,customer_id):
        if my_shop.getCustomer(customer_id): # if customer is found
            return jsonify(my_shop.getCustomer(customer_id).returnBonusPoints()) # return bonus points
        else:
            return jsonify("Customer not found")

    @CustomerAPI.doc(description="adding bonus points", params={"bonus_points": "bonus points"})
    def put(self,customer_id):
        args = request.args # get bonus points
        bonus_points = args["bonus_points"]
        if my_shop.getCustomer(customer_id):
            my_shop.getCustomer(customer_id).addBonusPoints(bonus_points)  # how many bonus points i want to input
            return jsonify("Points added")
        else:
            return jsonify("Customer not found")


CouponsAPI = Namespace('coupons',
                       description='Coupon Management')

@CouponsAPI.route("/")
class Coupons(Resource):
    @CouponsAPI.doc(description="Add new coupon", params={"number": "coupon number",
                    "product_category": "product category","validity": "validity","discount_percentage": "discount percentage"})
    def post(self):
        args = request.args # get coupon details
        number = args["number"]
        product_category = args["product_category"]
        validity = args["validity"] # validity in days
        discount_percentage = args["discount_percentage"]
        if my_shop.newCoupon(number, product_category, validity, discount_percentage): # if coupon is added
            return jsonify("Coupon added")
        else:
            return jsonify("Coupon not added")

    @CouponsAPI.doc(description="Get all valid coupons")
    def get(self):
        return jsonify(my_shop.getCoupons())





@CustomerAPI.route('/verify')
class CustomerVerficiation(Resource):
    @CustomerAPI.doc(
        description="Verify customer email address",
        params={'token': 'Verification Token sent by email',
                'email': 'Customer Email'})
    def put(self):
        args = request.args # get token and email
        token = args['token']
        email = args['email']
        customer = my_shop.getCustomerbyEmail(email) # get customer
        if customer is None: # if customer is not found
            return jsonify("Customer not found.")
        if customer.verify(token): # if customer is verified
            return jsonify("Customer is now verified.")
        else:
            return jsonify("Invalid token.")


@CustomerAPI.route('/pwreset')
class CustomerPWReset(Resource):
    @CustomerAPI.doc(
        description="Generate a temporary password and send via email.", )
    def post(self):
        customer_id = request.args["customer_id"] # get customer id
        c = my_shop.getCustomer(customer_id) # get customer
        return jsonify(c.generate_temporary_password()) #  generate temporary password

    @CustomerAPI.doc(
        description="Allow password reset based on the temporary password",
        params={'temp_pw': 'Password sent by email',
                'new_pw': 'New password'})
    def put(self):
        args = request.args
        customer_id = args["customer_id"]
        temp_pw = args["temp_pw"]  # get temporary password
        new_pw = args["new_pw"]  # get new password
        c = my_shop.getCustomer(customer_id)
        if not c:
            return jsonify("wrong customer id")
        if c.reset_password(temp_pw,new_pw): # if password is reset
            return jsonify("Updated")
        else:
            return jsonify("Wrong temporary password")


