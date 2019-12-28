#
# 山札管理クラス
#

import random
from card import Card

class Deck(Card):
    """Deck manage class"""

    #--コンストラクタ
    def __init__(self):
        self.deck = []

    #--デッキを初期化
    def deckinit(self):
        for n in range(52):
            self.deck.append(Card(n))

    #--デッキからカードを引く
    def draw(self):
        if(len(self.deck) == 0):
            return -1
            
        rst = random.choice(self.deck)
        self.deck.remove(rst)
        return rst.getval()
