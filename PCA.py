# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:13:54 2016

@author: YI
"""

import numpy as np

#feature scaling
def normalize(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    norm = (data - mean)/ std
    return norm

 
def pca(data,n):
    norm = normalize(data)  
    #covariance
    covmat = np.cov(norm, rowvar=0)
    #rowvar!=0 each row represents a variable, with observations in the columns

    #eigenvalues and eigenvectors
    eigvalues, eigvectors = np.linalg.eig(np.mat(covmat))
    #eigvectors: one column is a eigenvector

    #keep the principal components k
    eigvaluesIndice = np.argsort(eigvalues)
    max_eigvaluesIndice = eigvaluesIndice[-1:-(n+1):-1]
    max_eigvectors = eigvectors[:,max_eigvaluesIndice]
    newdata = norm * max_eigvectors
    return newdata
    
#calculate n based on the percentage
def n(eigenvalues,percentage):
    sort_eigvalues = np.sort(eigenvalues)
    sort_eigvalues = sort_eigvalues[-1::-1]
    sum_eigvalues = np.sum(sort_eigvalues)
    pmsum = 0
    num = 0
    for i in sort_eigvalues:
        if pmsum >= sum_eigvalues * percentage:
            return num
    pmsum += 0
    num += 1
    



