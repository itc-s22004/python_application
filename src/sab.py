from collections import defaultdict

import numpy as np
import requests
from googletrans import Translator
from matplotlib import pyplot as pyp

fir = "https://api.punkapi.com/v2/beers"
res = requests.get(fir)
cho = res.json()


for i in range(len(cho)):
    name = cho[i]["name"]
    id = cho[i]["id"]
    print(name, id)


while True:
    pref = int(input("number:"))
    url = "https://api.punkapi.com/v2/beers?ids=" + str(pref)
    res = requests.get(url)
    beer = res.json()

    for i in range(len(beer)):
        name = beer[i]["name"]
        id = beer[i]["id"]
        des_en = beer[i]["description"]
        tr = Translator(service_urls=["translate.googleapis.com"])
        des_ja = tr.translate(des_en, dest="ja").text

        ma = beer[i]["ingredients"]["malt"]
        len_malt = len(ma)
        malt_name = []
        malt_amount = []
        malt_dict = defaultdict(list)
        for j in range(len_malt):
            malt = ma[j]["name"]
            malt_name.append(malt)
            malt_amo_val = ma[j]["amount"]["value"]
            malt_amount.append(malt_amo_val)
            malt_dict[malt].append(malt_amo_val)

        ho = beer[i]["ingredients"]["hops"]
        len_hops = len(ho)
        hops_name = []
        hops_amount = []
        hops_dict = defaultdict(list)
        for j in range(len_hops):
            hops = ho[j]["name"]
            hops_name.append(hops)
            hops_amo_val = ho[j]["amount"]["value"]
            hops_amount.append(hops_amo_val)
            hops_dict[hops].append(hops_amo_val)

    print(name, id)
    print(des_ja)

    def func(pct, allvals):
        absolute = int(pct / 100.0 * np.sum(allvals))
        return "{:.1f}% ({:d} )".format(pct, absolute)

    while True:
        selection = input("pie: malt > 1 or hops > 2: ")
        if selection == "1":
            labels1, labels2 = malt_name, hops_name
            data1, data2 = malt_amount, hops_amount
            ex = [0 for i in range(len(data1))]
            pyp.pie(data1, labels=labels1, explode=ex, autopct="%11.1f%%")
            print(f"麦：{malt_dict}")
            pyp.title("beer : malt")
            pyp.show()
            """
            fig, ax = pyp.subplots(subplot_kw=dict(aspect="equal"))

            explode = [0 for i in range(len(data1))]
            wedges, texts, autotexts = ax.pie(
                data1,
                autopct=lambda pct: func(pct, data1),
                startangle=140,
                ecplode=explode,
            )
            ax.legend(wedges, labels1, title="pie1", loc="pie2")
            pyp.setp(autotexts, size=10, weight=700)
            ax.set_title("pie3")
            pyp.show()
            """

        if selection == "2":
            ex = [0 for i in range(len(data2))]
            pyp.pie(data2, labels=labels2, explode=ex, autopct="%11.1f%%")
            print(f"ホップ：{hops_dict}")
            pyp.title("beer : hops")
            pyp.show()
        # if selection == '':

        if selection := input("他をpie y/n: ") == "n":
            break

    if res := input("他を見る？ y/n: ") == "n":
        break
