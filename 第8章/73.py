import numpy as np
from stemming.porter2 import stem
import pylab as pl
import codecs
import scipy.optimize as opt

fname_features = 'features.txt'
sentiments = 'sentiment.txt'
stopwords = []

with open('stopwords.txt') as f:
    """http://xpo6.com/list-of-english-stop-words/より"""
    for line in f:
        stopwords.append(line.strip('\n'))

def stopword_or_not(word):
    if word in stopwords:
        return True
    return False

def sigmoid(X):
    return 1 / (1 + np.exp(- X))

def cost(theta, X, y):
    p_1 = sigmoid(np.dot(X, theta)) # predicted probability of label 1
    log_l = (-y)*np.log(p_1) - (1-y)*np.log(1-p_1) # log-likelihood vector

    return log_l.mean()

def grad(theta, X, y):
    p_1 = sigmoid(np.dot(X, theta))
    error = p_1 - y # difference between label and prediction
    grad = 1 / y.size * (p_1 - y).dot(X)# gradient vector

    return grad

def extract_features(data, dict_features):
    '''文章から素性を抽出
    文章からdict_featuresに含まれる素性を抽出し、
    dict_features['(素性)']の位置を1にした行列を返す。
    なお、先頭要素は固定で1。素性に対応しない重み用。

    戻り値：
    先頭要素と、該当素性の位置+1を1にした行列
    '''
    data_one_x = np.zeros(len(dict_features) + 1, dtype=np.float64)
    data_one_x[0] = 1       # 先頭要素は固定で1、素性に対応しない重み用。

    for word in data.split(' '):

        # 前後の空白文字除去
        word = word.strip()

        # ストップワード除去
        if stopword_or_not(word):
            continue

        # ステミング
        word = stem(word)

        # 素性のインデックス取得、行列の該当箇所を1に
        try:
            data_one_x[dict_features[word]] = 1
        except:
            pass        # dict_featuresにない素性は無視

    return data_one_x

def load_dict_features():
    '''features.txtを読み込み、素性をインデックスに変換するための辞書を作成
    インデックスの値は1ベースで、features.txtにおける行番号と一致する。

    戻り値：
    素性をインデックスに変換する辞書
    '''
    with codecs.open(fname_features, 'r') as file_in:
        return {line.strip(): i for i, line in enumerate(file_in, start=1)}


def create_training_set(sentiments, dict_features):
    '''正解データsentimentsから学習対象の行列と、極性ラベルの行列を作成
    学習対象の行例の大きさは正解データのレビュー数×(素性数+1)。
    列の値は、各レビューに対して該当素性がある場合は1、なければ0になる。
    列の素性のインデックスはdict_features['(素性)']で決まる。
    先頭の列は常に1で、素性に対応しない重みの学習用。
    dict_featuresに存在しない素性は無視。

    極性ラベルの行列の大きさはレビュー数×1。
    肯定的な内容が1、否定的な内容が0。

    戻り値：
    学習対象の行列,極性ラベルの行列
    '''

    # 行列を0で初期化
    data_x = np.zeros([len(sentiments), len(dict_features) + 1], dtype=np.float64)
    data_y = np.zeros(len(sentiments), dtype=np.float64)

    for i, line in enumerate(sentiments):

        # 素性抽出
        data_x[i] = extract_features(line[3:], dict_features)

        # 極性ラベル行列のセット
        if line[0:2] == '+1':
            data_y[i] = 1

    return data_x, data_y


def predict(theta, X):
    '''Predict whether the label
    is 0 or 1 using learned logistic
    regression parameters '''
    m, n = X.shape
    p = np.zeros(shape=(m, 1))

    h = sigmoid(X.dot(theta.T))

    for it in range(0, h.shape[0]):
        if h[it] > 0.5:
            p[it, 0] = 1
        else:
            p[it, 0] = 0

    return p

def hypothesis(data_x, theta):
    '''仮説関数
    data_xに対して、thetaを使ってdata_yを予測

    戻り値：
    予測値の行列
    '''
    return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))

with codecs.open(sentiments, 'r') as f:
    X, y = create_training_set(list(f), dict_features)

theta = np.zeros(X.shape[1])
dict_features = load_dict_features()
X, y = create_training_set(sentiments, dict_features)
theta_1 = opt.fmin_bfgs(cost, theta, fprime=grad, args=(X, y))

with codecs.open(sentiments, 'r') as f:
    for line in f:
        # 素性抽出
        X = extract_features(line[3:], dict_features)

        # 予測、結果出力
        h = hypothesis(X, theta_1)
        if h > 0.5:
            print('{}\t{}\t{}\n'.format(line[0:2], '+1', h))
        else:
            print('{}\t{}\t{}\n'.format(line[0:2], '-1', 1 - h))
