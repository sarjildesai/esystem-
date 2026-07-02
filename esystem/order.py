from cart import add_to_cart, view_cart, remove_from_cart, checkout
import cart

orders = []


def place_order(username):
    if not cart:
        print("\nCart is Empty.")
        return

    total = 0
    items = []

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        items.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"]
        })

    orders.append({
        "customer": username,
        "items": items,
        "total": total
    })

    print("\n========== ORDER PLACED ==========")
    print("Customer :", username)
    print("Total Bill : ₹", total)
    print("Thank You for Shopping!")

    cart.clear()


def view_orders(username):
    found = False

    print("\n========== ORDER HISTORY ==========")

    for order in orders:
        if order["customer"] == username:
            found = True

            print("\nCustomer :", order["customer"])

            for item in order["items"]:
                print(
                    f"{item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']}"
                )

            print("Total :", order["total"])
            print("-" * 35)

    if not found:
        print("No Orders Found.")