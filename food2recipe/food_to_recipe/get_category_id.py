import requests
from .functions import *
import os

def get_id_list(word):
    print("get id list")
    RAKUTEN_API = os.getenv('RAKUTEN_API')
    url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426"

    params = {
        "applicationId": RAKUTEN_API,
        "format": "json",
        # "elements": "recipeTitle,recipeUrl",
        "formatVersion": 1,
        "categoryType": "small",
    }

    response = requests.get(url, params=params)    
    response_check(response)

    json_data = response.json()
    result = json_data["result"]["small"]
    
    id_list = get_category_id_list(result, word)
    return id_list


if __name__ == "__main__":
    print(get_id_list('すいとん'))
    
    
