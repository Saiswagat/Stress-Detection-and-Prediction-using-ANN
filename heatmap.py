import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Stress_prediction_data.csv')

# Select only the relevant columns
columns = ['Heart Rate','Body Movements','Respiratory Rate','EEG Data','Sleeping Hours','Blood Oxygen Level','Snoring Rate','Limb Movement Rate','Stress Level']
data = df[columns]

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Add title
plt.title('Heatmap of Health Parameters Correlation')

# Show the plot
plt.show()
