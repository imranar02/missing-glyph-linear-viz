import pandas as pd
import numpy as np

# Load dataset
csv_path = "data/Student_Performance.csv"
df = pd.read_csv(csv_path)

### Introduce MNAR missingness for visualization ###

# Sorting by variable 'Performance Index' (lowest performers first)
df_sorted = df.sort_values(by="Performance Index")

# Range for missing fraction (between 25% and 35%)
min_frac = 0.25
max_frac = 0.35

# Generate different random fractions for column 'Hours Studied' & 'Previous Scores'
missing_frac_hours = np.random.uniform(min_frac, max_frac)
missing_frac_prev_scores = np.random.uniform(min_frac, max_frac)

# Determine how many rows to mask for each column (lowest performers only)
n_missing_hours = int(missing_frac_hours * len(df_sorted))
n_missing_prev_scores = int(missing_frac_prev_scores * len(df_sorted))

# Select indices from low performers
low_perf_indices_hours = df_sorted.head(n_missing_hours).index
low_perf_indices_prev_scores = df_sorted.head(n_missing_prev_scores).index

# Introduce missingness to selected indices
df.loc[low_perf_indices_hours, 'Hours Studied'] = np.nan
df.loc[low_perf_indices_prev_scores, 'Previous Scores'] = np.nan

# Function to introduce random missingness in other columns
def random_missingness(df, column, min_frac, max_frac, seed):
    np.random.seed(seed)
    frac = np.random.uniform(min_frac, max_frac)
    missing_indices = df.sample(frac=frac, random_state=seed).index
    df.loc[missing_indices, column] = np.nan
    return df

# Introduce random missingness to other columns
df = random_missingness(df, 'Sleep Hours', 0.10, 0.15, seed=3)
df = random_missingness(df, 'Sample Question Papers Practiced', 0.07, 0.13, seed=4)
df = random_missingness(df, 'Extracurricular Activities', 0.10, 0.15, seed=3)
df = random_missingness(df, 'Performance Index', 0.03, 0.05, seed=4)

# Save the updated dataset
output_path = "data/student_performance_with_mnar.csv"
df.to_csv(output_path, index=False)
print(f"Conditional Missingness(CM) introduced successfully and saved into: {output_path}")
