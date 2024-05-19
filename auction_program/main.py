name_list = {}

isTrue = True
while isTrue:
    name = input("Enter your name: ")
    amount = int(input("Enter your bid $: "))
    
    name_list[name] = amount
    
    choice = input("Are there any other bidders? (y/n): ")
    if choice == "n":
        isTrue = False

print(name_list)

bider_name = ""
max_amount = 0
for key in name_list:
    if name_list[key] > max_amount:
        max_amount = name_list[key]
        bider_name = key


print(f"The winner is {bider_name} with a bid of ${max_amount}.")
