# import pandas as pd
# data = {
#     'Heart Rate':[75,80,90,85,95,70,100,78],
#     'Body Movements':[10,5,15,8,20,3,25,12],
#     'Respiratory Rate':[16,18,20,17,22,15,25,19],
#     'Stress Level':[0,0,1,1,1,0,1,0]
# }
# df = pd.DataFrame(data)
# df.to_csv('Stress_prediction_data.csv',index=False)
# print("CSV file created:stress_prediction_data.csv")

import pandas as pd
import numpy as np

# Defining data for 100 rows
data = {
    'Snoring Rate': np.random.randint(46, 98, 100),  # Random snoring rate between 0-20
    'Respiratory Rate': np.random.randint(15, 30, 100),  # Random respiratory rate between 12-30
    'Body Temperature': np.random.randint(86, 98, 100),  # Random body movements between 0-30
    'Limb Movement Rate': np.random.randint(5, 18, 100),  # Random limb movement rate between 0-15
    'Blood Oxygen Level': np.random.randint(84, 96, 100),  # Random blood oxygen level between 90-100
    'Eye Movement': np.random.uniform(60, 105, 100),  # Random EEG data between 0.5-5.0
    'Sleep Hours': np.random.uniform(0, 9, 100),  # Random sleeping hours between 4-10
    'Heart Rate': np.random.randint(52, 84, 100),  # Random heart rate between 60-110
    'Stress Level': np.random.randint(0, 2, 100)  # Random stress level (0 or 1)
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving to CSV file
df.to_csv('Stress_prediction_data.csv', index=False)

print("CSV file created: Stress_prediction_data.csv")
