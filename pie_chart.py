import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Stress_prediction_data.csv')

# Count the number of stressed and not stressed individuals
stress_counts = data['Stress Level'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(stress_counts, labels=['Not Stressed', 'Stressed'], autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
plt.title('Distribution of Stressed and Not Stressed Individuals')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()
