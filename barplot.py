import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv('Stress_prediction_data.csv')
sns.set(style="whitegrid")
average_heart_rate=df.groupby('Stress Level')['Heart Rate'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(data=average_heart_rate,x='Stress Level',y='Heart Rate',palette='coolwarm')
plt.title('Avearage Heart Rate by Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Average Heart Rate')
plt.xticks(rotation=0)
plt.show()