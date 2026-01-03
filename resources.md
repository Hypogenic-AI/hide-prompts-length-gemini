# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "Is it easier or harder to hide adversarial prompts in longer documents?".

## Papers
| Title | Authors | Year | File | Key Insight |
|-------|---------|------|------|-------------|
| Lost in the Middle | Liu et al. | 2023 | `papers/2023_lost_in_the_middle.pdf` | Models ignore info in the middle of long contexts. |
| Cognitive Overload Attack | Li et al. | 2024 | `papers/2024_cognitive_overload_attack.pdf` | Complex long contexts can bypass safety filters. |
| Indirect Prompt Injection | Greshake et al. | 2023 | `papers/2023_indirect_prompt_injection.pdf` | Attacks can be hidden in retrieved docs. |
| Universal Adversarial Attacks | Zou et al. | 2023 | `papers/2023_universal_adversarial_attacks.pdf` | GCG attack generates optimized suffixes. |
| Many-Shot Jailbreaking | Anthropic | 2024 | `papers/2024_many_shot_jailbreaking.pdf` | Many shots (long context) bypass safety. |

## Datasets
| Name | Source | Type | Location | Notes |
|------|--------|------|----------|-------|
| **Wikitext-103** | HuggingFace | Long Text | `datasets/wikitext_103/` | "Haystack" documents (100M+ tokens). |
| **AdvBench** | LLM Attacks Repo | Harmful Prompts | `datasets/advbench.csv` | "Needle" prompts (500 examples). |

## Code Repositories
| Name | Purpose | Location |
|------|---------|----------|
| **llm-attacks** | GCG Implementation | `code/llm-attacks/` |
| **cognitive-overload-1** | Attack Impl | `code/cognitive-overload-1/` |
| **cognitive-overload-2** | Attack Impl | `code/cognitive-overload-2/` |
| **lost-in-the-middle** | Evaluation | `code/lost-in-the-middle/` |

## Notes
- `LongBench` was attempted but failed due to remote code policy; `Wikitext-103` is used as a standard alternative for long documents.
- All code repos are cloned and ready for inspection.
- Datasets are locally saved and gitignored.
