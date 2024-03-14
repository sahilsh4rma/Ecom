# E-commerce Site Source Code

This repository contains the source code for an e-commerce website developed using Django.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [File Structure](#file-structure)
4. [Functionality](#functionality)
5. [Contributing](#contributing)
6. [License](#license)

## Overview

This e-commerce website allows users to browse products, view product details, add products to the cart, and proceed to checkout. It includes features such as pagination for product listing, search functionality, and a simple checkout process. The project is built using Django, a high-level Python web framework, and utilizes HTML, CSS, and JavaScript for the frontend.

## Installation

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```
    cd e-commerce-site
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Django development server:

    ```
    python manage.py runserver
    ```

5. Access the website in your web browser at `http://localhost:8000`.

## File Structure

- **shop/**: Django app directory containing views, models, and templates.
  - **admin.py**: Configuration for Django admin panel.
  - **models.py**: Database models for products and orders.
  - **views.py**: Functions handling HTTP requests and rendering templates.
  - **templates/**: HTML templates for rendering pages.
- **static/**: Contains static files such as CSS, JavaScript, and images.
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django's command-line utility for managing the project.
- **README.md**: Documentation file.

## Functionality

- **Index Page**: Displays a list of products with pagination and search functionality.
- **Product Detail Page**: Shows detailed information about a specific product.
- **Checkout Page**: Allows users to review their cart items and enter shipping details before placing an order.
- **Add to Cart**: Users can add products to their cart, which is stored in the browser's local storage.
- **Persistent Cart**: The cart items persist across sessions using browser local storage.
- **Order Processing**: Upon checkout, users can submit their shipping details, which are saved in the database as an order.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Author

--Sahil
