import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Untitled form (Responses).xlsx")

# Column 2 = Living arrangement
# Column 6 = Major spending
living = df.iloc[:, 2]
spending = df.iloc[:, 6]

data = pd.crosstab(living, spending)

data.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Living Arrangement vs Major Spending")
plt.xlabel("Living Arrangement")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("living_vs_spending.png")
plt.show()