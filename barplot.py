
import pandas as pd
import matplotlib.pyplot as plt

# reading the csv  
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)
print(data.columns)


def cal_barplot(): # creating a function
    
# plotting the bar plot
    plt.figure(figsize=(45,20))
    r = plt.bar(data_["name"],data_["spi"],color=["blue","indigo","green","pink","orange","black","cyan","chocolate","gold","coral","red","darkblue","lightgreen","darkred","wheat","azure","yellow","crimson","thistle","plum"],edgecolor="black",align="center")
    plt.xticks(fontsize=40,rotation=90) # changing the x bar elements properties
    plt.yticks(fontsize=40) # changing the y bar element properties
    plt.bar_label(r,padding=5,fontsize=35) # label each bar with its value
    plt.xlabel("CLUBS",fontsize=50) # labelling the x axis
    plt.ylabel("SPI (SOCCER POWER INDEX)",fontsize=50) # labelling the y axis
    plt.title("SPI RATING OF EACH TEAMS ",fontsize=80) # giving the title
    plt.savefig("barplot.png") # saving the file as png
    plt.show()
    
cal_barplot() # calling function