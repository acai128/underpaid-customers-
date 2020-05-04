
#create function
def check_over_payment(customer-orders.txt):

    melon_price = 1.00 

    file = open("customer-orders.txt") #open file to accces data 

for line in file: 
    info = line.split('|') #andrea cruz, 12, 12.00

    customer_name = info[1] #access name in index 1 
    melon_num = info[2] #access melon count in index 2 
    amount_paid = float(info[3]) #access amount paid in index 3 

    expected = melon_num * melon_price #get expected price by multiplying melon number and melon price 

    if expected != amount_paid: 
        print (f"{customer_name} paid {amount_paid} but correct total is {$expcected}") 

print(check_over_payment("customer-orders.txt"))


'''

'''