from flask import Flask
from flask_restx import Api

from api.CustomerAPI import CustomerAPI, CouponsAPI
from api.ProductsAPI import ProductAPI, ProductsAPI
from util.json_utils import ShopJsonEncoder

superShopApp = Flask(__name__)

# need to extend this class for custom objects, so that they can be jsonified
superShopApp.json_encoder = ShopJsonEncoder
superShopAPI = Api(superShopApp, version='1.0', title='SuperShopManager',
                   contact_email="22IMC10242@fh-krems.ac.at",
                   description='Shop Management API')

# Add all the parts of the API here
superShopAPI.add_namespace(CustomerAPI)
superShopAPI.add_namespace(CouponsAPI)
superShopAPI.add_namespace(ProductAPI)
superShopAPI.add_namespace(ProductsAPI)

if __name__ == '__main__':
    superShopApp.run(debug=False, port=7890)
