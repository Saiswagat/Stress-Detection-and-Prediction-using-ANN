import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Stress_prediction_data.csv')

# Use the index as a proxy for time
df['Index'] = df.index

# Plotting the line graph for Sleep Hours and Heart Rate
plt.figure(figsize=(12, 6))

# Plot Sleep Hours over index (time)
plt.plot(df['Index'], df['Sleeping Hours'], label='Sleeping Hours', color='blue', marker='o')

# Plot Heart Rate over index (time)
plt.plot(df['Index'], df['Heart Rate'], label='Heart Rate', color='green', marker='x')

# Optional: Plot Stress Levels on the same graph (as a secondary y-axis)
plt.twinx()  # Create a second y-axis
plt.plot(df['Index'], df['Stress Level'], label='Stress Level', color='red', linestyle='--')

# Adding labels, title, and legend
plt.xlabel('Time (Index)')
plt.ylabel('Sleeping Hours and Heart Rate')
plt.title('Trends of Sleeping Hours, Heart Rate, and Stress Level Over Time')
plt.legend(loc='upper left')

# Show the plot
plt.show()
