
def exchange_money(budget, exchange_rate):
   

    return budget/exchange_rate
print(exchange_money(220,2))

def get_change(budget, exchanging_value):

    return budget - exchanging_value
print("The change is:",get_change(227.50,210))


def get_value_of_bills(denomination, number_of_bills):#denomation:single value of bill,the total number of bill
    
    return denomination * number_of_bills
print("The value of bills is:",get_value_of_bills(10,200))


def get_number_of_bills(amount, denomination):
   
    return amount//denomination
print("The Number of bills:",get_number_of_bills(589,10))
    


def get_leftover_of_bills(amount, denomination):
    
    return amount%denomination
print("The left amount is",get_leftover_of_bills(589,10))


def exchangeable_value(budget, exchange_rate, spread, denomination):

    return ((budget/(exchange_rate *(1+spread/100)))// denomination*denomination)
print("The exchangable value is ",exchangeable_value(220,2,5,21))
