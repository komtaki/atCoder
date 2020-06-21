money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)


def resolve():
    for i in range(2 ** n):
        bag = []
        for j in range(n):  # このループが一番のポイント
            if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める

    print(bag)


resolve()