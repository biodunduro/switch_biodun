the_list = ["James", 75, ["first", "baby"], ("football", "orange",), {"position":"first"}, "Ben", 250, {"make":"samsung",}]

def extract_list(item_list):
    for item in item_list:
        if type(item) == list or type(item) == tuple:
            extract_list(item)
        if type(item) == dict:
            extract_list(item[key])

            print(item)
        


extract_list(the_list)
