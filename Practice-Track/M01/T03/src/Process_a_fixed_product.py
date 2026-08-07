product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Create the fixed product record as a tuple
product_record = (product_id, product_name, category, unit_price, quantity)

# Access the product ID and product name using indexes
prod_id = product_record[0]
prod_name = product_record[1]

# Unpack the complete tuple
id1, name1, category1, price1, quantity1 = product_record

# Calculate the stock value
stock_value = price1 * quantity1

# Determine the stock status
if quantity1 == 0:
    stock_status = "Out of Stock"
elif quantity1 <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the processed product records
print(f"Product ID: {id1}")
print(f"Product Name: {name1}")
print(f"Category: {category1}")
print(f"Unit Price: {price1:.2f}")
print(f"Available Quantity: {quantity1}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")