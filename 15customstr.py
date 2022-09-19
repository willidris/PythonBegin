Product_name = input("enter your product name please:")
Product_condition = input("enter your condition please:")

#output = "Hello," + first_name + " " + last_name
#output = "Hello, {} {}".format(first_name, last_name)
#output = "Hello, {1}, {0}".format(first_name, last_name)
#output = f"Hello,{first_name} {last_name}"
output = "Your product, {1} {0}".format(Product_name, Product_condition)
print(output)