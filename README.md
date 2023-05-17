# Food To Recipe
![Untitled (26)](https://github.com/kazukiyoda7/food2recipe/assets/96679679/ebf00b75-f807-432b-9871-0a30f42fea83)

## 主な機能

1. 食材の管理：自分の食材の基本情報を管理
2. ![Untitled (27)](https://github.com/kazukiyoda7/food2recipe/assets/96679679/3c1306cb-3026-47f0-96e5-4a3f8ea2792d)
3. 人気レシピの検索：手持ちの食材を把握しながら人気レシピを検索
![Untitled (28)](https://github.com/kazukiyoda7/food2recipe/assets/96679679/a05b9bd8-c196-4cb6-acd4-427f6f4c0fd9)

## 検索機能の概要
![検索機能の概要](https://github.com/kazukiyoda7/food2recipe/assets/96679679/eb980faf-f46c-4c3f-a1cd-ffd97808e332)

#### 一連の流れ
1. 食材の名前をサーバが受け取る
2. 楽天レシピカテゴリ一覧APIにカテゴリ一覧を要求
3. カテゴリ一覧を受け取る
4. 受け取ったカテゴリ一覧から食材の名前と一致するカテゴリがあるか探索
5. 食材名と一致するカテゴリがなければ検索を停止，あればそのカテゴリのIDを取得
6. 楽天レシピカテゴリ別ランキングAPIにアクセスし，カテゴリIDからカテゴリ上位のレシピを要求
7. APIからレシピを受け取り，クライアントにレシピ情報を返す

## 利用した技術
* Python
* Django
* HTML
* CSS
* 楽天API(レシピカテゴリ一覧API，レシピカテゴリ別ランキングAPI)

## Update予定
* 検索アルゴリズムの改善：今のままだと1種類の食材のみを元に検索をかけているため，在庫内の複数の食材を考慮した検索アルゴリズムにする必要がある．
* 利用者の好みにフィットしたレシピ提案をできるようにする（ChatGPTの利用？）．
