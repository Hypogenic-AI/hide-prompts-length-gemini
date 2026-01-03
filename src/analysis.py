import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze():
    output_dir = "results"
    df = pd.read_json(os.path.join(output_dir, "experiment_results.json"))
    
    # Filter main experiment
    main_df = df[df['is_baseline'] == False].copy()
    
    # Map classifications to numeric
    # ASR: Compliance
    main_df['is_compliance'] = main_df['classification'].apply(lambda x: 1 if 'COMPLIANCE' in x else 0)
    # Refusal
    main_df['is_refusal'] = main_df['classification'].apply(lambda x: 1 if 'REFUSAL' in x else 0)
    # Ignored
    main_df['is_ignored'] = main_df['classification'].apply(lambda x: 1 if 'BENIGN' in x else 0)
    
    # Group by Length and Position
    grouped = main_df.groupby(['length', 'position']).agg({
        'is_compliance': 'mean',
        'is_refusal': 'mean',
        'is_ignored': 'mean',
        'needle': 'count'
    }).reset_index()
    
    print("Analysis Summary:")
    print(grouped)
    
    # Save summary
    grouped.to_csv(os.path.join(output_dir, "analysis_summary.csv"), index=False)
    
    # Visualization: Refusal Rate vs Length (by Position)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=grouped, x='length', y='is_refusal', hue='position', marker='o', palette='viridis')
    plt.title('Refusal Rate vs Document Length')
    plt.xlabel('Document Length (Tokens)')
    plt.ylabel('Refusal Rate')
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "refusal_rate_lineplot.png"))
    plt.close()
    
    # Visualization: Ignore Rate vs Length
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=grouped, x='length', y='is_ignored', hue='position', marker='o', palette='magma')
    plt.title('Ignore Rate (Attack Missed) vs Document Length')
    plt.xlabel('Document Length (Tokens)')
    plt.ylabel('Ignore Rate')
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "ignore_rate_lineplot.png"))
    plt.close()

    # Visualization: ASR vs Length
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=grouped, x='length', y='is_compliance', hue='position', marker='o', palette='coolwarm')
    plt.title('Attack Success Rate (Compliance) vs Document Length')
    plt.xlabel('Document Length (Tokens)')
    plt.ylabel('ASR')
    plt.ylim(-0.1, 1.1)
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "asr_lineplot.png"))
    plt.close()

    # Heatmap for Refusal Rate
    pivot_refusal = grouped.pivot(index='position', columns='length', values='is_refusal')
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_refusal, annot=True, cmap='Blues', vmin=0, vmax=1)
    plt.title('Refusal Rate Heatmap')
    plt.savefig(os.path.join(output_dir, "refusal_heatmap.png"))
    plt.close()

if __name__ == "__main__":
    analyze()
