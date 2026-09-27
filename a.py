import pandas as pd

df = pd.read_excel("Untitled form (Responses).xlsx")

print("\nYOUR EXCEL COLUMN NAMES:\n")

for i, column in enumerate(df.columns):
    print(i, "->", repr(column))