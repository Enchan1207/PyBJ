#
# 手札管理クラス
#

from card import Card

class Hand(Card):
    """Hand manage class"""

    #--コンストラクタ
    def __init__(self):
        self.hand = []

    #--手札にカードを追加
    def add(self, num):
        self.hand.append(Card(num))

    #--手札の合計数値を取得
    def getsum(self):
        val = 0
        for card in self.hand:
            val += card.getval()
        
        return val

