
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
items1 = [Item(2,3), Item(3,4), Item(4,8), Item(5,8), Item(9,10)]
items2 = [Item(10,60), Item(20,100), Item(30,120)]

def knapsack_recursive(itemlist, totalweight):
    '''return the maximum value that can be put in a knapsack
       that holds totalweight'''
    if totalweight == 0 or itemlist == []:
        return 0
    if itemlist[0].weight > totalweight:
        return knapsack_recursive(itemlist[1:], totalweight)
    else:
        a = knapsack_recursive(itemlist[1:], totalweight - itemlist[0].weight)
        b = knapsack_recursive(itemlist[1:], totalweight)
        val_with_item = itemlist[0].value + a                          
        val_without_item = b
        return max(val_with_item, val_without_item)

define knapsack_dynamic(itemlist, totalweight):
    tab = dict()
    for item in range(len(itemlist)+1):
        for weight in range(totalweight+1):
            if item == 0 or weight == 0:
                tab[item,weight] = 0
            elif tab[item,weight] <= totalweight:
                tab[item,weight] = max(itemlist[i-1] +
    

print(knapsack_recursive(items1, 20))
        
print(knapsack_recursive(items2, 50))
        
    
