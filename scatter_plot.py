import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the dataset
df = pd.read_csv('Stress_prediction_data.csv')
sns.set(style="whitegrid")

# Create a scatter plot for Respiratory Rate vs. Heart Rate
plt.figure(figsize=(10, 6))

# Scatter plot with distinct colors for stress levels
scatter = sns.scatterplot(data=df, x='Heart Rate', y='Respiratory Rate', hue='Stress Level', 
                          palette={0: 'blue', 1: 'red'}, s=100, alpha=0.7)

# Customize the plot
plt.title('Heart Rate vs. Respiratory Rate by Stress Level')
plt.xlabel('Heart Rate')
plt.ylabel('Respiratory Rate')

# Create a custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', label='No Stress (0)', 
                       markerfacecolor='blue', markersize=10),
           plt.Line2D([0], [0], marker='o', color='w', label='Stress (1)', 
                       markerfacecolor='red', markersize=10)]
plt.legend(handles=handles, title='Stress Level')

plt.grid(True)

# Show the plot
plt.show()
