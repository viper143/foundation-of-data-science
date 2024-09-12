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
summary_data = df1.describe()
print(summary_data)

# correlation_matrix =df1.corr()
# sns.heatmap(correlation_matrix,annot=True)

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

ax3 = plt.subplot(3, 1, 3)
ax3.axis('off')  # Turn off the axis for the table

# Create the table for descriptive statistics
wellbeing_table = ax3.table(cellText=wellbeing_stats.values, colLabels=wellbeing_stats.columns, rowLabels=wellbeing_stats.index, loc='center')

# Adjust the table properties
wellbeing_table.auto_set_font_size(False)
wellbeing_table.set_fontsize(10)
wellbeing_table.scale(1.2, 1.2)

# Set title
ax3.set_title("Descriptive Statistics of Well-Being Indicators", fontsize=14)



# Calculate average screen time for males and females
male_avg = df_male[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()
female_avg = df_female[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].mean()

# Create a bar chart for comparison
labels = male_avg.index
x = np.arange(len(labels))  # positions for the bars
width = 0.4  # width of the bars

plt.figure(figsize=(10, 6))
bar_male=plt.bar(x - width/2, male_avg, width=width, label='Male')  # Shifted to the left
bar_female=plt.bar(x + width/2, female_avg, width=width, label='Female')  # Shifted to the right
add_value_labels(bar_male)
add_value_labels(bar_female)
plt.xlabel('Screen Time Metrics')
plt.ylabel('Average Values')
plt.title('Average Screen Time by Gender')
plt.xticks(x, labels)

#plotting histogram of data set3
columns_to_plot = ['Optm', 'Usef', 'Relx', 'Intp']

# Set up a figure with subplots, 2 rows and 2 columns
plt.figure(figsize=(10, 8))

# Loop through the columns and plot each histogram in a subplot
for i, col in enumerate(columns_to_plot, 1):
    plt.subplot(2, 2, i)  # 2 rows and 2 columns grid
    plt.hist(df3[col], bins=5, edgecolor='black', color='skyblue')
    plt.title(f'Histogram of {col}', fontsize=10)  # Title for each plot
    plt.xlabel('Value', fontsize=8)  # X-axis label
    plt.ylabel('Frequency', fontsize=8)  # Y-axis label

# Adjust the layout to avoid overlap

# Use tight_layout to adjust the spacing automatically

plt.tight_layout()
plt.legend()
plt.show()