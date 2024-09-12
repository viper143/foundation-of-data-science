import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2),
                 ha='center', va='bottom')
# Load your CSV files into DataFrames (replace 'path_to_file' with the actual file paths)
df1 = pd.read_csv('dataset1.csv')  # Dataset 1: ID, gender, minority, deprived
df2 = pd.read_csv('dataset2.csv')  # Dataset 2: ID, C_we, C_wk, G_we, G_wk, S_we, S_wk, T_we, T_wk
df3= pd.read_csv('dataset3.csv')

# Step 1: Combine data sets on 'ID'
combined_df = pd.merge(df1, df2, on='ID')

# Step 2: Create df_male and df_female based on gender
df_male = combined_df[combined_df['gender'] == 0].drop(columns=['ID', 'gender','minority','deprived'])
df_female = combined_df[combined_df['gender'] == 1].drop(columns=['ID', 'gender','minority','deprived'])
df_wellBeingIndicator=df3.drop(columns=['ID'])
# Step 3: Perform descriptive analysis for both male and female dataframes
male_stats = df_male.describe().round(2)
female_stats = df_female.describe().round(2)
wellbeing_stats=df_wellBeingIndicator.describe().round(2)
# Display the combined dataframe and the descriptive analysis
print("Descriptive Analysis for Males (ID column excluded):")
print(male_stats)
print("\nDescriptive Analysis for Females (ID column excluded):")
print(female_stats)
print("\n Descriptive Analysis of Well Being Indicator")
print(wellbeing_stats)
# Visualization

# Calculate average screen time for males and females (excluding ID column)
male_avg = df_male[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()
female_avg = df_female[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()

fig = plt.figure(figsize=(14, 8))

# First subplot: Male descriptive statistics (1, 1, 3)
ax1 = plt.subplot(3, 1, 1)
ax1.axis('off')  # Turn off the axis for the table
male_table = ax1.table(cellText=male_stats.values, colLabels=male_stats.columns, rowLabels=male_stats.index, loc='center')
male_table.auto_set_font_size(False)
male_table.set_fontsize(10)
male_table.scale(1.2, 1.2)
ax1.set_title("Descriptive Statistics for Males", fontsize=14)

# Second subplot: Female descriptive statistics (2, 1, 3)
ax2 = plt.subplot(3, 1, 2)
ax2.axis('off')  # Turn off the axis for the table
female_table = ax2.table(cellText=female_stats.values, colLabels=female_stats.columns, rowLabels=female_stats.index, loc='center')
female_table.auto_set_font_size(False)
female_table.set_fontsize(10)
female_table.scale(1.2, 1.2)
ax2.set_title("Descriptive Statistics for Females", fontsize=14)
#Descriptive Analysis of Well being indicator
topics = ['Optm', 'Relx', 'Conf', 'Intp']

# Create a frequency table for each topic
frequency_table = pd.DataFrame()

for topic in topics:
    frequency_table[topic] = df_wellBeingIndicator[topic].value_counts().sort_index()

# Fill missing values with 0 and ensure values are integers
frequency_table = frequency_table.fillna(0).astype(int)
descriptive_stats = pd.DataFrame({
    'Mean': frequency_table.mean(),
    'Standard Deviation': frequency_table.std(),
    'Min': frequency_table.min(),
    'Max': frequency_table.max(),
    '25th Percentile': frequency_table.quantile(0.25),
    '50th Percentile (Median)': frequency_table.median(),
    '75th Percentile': frequency_table.quantile(0.75)
})
# Plot the frequency table in the third subplot (3,1,3)
ax3 = plt.subplot(3, 1, 3)
ax3.axis('off')  # Turn off the axis for the table

# Create the table for descriptive statistics
wellbeing_table = ax3.table(cellText=descriptive_stats.values.round(2), 
                            colLabels=descriptive_stats.columns, 
                            rowLabels=descriptive_stats.index, 
                            loc='center')

# Adjust the table properties
wellbeing_table.auto_set_font_size(False)
wellbeing_table.set_fontsize(10)
wellbeing_table.scale(1.2, 1.2)

# Set title
ax3.set_title("Descriptive Statistics of Well-Being Indicators", fontsize=14)

# Show the plot
plt.tight_layout()


# Calculate average screen time for males and females
male_avg = df_male[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()
female_avg = df_female[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()

# Create a bar chart for comparison
# labels = male_avg.index
# x = np.arange(len(labels))  # positions for the bars
# width = 0.4  # width of the bars

# plt.figure(figsize=(10, 6))
# bar_male=plt.bar(x - width/2, male_avg, width=width, label='Male')  # Shifted to the left
# bar_female=plt.bar(x + width/2, female_avg, width=width, label='Female')  # Shifted to the right
# add_value_labels(bar_male)
# add_value_labels(bar_female)
# plt.xlabel('Screen Time Metrics')
# plt.ylabel('Average Values')
# plt.title('Average Screen Time by Gender')
# plt.xticks(x, labels)
plt.tight_layout()
plt.legend()
plt.show()
