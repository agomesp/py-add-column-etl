import pandas as pd

input_file = 'input_data.csv'
output_file = 'output_data.csv'

df = pd.read_csv(input_file)

df['Total'] = df['Column1'] + df['Column2']

df.to_csv(output_file, index=False)

print(f"Transformation complete. Transformed data saved to {output_file}")
