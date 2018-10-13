import pandas as pd
downloaded_data = pd.read_csv("/Users/davidchudzicki/Downloads/ofxdownload (2).csv")  # delete the bottom table manually
ticker_to_category = pd.read_csv("ticker_to_category.csv")
by_cat = pd.merge(downloaded_data, ticker_to_category).drop(downloaded_data.columns.difference(["Category", "Total Value"]), 1).groupby("Category").sum()
df = pd.read_csv("/Users/davidchudzicki/vanguard/category_targets.csv").merge(by_cat.reset_index())

total = df['Total Value'].sum()
new_total = total + 36000

df = df.rename(columns={'Total Value': 'CurrentDollars'})


df['TargetDollars'] = df.TargetProportion * new_total

df['PurchaseAmount'] = df.TargetDollars - df.CurrentDollars
