# Paste your code into this box 
def item_order(order):
    orders = order.split() 
    
    output = 'salad:' + str(orders.count('salad')) + ' '
    output += 'hamburger:' + str(orders.count('hamburger')) + ' '
    output += 'water:' + str(orders.count('water'))
    
    return output
    
order = item_order("salad water hamburger salad hamburger")
print order