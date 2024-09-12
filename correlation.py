import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, ttest_ind

# Load datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')
df3 = pd.read_csv('dataset3.csv')

# Merge datasets on ID for correlation analysis
df = pd.merge(df1, df2, on='ID')
df = pd.merge(df, df3, on='ID')


# Inferential Analysis 1: Correlation between screen time and well-being
total_screen_time = df[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)
well_being_score = df['Optm']  # Example for optimism, repeat for other indicators
corr, p_value = pearsonr(total_screen_time, well_being_score)
print(f'Correlation: {corr}, P-value: {p_value}')