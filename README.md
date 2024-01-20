# Project Name

## Used Technologies

- Python: version 3.10
- Database: PostgreSQL (version 14.3)

## Setup Guide

To setup this project locally, use Python virtual environment. 

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install Requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Setup a local PostgreSQL server and update the following environmental variables in your .env file (given below are sample values):
    ```bash
    ENV DB_NAME=postgres
    ENV DB_USER=postgres
    ENV DB_PASSWORD=postgres
    ENV DB_HOST=db
    ENV DB_PORT=5432
    ```

4. Update the database with migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a super admin user:
    ```bash
    python manage.py createsuperadmin
    ```

6. Finally, start the server:
    ```bash
    python manage.py runserver
    ```

**Note:** If you are starting the server using 'docker-compose up', a superadmin user will be automatically created in the system using the following credentials:
- username: superadmin
- password: 1234

## MVP Prioritization and Covered Endpoints

1. **As a company, I want all my products in a database:**
    - API Endpoint: `POST /products`
    - Description: Allows the company to add products to the database.

2. **As a client, I want to see an overview of all the products:**
    - API Endpoint: `GET /products`
    - Description: Provides a list of all products for clients to view.

3. **As a client, I want to view the details of a product:**
    - API Endpoint: `GET /products/{productId}`
    - Description: Fetches the details of a specific product.

4. **As a client, I want to add a product to my shopping cart:**
    - API Endpoint: `POST /cart/add`
    - Description: Allows clients to add a product to their shopping cart.

5. **As a client, I want to remove a product from my shopping cart:**
    - API Endpoint: `POST /cart/remove`
    - Description: Enables clients to remove a product from their shopping cart.

6. **As a client, I want to order the current contents in my shopping cart/As a client, I want to select a delivery date and time:**
    - API Endpoint: `POST /orders`
    - Description: Allows clients to place an order based on the items in their shopping cart with delivery date.