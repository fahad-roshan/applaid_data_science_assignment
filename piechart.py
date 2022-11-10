

import pandas as pd
import matplotlib.pyplot as plt

# reading the csv file data
data = pd.read_csv("D:\\soccer-spi\\spi_global_rankings.csv")
data_ = data.head(20)


#mapping the league to a correspinding number and create a new column
data_["league1"] = data_["league"].map({"Barclays Premier League":0,"Dutch Eredivisie":1,"French Ligue 1":2,"German Bundesliga":3,"Italy Serie A":4,"Spanish Primera Division":5,"Portuguese Liga":6}).astype(float)
print(data_["league1"])
print(data_)

# grouping the data's in column league and taking its count 
d = data_.groupby(["league"])
d = d["rank"].count()

print(d) # print the grouped data of league

def pie_chart(): # creating the function
    
   #plotting the pie chart
   plt.figure()
   plt.pie(d,labels=["Barclays Premier League","Dutch Eredivisie","French Ligue 1","German Bundesliga","Italy Serie A","Spanish Primera Division","Portuguese Liga"],autopct="%1.1f%%")
   plt.title("Top 20 Teams and their corresponding league")
   plt.legend(bbox_to_anchor=(2,1),loc = "upper left",shadow=False,prop={"size":9})
   plt.savefig("pie_chart.png")
   plt.show()
   
pie_chart() # calling function  
