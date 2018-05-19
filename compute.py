import pandas as pd
df = pd.read_csv("/Users/davidchudzicki/Downloads/ofxdownload (1).csv")  # delete the bottom table manually
ticker_to_category = pd.read_csv("ticker_to_category.csv")
by_cat = pd.merge(df, ticker_to_category).drop(df.columns.difference(["Category", "Total Value"]), 1).groupby("Category").sum()
by_cat['Percent'] = 100*by_cat/by_cat.sum()
with_targets = pd.read_csv("/Users/davidchudzicki/vanguard/category_targets.csv").merge(by_cat.reset_index())
print(with_targets)
