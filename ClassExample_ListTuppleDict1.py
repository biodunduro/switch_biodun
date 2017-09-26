the_list = ["James", 75, ["first", "baby"], ("football", "orange",), {"position":"first"}]

def extract_list(item_list):
    for item in item_list:
        print(item)


extract_list(the_list)
