# SuperShopManager

SuperShopManager is a RESTful API project developed for a Super Shop Management system, built as a part of Programming II course. The API allows management of customers, products, orders, and special discounts through a clean and well-defined interface to simulate real-world shop operations.

## Features

### Management of Customers
- Retrieve a list of all customers or specific customer data.
- Register, update, or delete customers including details such as customer ID, date of birth, shipping address, email, and bonus points.
- Customer account verification via a random number and temporary passwords for password resets.

### Management of Products
- Add or remove product units (quantities available).
- Get detailed information about products.
- Manage product inventory upon sales and reorder low-stock items automatically.

### Management of Customer Orders
- Each customer has a shopping cart for adding/removing products and changing quantities.
- Place orders with simulated credit card validation using a 'mock credit card verification' service.
- Track purchase history to recommend new products.
- Bonus points earned per customer purchase for special offers.

### Management of Festival and Weekend Sales Discounts
- Apply special discounts valid for a limited period on certain product categories.

## API Implementation

- Developed in Python using Flask-RESTful.
- Supports HTTP methods: GET, POST, PUT, DELETE.
- JSON as the primary data exchange format.
- Fully adheres to REST API standards.
