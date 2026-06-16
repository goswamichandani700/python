#Create a stacked bar chart showing the Indian Government budget allocation across the following categories:

 #Interest Payments
 #States' Share of Taxes & Duties
# Central Sector Schemes
# Defence
 #Centrally Sponsored Schemes
 #Finance Commission & Other Transfers
 #Subsidies
 #Pensions
 #Capital Expenditure
 #Rural Development

import matplotlib.pyplot as plt

budget = ["Budget"]

interest = [20]
states = [22]
central = [16]
defence = [8]
css = [8]
finance = [8]
subsidies = [6]
pensions = [4]
capital = [8]
rural = [9]

# Bottom calculations
states_bottom = interest

central_bottom = [i + s for i, s in zip(interest, states)]

defence_bottom = [i + s + c for i, s, c in zip(interest, states, central)]

css_bottom = [i + s + c + d for i, s, c, d in zip(interest, states, central, defence)]

finance_bottom = [i + s + c + d + cs for i, s, c, d, cs in zip(interest, states, central, defence, css)]

subsidies_bottom = [i + s + c + d + cs + f for i, s, c, d, cs, f in zip(interest, states, central, defence, css, finance)]

pensions_bottom = [i + s + c + d + cs + f + sub for i, s, c, d, cs, f, sub in zip(interest, states, central, defence, css, finance, subsidies)]

capital_bottom = [i + s + c + d + cs + f + sub + p for i, s, c, d, cs, f, sub, p in zip(interest, states, central, defence, css, finance, subsidies, pensions)]

rural_bottom = [i + s + c + d + cs + f + sub + p + cap for i, s, c, d, cs, f, sub, p, cap in zip(interest, states, central, defence, css, finance, subsidies, pensions, capital)]

plt.bar(budget, interest, label='Interest Payments')
plt.bar(budget, states, bottom=states_bottom, label="States' Share of Taxes & Duties")
plt.bar(budget, central, bottom=central_bottom, label='Central Sector Schemes')
plt.bar(budget, defence, bottom=defence_bottom, label='Defence')
plt.bar(budget, css, bottom=css_bottom, label='Centrally Sponsored Schemes')
plt.bar(budget, finance, bottom=finance_bottom, label='Finance Commission & Other Transfers')
plt.bar(budget, subsidies, bottom=subsidies_bottom, label='Subsidies')
plt.bar(budget, pensions, bottom=pensions_bottom, label='Pensions')
plt.bar(budget, capital, bottom=capital_bottom, label='Capital Expenditure')
plt.bar(budget, rural, bottom=rural_bottom, label='Rural Development')

plt.xlabel("Budget")
plt.ylabel("Allocation (%)")
plt.title("Indian Government Budget Allocation")
plt.legend()
plt.tight_layout()
plt.show()