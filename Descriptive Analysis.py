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

# Descriptive Analysis 1: Average Screen Time by Gender
gender_avg_screen_time = df.groupby('gender')[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()
gender_avg_screen_time.plot(kind='bar')
plt.title('Average Screen Time by Gender')
plt.show()
