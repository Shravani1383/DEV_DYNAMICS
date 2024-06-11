# Inventory Management System

This project is an inventory management system for an e-commerce store. It allows administrators to add/remove products from inventory and customers to add items to the cart. It also supports applying discount coupons.

## APIs

### 1. Add Item to Inventory
- **Endpoint**: `/addItemToInventory`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "productId": "123",
    "quantity": 10
  }

### 2. Remove Item from Inventory
- **Endpoint**: `/removeItemFromInventory`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "productId": "123",
    "quantity": 10
  }
 
 ### 3. Add Item to Cart
- **Endpoint**: '/addItemToCart'
-**Method**: POST
-**Request Body**:
```json
  {
   "customerId": "cust1",
   "productId": "123",
   "quantity": 2
  }

### 4. Apply Discount Coupon
- **Endpoint**: '/applyDiscountCoupon'
-**Method**: POST
-**Request Body**:
```json
  {
   "cartValue": 1000,
  "discountId": "DISCOUNT20"
  }  
 
 
