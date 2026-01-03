import pandas as pd
import json

try:
    df = pd.read_json("results/experiment_results.json")
    print("Total records:", len(df))
    print("Baselines:", len(df[df['is_baseline'] == True]))
    print("Main:", len(df[df['is_baseline'] == False]))
    
    main_df = df[df['is_baseline'] == False]
    print("\nCounts by Length:")
    print(main_df['length'].value_counts())
    print("\nCounts by Position:")
    print(main_df['position'].value_counts())
    print("\nUnique Needles:", main_df['needle'].nunique())
except Exception as e:
    print(e)
