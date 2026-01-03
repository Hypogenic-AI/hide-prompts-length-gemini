# Datasets

## 1. Wikitext-103 (Raw)
- **Source**: HuggingFace `wikitext` (config: `wikitext-103-raw-v1`)
- **Description**: A collection of over 100 million tokens extracted from the set of verified Good and Featured articles on Wikipedia. Ideal for testing long context handling.
- **Location**: `datasets/wikitext_103/`
- **Loading**:
  ```python
  from datasets import load_from_disk
  dataset = load_from_disk("datasets/wikitext_103")
  ```

## 2. AdvBench
- **Source**: `llm-attacks` repository (Zou et al.)
- **Description**: A set of 500 harmful behaviors/instructions used to test LLM safety.
- **Location**: `datasets/advbench.csv`
- **Format**: CSV with columns for the instruction.
- **Loading**:
  ```python
  import pandas as pd
  df = pd.read_csv("datasets/advbench.csv")
  harmful_prompts = df['goal'].tolist()
  ```
