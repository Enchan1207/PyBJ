#
# カード管理クラス
#

class Card(object):
    """Card manage class"""

    #--コンストラクタ
    def __init__(self, intval_): #単純に初期化
        self.intval = intval_

    #--カードに値を設定
    def set(self, intval_):
        self.intval = intval_

    #--カードの数値を取得
    def getval(self):
        return self.intval - ((self.intval - 1) // 13) * 13

    #カードの種類を取得
    def getfig(self):
        return ["クローバー", "スペード", "ハート", "ダイヤ"][self.intval_ // 14]

    
