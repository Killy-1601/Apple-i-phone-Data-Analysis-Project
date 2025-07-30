# for the iphone sales analysis task, i have collected a dataset containing data about the sales of iphone in india of flipkart. 


# it will be an ideal dataset to analyze the sales of iphone in india.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
pd.read_csv("apple.csv")
yashdata = pd.read_csv("apple.csv")
print(yashdata.head())
#print (yashdata.head())
#print(yashdata.isnull().sum())
#print(yashdata.describe())


#high rated top 10 iphone
high_rate=yashdata.sort_values(by=["Star Rating"], ascending=False)
high_rate = high_rate.head(10)


#print(high_rate['Product Name'])
iphone=high_rate['Product Name'].value_counts()
label=iphone.index
counts=high_rate["Number Of Ratings"]
figure = px.bar(high_rate, x=label, y=counts,title="Number of ratings of high rated iphonr")
figure.show()


#print(high_rate['Product Name'])
iphone=high_rate['Product Name'].value_counts()
label=iphone.index
counts=high_rate["Number Of Reviews"]
figure = px.bar(high_rate, x=label, y=counts,title="Number of reviews of high rated iphonr")
figure.show()


# Relatiomship between sale price and number of ratings of iphone
figure=px.scatter(data_frame=yashdata, x="Number Of Ratings", y="Sale Price",size="Discount Percentage",trendline="ols",title="Relatiomship between sale price and number of ratings of iphone")
figure.show()


# Relatiomship between Discount Percentage and number of ratings of iphone
figure=px.scatter(data_frame=yashdata, x="Number Of Ratings", y="Discount Percentage",size="Sale Price",trendline="ols",title="Relatiomship between Discount Percentage and number of ratings of iphone")
figure.show()
