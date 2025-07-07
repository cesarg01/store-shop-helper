'''
    File with functions to calculate how how much of each item to buy for the department to run for the
    day or for the next few days.
'''

import math

# Global variable
percent_incr = 20

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

# Get projected sales for item
def get_projected_sales(total_sales):
    # Formula to get projected sales
    new_sales_number = percent_incr * (total_sales/100)
    proj_sales = total_sales + new_sales_number

    return proj_sales

# Passing a reference of the steel dictionary
def get_pizza_boxes(steel, pizza_sold):
    # Get the projected sales
    proj_pizza_sales = get_projected_sales(pizza_sold)

    print(proj_pizza_sales)
    # Find out how many boxes to get
    total_pizza_boxes = proj_pizza_sales / steel["pizza_boxes"]["quantity"]
    # If when dividing by the quantity of boxes equates to a having a decimal add 1 to the total pizza
    # boxes needed.
    if(total_pizza_boxes % 1 != 0):
        total_pizza_boxes += 1
        total_pizza_boxes = math.trunc(total_pizza_boxes)

    return total_pizza_boxes

# Get total beverage sales and return a dictionary
def get_beverage_sales(steel, product_sale_info):

    total_beverage_sales = {'Soda': 0, 'Smoothie': 0, 'Cold Brew': 0}
    # Loop through the dictionary and sum all the valus associated with each item we are looking for
    for i in product_sale_info:
        if 'soda' in i.lower():
            total_beverage_sales['Soda'] += product_sale_info[i]['sales']
        
        elif 'smoothie'in i.lower():
            total_beverage_sales['Smoothie'] += product_sale_info[i]['sales']
        
        elif 'mocha' in i.lower() or 'latte' in i.lower():
            total_beverage_sales['Cold Brew'] += product_sale_info[i]['sales']

    print('This is how much soda was sold', total_beverage_sales['Soda'])

    return total_beverage_sales

# Get the number of straw sleeves needed
def get_straws(steel, total_beverage_sales, hot_dog_sales):

    straws_info = {'Straw boxes': 0, 'Straw sleeves': 0}

    drinks_sold = total_beverage_sales['Soda'] + total_beverage_sales['Smoothie'] + total_beverage_sales['Cold Brew'] + hot_dog_sales
    proj_drinks_sold = get_projected_sales(drinks_sold)
    straws_needed = proj_drinks_sold / steel["paper_straws"]["sleeve"]
    total_straw_boxes = proj_drinks_sold / steel["paper_straws"]["quantity"]

    if (straws_needed % steel["paper_straws"]["sleeve"]) > 0:
        straws_needed += 1
        total_sleeves = math.trunc(straws_needed)
        straws_info['Straw sleeves'] = total_sleeves

    if (total_straw_boxes % steel["paper_straws"]["quantity"]) > 0:
        total_straw_boxes += 1
        total_boxes = math.trunc(total_straw_boxes)
        straws_info['Straw boxes'] = total_boxes

    return straws_info

# Get how much soda lids will be needed
def get_soda_lids(steel, total_beverage_sales, hot_dog_sales):

    soda_lid_info = {'Soda lid boxes': 0, 'Soda lid sleeves': 0}

    drinks_sold = total_beverage_sales['Soda'] + hot_dog_sales
    proj_drinks_sold = get_projected_sales(drinks_sold)
    soda_lids_needed = proj_drinks_sold / steel["soda_lids"]["sleeve"]
    # Find out how many boxes of soda to get
    total_soda_lid_boxes = proj_drinks_sold / steel['soda_lids']['quantity']

    if (soda_lids_needed % steel["soda_lids"]["sleeve"]) > 0:
        soda_lids_needed += 1
        total_sleeves = math.trunc(soda_lids_needed)
        soda_lid_info['Soda lid sleeves'] = total_sleeves

    if (total_soda_lid_boxes % steel["soda_lids"]["quantity"]) > 0:
        total_soda_lid_boxes += 1
        total_boxes = math.trunc(total_soda_lid_boxes)
        soda_lid_info['Soda lid boxes'] = total_boxes

    return soda_lid_info

# Get how much soda will be needed
def get_soda_cups(steel, single_soda, combo_soda):

    # Dictionary that has info on how many boxes and sleeves you will need of soda
    soda_info = {'Soda boxes': 0, 'Soda sleeves': 0}

    total_soda = single_soda + combo_soda
    proj_soda_sales = get_projected_sales(total_soda)
    print("Projected soda sales: ", proj_soda_sales)

    # Find out how many sleeves to get
    total_soda_cups = proj_soda_sales / steel["soda_cups"]["sleeve"]
    # Find out how many boxes of soda to get
    total_soda_boxes = proj_soda_sales / steel['soda_cups']['quantity']
    # If when dividing by the quantity of boxes equates to a having a decimal add 1 to the total pizza
    # boxes needed.
    if(total_soda_cups % 1 != 0):
        total_soda_cups += 1
        total_sleeves = math.trunc(total_soda_cups)
        soda_info['Soda sleeves'] = total_sleeves

    if(total_soda_boxes % 1 != 0):
        total_soda_boxes += 1
        total_boxes = math.trunc(total_soda_boxes)
        soda_info['Soda boxes'] = total_boxes

    return soda_info

# Get how many 16oz cups we will need
def get_clear_cups(steel, total_smoothie, total_cold_brew, total_ice_cream):

    # Dictionary that has info on how many boxes and sleeves you will need of 16oz cups
    clear_cup_info = {'16oz boxes': 0, '16oz sleeves': 0}

    total_cups = total_smoothie + total_cold_brew + total_ice_cream
    proj_cup_sales = get_projected_sales(total_cups)
    print("Projected smoothie, cold brew, and ice cream sales: ", proj_cup_sales)

    # Find out how many sleeves to get
    total_clear_cups = proj_cup_sales / steel["sixteen_oz_cups"]["sleeve"]
    # Find out how many boxes of 16oz cups to get
    total_cup_boxes = proj_cup_sales / steel['sixteen_oz_cups']['quantity']
    # If when dividing by the quantity of boxes equates to a having a decimal add 1 to the total 
    # boxes needed.
    if(total_clear_cups % 1 != 0):
        total_clear_cups += 1
        total_sleeves = math.trunc(total_clear_cups)
        clear_cup_info['16oz sleeves'] = total_sleeves

    if(total_cup_boxes % 1 != 0):
        total_cup_boxes += 1
        total_boxes = math.trunc(total_cup_boxes)
        clear_cup_info['16oz boxes'] = total_boxes

    return clear_cup_info

def get_food_bags(steel, total_hot_dogs, total_bakes):
    food_bag_info = {'Food bag boxes': 0, 'Food bag sleeves': 0}

    total_bags = total_hot_dogs + total_bakes
    proj_bag_sales = get_projected_sales(total_bags)
    proj_bag_sleeves = proj_bag_sales
    if(proj_bag_sleeves % 1 != 0):
        proj_bag_sleeves += 1
        proj_bag_sleeves = math.trunc(proj_bag_sleeves)

    food_bag_info['Food bag sleeves'] = proj_bag_sleeves

    total_boxes = proj_bag_sales / steel['food_bags']['quantity']

    if(total_boxes % 1 != 0):
        total_boxes += 1
        total_boxes = math.trunc(total_boxes)
        food_bag_info['Food bag boxes'] = total_boxes
    
    

    return food_bag_info