import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize():
    dataset = pd.read_csv("t2med_fertility/fertility_data_day1.csv")
    # dataset.plot.scatter(x="AGE", y="FSH", c="FR", colormap="viridis")
    # plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    ax.scatter(dataset[["AGE"]], dataset[["FSH"]], dataset[["Estradiol"]], c=dataset[["FR"]], s=(plt.rcParams['lines.markersize'] * 0.6) ** 2)

    ax.set_xlabel('AGE')
    ax.set_ylabel('FSH')
    ax.set_zlabel('Estradiol')

    plt.show()

    # g = sns.pairplot(training_set[["spread", "PCR_01", "PCR_02", "PCR_09"]], plot_kws={"s": 12}, hue = "spread")
    # g.fig.suptitle("pcr-spread correlation", y=1.04)
    # for ax in np.ravel(g.axes):
    #  ax.grid(alpha=0.5)
    # g.fig.set_size_inches(12,8)

