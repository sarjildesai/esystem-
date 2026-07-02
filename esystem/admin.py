from product import (
    add_product,
    update_product,
    delete_product,
    show_products
)

from cart import view_all_carts


def admin_menu():
    while True:
        print("\n===== ADMIN PANEL =====")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. View Customer Carts")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            update_product()

        elif choice == "3":
            delete_product()

        elif choice == "4":
            show_products()

        elif choice == "5":
            view_all_carts()

        elif choice == "6":
            print("Admin Logged Out")
            break

        else:
            print("Invalid Choice")