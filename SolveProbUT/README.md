# SolveProbUT

東大入試問題2023［2］ をモンテカルロシミュレーションで解く．

参考：[東大の確率問題にシミュレーションで挑戦してみた【2023 東京大学】](https://www.youtube.com/watch?v=sX93c46Jfmw)

## 問題文

引用： [令和5年度第2次学力試験 | 東京大学](https://www.u-tokyo.ac.jp/ja/admissions/undergraduate/e01_05_23.html) 数学（理科）

> **第2問**
> 黒玉3個，赤玉4個，白玉5個が入っている袋から玉を1個ずつ取り出し，取り出した玉を順に横一列に12個すべて並べる。ただし，袋から個々の玉が取り出される確率は等しいものとする。  
> (1) どの赤玉も隣り合わない確率 $p$ を求めよ。  
> (2) どの赤玉も隣り合わないとき，どの黒玉も隣り合わない条件付き確率 $q$ を求めよ。

答えは  
(1): 14/55≒0.2545...  
(2): 103/168≒0.6130...

## シミュレーション

### (1)

```py
box = np.array([0,0,0,1,1,1,1,2,2,2,2,2])
process = 8
width = 1.95996

def trial(rnd:np.random.RandomState):
    """黒(0)x3, 赤(1)x4, 白(2)x5 をランダムに並べた配列を得る"""
    return rnd.choice(box, 12, replace=False)

def red(seq):
    """配列`seq`で赤が隣り合わない条件"""
    for i in range(11):
        if 1==seq[i]==seq[i+1]: return False
    return True

def q1_sub(random_state):
    """ランダム順列を生成し，赤が隣り合わないなら1,そうでなければ0を返す"""
    seq = trial(np.random.RandomState(random_state))
    return int(red(seq))

def q1(n_trial):
    """`q1_sub`を`n_trial`回試行（並列実行）して確率 p の信用区間を得る"""
    with Pool(process) as p:
        res = p.map(q1_sub, range(n_trial))
    count = sum(res)
    p = count / n_trial
    w = ((p*(1-p))/n_trial)**0.5
    return p - width * w, p + width * w
```

実行結果

```text
1000    0.22702052588333171     0.2809794741166683
10000   0.24398502263489805     0.261014977365102
100000  0.25217897752684854     0.25758102247315146
1000000 0.2539379587327672      0.25564604126723284
10000000        0.2543673823815792      0.25490741761842084
```

シミュレーションにより， $n=10^7$ で95%信頼区間 $0.2543\dots < p < 0.2549\dots$ を得た．  
これは真の値 $p=14/55\fallingdotseq 0.2545\dots$ と矛盾しない．

### (2)

```py
def red_and_black(seq):
    """配列`seq`で赤が隣り合わず，かつ黒が隣り合わない条件"""
    for i in range(11):
        if 1==seq[i]==seq[i+1]: return False
    for i in range(11):
        if 0==seq[i]==seq[i+1]: return False
    return True

def q2_sub(random_state):
    """ランダム順列を生成し，赤，黒が隣り合わないなら1,そうでなければ0をそれぞれ返す"""
    seq = trial(np.random.RandomState(random_state))
    r = red(seq)
    count_r = int(r)
    if r:
        count_rb = int(red_and_black(seq))
    else:
        count_rb = 0
    return count_r, count_rb


def q2(n_trial):
    """`q2_sub`を`n_trial`回試行（並列実行）して確率 q の信用区間を得る"""
    with Pool(process) as p:
        res = p.map(q2_sub, range(n_trial))
    count_r, count_rb = np.sum(res, axis=0)
    q = count_rb / count_r
    w = ((q*(1-q))/count_r)**0.5
    return q - width * w, q + width * w
```

実行結果

```text
1000    0.5220342008391219      0.6433201298695395
10000   0.5928733635883228      0.630889012649301
100000  0.6094937040807653      0.6214384993090651
1000000 0.6104900979745831      0.6142736308709065
10000000        0.6123109189884975      0.6135074407654114
```

シミュレーションにより， $n=10^7$ で95%信頼区間 $0.6123\dots < p < 0.6135\dots$ を得た．  
これは真の値 $q=103/168\fallingdotseq 0.6130\dots$ と矛盾しない．
