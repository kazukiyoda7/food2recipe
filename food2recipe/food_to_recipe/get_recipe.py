from .get_category_id import get_id_list
from .get_rank import get_ranking
import time

def get_recipes(word):
    # 検索ワードのID取得
    id_list = get_id_list(word)
    if len(id_list)==0:
        print("該当するレシピがありませんでした。")

    # 3秒間インターバル
    time.sleep(3)

    # ランキング取得
    ranking = get_ranking(id_list)
    ranking = ranking[:5]

    return ranking