
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


# Inferential Analysis 2: T-test for screen time by deprivation level
deprived_group = df[df['deprived'] == 1]['C_we']
non_deprived_group = df[df['deprived'] == 0]['C_we']
t_stat, p_value = ttest_ind(deprived_group, non_deprived_group)
print(f'T-test: T-statistic = {t_stat}, P-value = {p_value}')
