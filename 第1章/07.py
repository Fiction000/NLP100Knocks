'''
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''
# coding: utf-8

def xyz(x, y, z):
    """「x時のｙはｚ」という文字列を返す"""
    return str(x) + "時の" + str(y) + "は" + str(z)

x = 12
y = "気温"
z = 22.4
print(xyz(x, y, z))
