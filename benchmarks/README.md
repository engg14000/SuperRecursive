# 📊 Benchmarks

> Evaluate and compare prompt effectiveness across different AI models and techniques.

## Benchmark Categories

### [Prompt Technique Comparison](technique-comparison.md)
Compare CoT, ToT, ReAct, and other techniques across task types.

### [Model Comparison](model-comparison.md)
How the same prompt performs across different AI models.

### [Context Window Optimization](context-window.md)
Measuring impact of context organization strategies.

## How We Benchmark

### Methodology
1. **Fixed test set**: Same inputs for every comparison
2. **Multiple runs**: 3-5 runs per configuration for statistical significance
3. **Blind evaluation**: Outputs evaluated without knowing which variant produced them
4. **Quantitative metrics**: Accuracy, completeness, token efficiency
5. **Reproducible**: All prompts and test sets are published

### Metrics

| Metric | Description | How Measured |
|--------|-------------|:---:|
| Accuracy | Correctness of output | Human eval (1-10) |
| Completeness | All requirements addressed | Checklist (%) |
| Efficiency | Tokens used vs. quality | Quality/tokens |
| Consistency | Same quality across runs | Std deviation |
| Speed | Time to complete | Seconds |

## Contributing Benchmarks

See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to submit benchmark results. Include:
- The exact prompt used
- Model and version
- Test inputs
- Raw outputs
- Your scoring methodology
