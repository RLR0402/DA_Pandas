#Rainer Luis 
#CPS*3320*01

# EXAMPLES OF NUMPY AND PANDAS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#import data from a csv file
inventoryReport = pd.DataFrame(pd.read_csv('AllSiteInventoryReport_022823v2.csv'))


# lets now clean up the data 
# delete empty cells 

CleanInventoryReport = inventoryReport.dropna()




# Calculate the Inventory asset value (total cost of inventory assets)

CleanInventoryReport["Inventory Asset"] = CleanInventoryReport["Inventory QTY"] * CleanInventoryReport["Asset Value"]

# Calculate the Physical asset value 

CleanInventoryReport["Physical Asset"] = CleanInventoryReport["Physical QTY"] * CleanInventoryReport["Asset Value"]

#Calculate the variance (qty difference between inventory and physcial)
CleanInventoryReport["Variance QTY"] = CleanInventoryReport["Physical QTY"] - CleanInventoryReport["Inventory QTY"] 

#Calculate the Difference in cost of the physical and invenetory 
CleanInventoryReport["Difference"] = CleanInventoryReport["Physical Asset"] - CleanInventoryReport["Inventory Asset"]

# now lets create a csv file with the new data 
#purchase.to_csv('fruit_purchase2.csv')
CleanInventoryReport.to_csv('AnalyzedInventoryReport.csv')


#lets list the types 

#WIP
TotalWip = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'WIP', 'Difference'].sum()
TotalWip = abs(TotalWip)
#Finish Good
TotalFinishGood = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Finish Good ', 'Difference'].sum()
TotalFinishGood = abs(TotalFinishGood)
#Ingredient
TotalIngredient = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Ingredient ', 'Difference'].sum()
TotalIngredient = abs(TotalIngredient)
#Packaging
TotalPackaging = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Packaging', 'Difference'].sum()
TotalPackaging = abs(TotalPackaging)
#Coating
TotalCoating = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Coating', 'Difference'].sum()
TotalCoating = abs(TotalCoating)
#granola
#TotalGranola = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Granola', 'Difference'].sum()
#TotalGranola = abs(TotalGranola)
#yogurt
TotalYogurt = CleanInventoryReport.loc[CleanInventoryReport['Item Type'] == 'Yogurt', 'Difference'].sum()
TotalYogurt = abs(TotalYogurt)
# create a pie chart with percentage of diff based on type

y = np.array([TotalWip,TotalFinishGood,TotalIngredient,TotalPackaging,TotalCoating,TotalYogurt])
mylabels = ["WIP", "Finish Good", "Ingredient", "Packaging", "Coating"  , "Yogurt"]


plt.pie(y, labels = mylabels,autopct='%1.1f%%' )
plt.show() 

