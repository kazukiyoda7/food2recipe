import re

def response_check(response):
    if response.status_code == 200:
        print("OK: 200")
        return 200
    else:
        print(f"Error: {response.status_code}")
        return 0
    

def get_category_id_list(result, word):
    id_list = list(map(lambda x: re.search(r'category/(\d+-\d+-\d+)/',x['categoryUrl']).group(1), filter(lambda x: x['categoryName'] == word, result)))
    return id_list