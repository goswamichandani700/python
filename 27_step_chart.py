# Create a step chart showing the prices of gold, silver, and copper over the last 25 years.
import matplotlib.pyplot as plt

# 1. Timeline list: Last 25 years (2001 to 2025)
years = [
    2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025
]

# 2. Performance Index lists (Base 100 in 2001 to show relative growth)
gold_price = [
    100, 114, 131, 148, 162, 221, 255, 318, 363, 448,
    574, 613, 517, 467, 423, 458, 482, 467, 517, 644,
    656, 654, 715, 843, 915
]

silver_price = [
    100, 106, 111, 151, 167, 261, 304, 339, 332, 463,
    810, 711, 531, 433, 360, 393, 387, 360, 375, 477,
    581, 510, 545, 680, 725
]

copper_price = [
    100, 103, 115, 178, 224, 404, 431, 414, 321, 451,
    512, 473, 442, 403, 311, 290, 372, 364, 342, 361,
    542, 511, 494, 532, 560
]

years = list(range(2000,2025))

plt.figure(figsize=(18,12))
plt.step(years,gold_price,where='mid',color='yellow')
plt.step(years,silver_price,where='mid',color='grey')
plt.step(years,copper_price,where='mid',color='green')
plt.xlabel('year')
plt.xticks(ticks=years)
plt.ylabel('Petrol Price')
plt.show()