import pandas as pd

df = pd.read_csv(r'/Users/ravkan/Desktop/report.csv')
print(df[df["lineItem/ProductCode"] == 'AmazonEC2'].head(10))