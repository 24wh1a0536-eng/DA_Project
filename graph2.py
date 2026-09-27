import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Untitled form (Responses).xlsx")

# Column 10 = Unplanned purchases
# Column 11 = Monthly budgeting
unplanned = df.iloc[:, 10]
budget = df.iloc[:, 11]

data = pd.crosstab(budget, unplanned)

data.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Budgeting vs Unplanned Purchases")
plt.xlabel("Monthly Budget Planning")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("budgeting_vs_unplanned.png")
plt.show()