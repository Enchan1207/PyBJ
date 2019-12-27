#
# ブラックジャックを書いてみる
#

import random

#--
deck = [] #山札
mycard = [] #自分の手札
cpcard = [] #CPUの手札

def main():
    #--デッキ初期化
    for n in range(52):
        deck.append(n + 1)

    print(str(len(deck)) + "毎のカードでデッキを初期化しました")

    #--自分のターン

    flg = False

    while flg == False:
        #カードを引く?
        print("山札からカードを引きますか?(y/n)")
        dat = input(">")
        if(dat in ['Y', 'y']):
            #--カードを引く
            rst = deck[random.randrange(len(deck))]
            deck.remove(rst)
            mycard.append(rst)
            print(getfig(rst) + "の" + str(getval(rst)) + "を引きました。")

        else:
            #--引かずに次へ
            print("カードを引かずに次へ進みます。")
            flg = True

        myc = calc(mycard)
        print("カードの数値:" + str(myc))

    #--CPUのターン

    #互いのカードの数値を計算
    print("カードの数値を計算します。")
    myc = calc(mycard)
    cpc = calc(cpcard)
    print("自分:" + str(myc))
    print("CPU:" + str(cpc))

    #勝敗判定
    if(myc > 20):
        print("あなたの負けです。")
    elif(myc <= 20 and myc > cpc):
        print("あなたの勝ちです。")
    else:
        print("引き分けです。")

    return 0


#--関数

#カードの数値合計を計算
def calc(cards):
    val = 0
    for card in cards:
        val += getval(card)
    
    return val


#カードの数値を取得
def getval(num):
    return num - ((num - 1) // 13) * 13

#カードの種類を取得
def getfig(num):
    print(num)
    return ["クローバー", "スペード", "ハート", "ダイヤ"][num // 14]

main()