import csv
movie_list_injp = [["トップ・ガン", "危険なビジネス", "マイノリティリポート"],
                   ["タイタニック", "レベナント", "インセプション"],
                   ["訓練の日々", "火事場の男", "飛行"]]

with open("movie_in_jp.csv", "w", encoding="UTF-8") as f:
    w = csv.writer(f, delimiter=",")
    for list in movie_list_injp:
        w.writerow(list)
