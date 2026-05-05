# Research Notes

Snapshot date: 2026-05-05.

## Model Roster Sources

- OpenAI: API docs recommend `gpt-5.5` as the flagship model for complex reasoning and coding.
- Anthropic: Claude docs list `claude-opus-4-7` as the most capable generally available model, with a 1M context window.
- Google: Google announced Gemini 3.1 Pro for developers in preview via the Gemini API. The roster uses `gemini-3.1-pro-preview` and should be rechecked against the Gemini API model list before a paid run.
- xAI: xAI overview lists Grok 4.3 as the current Grok model.
- DeepSeek: DeepSeek V4 Preview docs list `deepseek-v4-pro` and `deepseek-v4-flash`, with API availability and 1M context.
- Mistral: Mistral Medium 3.5 docs list `mistral-medium-3.5` as a frontier-class multimodal model for agentic and coding use cases.
- Cohere: Cohere docs list `command-a-reasoning-08-2025`, 256k context, and 32k max output.
- Alibaba Qwen: Alibaba Cloud Model Studio docs list `qwen3.6-plus`, 1M context, function calling, built-in tools, and structured output.
- Moonshot Kimi: Kimi model docs list `kimi-k2.6` as the latest multimodal model with 256k context.
- MiniMax: MiniMax API docs list `MiniMax-M2.7` and `MiniMax-M2.7-highspeed`.
- Z.AI GLM: Amazon Bedrock model card lists `zai.glm-5`, active lifecycle, and 200k context.
- Meta: Meta Llama 4 Maverick model card lists `meta-llama/Llama-4-Maverick-17B-128E-Instruct`, 1M context, and open weights under the Llama 4 license.

## Benchmark Design Sources

- OpenAI evaluation guidance emphasizes task-specific evals, logging, automated scoring where possible, and human calibration for harder rubrics: https://platform.openai.com/docs/guides/evaluation-best-practices
- Anthropic evaluation guidance recommends task-specific test cases, automated grading where possible, and clear rubrics for judge-model grading: https://docs.anthropic.com/en/docs/build-with-claude/develop-tests
- Stanford HELM emphasizes broad scenario coverage, multi-metric reporting, standardization, and prompt/output transparency: https://crfm.stanford.edu/2022/11/17/helm.html
- ForecastBench is relevant for future forecasting work because it uses dynamic, contamination-resistant forecasting questions and Brier-style scoring: https://www.forecastbench.org/about/

## Open Questions

- Confirm Google's exact API model code for Gemini 3.1 Pro before the first paid run.
- Decide whether to include Perplexity, AI21, Liquid, or other providers in an "extended" roster.
- Add provider adapters only after the prompt, scoring, and result metadata are stable.
