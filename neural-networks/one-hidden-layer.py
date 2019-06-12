# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 13:46:08 2018

@author: usman
"""
 
import numpy as np  

np.random.seed(0)

def sigmoid(x):  
    return 1/(1+np.exp(-x))

def sigmoid_der(x):  
    return sigmoid(x) *(1-sigmoid (x))

feature_set = np.array([[0,1,0,1],
                        [0,0,1,0],
                        [1,0,1,0],
                        [1,1,0,1]])
labels = np.array([1,0,0,1]).reshape(4,1)
wh = np.random.rand(len(feature_set[0]),4)  
wo = np.random.rand(4, 1)  
lr = 0.1

for epoch in range(1500):  
    # feedforward
    zh = np.dot(feature_set, wh)
    ah = sigmoid(zh)

    zo = np.dot(ah, wo)
    ao = sigmoid(zo)

    # Phase1 =======================

    error_out = ((1 / 2) * (np.power((ao - labels), 2)))

    dcost_dao = ao - labels
    dao_dzo = sigmoid_der(ao) 
    dzo_dwo = ah

    dcost_wo = np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

    # Phase 2 =======================

    # dcost_w1 = dcost_dah * dah_dzh * dzh_dw1
    # dcost_dah = dcost_dzo * dzo_dah
    dcost_dzo = dcost_dao * dao_dzo
    dzo_dah = wo
    dcost_dah = np.dot(dcost_dzo , dzo_dah.T)
    dah_dzh = sigmoid_der(zh) 
    dzh_dwh = feature_set
    dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

    # Update Weights ================

    wh -= lr * dcost_wh
    wo -= lr * dcost_wo

def calc(arr):
    input = np.array(arr)
    l1 = sigmoid(np.dot(input, wh))
    o = sigmoid(np.dot(l1, wo))
    return o

# print(calc([0,1,0,0]))
# print(dcost_dao * dao_dzo)
# print(np.dot(dzo_dwo,dcost_dao * dao_dzo))
print(ao)
