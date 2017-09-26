def calculate_area():
    length = input('Enter length: ')
    breadth = input('Enter breadth: ')

    while not str.isdigit(length) and not str.isdigit(breadth):
        print('Please enter values')
        length = input('Enter length: ')
        breadth = input('Enter breadth: ')
        print('Please enter values')
        
    else:
        length = int(length)
        breadth = int(breadth)
        area = length * breadth
        print('The area of the shape is: ', area)
        return area




calculate_area()
