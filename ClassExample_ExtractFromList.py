the_list = ["James", 75, ["first", "baby"], ("football", "orange",), {"position":"first"}]

def extract_list(item_list):
    for item in item_list:
        if type(item) == list or type(item) == tuple:
            for item_b in item:
                print(item_b)
        elif type(item) == dict:
            for key in item:
                print(item[key])
        
        else:
            
            print(item)


extract_list(the_list)
