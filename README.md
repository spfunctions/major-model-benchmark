# Major Model Benchmark

Open benchmark harness for comparing current major AI models on general work: reasoning, coding, structured output, long-context extraction, tool-use readiness, and lightweight data analysis.

This repository is a reproducibility-first benchmark starter. It publishes the model roster, task format, scoring code, and raw result schema before any leaderboard claims.

## Current Roster

Roster snapshot: `2026-05-05`.

The benchmark roster is in [model_roster.json](model_roster.json). It currently tracks OpenAI, Anthropic, Google, xAI, DeepSeek, Mistral, Cohere, Alibaba Qwen, Moonshot Kimi, MiniMax, Z.AI GLM, and Meta Llama.

Provider model names move quickly. Every run should record:

- exact model ID used by the provider
- whether the ID is a stable snapshot, alias, preview, or partner-hosted ID
- temperature, max output, reasoning mode, tool access, and timestamp
- raw prompt and raw output

See [docs/research-notes.md](docs/research-notes.md) for the source notes behind the initial roster.

## What This Measures

The public seed suite in [tasks/general_seed.jsonl](tasks/general_seed.jsonl) is intentionally small. It validates the harness and scoring path. Larger benchmark suites should be versioned under `tasks/vYYYY-MM-DD/` and should include public seed tasks plus private holdout tasks.

Task families:

- `reasoning`: compact logic and quantitative reasoning
- `coding`: bug diagnosis and patch generation
- `structured-output`: JSON extraction and schema discipline
- `long-context`: retrieval of the exact relevant clause from distractors
- `data-analysis`: table arithmetic and probabilistic scoring
- `calibration`: probability math and uncertainty discipline

## Run

Validate roster/tasks and emit placeholder rows:

```bash
python src/sf_benchmark/runner.py \
  --models model_roster.json \
  --tasks tasks/general_seed.jsonl \
  --out results/dry-run.json
```

Score a JSONL file of model responses:

```bash
python src/sf_benchmark/runner.py \
  --models model_roster.json \
  --tasks tasks/general_seed.jsonl \
  --responses examples/responses.seed.jsonl \
  --out results/scored-seed.json
```

Run tests:

```bash
python -m unittest discover -s tests
```

## Response Format

`--responses` expects JSONL:

```json
{"model":"openai/gpt-5.5","task_id":"data.table.001","output":"0.715"}
```

Results follow [schemas/result.schema.json](schemas/result.schema.json).

## Benchmark Rules

- Use the same prompt and same tool policy across models in the same run.
- Prefer stable snapshot IDs; if using aliases, record the alias resolution date.
- Do not rank models until raw outputs, scoring code, and run metadata are public.
- Report accuracy next to latency, cost, refusal/error rate, and output length.
- Keep public seed tasks separate from private holdout tasks to reduce benchmark overfitting.

The methodology is in [docs/methodology.md](docs/methodology.md).

## Related

The companion domain benchmark is [spfunctions/prediction-market-model-benchmark](https://github.com/spfunctions/prediction-market-model-benchmark).

## License

MIT.
