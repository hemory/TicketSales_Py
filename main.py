# constants are capitalized
TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100 

#Functions--------

def calculate_price(number_of_tickets):
    
    # create constance for 2 doallr service charge and add it to due
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


# ----------

while tickets_remaining >= 1:

    # Output how many tickets are remaining using the tickets remaining variable
    
    print(f"There are {tickets_remaining} tickets remaining.")
    
    username = input("Enter your name: ")
    
    try:
            num_tickets = int(input(f"How many tickets would you like to purchase {username}?: "))
            # Raise a ValueError if the request is for more tickets than are available
            if num_tickets > tickets_remaining:
                raise ValueError(f"There are only {tickets_remaining} tickets remaining.")
    except ValueError as err:
        # Include the error text in the output
        print(f"Oh no, we ran into an issue. {err}. Please try again.")
    else:
        total = calculate_price(num_tickets)
        print(f"The total due is ${total}")
    
        # prompt user if they would like to continue? Y/N
        # If they want to proceed
            # print out the screen "Sold!" to confirm
            # and then decrement the number of remaining tickets
        # else
            # Thank them by name
        
        keep_going = input("Continue Y/N: ")
        
        if keep_going.lower() == "y":
            print("Sold!")
            # TODO Gather credit card info and process it
            tickets_remaining -= num_tickets
        else:
            print(f"Thank you, {username}")
    
# Notify the user that the tickets are sold out
print("All the tickets are sold out!")
