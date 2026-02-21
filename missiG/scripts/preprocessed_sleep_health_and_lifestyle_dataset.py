import pandas as pd
import numpy as np

# Load dataset
csv_path = "data/Sleep_health_and_lifestyle_dataset.csv"
df = pd.read_csv(csv_path)

### Introduce Conditional Missingness for visualization ###
# if 'Stress Level' >= 7.5, introduce missing values for variable 'Sleep Duration' or 'Quality of Sleep' or both
high_stress = df[df['Stress Level'] >= 7.5]
n_stress_missing = int(np.random.uniform(0.15, 0.2) * len(high_stress))
stress_indices = high_stress.sample(n=n_stress_missing, random_state=0).index
choice = np.random.choice(['Sleep Duration', 'Quality of Sleep', 'both'])
if choice == 'Sleep Duration':
    df.loc[stress_indices, 'Sleep Duration'] = np.nan
elif choice == 'Quality of Sleep':
    df.loc[stress_indices, 'Quality of Sleep'] = np.nan
else:  # 'both'
    df.loc[stress_indices, ['Sleep Duration', 'Quality of Sleep']] = np.nan

# if 'Physical Activity Level' < 50, introduce missing values for variable 'Daily Steps'
low_activity = df[df['Physical Activity Level'] < 50]
n_activity_missing = int(np.random.uniform(0.05, 0.15) * len(low_activity))
activity_indices = low_activity.sample(n=n_activity_missing, random_state=1).index
df.loc[activity_indices, 'Daily Steps'] = np.nan

# if 'Sleep Disorder' == 'Insomnia', introduce missing values for variable 'Sleep Duration'
insomnia = df[df['Sleep Disorder'] == 'Insomnia']
n_insomnia_missing = int(np.random.uniform(0.15, 0.2) * len(insomnia))
insomnia_indices = insomnia.sample(n=n_insomnia_missing, random_state=2).index
df.loc[insomnia_indices, 'Sleep Duration'] = np.nan

# if 'Sleep Disorder' == 'Sleep Apnea', introduce missing values for variable 'Quality of Sleep'
apnea = df[df['Sleep Disorder'] == 'Sleep Apnea']
n_apnea_missing = int(np.random.uniform(0.15, 0.2) * len(apnea))
apnea_indices = apnea.sample(n=n_apnea_missing, random_state=3).index
df.loc[apnea_indices, 'Quality of Sleep'] = np.nan

# if 'Occupation' == Nurse or Doctor, introduce missing values for variable 'Sleep Duration' or 'Quality of Sleep' or both
nurse_doctor = df[df['Occupation'].isin(['Nurse', 'Doctor'])]
n_nd_missing = int(np.random.uniform(0.0, 0.12) * len(nurse_doctor))
nd_indices = nurse_doctor.sample(n=n_nd_missing, random_state=4).index
choice = np.random.choice(['sleep_duration', 'quality_sleep', 'both'])
if choice == 'sleep_duration':
    df.loc[nd_indices, 'Sleep Duration'] = np.nan
elif choice == 'quality_sleep':
    df.loc[nd_indices, 'Quality of Sleep'] = np.nan
else:  # 'both'
    df.loc[nd_indices, ['Sleep Duration', 'Quality of Sleep']] = np.nan

# Function to introduce random missingness in other columns
def random_missingness(df, column, min_frac, max_frac, seed):
    np.random.seed(seed)
    frac = np.random.uniform(min_frac, max_frac)
    missing_indices = df.sample(frac=frac, random_state=seed).index
    df.loc[missing_indices, column] = np.nan

# Introduce random missingness to other columns
random_missingness(df, 'Age', 0.05, 0.1, seed=10)
random_missingness(df, 'Physical Activity Level', 0.0, 0.15, seed=11)
random_missingness(df, 'Stress Level', 0.0, 0.15, seed=12)
random_missingness(df, 'BMI Category', 0.0, 0.15, seed=13)
random_missingness(df, 'Blood Pressure', 0.0, 0.15, seed=14)
random_missingness(df, 'Heart Rate', 0.0, 0.15, seed=15)
random_missingness(df, 'Occupation', 0.0, 0.05, seed=16)

# Save the updated dataset
output_path = "data/Sleep_health_and_lifestyle_dataset_with_mnar.csv"
df.to_csv(output_path, index=False)
print(f"Conditional Missingness(CM) introduced successfully and saved into: {output_path}")
