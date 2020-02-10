"""
Aim of this plot is to visualize number of houses sold in consecutive years
"""

from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

csv_path = "/home/mash-tensor/universe/dev/github-runme/data-visualization/data/housing_prices/train.csv"

plt.style.use('ggplot')

df = pd.read_csv(csv_path)
year_sold = df["YrSold"]

year_counter = Counter(year_sold)
year = year_counter.keys()
sale_count = year_counter.values()

plt.bar(year, sale_count, label="House sold per year")

plt.legend()
plt.xlabel("Year")
plt.ylabel("Num of houses sold")
plt.title("Houses sold per year")
plt.savefig("houses_sold_bar_plot.png")
plt.show()
