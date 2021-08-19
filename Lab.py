# Your Project Code

# Printing the mainmenu
def menu() :
    # Printing the mainmenu
    print("CAR INSTALLMENTS PROGRAM")
    print("-" * 60)
    print("-" * 60)
    print("1. Add New Customer")
    print("2. Display Information for All Customers")
    print("3. Display Information for a Customer")
    print("4. Eligibility of a Customer")
    print("5. Compute Monthly Payment Amount")
    print("6. Display Amortization Table")
    print("7. Exit")
    print("-" * 60)
    print("-" * 60)

# Adding a new customer
def addNewCustomer():
    # Read All the lines of the file
    infile = open("customer.txt", "r")
    customers = infile.readlines()
    infile.close()

    # Open the file for adding a customer
    infile = open("customer.txt", "a")
    count = 0
    # To remove the new line charecter and split to get the ID number only
    for i in customers:
        i.rstrip()
        lineList = i.split("   ")
        customers[count] = lineList[0]
        count += 1
    try:
        # We take the ID, Salary and Age of the Customer
        id = str(input("Enter Customer ID:"))
        if id.isdigit() :
            # We check if the ID already exists
            if str(id) in customers:
                print("The ID you have chosen already exists")
            else:
                salary = float(input("Enter salary:"))
                age = int(input("Enter Age:"))
                # We write in the file the new customer with his(her) Information
                infile.write("\n" + str(id) + "   " + str(salary) + "   " + str(age))
                print("Customer successfully Added")
        else:
            print("You should enter a valid input")


    except ValueError:
        print("You should enter a valid input")
    infile.close()
    # We ask the user if he want to continue or not
    flag = input("Would u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Displaying all customers
def disAll():
    # Read All the lines of the file
    infile = open("customer.txt", "r")
    customers = infile.readlines()
    infile.close()

    # Create lists
    names = []
    salarys = []
    ages = []

    # We seperate the ID, Name and Age in diffrante lists
    for i in customers:
        i.rstrip()
        lineList = i.split("   ")
        names.append(lineList[0])
        salarys.append(lineList[1])
        ages.append(lineList[2])

    # We print all the information
    print("CustomerID   Salary   Age")
    print("-" * 30)
    for i in range(len(names)):
        print("%-13s" % names[i], end="")
        print("%-9s" % salarys[i], end="")
        print(ages[i], end="")

    # We ask the user if he want to continue or not
    flag = input("\nWould u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Display one customer
def disCus():
    # We get the information of the customer
    customer = getCus()
    if customer :
        # We print for the required customer
        print("CustomerID   Salary   Age")
        print("-" * 30)
        print("%-13s" % customer[0], end="")
        print("%-9s" % customer[1], end="")
        print(customer[2])

    # We ask the user if he want to continue or not
    flag = input("Would u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Get one customer
def getCus() :
    # We read the file and take the information and but it in a list
    infile = open("customer.txt", "r")
    customers = infile.readlines()
    infile.close()
    idList = []
    # We take the list and split it and get only the id list
    for i in customers:
        i.rstrip()
        lineList = i.split("   ")
        idList.append(lineList[0])
    # We get the id of the customer
    value = str(input("Enter Customer ID: "))
    if value.isdigit() :
        try:
            # We get the name,salary and age of the customer
            index = idList.index(str(value))
            customer = customers[index].rstrip()
            customer.rstrip()
            customer = customer.split("   ")
            # We return the information of the customer
            return (customer[0], customer[1], customer[2])
        except ValueError:
            print("No customer found with this ID")
            # We return false
            return (0)
    else:
        print("You should enter a valid input")
        return(0)

# Check For Eligibility
def elig() :

    customer = getCus()
    if customer :
        # We check if the user is eligible or not and display the output for the user
        if float(customer[2]) < 63 and float(customer[1]) > 2999 :
            print("Customer " + str(customer[0]) + " is eligible")
        else :
            print("Customer " + str(customer[0]) + " is Not eligible")

    # We ask the user if he want to continue or not
    flag = input("Would u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Computes Monthly Payment Amount
def comMonPay() :
    # We get the customer information
    customer = getCus()
    if customer :
        # We take the loan, annual and years from the customer
        loan = float(input("Loan: "))
        annual = float(input("Annual Rate: "))
        years = int(input("Years: "))
        # We do some calculation
        monIntRate = annual/12
        numPayments = years*12
        term = (1+monIntRate)**numPayments
        monPay = (loan * monIntRate * term)/(term - 1)
        # Print the result to the customer
        print("Monthly payment: SR %.2f" %monPay)

    # We ask the user if he want to continue or not
    flag = input("Would u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Displays Amortization Table
def disAmorTable() :
    # We get the customer information
    customer = getCus()
    if customer:
        # We take the balance, annual and years from the customer
        balance = float(input("Loan: "))
        annual = float(input("Annual Rate: "))
        years = int(input("Years: "))
        # We do some calculation
        monIntRate = annual / 12
        numPayments = years * 12
        term = (1 + monIntRate) ** numPayments
        monPay = (balance * monIntRate * term) / (term - 1)
        print("Month   Interest   Principal   Balance")
        print("-" * 38)
        # Calculate, print, and store the information in a file
        infile = open(str(customer[0]) + ".txt", "w")
        infile.write("Month   Interest   Principal   Balance\n")
        infile.write(str(str("-" * 38) + "\n"))
        for i in range(1,13) :
            monInt = monIntRate * balance
            if i != 12 :
                principal = monPay - monInt
            else :
                principal = balance
                monPay = balance + monInt
            balance = balance - principal
            # We print The information to the customer
            print("%-9d" % i, end="")
            print("%-11.2f" % monInt, end="")
            print("%-12.2f" %principal, end="")
            print("%.2f" %balance)
            # We store The information of the customer to a file (The file name is the customer ID)
            infile.write(str("%-9d" % i))
            infile.write(str("%-11.2f" % monInt))
            infile.write(str("%-12.2f" %principal))
            infile.write(str("%.2f\n" %balance))
        infile.close()

    # We ask the user if he want to continue or not
    flag = input("Would u like to Quit or return to main menu (0 Quit , 1 return): ")
    return flag

# Main function for printing and getting the choice of the customer
def main():
    flag = True
    while flag:
        # Print The menu
        menu()
        # We take the choice and validate it
        choice = input("Enter Your Choice: ")
        while not (choice.isdigit() and int(choice) >= 1 and int(choice) <= 7):
            print("Invalid Choice! Please Enter a Valid Choice")
            choice = input("Enter Your Choice: ")
        # After validation we choose what the user requested
        if int(choice) == 1:
            flag = int(addNewCustomer())
        elif int(choice) == 2:
            flag = int(disAll())
        elif int(choice) == 3:
            flag = int(disCus())
        elif int(choice) == 4 :
            flag = int(elig())
        elif int(choice) == 5 :
            flag = int(comMonPay())
        elif int(choice) == 6 :
            flag = int(disAmorTable())
        else :
            flag = False

main()