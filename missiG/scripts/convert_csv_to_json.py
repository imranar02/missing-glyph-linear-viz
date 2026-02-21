import pandas as pd
import json

# Set Input & Output path
csv_path = "data/food-consumption.csv"
output_path = "data/food-consumption.json"

# Load dataset (csv) into a dataframe
df = pd.read_csv(csv_path)

## Dropping columns (when needed)
#if "Person ID" in df.columns:
    #df = df.drop(columns=["Person ID"])

#if "Observations" in df.columns:
    #df = df.drop(columns=["Observations"])

# Set up json file structure


features_data = []              # A list to include information for each feature
features = df.columns.tolist()  # A list that contain columns names in the dataset

## Loop through each feature
for feature in features:
    column = df[feature]                # extract column data
    missing_mask = column.isna()        # set up boolean mask for missing values
    missing_count = missing_mask.sum()  # calculate total number of missing values in the current feature

    # Labelling type for each feature
    if column.dtype == 'object':
        feature_type = "categorical"
    elif pd.api.types.is_numeric_dtype(column):
        # removing any missing values, ensuring only non-missing datas are analyzed and calculate the number of unique values
        unique_vals = column.dropna().unique()
        # if few unique integer-like values, it considers as categorical type
        if len(unique_vals) <= 5 and all(float(x).is_integer() for x in unique_vals):
            feature_type = "categorical"
        else:
            feature_type = "numerical"
    else:
        feature_type = "categorical"

    # Store recorded values for the numerical features or category counts for the categorical features
    if feature_type == "numerical":
        recorded_values = column.dropna().tolist()
        categories = None
    else:
        recorded_values = None
        categories = column.dropna().value_counts().to_dict()


    # Calculate JM with every other feature
    joint_missing = []
    for other in features:
        if other == feature:
            joint_missing.append(0)                             # prevent JM with itself
        else:
            both_missing = df[feature].isna() & df[other].isna()#
            joint_missing.append(int(both_missing.sum()))

    # Store recorded values for other features conditioned on values for this feature are missing
    conditioned_on_missing = {}
    for other in features:
        if other != feature:
            conditioned_vals = df.loc[missing_mask, other].dropna().tolist()
            conditioned_on_missing[other] = conditioned_vals

    # A dictionary to store information for each feature
    feature_info = {
        "name": feature,
        "type": feature_type,
        "missing": int(missing_count),
        "jointMissing": joint_missing,
        "conditionedOnMissing": conditioned_on_missing
    }

    # Add recorded values or categories to the JSON file
    if feature_type == "numerical":
        feature_info["recorded"] = recorded_values
    else:
        feature_info["categories"] = categories

    # Append feature info to the dataset list
    features_data.append(feature_info)

# Save the JSON file to output path
with open(output_path, "w") as f:
    json.dump(features_data, f, indent=2)

print(f"JSON file saved into: {output_path}")
