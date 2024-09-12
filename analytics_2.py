 # Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset for well-being indicators analysis
wellbeing_dataset_path = '/mnt/data/dataset3.csv'

# Load the dataset and inspect the first few rows
wellbeing_dataset = pd.read_csv(wellbeing_dataset_path)

# Extract relevant columns for the well-being analysis (Optm, Relx, Conf)
wellbeing_columns = ['Optm', 'Relx', 'Conf']

# Calculate the frequency distribution for each column
wellbeing_distribution = wellbeing_dataset[wellbeing_columns].apply(pd.Series.value_counts)

# Visualize each well-being indicator as histograms
for column in wellbeing_columns:
    plt.figure(figsize=(6, 4))
    plt.hist(wellbeing_dataset[column], bins=5, edgecolor='black', alpha=0.7)
    plt.title(f'Distribution of {column}')
    plt.xlabel(f'{column} Scores')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
