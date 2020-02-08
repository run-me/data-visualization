import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_path = "/home/mash-tensor/universe/dev/github-runme/data-visualization/data/housing_prices/train.csv"
data = pd.read_csv(data_path)

data = data.sort_values(by=['YearBuilt'])

year_built = data['YearBuilt'][200:]
quality = data['SalePrice'][200:]

plt.plot(year_built, quality)
plt.show()
