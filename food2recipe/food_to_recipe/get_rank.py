import requests
from .functions import *
from .get_category_id import get_id_list
import os

def get_ranking(id_list):

    RAKUTEN_API = os.getenv('RAKUTEN_API')
    url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"

    # レシピの取得
    print("get recipes")
    params = {
        "applicationId": RAKUTEN_API,
        "format": "json",
        # "elements": "recipeTitle,recipeUrl",
        "formatVersion": 1,
        "categoryId": id_list[0],
    }


    response = requests.get(url, params=params)
    response_check(response)

    json_data = response.json()
    ranking = json_data["result"]
    return ranking

    
if __name__ == "__main__":
    id_list = get_id_list('すいとん')
    ranking = get_ranking(id_list)
    print(ranking)