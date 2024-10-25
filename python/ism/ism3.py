# sun = "down"
# if sun == "down":
#     print("Good Night!")
# elif sun == "up":
#     print("Good Morning!")
# else:
#     print("No option for this")

total = 100
sale_tax_rate = 0.065
taxable = True

if taxable:
    print(f"Subtotal: ${total:.2f}")
    sale_tax = total * sale_tax_rate
    print(f"Sales Tax: ${sale_tax:.2f}")
    total = total + sale_tax
print(f"Total: ${total:.2f}")

# light_color= "green"
# if light_color == "green":
#     print("Go!")
# elif light_color == "yellow":
#     print("Ready!")
# elif light_color == "red":
#     print("stop!")
# else:
#     print("Proceed with caution.")