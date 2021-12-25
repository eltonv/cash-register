from DiscountApplier import process_workbook

# Greet
disc_percent = input('Hello, please enter the discount percentage: \n')

# FUTURE IMPLEMENTATION#

# - Ask for coupon code
# - Use database to retrieve the value associated
#   with the coupon code

# - Ask what Items they want to purchase (display list with price)
# - Take user input of items
# - Make input into a list
# - Feed it to module that assigns them to the Excel sheet (by row)
# - Use database to retrieve the price associated with each item

process_workbook('transactions.xlsx', int(disc_percent))
