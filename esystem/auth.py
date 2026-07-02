
users = []


def register():
    print("\n========== REGISTER ==========")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists!")
            return

    if len(users) == 0:
        role = "admin"
        print("Congratulations! You are the Admin.")
    else:
        role = "customer"

    users.append({
        "username": username,
        "password": password,
        "role": role
    })

    print("Registration Successful!")

def login():
    print("\n========== LOGIN ==========")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\nWelcome {username}!")
            return user

    print("Invalid Username or Password.")
    return None

def show_users():
    print("\n========== REGISTERED USERS ==========")

    for user in users:
        print(
            f"Username : {user['username']} | "
            f"Role : {user['role']}"
        )