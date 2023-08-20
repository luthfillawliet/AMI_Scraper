import pandas as pd
import openpyxl
filepath = "data//datameter.xlsx"
df = pd.read_excel(io=filepath,sheet_name="summary",)

print(df["jumlahbaris"])
jumlahbaris = df.loc[0,"jumlahbaris"]
for i in range(0,jumlahbaris): #given output of 20 print
    print("a")
