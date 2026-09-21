# Module 5 - Activity

# Sets for unique categories
categories = {"Hardware", "Software", "Peripherals"}
categories.add("Networking")

# List of Dictionaries for store inventory
inventory = [
    {"id": "DEV01", "name": "wireless mouse", "price": 250.00, "category": "Peripherals"},
    {"id": "DEV02", "name": "mechanical keyboard", "price": 850.00, "category": "Peripherals"},
    {"id": "DEV03", "name": "python IDE license", "price": 1200.00, "category": "Software"}
]

# String cleaning and Dictionary processing
print("--- Inventory Catalog ---")
for item in inventory:
    # Applying String Methods
    formatted_name = item["name"].title().strip()
    print(f"ID: {item['id']} | Name: {formatted_name} | Price: R{item['price']:.2f} | Category: {item['category']}")

print(f"\nAvailable Product Categories: {', '.join(categories)}")