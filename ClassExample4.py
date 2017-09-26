print('====This program finds the side of a right angle triangle using a formula ===')

def findSide(side_unknown, knownside1, knownside2):
    '''hyp, adj, opp'''
    side_unknown = ''
    side_unknown = input("Please enter the side you want to find: ' 'adj' or 'hyp' or 'opp'")
    sides_list=['hyp', 'adj', 'opp']
    if side_unknown in sides_list:
        if side_unknown == 'hyp':
            side_unknown = (knownside1**2 + knownside2**2)**0.5
        elif side_unknown == 'adj':
            side_unknown = knownside1**2 - knownside2**2
        elif side_unknown == 'opp':
            side_unknown = knownside1**2 + knownside2**2
        print('The side unknown is', side_unknown)
        return side_unknown

findSide('hyp', 12, 15)
