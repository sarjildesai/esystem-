from auth import register, login
from product import show_products, search_product
from admin import admin_menu
from cart import add_to_cart, view_cart, remove_from_cart, checkout
def customer_menu(user):
    while True:
        print("\n===== CUSTOMER PANEL =====")
        print("1. View Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            search_product()

        elif choice == "3":
          add_to_cart(user["username"])

        elif choice == "4":
         view_cart(user["username"])

        elif choice == "5":
         remove_from_cart(user["username"])

        elif choice == "6":
         checkout(user["username"])

        elif choice == "7":
            print("Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")
            
while True:
    print("\n===== E-COMMERCE =====")
    print("1. Register")
    print("2. Login")
    print("3. View Products")
    print("4. Search Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user = login()
        if user:
            if user["role"] == "admin":
                admin_menu()
            else:
             customer_menu(user)

    elif choice == "3":
        show_products() 

    elif choice == "4":
        search_product()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice")      
        
