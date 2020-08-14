# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:54:14 2020

@author: CCCam

Contains funciton to plot prediction error chart that will be used in jupyter notebook
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import mean_absolute_error as MAE

def prediction_error_chart(y_train, y_test, y_train_pred,y_test_pred):
    #plot predictions against actual values
    sns.set_style('whitegrid')
    sns.set_palette(sns.color_palette("BrBG", 2))
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=y_train_pred, y=y_train,alpha=.8)
    sns.scatterplot(x=y_test_pred, y=y_test,alpha=.8)
    
    #create perfect prediction line
    xmin, xmax = plt.xlim()
    plt.plot(np.arange(xmin, xmax, 0.01), np.arange(xmin, xmax, 0.01), c='k')

    plt.title('Prediction vs Actual', fontweight = 'bold')
    plt.xlabel('Prediction')
    plt.ylabel('Actual')
    plt.legend(loc = 'upper left', labels =['Perfect Accuracy','Train','Test'])
    plt.grid()
    plt.show()
    
    #compute RMSE for train and test data
    train_MAE = MAE(y_train_pred,y_train).round(2)
    test_MAE = MAE(y_test_pred,y_test).round(2)

    print('Train MAE: ' + str(train_MAE))
    print('Test MAE: ' + str(test_MAE))
