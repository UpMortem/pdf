import tabula

input_path = "input.pdf"
output_path = "output.csv"

# extract all tables from the PDF as a list of dataframes
dfs = tabula.read_pdf(input_path, pages='all')

# write each dataframe to a separate CSV file
for i, df in enumerate(dfs):
    df.to_csv(f"{output_path}_{i}.csv", index=False)

