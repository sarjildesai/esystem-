from itertools import product


products = [
    {"id": 1, "name": "Laptop", "price": 60000, "stock": 10},
    {"id": 2, "name": "Phone", "price": 25000, "stock": 15},
    {"id": 3, "name": "Mouse", "price": 500, "stock": 30},
    {"id": 4, "name": "Keyboard", "price": 1200, "stock": 20},
    {"id": 5, "name": "Monitor", "price": 15000, "stock": 8},
]


def show_products():
    print("\n========== PRODUCT LIST ==========")

    if not product:
        print("No products available.")
        return

    print("{:<5} {:<20} {:<10} {:<10}".format(
        "ID", "Name", "Price", "Stock"))

    print("-" * 50)

    for p in products:
        print("{:<5} {:<20} ₹{:<9} {:<10}".format(
            p["id"],
            p["name"],
            p["price"],
            p["stock"]
        ))


def search_product():
    keyword = input("\nEnter product name: ").lower()

    found = False

    for p in products:
        if keyword in p["name"].lower():
            print("\nProduct Found")
            print("------------------------")
            print("ID    :", p["id"])
            print("Name  :", p["name"])
            print("Price :", p["price"])
            print("Stock :", p["stock"])
            found = True

    if not found:
        print("Product not found.")

def get_product(pid):
    for p in products:
        if p["id"] == pid:
            return p
    return None

def add_product():
    print("\n===== ADD PRODUCT =====")

    pid = len(products) + 1

    name = input("Product Name : ")

    price = float(input("Price : "))

    stock = int(input("Stock : "))

    products.append({
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock
    })

    print("Product added successfully.")

def update_product():
    show_products()

    pid = int(input("\nEnter Product ID: "))

    product = get_product(pid)

    if product is None:
        print("Product not found.")
        return

    print("\nLeave blank to keep old value.")

    name = input("New Name: ")

    if name != "":
        product["name"] = name

    price = input("New Price: ")

    if price != "":
        product["price"] = float(price)

    stock = input("New Stock: ")

    if stock != "":
        product["stock"] = int(stock)

    print("Product updated successfully.")

def delete_product():
    show_products()

    pid = int(input("\nEnter Product ID: "))

    product = get_product(pid)

    if product is None:
        print("Product not found.")
        return

    products.remove(product)

    print("Product deleted successfully.")