def get_tickets(requested, available):
    """
    Validates the requested tickets.
    Returns the number of tickets to sell (max 4 or available).
    """
    if requested > 4:
        print("You can only buy up to 4 tickets at a time.")
        return 0
    elif requested > available:
        print(f"Only {available} tickets left. Cannot sell {requested}.")
        return 0
    elif requested <= 0:
        print("You must buy at least 1 ticket.")
        return 0
    else:
        return requested

def main():
    total_tickets = 10
    tickets_sold_count = 0  # renamed and initialized here
    buyers = 0

    while tickets_sold_count < total_tickets:
        available = total_tickets - tickets_sold_count
        print(f"\nTickets remaining: {available}")
        try:
            requested = int(input("How many tickets would you like to buy? (up to 4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        sold = get_tickets(requested, available)
        if sold > 0:
            tickets_sold_count += sold
            buyers += 1
            print(f"{sold} tickets sold. {total_tickets - tickets_sold_count} tickets remaining.")

    print("\nAll tickets sold!")
    print(f"Total buyers: {buyers}")

if __name__ == "__main__":
    main()
