from product import products
carts = {}


def add_to_cart(username):
    if username not in carts:
        carts[username] = []

    cart = carts[username]

    try:
        pid = int(input("Enter Product ID: "))
    except ValueError:
        print("Invalid Product ID")
        return

    for product in products:

        if product["id"] == pid:

            if product["stock"] <= 0:
                print("Out of Stock")
                return

            for item in cart:
                if item["id"] == pid:
                    item["quantity"] += 1
                    product["stock"] -= 1
                    print("Quantity Updated")
                    return

            cart.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": 1
            })

            product["stock"] -= 1
            print("Product Added Successfully")
            return

    print("Product Not Found")


def view_cart(username):
    cart = carts.get(username, [])

    if not cart:
        print("Cart is Empty")
        return

    total = 0

    print("\n========== YOUR CART ==========")
    print("{:<5} {:<20} {:<10} {:<10}".format(
        "ID", "Name", "Qty", "Subtotal"))

    print("-" * 50)

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print("{:<5} {:<20} {:<10} ₹{}".format(
            item["id"],
            item["name"],
            item["quantity"],
            subtotal
        ))

    print("-" * 50)
    print("Total = ₹", total)


def remove_from_cart(username):
    cart = carts.get(username, [])

    if not cart:
        print("Cart is Empty")
        return

    try:
        pid = int(input("Enter Product ID to Remove: "))
    except ValueError:
        print("Invalid ID")
        return

    for item in cart:

        if item["id"] == pid:

            for product in products:
                if product["id"] == pid:
                    product["stock"] += item["quantity"]

            cart.remove(item)
            print("Removed Successfully")
            return

    print("Product Not Found")


def checkout(username):
    cart = carts.get(username, [])

    if not cart:
        print("Cart is Empty")
        return

    total = 0

    print("\n========== BILL ==========")

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            item["name"],
            "x",
            item["quantity"],
            "= ₹",
            subtotal
        )

    print("----------------------------")
    print("Total Bill = ₹", total)
    print("----------------------------")
    print("Order Placed Successfully")

    cart.clear()


def view_all_carts():
    print("\n========== CUSTOMER CARTS ==========")

    if not carts:
        print("No customer carts available.")
        return

    for username, cart in carts.items():

        print(f"\nCustomer: {username}")

        if not cart:
            print("Cart is Empty")
            continue

        total = 0

        for item in cart:
            subtotal = item["price"] * item["quantity"]
            total += subtotal

            print(
                f"{item['name']} | Qty: {item['quantity']} | Price: ₹{item['price']}"
            )

        print("Total: ₹", total)