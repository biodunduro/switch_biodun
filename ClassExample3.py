print('====This is a program for calculating pythagoras theorem====')

def find_hypotenus():
    opposite = input('Enter value for opposite: ')
    adjacent= input('Enter value for adjacent: ')

    while not str.isdigit(opposite) and not str.isdigit(adjacent):
        print('Please enter values')
        opposite = input('Enter value for opposite: ')
        adjacent = input('Enter value for adjacent: ')
        
        
    else:
        opposite= int(opposite)
        adjacent = int(adjacent)
        hypotenus = opposite**2 - adjacent**2
        print('The value is: ', hypotenus)
        return hypotenus




find_hypotenus()
