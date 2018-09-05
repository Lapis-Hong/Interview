#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/9/4


"""
Prob 1: Calculate information gain. 

    Gain(D, a) = Ent(D) - Ent(D|a)
    Ent(X) = -p*log(p)
    Ent(Y|X) = -p(X=x) * Ent(Y|x)
    
Prob 2: Calculate KL divergence (relative entropy).

    D(P||Q) = P(x)*log(P(x)/Q(x)) = cross_entropy(p, q) - entropy(p)
    and 0*log(0/q(x))=0; p(x)*log(p(x)/0)=infinity
    
"""
import math

# ======== Prob 1 ========


def distribution(x):
    dist = {}
    for e in x:
        dist[e] = dist.get(e, 0) + 1.0/len(x)
    return dist


def cal_entropy(x):
    dist = distribution(x)
    ent = 0.0
    for p in dist.values():
        ent += -math.log(p) * p
    return ent


def cal_condition_entropy(x, y):
    x_dist = distribution(x)
    y_cond_dist = {}
    for x_, y_ in zip(x, y):
        if x_ not in y_cond_dist:
            y_cond_dist[x_] = [y_]
        else:
            y_cond_dist[x_].append(y_)
    y_cond_ent = 0.0
    for x_, y_ in y_cond_dist.items():
        x_prob = x_dist[x_]
        y_ent = cal_entropy(y_)
        y_cond_ent += x_prob * y_ent
    return y_cond_ent


def info_gain(x, y):
    return cal_entropy(y) - cal_condition_entropy(x, y)


# ======== Prob 2 ========


def kl_divergence(x, y):
    x_dist = distribution(x)
    y_dist = distribution(y)
    value_space = list(set(x_dist.keys()) | set(y_dist.keys()))  # union set

    kl = 0.0
    for value in value_space:
        p_x = x_dist.get(value) or 0
        q_x = y_dist.get(value) or 0
        if q_x == 0:
            kl += float("inf")
        elif p_x == 0:
            kl += 0.0
        else:
            kl += p_x * math.log(p_x/q_x)
    return kl


if __name__ == '__main__':
    x = [1, 1, 2, 0, 3]
    y = [1, 1, 0, 0, 0]
    gain = info_gain(x, y)
    print(gain)

    p = [1, 1, 1, 2, 2, 4, 1, 2, 3]
    q = [1, 1, 2, 2, 2, 4, 1, 2, 3]
    kl = kl_divergence(p, q)
    print(kl)
