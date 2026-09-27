import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Untitled form (Responses).xlsx")

# Column 5 = Savings
# Column 11 = Monthly budgeting
savings = df.iloc[:, 5]
budget = df.iloc[:, 11]

data = pd.crosstab(budget, savings)

data.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Budgeting vs Savings")
plt.xlabel("Monthly Budget Planning")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("budgeting_vs_savings.png")
plt.show()