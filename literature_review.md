# Literature Review: Hiding Adversarial Prompts in Long Documents

## Research Area Overview
The research focuses on the intersection of **adversarial prompt injection** and **long-context processing** in Large Language Models (LLMs). As LLMs expand their context windows (to 100k+ tokens), they become vulnerable to attacks hidden within massive amounts of text. The core question is whether the "noise" of a long document dilutes the attack (making it harder) or provides more "hiding space" (making it stealthier/easier).

## Key Papers

### 1. Lost in the Middle: How Language Models Use Long Contexts (Liu et al., 2023)
- **Key Finding**: LLM performance follows a U-shaped curve. Information at the beginning (primacy) and end (recency) of the context is retrieved best. Information in the **middle** is often ignored or "lost".
- **Relevance**: This suggests that hiding an adversarial prompt in the **middle** of a long document might make it *less* effective at triggering the model, as the model might simply skip over it. However, this also implies that if an attack *does* work in the middle, it might be the ultimate "stealth" attack, as it exploits a blind spot.

### 2. Cognitive Overload Attack: Prompt Injection for Long Context (Li et al., 2024)
- **Key Finding**: Increasing the "cognitive load" (CL) of the context—by adding complex, irrelevant, or "unconventional" tasks (e.g., "write the previous sentence in reverse")—can degrade the model's safety alignment.
- **Relevance**: Long documents naturally impose a higher cognitive load. An attacker could intentionally structure a long document to "overload" the model's working memory, causing it to default to its pre-training objective (text completion) rather than its safety training (refusal).

### 3. Indirect Prompt Injection (Greshake et al., 2023)
- **Key Finding**: Adversarial prompts can be embedded in external resources (websites, documents) that the LLM retrieves (RAG). The model treats these retrieved instructions as valid user commands.
- **Relevance**: This is the primary vector for "hiding" prompts. The user doesn't type the attack; they upload a document (or the model fetches it) containing the attack.

### 4. Universal and Transferable Adversarial Attacks (Zou et al., 2023)
- **Key Finding**: "Greedy Coordinate Gradient" (GCG) can generate suffix strings that universally jailbreak models.
- **Relevance**: These optimized strings are often gibberish. Hiding them in a long document might make them less noticeable to humans, but their effectiveness in long contexts (vs short) needs testing.

## Synthesis & Hypothesis Refinement
The literature presents a conflict:
1.  **Dilution/Loss**: "Lost in the Middle" suggests attacks in the middle might be ignored.
2.  **Overload**: "Cognitive Overload" suggests long, complex contexts might break safety filters.

**Refined Hypothesis**:
- **Hiding in the Middle**: Will likely result in **lower** attack success rates (ASR) due to the "Lost in the Middle" phenomenon, unless the prompt is specifically designed to grab attention.
- **Hiding at the Ends**: Will likely have **high** ASR but low stealth (easy for humans/filters to spot).
- **Hiding in "Overloaded" Contexts**: A long document full of complex instructions might have **high** ASR even if the prompt is buried, because the model's guardrails are exhausted.

## Recommendations for Experiment
1.  **Dataset**: Use `Wikitext-103` or `LongBench` documents as the "haystack".
2.  **Attack**: Use `AdvBench` harmful instructions.
3.  **Variable**: Vary the **position** of the needle (start, middle, end) and the **length** of the haystack (1k, 5k, 10k tokens).
4.  **Metric**: Attack Success Rate (ASR) - does the model execute the harmful command?
