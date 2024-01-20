# MVP Prioritization and covered endpoints:

1. As a company, I want all my products in a database:

API Endpoint: POST /products
Description: Allows the company to add products to the database.

2. As a client, I want to see an overview of all the products:

API Endpoint: GET /products
Description: Provides a list of all products for clients to view.

3. As a client, I want to view the details of a product:

API Endpoint: GET /products/{productId}
Description: Fetches the details of a specific product.

4. As a client, I want to add a product to my shopping cart:

API Endpoint: POST /cart/add
Description: Allows clients to add a product to their shopping cart.

5. As a client, I want to remove a product from my shopping cart:

API Endpoint: POST /cart/remove
Description: Enables clients to remove a product from their shopping cart.

6. As a client, I want to order the current contents in my shopping cart/As a client, I want to select a delivery date and time::

API Endpoint: POST /orders
Description: Allows clients to place an order based on the items in their shopping cart with delivery date.
