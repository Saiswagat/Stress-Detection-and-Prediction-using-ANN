import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
data = pd.read_csv('Stress_prediction_data.csv')

# Create a figure for the box plot
plt.figure(figsize=(12, 8))

# Create a box plot comparing selected features with Stress Levels
plt.boxplot([data['Snoring Rate'], data['Respiratory Rate'], data['Limb Movement Rate'], data['Blood Oxygen Level'], data['Stress Level']], 
            patch_artist=True, 
            labels=['Snoring Rate', 'Respiratory Rate', 'Limb Movement Rate', 'Blood Oxygen Level', 'Stress Level'])

# Set different colors for each box
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightsalmon']
for patch, color in zip(plt.boxplot([data['Snoring Rate'], data['Respiratory Rate'], data['Limb Movement Rate'], data['Blood Oxygen Level'], data['Stress Level']], patch_artist=True)['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Comparison of Various Features with Stress Level')
plt.ylabel('Value')
plt.grid(axis='y')  # Add a grid for better visibility
plt.show()
