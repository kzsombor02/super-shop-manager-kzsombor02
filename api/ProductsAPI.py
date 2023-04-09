from flask import jsonify, request
from flask_restx import Resource, Namespace

from model.Customer import Customer
from model.Product import Product
from model.data import my_shop

ProductAPI = Namespace('product',
                       description='Product Management')


@ProductAPI.route('/')
class AddProductA(Resource):
    @ProductAPI.doc(descripiton= "Adding products" ,params={'name': 'Product name',
                            'expiry': 'expiry date',
                            'category': 'product category',
                            "product_id": "product_id",
                            "serial_num":"serial_num",
                            "price": "price"})
    def post(self):
        # get the post parameters
        args = request.args
        product_id = args["product_id"]
        name = args['name']
        serial_num = args["serial_num"]
        expiry = args['expiry']
        category = args['category']
        price = args["price"]


        new_product = Product(product_id,name,serial_num, expiry, category,price)
        # add the product
        if my_shop.getProductById(product_id): # if the product already exists
            return jsonify("Product with the id already exists")
        else:
            my_shop.addProduct(new_product) # add the product to the shop
            return jsonify(new_product)




@ProductAPI.route("/<product_id>")
class single_product(Resource):
    def delete(self,product_id):
       if my_shop.deleteProduct(product_id): # if the product is deleted successfully
           return jsonify("Deleted")
       else:
           return jsonify("Not found")

    @ProductAPI.doc(descripiton="changing stock", params={"quantity": "quantity"})
    def put(self,product_id):
        quantity = request.args["quantity"] # get the quantity
        if my_shop.changeStock(product_id,quantity): # if the stock is changed successfully
            return jsonify("Stock was changed!")
        else:
            return jsonify("Product does not exist!")

    def get(self,product_id):
        if my_shop.getProductById(product_id): # if the product is found
            return jsonify(my_shop.getProductById(product_id)) # return the product
        else:
            return jsonify("Product does not exist!")


@ProductAPI.route("/sell")
class sellProduct(Resource):
    @ProductAPI.doc(descripiton="selling items", params={"customer_id": "Customer id", "product_id": "Product id", "quantity": "quantity"})
    def put(self):
        customer_id = request.args["customer_id"]
        product_id = request.args["product_id"]
        quantity = request.args["quantity"]
        if my_shop.sellProduct(customer_id,product_id,quantity):
            return jsonify("Product was sold!")
        else:
            return jsonify("Product does not exist!")

@ProductAPI.route("/remove")
class removeProduct(Resource):
    @ProductAPI.doc(descripiton="removing items", params={"product_id": "Product id", "reason": "reason for removal"})
    def put(self):
        args = request.args
        product_id = args["product_id"]
        reason = args["reason"]
        if my_shop.removeProduct(product_id,reason):
            return jsonify("Product was removed")
        else:
            return jsonify("Product not found")




ProductsAPI = Namespace('products',
                       description='Products Management')

@ProductsAPI.route("/")
class GetProducts(Resource):
    def get(self):
        return jsonify(my_shop.products)

@ProductsAPI.route("/reorder")
class Reorder(Resource):
    @ProductsAPI.doc(descripiton="reordering items", params={"product_id": "Product id"})
    def get(self):
        args = request.args
        product_id = args["product_id"]
        return jsonify (my_shop.reorderProduct(product_id))




