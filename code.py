# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

data = data.rename(columns = {'Total' : 'Total_Medals'})

print(data.head(10))
#Code starts here


# --------------
#Code starts here
data['Better_Event'] = np.where((data['Total_Summer']) == (data['Total_Winter']),'Both',
                        np.where((data['Total_Summer']) > (data['Total_Winter']),'Summer','Winter'))
print(data['Better_Event']) 

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here




top_countries = pd.DataFrame(data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']])
print(top_countries.tail(10))

top_countries = top_countries.drop(top_countries.tail(1).index)
print(top_countries.tail(10))

def top_ten(x,y):
    country_list = []
    top_10 = x.nlargest(10, y)
    country_list = top_10['Country_Name']
    return country_list

top_10_summer =list(top_ten(top_countries, 'Total_Summer'))
print(top_10_summer)
top_10_winter = list(top_ten(top_countries, 'Total_Winter'))
print(top_10_winter)
top_10 = list(top_ten(top_countries, 'Total_Medals'))
print(top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)

winter_df = data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)

top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)

summer_df.plot(x="Country_Name", y="Total_Summer", kind="bar")
plt.show()

winter_df.plot(x="Country_Name", y="Total_Winter", kind="bar")
plt.show()

top_df.plot(x="Country_Name", y="Total_Medals", kind="bar")
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = round((summer_df['Gold_Summer'] / summer_df['Total_Summer']),2)
#print(summer_df)

summer_max_ratio = summer_df['Golden_Ratio'].max()
print(summer_max_ratio)

summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)



winter_df['Golden_Ratio'] = (winter_df['Gold_Winter'] / winter_df['Total_Winter'])
#print(winter_df)

winter_max_ratio = winter_df['Golden_Ratio'].max()
print(winter_max_ratio)

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)


top_df['Golden_Ratio'] = (top_df['Gold_Total'] / top_df['Total_Medals'])
print(top_df)

top_max_ratio = top_df['Golden_Ratio'].max()
print(top_max_ratio)

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)




# --------------
#Code starts here
print(data.tail(5))

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
print(data_1['Total_Points'])

most_points = data_1['Total_Points'].max()
print(most_points)

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
print(best)

best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)
plt.show()


