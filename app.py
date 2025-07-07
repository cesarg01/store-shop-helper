from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from dotenv import load_dotenv
import os
from my_functions import *

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


# JSON data of the steel
steel = {
    "smoothie_base": {
        "quantity": 2
    },
    "soda_cups": {
        "quantity": 1200,
        "sleeve": 50,
        "sleeves": 24
    },
    "soda_lids": {
        "quantity": 2000,
        "sleeve": 100,
        "sleeves": 20
    },
    "sixteen_oz_cups": {
        "quantity": 1000,
        "sleeve": 50,
        "sleeves": 20
    },
    "sip_lids": {
        "quantity": 1000,
        "sleeve": 100,
        "sleeves": 10
    },
    "paper_straws": {
        "quantity": 2000,
        "sleeve": 500,
        "sleeves": 4
    },
    "food_bags": {
        "quantity": 1000,
    },
    "pizza_boxes": {
        "quantity": 50
    },
    "cookie_bags": {
        "quantity": 1000
    },
    "croutons": {
        "quantity": 100
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guide', methods=['GET', 'POST'])
def get_shop_days():
    if request.method == 'POST':
        # Cannot get value of the form trying to get the id value. Added the <name> attribute to the form
        # to be able to get the value of 'shop_days'
        shop_days = request.form.get('shop_days', None)
        print(shop_days)

        

    return render_template('guide.html', shop_days=shop_days)


@app.route('/shop_info', methods=['GET', 'POST'])
def get_user_data():
    if request.method == 'POST':
        pizza = request.form.get("pizza_boxes1")
        # Process the data (e.g., save to database)
        result = {'message': 'Data received successfully', 'pizza': pizza}
        days = int(request.args.get('shop_day', None))
        print(days)
        print(jsonify(result))
        print(steel['cookie_bags']['quantity'])
        product_names = ['pizza_boxes', 'fc_soda', 'fe_soda', 'fc_smoothie', 'fe_smoothie', 'fc_mocha', 'fe_mocha"', 'kiosk_soda', 'kiosk_smoothie', 'kiosk_mocha"', 'fc_latte"', 'kiosk_latte"', 'fe_latte', 'bake_sales', 'ice_cream_sales', 'hotdog_sales']
        product_sales = []
        # Counter to key track where in the loop 
        counter = 0

        for product in product_names:
            total_product_sales = 0
            for day in range(1, days+1):
                # Check if any errors occur which means no sale for the product was found.
                try:
                    # Get the sale for the day and add it to the total
                    product_day_sale = request.form.get(product + str(day))
                    total_product_sales += int(product_day_sale)
                except (ValueError, TypeError):
                    print(f"Error: Item was not found.")
                
            #if product == 'pizza_boxes':
             #   product_sales.append(total_product_sales)
              #  total_pizza_sales = get_pizza_boxes(steel, total_product_sales)
               # print('You will need ', total_pizza_sales)
            # For each product id sales data add to list containing sales

            if product == product_names[counter]:
                product_sales.append(total_product_sales)
                print(product, product_sales[counter], counter)

            counter += 1
        # Convert all the sale info for each product into a nested dictionary
        product_sale_info = {}
        for i, j in zip(product_names, product_sales):
            product_sale_info[i] = {'sales': j}
        print(product_sale_info)

        total_beverage_sales = get_beverage_sales(steel, product_sale_info)

        projected_shop_items = {}
        projected_shop_items['Pizza boxes'] = get_pizza_boxes(steel, product_sale_info['pizza_boxes']['sales'])
        projected_shop_items['Soda cups'] = get_soda_cups(steel, total_beverage_sales['Soda'], product_sale_info['hotdog_sales']['sales'])
        projected_shop_items['Soda lids'] = get_soda_lids(steel, total_beverage_sales, product_sale_info['hotdog_sales']['sales'])
        projected_shop_items['16oz cups'] = get_clear_cups(steel, total_beverage_sales['Smoothie'], total_beverage_sales['Cold Brew'], product_sale_info['ice_cream_sales']['sales'])
        projected_shop_items['Straws'] = get_straws(steel, total_beverage_sales, product_sale_info['hotdog_sales']['sales'])
        projected_shop_items['Food bags'] = get_food_bags(steel, product_sale_info['hotdog_sales']['sales'], product_sale_info['bake_sales']['sales'])

        print(projected_shop_items)

    return render_template('shop_info.html', projected_shop_items=projected_shop_items)