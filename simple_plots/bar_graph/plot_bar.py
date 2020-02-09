import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

style = plt.style.use('ggplot')

plt.style.use(style)
data_path = "/home/mash-tensor/universe/dev/github-runme/data-visualization/data/housing_prices/train.csv"
data = pd.read_csv(data_path)

data = data.sort_values(by=['YearBuilt'])

year_built = data['YearBuilt'][200:1000]
sale_price = data['SalePrice'][200:1000]
area = data["LotArea"][200:1000]

plt.plot(year_built, sale_price, label="Sale Price", color='b', linestyle='--', marker='+')
plt.plot(year_built, area, label="Sq foot area", color='r', linestyle='-', marker='o')

plt.xlabel("year built -->")
plt.ylabel("price in USD -->")

plt.legend()

plt.title('House price in USD by built year style of the plot {}'.format(style))
plt.show()
