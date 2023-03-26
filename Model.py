import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import sklearn as sk


def result():
    df = pd.DataFrame(columns=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'])
    k = 3  # number of neighbors
    data = pd.read_csv('t2med_fertility/fertility_data_day1.csv')
    X = data.drop('FR', axis=1)
    y = data['FR']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_vec = []

    for i in range(7):
        model_vec.append(KNeighborsRegressor(n_neighbors=k))

    subd_X_train = np.array_split(X_train, 7)
    subd_y_train = np.array_split(y_train, 7)
    subd_X_test = np.array_split(X_test, 7)
    subd_y_test = np.array_split(y_test, 7)

    pred_vec = []

    # Print the sub-DataFrames
    for i in range(7):
        model_vec[i].fit(subd_X_train[i], subd_y_train[i])
        y_pred = model_vec[i].predict(subd_X_test[i])
        pred_vec.append(y_pred[0])

    return pred_vec

    # model.fit(X_train, y_train)
    # y_pred = model.predict(X_test)
    # mse = mean_squared_error(y_test, y_pred)
    # print('MSE')

def print_map():
    df = pd.DataFrame(columns=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'])
    df.loc[0] = [0.5, 0.73, 0.73, 0.8, 0.67, 0.57, 0.67]
    # create heatmap by column
    sns.heatmap(df, annot=True, cmap='viridis')
    plt.show()