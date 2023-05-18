# Function to convert dBm to milliwatts
def dbm_to_milliwatt(dbm):
    milliwatt = 10 ** (dbm / 10)  # Convert dBm to milliwatts using the formula
    return milliwatt

# Prompt the user to choose between converting a single value or a list of values
choice = input("Do you want to convert a single value or a list of values? (single/list): ")

if choice.lower() == "single":
    # Convert a single value
    dbm = float(input("Enter the value in dBm: "))  # Convert the input to a floating-point number
    milliwatt = dbm_to_milliwatt(dbm)
    print(f"\n{dbm:.2f} dBm is equal to {milliwatt:.6f} milliwatts.")
elif choice.lower() == "list":
    # Convert a list of values
    print("\nEnter 6 values in dBm:")
    dbm_values = []
    for i in range(1, 7):
        dbm = float(input(f"Value {i}: "))  # Convert the input to a floating-point number
        dbm_values.append(dbm)

        if len(dbm_values) < 6:
        print("\nPlease enter 6 more values to complete the list.")

    # Print the table header
    print("\nValue    dBm      Milliwatt")
    print("----------------------------")

    # Iterate over the entered dBm values, calculate and display the milliwatt values in the table
    for i, dbm in enumerate(dbm_values, start=1):
        milliwatt = dbm_to_milliwatt(dbm)
        print(f"{i:2d}    {dbm:7.2f}    {milliwatt:10.6f}")
else:
    print("Invalid choice. Please choose 'single' or 'list'.")
