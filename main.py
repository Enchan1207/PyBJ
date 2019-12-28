#
# ブラックジャックを書いてみる
#

from deck import Deck
from hand import Hand

#--
deck = Deck()
myhand = Hand()
cphand = Hand()

#--デッキ初期化
deck.deckinit()
print("デッキを初期化しました")

#--先にcpuもプレイヤーも強制的に一枚ドロー
myhand.add(deck.draw())
cphand.add(deck.draw())

#--自分のターン
myc = myhand.getsum()
print("カードの数値:" + str(myc))

flg = False
while flg == False:
    #カードを引く?
    print("山札からカードを引きますか?(y/n)")
    dat = input(">")
    if(dat in ['Y', 'y']):
        newcd = deck.draw()
        if(newcd != -1):
            myhand.add(newcd)
        else:
            print("山札が空です。")
            flg = True

    else:
        flg = True

    myc = myhand.getsum()
    print("カードの数値:" + str(myc))

#--CPUのターン

#次に何を引いても負けにならない(=20-13=7未満)なら引き続ける
cpc = cphand.getsum()
while cpc < 7:
    cphand.add(deck.draw())
    cpc = cphand.getsum()

#TODO:
#これだとwhileの最後に来たカードまたは一発目に引いた7以上のカードだけで勝負が決まってしまうので、
#「勝負に行くかどうか」を考えなきゃならない

#互いのカードの数値を計算
print("カードの数値を計算します。")
myc = myhand.getsum()
cpc = cphand.getsum()
print("自分:" + str(myc))
print("CPU:" + str(cpc))

#勝敗判定
if(myc > 20 or myc < cpc):
    print("あなたの負けです。")
elif(myc <= 20 and myc > cpc):
    print("あなたの勝ちです。")
else:
    print("引き分けです。")

exit(0)