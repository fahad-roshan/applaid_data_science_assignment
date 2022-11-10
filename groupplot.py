

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#reading the csv file
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)

def groupedgraph(): # creating a function
    # plotting grouped graph 
    plt.figure(figsize=(45,20))
    teams = np.arange(len(data_["name"]))
    width=0.40
    plt.xlabel("CLUBS",fontsize=60)
    plt.ylabel("offensive and defensive",fontsize=60)
    plt.title("Comparing the offensive and defensive rating of each clubs ",fontsize=80)
    r1 = plt.bar(teams-0.2,data_["off"],width,color="blue",label="offensive")
    r2 = plt.bar(teams+0.2,data_["def"],width,color="red",label="defensive")
    plt.xticks(teams,data_["name"],fontsize=40,rotation=90)
    plt.yticks(fontsize=40)
    plt.bar_label(r1, padding=3,fontsize=40)
    plt.bar_label(r2, padding=3,fontsize=40)
    plt.legend(fontsize=70)
    plt.savefig("group_graph.png")
    plt.show()

groupedgraph()    # calling function
