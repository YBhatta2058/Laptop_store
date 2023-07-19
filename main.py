import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to read laptops data from the text file
def read_laptops_data(filename):
    laptops_data = []
    with open(filename, 'r') as file:
        for line in file:
            laptop_info = line.strip().split(', ')
            laptops_data.append(laptop_info)
    return laptops_data

# Function to write laptops data back to the text file
def write_laptops_data(filename, laptops_data):
    with open(filename, 'w') as file:
        for laptop_info in laptops_data:
            file.write(', '.join(laptop_info) + '\n')

# Function to generate a unique note/invoice filename
def generate_unique_filename(transaction_type, laptop_name, customer_name):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return f"{transaction_type}_{laptop_name}_{customer_name}_{timestamp}.pdf"

# Function to generate a sales note/invoice as a PDF
def generate_sales_invoice_pdf(laptop_name, brand_name, customer_name, quantity, price_per_unit, shipping_cost):
    total_amount = quantity * price_per_unit
    total_amount_with_shipping = total_amount + shipping_cost

    c = canvas.Canvas(generate_unique_filename('Sales', laptop_name, customer_name), pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(250, 770, "Sales Invoice")

    # Customer Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 720, "Customer Name:")
    c.drawString(180, 720, customer_name)

    # Laptop Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 690, "Laptop Name:")
    c.drawString(180, 690, laptop_name)
    c.drawString(50, 670, "Brand:")
    c.drawString(180, 670, brand_name)

    # Purchase Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 640, "Date and Time of Purchase:")
    c.drawString(250, 640, str(datetime.datetime.now()))
    c.drawString(50, 620, "Quantity:")
    c.drawString(180, 620, str(quantity))
    c.drawString(50, 600, "Price per Unit:")
    c.drawString(180, 600, f"${price_per_unit}")
    c.drawString(50, 580, "Total Amount (without shipping cost):")
    c.drawString(350, 580, f"${total_amount}")
    c.drawString(50, 560, "Shipping Cost:")
    c.drawString(180, 560, f"${shipping_cost}")
    c.drawString(50, 540, "Total Amount to be Paid (including shipping cost):")
    c.drawString(350, 540, f"${total_amount_with_shipping}")

    c.save()

# Function to generate a purchase order note/invoice as a PDF
def generate_purchase_order_pdf(distributor_name, laptop_name, brand_name, quantity, price_per_unit):
    net_amount = quantity * price_per_unit
    vat_amount = net_amount * 0.13
    gross_amount = net_amount + vat_amount

    c = canvas.Canvas(generate_unique_filename('PurchaseOrder', laptop_name, distributor_name), pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(250, 770, "Purchase Order")

    # Distributor Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 720, "Distributor Name:")
    c.drawString(180, 720, distributor_name)

    # Laptop Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 690, "Laptop Name:")
    c.drawString(180, 690, laptop_name)
    c.drawString(50, 670, "Brand:")
    c.drawString(180, 670, brand_name)

    # Purchase Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 640, "Date and Time of Purchase:")
    c.drawString(250, 640, str(datetime.datetime.now()))
    c.drawString(50, 620, "Quantity:")
    c.drawString(180, 620, str(quantity))
    c.drawString(50, 600, "Price per Unit:")
    c.drawString(180, 600, f"${price_per_unit}")
    c.drawString(50, 580, "Net Amount:")
    c.drawString(180, 580, f"${net_amount}")
    c.drawString(50, 560, "VAT Amount (13%):")
    c.drawString(180, 560, f"${vat_amount}")
    c.drawString(50, 540, "Gross Amount (with VAT):")
    c.drawString(250, 540, f"${gross_amount}")

    c.save()
'''
# Function to display laptops available in stock
def display_laptops_stock(laptops_data):
    print("\nLaptops Available in Stock:")
    print("----------------------------")
    print("{:<15} {:<10} {:<10} {:<10}".format("Laptop", "Brand", "Price", "Quantity"))
    print("-" * 45)
    for laptop_info in laptops_data:
        laptop_name, brand_name, price, quantity, *_ = laptop_info
        print("{:<15} {:<10} {:<10} {:<10}".format(laptop_name, brand_name, price, quantity))
'''

# Function to display laptops available in stock
def display_laptops_stock(laptops_data):
    print("\nLaptops Available in Stock:")
    print("----------------------------")
    print("{:<15} {:<10} {:<10} {:<10} {:<15} {:<15}".format("Laptop", "Brand", "Price", "Quantity", "Processor", "Graphics Card"))
    print("-" * 75)
    for laptop_info in laptops_data:
        laptop_name, brand_name, price, quantity, processor, graphics_card = laptop_info
        print("{:<15} {:<10} {:<10} {:<10} {:<15} {:<15}".format(laptop_name, brand_name, price, quantity, processor, graphics_card))




# Main function to handle transactions
def handle_transactions(laptops_data):
    distributor_name = "ITTI Laptop Store, Putalisadak"  # Replace with your laptop shop name
    while True:
        print("\n1. Display Laptops Available in Stock")
        print("2. Sell Laptop")
        print("3. Order Laptop")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Display Laptops Available in Stock
            display_laptops_stock(laptops_data)
            
        
        elif choice == 2:  # Sell Laptop
            laptop_name = input("Enter the laptop name: ")
            brand_name = input("Enter the brand name: ")
            customer_name = input("Enter the customer name: ")
            quantity = int(input("Enter the quantity sold: "))
            # Find the laptop in the data and update stock
            for laptop_info in laptops_data:
                if laptop_info[0] == laptop_name and laptop_info[1] == brand_name:
                    price_per_unit = float(laptop_info[2].replace('$', ''))
                    laptop_info[3] = str(int(laptop_info[3]) - quantity)  # Update stock
                    # Generate and save the sales invoice PDF
                    shipping_cost = 50  # You can modify the shipping cost if needed
                    generate_sales_invoice_pdf(laptop_name, brand_name, customer_name, quantity, price_per_unit, shipping_cost)
                    break
            else:
                print("Laptop not found in stock!")

        elif choice == 3:  # Order Laptop
            laptop_name = input("Enter the laptop name: ")
            brand_name = input("Enter the brand name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter the quantity to order: "))
            processor = input("Enter processor: ")
            card = input("Enter graphics card: ")
            
            # Calculate the price_per_unit based on user input
            price_per_unit = price

            # Find the laptop in the data and update stock
            for laptop_info in laptops_data:
                if laptop_info[0] == laptop_name and laptop_info[1] == brand_name:
                    laptop_info[3] = str(int(laptop_info[3]) + quantity)  # Update stock
                    price_per_unit = float(laptop_info[2].replace('$', ''))  # Update price_per_unit if laptop found
                    break

            else:
                # Add a new laptop to the list
                laptops_data.append([laptop_name, brand_name, f"${price}", str(quantity), processor, card])

            # Generate and save the purchase order invoice PDF
            generate_purchase_order_pdf(distributor_name, laptop_name, brand_name, quantity, price_per_unit)

        

        elif choice == 4:  # Exit
            break

        else:
            print("Invalid choice!")

    # Update the text file with the updated laptops data
    write_laptops_data("laptops_data.txt", laptops_data)
    print("Data saved successfully!")


if __name__ == "__main__":
    # Read laptops data from the text file
    laptops_data = read_laptops_data("laptops_data.txt")

    # Start handling transactions
    handle_transactions(laptops_data)
