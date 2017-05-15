#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:56:21 2017

@author: 390771
"""
import os
import pydub
import python_speech_features as psf
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
path = r'/home/390771/Data/noise/audiolib/norNoise'
outputPath = r'/home/390771/cc/norNoise'
fileName = os.listdir(path)[1]
print fileName
pathName = os.path.join(path, fileName)
if fileName.find(".mp3") != -1 or fileName.find(".MP3") != -1:
    sounds = pydub.AudioSegment.from_mp3(pathName)
elif fileName.find(".wav") != -1 or fileName.find(".WAV") != -1:
    sounds = pydub.AudioSegment.from_wav(pathName)
else:
    print 'error !'
sampleDatas = sounds.get_array_of_samples()
arrSampleDatas = np.array(sampleDatas)
norSampleDatas = preprocessing.normalize(arrSampleDatas)
print sounds.channels
channelsIndex = np.array(range(0,norSampleDatas.shape[0],2))
#
channelTwoIndex = np.array(range(1,norSampleDatas.shape[0],2))
#
dataChannelOne = arrSampleDatas[channelsIndex]
#
plt.plot(dataChannelOne)
dataChannelTwo = arrSampleDatas[channelTwoIndex]
#
plt.plot(dataChannelTwo)
# datas.tofile(r'/home/390771/a.txt')
# frame_rate = sounds.frame_rate
# rawData = sounds.raw_data
#
# print sounds.frame_rate
#
#
#
#
# datasArrary = np.array(datas)
# file_path = r'/home/390771/a.txt'

# fp = open(file_path, "w+")
# for item in sounds.raw_data:
#     fp.write(str(item) + "\n")  # list中一项占一行
#     fp.close()
# dataIndex = np.array(range(0,len(datasArrary),2))
# psMFCC = psf.mfcc(datasArrary[dataIndex], frame_rate)
# temp = psMFCC.tolist()
 
 
 