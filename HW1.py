
import pandas as pd

file_name = "dna_excel_project.xlsx"
df = pd.read_excel(file_name)

print(df.head(5))
