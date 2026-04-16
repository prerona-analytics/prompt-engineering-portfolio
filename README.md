# prompt-engineering-portfolio
In this portfolio you will find out how I design prompt systems that combine LLM reasoning with real data validation.   My focus is not just generating outputs, but ensuring correctness and reproducibility.
Churn Analysis: LLM-Augmented EDA
- Prompt chaining: context → hypothesis → validation → summary
- LLM used for hypothesis generation
- Python used for statistical validation
- Insight synthesis for business decisions
- Churn Analysis: LLM-Augmented EDA
- Prompt chaining: context → hypothesis → validation → summary
- LLM used for hypothesis generation
- Python used for statistical validation
- Insight synthesis for business decisions
- What I Demonstrate
- Prompt architecture design
- LLM + Data integration
- Analytical thinking with validation
- Structured prompt pipelines (not random prompting)
-  Projects: Churn LLM EDA:
-  Problem
Identify key drivers of customer churn using a hybrid approach: LLM hypothesis generation + statistical validation.

Solution
Dataset → Prompt Context → LLM Hypothesis → Python Validation → Insight Layer

Prompt Chain:
Context Setup (schema + sample rows)
Hypothesis Generation
Validation Request
Insight Synthesis

Example Prompt:
"Given this dataset schema and sample rows, suggest 5 possible churn drivers"

Validation Layer:
Every hypothesis is tested using Pandas:
Groupby analysis
Correlation checks

Limitations:
LLM hallucinated income-churn relationship
Needed statistical validation

- Dataset: Telco churn
- Goal: Identify churn drivers
- Approach: LLM + Pandas validation

LLM output is a first draft — not a final answer.  
Every insight is validated before use.

Future Work:
- Prompt evaluation framework
- Multi-agent prompt systems


Key Insight:
LLMs accelerate thinking, not replace analysis.
