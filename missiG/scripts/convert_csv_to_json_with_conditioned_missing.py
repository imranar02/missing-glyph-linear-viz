import pandas as pd
import json

csv_path = "data/test_student.csv"
output_path = "data/test_student.json"

# load csv
df = pd.read_csv(csv_path)

if "Observation" in df.columns:
    df = df.drop(columns=["Observation"])

# prepare JSON output
features_data = []
features = df.columns.tolist()

for feature in features:
    column = df[feature]
    missing_mask = column.isna()
    missing_count = missing_mask.sum()

    # detect feature type
    if column.dtype == 'object' or column.nunique(dropna=True) < 10:
        feature_type = "categorical"
        categories = column.dropna().value_counts().to_dict()
        recorded_values = None
    else:
        feature_type = "numerical"
        categories = None
        recorded_values = column.dropna().tolist()

    # compute joint missingness
    joint_missing = []
    for other in features:
        if other == feature:
            joint_missing.append(0)
        else:
            both_missing = df[feature].isna() & df[other].isna()
            joint_missing.append(int(both_missing.sum()))

    # compute conditioned values: other features when this one is missing
    conditioned_on_missing = {}
    for other in features:
        if other != feature:
            conditioned_vals = df.loc[missing_mask, other].dropna().tolist()
            conditioned_on_missing[other] = conditioned_vals

    # create JSON object
    feature_info = {
        "name": feature,
        "type": feature_type,
        "missing": int(missing_count),
        "jointMissing": joint_missing,
        "conditionedOnMissing": conditioned_on_missing
    }

    if feature_type == "numerical":
        feature_info["recorded"] = recorded_values
    else:
        feature_info["categories"] = categories

    features_data.append(feature_info)

# Save JSON
with open(output_path, "w") as f:
    json.dump(features_data, f, indent=2)

print(f"✅ JSON file saved to: {output_path}")
