def calculate_and_display_results(table_name, total_charges, tip_rate, tax_rate):
    # Calculate the tip
    tip = total_charges * (tip_rate / 100)

    # Calculate the sales tax
    sales_tax = total_charges * (tax_rate / 100)

    # Calculate the total amount
    total_amount = total_charges + tip + sales_tax

    # Display the results for the table
    print(f"\nReceipt for {table_name}:")
    print(f"Total Food Charges: ${total_charges:.2f}")
    print(f"Tip ({tip_rate}%): ${tip:.2f}")
    print(f"Sales Tax ({tax_rate}%): ${sales_tax:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")
    print("------------------------------------------------------")

    return tip, sales_tax, total_amount


def main():
    # Get the default tip rate and tax rate
    default_tip_rate = 18.0
    default_tax_rate = 7.0

    # Prompt the user if they want to use custom rates
    use_custom_rates = input("Do you want to use custom tip and tax rates? (yes/no): ").strip().lower()

    # Set the tip rate and tax rate
    tip_rate = default_tip_rate if use_custom_rates != 'yes' else float(
        input("Enter the tip rate (default is 18%): ") or default_tip_rate)
    tax_rate = default_tax_rate if use_custom_rates != 'yes' else float(
        input("Enter the tax rate (default is 7%): ") or default_tax_rate)

    # Dictionary to store the results for each table
    results = {}
    grand_totals = {"Food Charges": 0.0, "Tip": 0.0, "Sales Tax": 0.0, "Total Amount": 0.0}

    while True:
        # Get the table name
        table_name = input("Enter the table name: ")

        # Initialize the total charges for this table
        total_charges = 0.0

        while True:
            # Get the charge for the food
            food_charge = float(input("Enter the charge for the food: $"))
            total_charges += food_charge

            # Prompt if the user wants to continue adding more charges
            another_charge = input("Do you want to add another charge for this table? (yes/no): ").strip().lower()
            if another_charge != 'yes':
                break

        # Calculate, store and display the results for this table
        tip, sales_tax, total_amount = calculate_and_display_results(table_name, total_charges, tip_rate, tax_rate)
        results[table_name] = {"Food Charges": total_charges, "Tip": tip, "Sales Tax": sales_tax,
                               "Total Amount": total_amount}

        # Update the grand totals
        grand_totals["Food Charges"] += total_charges
        grand_totals["Tip"] += tip
        grand_totals["Sales Tax"] += sales_tax
        grand_totals["Total Amount"] += total_amount

        # Prompt if the user wants to add charges for another table
        another_table = input("Do you want to add charges for another table? (yes/no): ").strip().lower()
        if another_table != 'yes':
            break

    # Display the summary for all tables
    print("\nSummary for all tables:")
    for table, charges in results.items():
        print(f"\n{table}:")
        for charge_type, amount in charges.items():
            print(f"{charge_type}: ${amount:.2f}")

    # Display the grand totals
    print("\nGrand Totals:")
    for total_type, grand_total in grand_totals.items():
        print(f"{total_type}: ${grand_total:.2f}")


if __name__ == "__main__":
    main()
