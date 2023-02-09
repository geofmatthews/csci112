
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
    values = dict()
    for item in range(len(itemlist)+1):
        for weight in range(totalweight+1):
            if item == 0 or weight == 0:
                values[item,weight] = 0
            elif itemlist[item-1].weight <= weight:
                a = itemlist[item-1].value + \
                    values[item-1, weight-itemlist[item-1].weight]
                b = values[item-1, weight]
                values[item,weight] = max(a,b)
            else:
                values[item,weight] = values[item-1, weight]
    texdump(values,len(itemlist)+1,totalweight+1)
    return values[len(itemlist),totalweight]

def texdump(values, nrows, ncols):
    print('\\begin{tabular}{|' + 'c|'*(1+ncols) + '}\\hline')
    for j in range(ncols+1):
        if j < 1:
            print('   &',end='')
        elif j < ncols:
            print(j-1,  end=' &')
        else:
            print(j-1, end='\\\\\\hline')
    for i in range(nrows):
        print(i, end=' &')
        for j in range(ncols):
            ender = ' &' if j < ncols-1 else ' \\\\\\hline\n'
            if (i,j) in values:
                print(values[i,j], end=ender)
            else:
                print('', end=ender)
    print('\\end{tabular}')
            
            

if __name__ == '__main__':
    import random
        
    items1 = [Item(2,3), Item(3,4), Item(4,8), Item(5,8), Item(9,10)]
    items2 = [Item(10,60), Item(20,100), Item(30,120)]
    print(knapsack_recursive(items1, 20))
    print(knapsack_recursive(items2, 50))
    print(knapsack_dynamic(items1, 20))
    print(knapsack_dynamic(items2, 50))
    weights = [random.randint(2,20) for i in range(5)]
    values = [random.randint(2,20) for i in range(5)]
    items = [Item(i,j) for i,j in zip(weights,values)]
    print(list(zip(weights,values)))
    print(knapsack_dynamic(items, 20))
            
    
