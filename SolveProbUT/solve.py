import time
import numpy as np
from multiprocessing import Pool

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

if __name__=="__main__":
    #n = 10**6
    for pw in 3,4,5,6,7:
        n = 10**pw
        start = time.time()
        r = q1(n)
        print(n, *r, time.time() - start, sep="\t")
        start = time.time()
        r = q2(n)
        print(n, *r, time.time() - start, sep="\t")
    """
    1000    0.22702052588333171     0.2809794741166683      0.36499977111816406
    1000    0.5220342008391219      0.6433201298695395      0.3580005168914795
    10000   0.24398502263489805     0.261014977365102       0.636000394821167
    10000   0.5928733635883228      0.630889012649301       0.6389992237091064
    100000  0.25217897752684854     0.25758102247315146     3.385000467300415
    100000  0.6094937040807653      0.6214384993090651      3.374000072479248
    1000000 0.2539379587327672      0.25564604126723284     32.734031677246094
    1000000 0.6104900979745831      0.6142736308709065      35.806997537612915
    10000000        0.2543673823815792      0.25490741761842084     350.6612038612366
    10000000        0.6123109189884975      0.6135074407654114      356.3810029029846"""