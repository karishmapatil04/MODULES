def calculate_due_amount(total_bill, amount_paid):
    """
    Calculate the remaining due amount after payment.
    
    Parameters:
        total_bill (float): Total bill amount
        amount_paid (float): Amount paid by the customer
    
    Returns:
        float: Remaining due amount
    """
    return total_bill - amount_paid


# Example usage
total_bill = float(input("Enter total bill amount: "))
amount_paid = float(input("Enter amount paid: "))

due = calculate_due_amount(total_bill, amount_paid)

if due > 0:
    print("Remaining due amount:", due)
elif due == 0:
    print("Bill fully paid. No due amount.")
else:
    print("Overpaid amount (change to return):", abs(due))