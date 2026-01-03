# Project: Hiding Adversarial Prompts in Long Documents

## Overview
This project investigates how document length (up to 32k tokens) and prompt position (Start, Middle, End) affect the success and detection of adversarial prompt injections.

## Key Findings
-   **Middle Position:** The "Lost in the Middle" phenomenon applies to attacks. Prompts hidden in the middle are completely ignored by the model (0% Refusal, 0% Success).
-   **End Position:** As document length increases, the model is *more* likely to detect and refuse the prompt at the end (Refusal increases from 0% at 4k to 67% at 32k).
-   **Mechanism:** Long contexts likely dilute the initial "Summarize" instruction, causing the model to react to the adversarial prompt at the end (Recency Bias).

## Reproduction
1.  **Setup:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```
2.  **Run Experiment:**
    ```bash
    python -m src.experiment_runner
    ```
3.  **Analyze:**
    ```bash
    python src/analysis.py
    ```

## File Structure
-   `src/`: Code for data, experiments, and analysis.
-   `results/`: JSON results and Plots.
-   `datasets/`: Wikitext and AdvBench.
