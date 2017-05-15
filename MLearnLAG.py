#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:56:21 2017

@author: 390771
"""
class MLearnLAG():

    def __init__(self,inputTrainPath,inputTestPath,modeName,outPutModePath,outPutModeEvelPath):
        self.__inputTrainPath = inputTrainPath
        self.__inputTestPath = inputTestPath
        self.__outPutModePath = outPutModePath
        self.__outPutModeEvelPath = outPutModeEvelPath
        self.__modeName = modeName
    def proData(self):
        print  'this is proData !'
    def train(self):
        print  'this is trainData !'
    def fit(self):
        print 'this is fit !'
    def evluateMode(self):
        print 'evluateMode suc !'

if __name__ == "__main__":
    MLearnLAG()

