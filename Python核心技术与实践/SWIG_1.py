# -*- coding:utf8 -*-
# @Time：2022/1/12 2:11 PM
# @Author： Huang Jeff

import numpy as np


def comptue_pca(data):
    m = np.mean(data, axis=0)
    datac = np.array([obs - m for obs in datq])
    T = np.dot(datac, datac.T)
    [u, s, v] = np.linalg.svd(T)

    pcs = [np.dot(datac.T, item) for item in u.T]

    return pcs, m, s, T, u


def compute_projections(I, pcs, m):
    projections = []
    for i in I:
        w = []
        for p in pcs:
            w.append(np.dot(i - m, p))
        projections.append(w)
    return projections


def reconstruct(w, X, m, dim=5):
    return np.dot(w[:dim], x[:dim, :]) + m


def normalize(samples, maxs=None):
    if not maxs:
        maxs = np.max(samples)
    return np.array([np.ravel(s) / maxs for s in samples])
