# Downloaded Papers

1.  **Lost in the Middle: How Language Models Use Long Contexts**
    *   **Filename**: `2023_lost_in_the_middle.pdf`
    *   **Authors**: Liu et al.
    *   **Year**: 2023
    *   **arXiv**: 2307.03172
    *   **Relevance**: fundamental paper showing that LLMs often ignore information in the middle of long contexts. This directly supports the hypothesis that hiding prompts "in the middle" might be effective (or ineffective if the model ignores them entirely, meaning the attack fails to execute).

2.  **Cognitive Overload Attack: Prompt Injection for Long Context**
    *   **Filename**: `2024_cognitive_overload_attack.pdf`
    *   **Authors**: Li et al.
    *   **Year**: 2024
    *   **arXiv**: 2410.11272
    *   **Relevance**: Directly addresses the research topic. Proposes a new attack that exploits long contexts to overload the model's cognitive capacity.

3.  **Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection**
    *   **Filename**: `2023_indirect_prompt_injection.pdf`
    *   **Authors**: Greshake et al.
    *   **Year**: 2023
    *   **arXiv**: 2302.12173
    *   **Relevance**: The seminal paper on indirect prompt injection, where attacks are hidden in external documents (e.g., websites) retrieved by the model.

4.  **Universal and Transferable Adversarial Attacks on Aligned Language Models**
    *   **Filename**: `2023_universal_adversarial_attacks.pdf`
    *   **Authors**: Zou et al.
    *   **Year**: 2023
    *   **arXiv**: 2307.15043
    *   **Relevance**: Introduces the "GCG" (Greedy Coordinate Gradient) attack, a standard baseline for generating adversarial suffixes. We can test if these strings are harder/easier to detect in long contexts.

5.  **Many-Shot Jailbreaking**
    *   **Filename**: `2024_many_shot_jailbreaking.pdf`
    *   **Authors**: Anthropic (Anwar et al.)
    *   **Year**: 2024
    *   **arXiv**: 2404.08138
    *   **Relevance**: Shows that long contexts (many shots) can be used to bypass safety filters. This is a form of "hiding" the malicious intent in a large volume of data (demonstrations).
