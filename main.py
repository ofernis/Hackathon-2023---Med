import numpy as np
import pandas as pd
import os
import Visualize as vis
import Model as model

# random ages between 30-45
def gen_age():
    # generate random number between 30-45
    age = np.random.randint(30, 46)
    return age

# random FSH between 1-20
def gen_FSH():
    # generate random number between 1-20 with mean 10 and std 5
    mean = 10
    std = 5
    sample = np.random.normal(mean, std, 1)
    return round(abs(sample[0]))

# random AMH between 0.5-1.5
def gen_AMH():
    mean = 0.85
    std = 0.1
    sample = np.random.normal(mean, std, 1)
    return abs(sample[0])

# random Estradiol between 50-200
def gen_Estradiol():
    mean = 100
    std = 15
    sample = np.random.normal(mean, std, 1)
    return abs(sample[0])

# random LH between 15-40
def gen_LH():
    mean = 30
    std = 5
    sample = np.random.normal(mean, std, 1)
    return abs(sample[0])

# u35 - 80% 35-7:76% 38-40:66% 40-45:40%
def gen_FR(age):
    mean = 0.5
    std = 0.1

    if age < 35:
        mean = 0.8
        std = 0.1
    elif age < 38:
        mean = 0.76
        std = 0.1
    else:
        mean = 0.4
        std = 0.05

    sample = np.random.normal(mean, std, 1)
    res = abs(sample[0])
    # round res to one number after the dot
    res = round(res, 1)
    return res


def generate_row():
    AGE = gen_age()
    FSH = gen_FSH()
    AMH = gen_AMH()
    Estradiol = gen_Estradiol()
    LH = gen_LH()
    FR = gen_FR(AGE)
    return [AGE, FSH, AMH, Estradiol, LH, FR]

def generate_data():
    # creating empty data frame
    # FR - fertility  rate
    for j in range(0, 7):
        df = pd.DataFrame(columns=['AGE', 'FSH', 'AMH', 'Estradiol', 'LH', 'FR'])

        # adding data_size of rows to df
        data_size = 1000
        for i in range(0, data_size):
            row_data = generate_row()
            # +1 is because the dummy 0 row
            df.loc[str(i + 1)] = row_data

        print(df.loc[:, 'FR'].mean())

        # exporting df to excel
        os.makedirs('t2med_fertility', exist_ok=True)
        index = j+1
        name = 't2med_fertility/fertility_data_day' + str(index) + '.csv'
        df.to_csv(name)


if __name__ == '__main__':
    # generate_data()
    # vis.visualize()
    # print("Forecast is: ", [round(x, 2) for x in model.result()])
    model.print_map()
