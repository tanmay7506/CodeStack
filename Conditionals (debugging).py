# debug the code given below
'''
main_dish = input()
time_of_day = int(input())
has_voucher =   ...
is_card_payment = ...

if main_dish == "panner tikka":
    cost = 250
    elif main_dissh == "butter chikcen":
        cost == 240
    elif main_dish = "masal dosa":
        cost = 200
    else: # if main dish is invalid print invalid dish and exit the code.
       print("Invalid main dish")
       exit() 

    if time_of_day >= 12 and time_of_day =< 15:
        total_cost = (1 - 0.15) * cost

    eles
        total_cost = cost

    if has_voucher
        total_cost =* 0.9  # Apply voucher discount

    if is_card_payment  # service charge for card payments
        service_charge = 0.05 * total_cost
        total_cost =+ servcie_charge

    print(f"{total_cost:.02f}")
'''
# debugged code below
main_dish = input()  # str: input dish name
time_of_day = int(input())  #int: input time in 24-HR format
has_voucher = input()  #bool: input True or False
is_card_payment = input()  #bool: input True or False

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:           # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    
        
if (12 <= time_of_day <= 15):  #discount of 15% on cost between 1200hrs and 1500hrs
    total_cost = 0.85 * cost
else:
   total_cost = cost

if (has_voucher == "True"):
    total_cost = 0.9 * total_cost  # Apply voucher discount
else:
    total_cost = total_cost
    
if (is_card_payment == "True"):  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost = total_cost + service_charge
else:
    total_cost = total_cost

print(f"{total_cost:.2f}")
