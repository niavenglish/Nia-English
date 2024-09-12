#Add an item to the cart
def add_item(cart, item_name, item_price):
    #Append for the item name and price
    cart.append({"name": item_name, "price": item_price})
#Calculate the total for evrything in the cart
def calculate_total(cart):
    #Calculate the sum
    total = sum(item["price"] for item in cart)
    return total
#Display the items inside the cart
def display_cart(cart):
    #Print the items in the cart
    print("Items in Cart:")
    for item in cart:
        print(f"{item['name']}: ${item['price']:.2f}")
    print("-" * 20)
#Main
def main():
    print("Welcome to the Online Shopping Cart!")
#Cart list for items
    cart = []

    while True:
        #Options for the user to chose from
        print("1. Add Item to Cart")
        print("2. Display Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            #Add function so items can be added to the cart
            add_item(cart, name, price)
            print(f"{name} added to cart.\n")

        elif choice == "2":
            #Display the cart
            display_cart(cart)

        elif choice == "3":
            #Total cost and cart summary
            total = calculate_total(cart)
            print("Cart Summary:")
            display_cart(cart)
            print(f"Total Cost: ${total:.2f}")
            break

        elif choice == "4":
            #Thank you message for any users that chooses option 4
            print("Thank you for using the Online Shopping Cart!")
            break

        else:
            #Message for users who chooses an option that is not avaiable
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
#Main function
    main()