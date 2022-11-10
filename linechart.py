

import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")

# taking the first 20 data from the data set
data_ = data.head(20)
def line_graph():
        
# plotting the graph 
    plt.figure(figsize=(45,20))
    plt.plot(data_["name"],data_["def"],"-p",linewidth=4,color="black",markersize=30,markerfacecolor="red",label="def")  
    plt.plot(data_["name"],data_["off"],"-p",linewidth=4,color="blue",markersize=30,markerfacecolor="green",label="off")
    plt.xlabel("CLUBS",fontsize=50)  # labelling the x axis
    plt.ylabel("Offensive and Defensive",fontsize=50) # labelling the y axis
    plt.xticks(rotation=90,fontsize=40)
    plt.yticks(fontsize=40) 
    plt.title("Line plot",fontsize=80) # giving the title
    plt.legend(fontsize=50) # giving the legend
    plt.savefig("line_plot.png")
    plt.show()

line_graph()    # calling function