
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

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

def knapsack_dynamic(itemlist, totalweight):
    tab = dict()
    for item in range(len(itemlist)+1):
        for weight in range(totalweight+1):
            if item == 0 or weight == 0:
                tab[item,weight] = 0
            elif itemlist[item-1].weight <= weight:
                a = itemlist[item-1].value + \
                    tab[item-1, weight-itemlist[item-1].weight]
                b = tab[item-1, weight]
                tab[item,weight] = max(a,b)
            else:
                tab[item,weight] = tab[item-1, weight]
    return tab[len(itemlist),totalweight]

if __name__ == '__main__':
        
    items1 = [Item(2,3), Item(3,4), Item(4,8), Item(5,8), Item(9,10)]
    items2 = [Item(10,60), Item(20,100), Item(30,120)]
    print(knapsack_recursive(items1, 20))
            
    print(knapsack_recursive(items2, 50))
    print(knapsack_dynamic(items1, 20))
            
    print(knapsack_dynamic(items2, 50))
            
    
