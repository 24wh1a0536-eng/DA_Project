import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATA
# ==========================================

file = "Untitled form (Responses).xlsx"

df = pd.read_excel(file)

print("\n===== DATASET =====")
print(df.head())

print("\nTotal students:", len(df))

print("\n===== COLUMN NAMES =====")

for i, column in enumerate(df.columns):
    print(i, "->", column)


# ==========================================
# FUNCTION TO FIND COLUMN
# ==========================================

def find_column(number):
    """
    Finds a survey question based on Q1, Q2, Q3 etc.
    """

    for column in df.columns:
        if str(column).strip().startswith(f"Q{number}"):
            return column

    return None


# Find all questions automatically

q1 = find_column(1)
q2 = find_column(2)
q3 = find_column(3)
q4 = find_column(4)
q5 = find_column(5)
q6 = find_column(6)
q7 = find_column(7)
q8 = find_column(8)
q9 = find_column(9)
q10 = find_column(10)
q11 = find_column(11)
q12 = find_column(12)


print("\n===== DETECTED QUESTIONS =====")

for number, column in enumerate(
    [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12],
    start=1
):
    print(f"Q{number} -> {column}")


# ==========================================
# BASIC INFORMATION
# ==========================================

print("\n===== BASIC INFORMATION =====")

print("\nYear of Study:")
print(df[q1].value_counts())

print("\nLiving Arrangement:")
print(df[q2].value_counts())

print("\nMain Source of Money:")
print(df[q3].value_counts())


# ==========================================
# MAJOR SPENDING
# ==========================================

print("\n===== MAJOR SPENDING =====")

spending = df[q6]

print(spending.value_counts())

print("\nPercentage:")
print(
    (spending.value_counts(normalize=True) * 100).round(2)
)


# GRAPH

plt.figure(figsize=(8, 5))

spending.value_counts().plot(kind="bar")

plt.title("Major Spending Categories")
plt.xlabel("Category")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("major_spending.png")

plt.show()


# ==========================================
# SAVINGS
# ==========================================

print("\n===== SAVINGS =====")

savings = df[q7]

print(savings.value_counts())

print("\nPercentage:")

print(
    (savings.value_counts(normalize=True) * 100).round(2)
)


plt.figure(figsize=(8, 5))

savings.value_counts().plot(kind="bar")

plt.title("Monthly Savings of Students")
plt.xlabel("Savings Range")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("savings.png")

plt.show()


# ==========================================
# MONTHLY MONEY
# ==========================================

print("\n===== MONTHLY MONEY =====")

money = df[q4]

print(money.value_counts())


plt.figure(figsize=(8, 5))

money.value_counts().plot(kind="bar")

plt.title("Monthly Money Received/Spent")
plt.xlabel("Money Range")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("monthly_money.png")

plt.show()


# ==========================================
# EXPENSE TRACKING
# ==========================================

print("\n===== EXPENSE TRACKING =====")

tracking = df[q9]

print(tracking.value_counts())

print("\nPercentage:")

print(
    (tracking.value_counts(normalize=True) * 100).round(2)
)


plt.figure(figsize=(8, 5))

tracking.value_counts().plot(kind="bar")

plt.title("How Often Students Track Expenses")
plt.xlabel("Frequency")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("expense_tracking.png")

plt.show()


# ==========================================
# UNPLANNED PURCHASES
# ==========================================

print("\n===== UNPLANNED PURCHASES =====")

unplanned = df[q10]

print(unplanned.value_counts())

print("\nPercentage:")

print(
    (unplanned.value_counts(normalize=True) * 100).round(2)
)


# ==========================================
# BUDGETING
# ==========================================

print("\n===== BUDGETING =====")

budget = df[q11]

print(budget.value_counts())

print("\nPercentage:")

print(
    (budget.value_counts(normalize=True) * 100).round(2)
)


# ==========================================
# EXPENSE STUDENTS WANT TO REDUCE
# ==========================================

print("\n===== EXPENSE TO REDUCE =====")

reduce = df[q12]

print(reduce.value_counts())

print("\nPercentage:")

print(
    (reduce.value_counts(normalize=True) * 100).round(2)
)


plt.figure(figsize=(8, 5))

reduce.value_counts().plot(kind="bar")

plt.title("Expenses Students Want to Reduce")
plt.xlabel("Expense")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("reduce_expenses.png")

plt.show()


# ==========================================
# CROSS ANALYSIS 1
# ==========================================

print("\n====================================")
print("LIVING ARRANGEMENT vs SPENDING")
print("====================================")

cross1 = pd.crosstab(
    df[q2],
    df[q6]
)

print(cross1)


# ==========================================
# CROSS ANALYSIS 2
# ==========================================

print("\n====================================")
print("BUDGETING vs UNPLANNED PURCHASES")
print("====================================")

cross2 = pd.crosstab(
    df[q11],
    df[q10]
)

print(cross2)


# ==========================================
# CROSS ANALYSIS 3
# ==========================================

print("\n====================================")
print("BUDGETING vs SAVINGS")
print("====================================")

cross3 = pd.crosstab(
    df[q11],
    df[q7]
)

print(cross3)


# ==========================================
# PATTERNS
# ==========================================

print("\n====================================")
print("PATTERNS")
print("====================================")

most_spending = spending.value_counts().idxmax()

print(
    "Most common spending category:",
    most_spending
)

most_saving = savings.value_counts().idxmax()

print(
    "Most common savings category:",
    most_saving
)

most_budget = budget.value_counts().idxmax()

print(
    "Most common budgeting behavior:",
    most_budget
)

most_tracking = tracking.value_counts().idxmax()

print(
    "Most common expense tracking behavior:",
    most_tracking
)

most_unplanned = unplanned.value_counts().idxmax()

print(
    "Most common unplanned purchase behavior:",
    most_unplanned
)

most_reduce = reduce.value_counts().idxmax()

print(
    "Most common expense students want to reduce:",
    most_reduce
)


# ==========================================
# END
# ==========================================

print("\n====================================")
print("ANALYSIS COMPLETED")
print("====================================")

print("""
The analysis has calculated:

1. Student distribution
2. Major spending categories
3. Savings patterns
4. Monthly money distribution
5. Expense tracking
6. Budgeting behavior
7. Unplanned purchases
8. Expenses students want to reduce
9. Living arrangement vs spending
10. Budgeting vs unplanned purchases
11. Budgeting vs savings

Graphs have also been saved as PNG files.
""")
