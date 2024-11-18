import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Stress_prediction_data.csv')

# List of features to create histograms for
features = [
    'Heart Rate','Body Movements','Respiratory Rate','Eye Movement','Sleeping Hours','Blood Oxygen Level','Snoring Rate','Limb Movement Rate','Stress Level'
]

# Create histograms
plt.figure(figsize=(15, 10))

for i, feature in enumerate(features):
    plt.subplot(3, 3, i + 1)  # 3 rows, 3 columns
    plt.hist(data[feature], bins=20, alpha=0.7, color='blue')
    plt.title(feature)
    plt.xlabel('Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
