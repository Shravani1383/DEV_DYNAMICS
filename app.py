from flask import Flask, request, jsonify

app = Flask(__name__)

# Inventory and Cart data structures
inventory = {}
carts = {}
discounts = {}

# API to add an item to the inventory
@app.route('/addItemToInventory', methods=['POST'])
def add_item_to_inventory():
    data = request.json
    product_id = data['productId']
    quantity = data['quantity']
    
    if product_id in inventory:
        inventory[product_id] += quantity
    else:
        inventory[product_id] = quantity
    
    return jsonify({"message": "Item added to inventory", "inventory": inventory}), 200

# API to remove an item from the inventory
@app.route('/removeItemFromInventory', methods=['POST'])
def remove_item_from_inventory():
    data = request.json
    product_id = data['productId']
    quantity = data['quantity']
    
    if product_id in inventory and inventory[product_id] >= quantity:
        inventory[product_id] -= quantity
        if inventory[product_id] == 0:
            del inventory[product_id]
        return jsonify({"message": "Item removed from inventory", "inventory": inventory}), 200
    else:
        return jsonify({"message": "Insufficient inventory"}), 400

# API to add an item to the cart
@app.route('/addItemToCart', methods=['POST'])
def add_item_to_cart():
    data = request.json
    customer_id = data['customerId']
    product_id = data['productId']
    quantity = data['quantity']
    
    if product_id in inventory and inventory[product_id] >= quantity:
        if customer_id not in carts:
            carts[customer_id] = {}
        
        if product_id in carts[customer_id]:
            carts[customer_id][product_id] += quantity
        else:
            carts[customer_id][product_id] = quantity
        
        inventory[product_id] -= quantity
        if inventory[product_id] == 0:
            del inventory[product_id]
        
        return jsonify({"message": "Item added to cart", "cart": carts[customer_id]}), 200
    else:
        return jsonify({"message": "Insufficient inventory"}), 400

# API to apply discount coupon
@app.route('/applyDiscountCoupon', methods=['POST'])
def apply_discount_coupon():
    data = request.json
    cart_value = data['cartValue']
    discount_id = data['discountId']
    
    if discount_id in discounts:
        discount = discounts[discount_id]
        discount_percentage = discount['discountPercentage']
        max_discount = discount['maxDiscountCap']
        
        discount_amount = (discount_percentage / 100) * cart_value
        if discount_amount > max_discount:
            discount_amount = max_discount
        
        discounted_price = cart_value - discount_amount
        
        return jsonify({"originalPrice": cart_value, "discountedPrice": discounted_price}), 200
    else:
        return jsonify({"message": "Invalid discount ID"}), 400

# Add some discount coupons for demonstration
discounts['DISCOUNT20'] = {'discountPercentage': 20, 'maxDiscountCap': 150}

if __name__ == '__main__':
    app.run(debug=True)
