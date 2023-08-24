import pandas as pd
fruit = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]})
fruit_sales = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]},
                           index=['2017 Sales', '2018 Sales'])
fruit.to_csv("fruit.csv")

