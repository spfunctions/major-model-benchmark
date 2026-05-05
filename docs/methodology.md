# Methodology

This benchmark follows four rules:

1. Evaluate the model, not a hidden product stack. Record prompts, model IDs, parameters, tool policy, and raw outputs.
2. Prefer automated scoring where the expected behavior is precise. Use human or judge-model review only for tasks with explicit rubrics.
3. Report more than accuracy. Include cost, latency, refusal/error rate, output length, and scoring coverage.
4. Treat the public seed suite as harness validation, not as the final leaderboard.

## Suite Design

Use three task layers:

- `seed`: public, small, stable tasks that prove the harness works.
- `public`: larger public suites for reproducibility and community debugging.
- `holdout`: private or delayed-release tasks for leaderboard claims.

Each task must include a stable ID, category, prompt, expected value, scoring method, and optional metadata.

## Scoring

The current scorer supports exact match, substring, label match, JSON exact match, JSON subset, and numeric range. New scoring methods should be deterministic, tested, and documented before they are used in a leaderboard.

## Reporting

A leaderboard row should include:

- model and provider
- model status: snapshot, alias, preview, or partner-hosted
- suite version and task count
- mean score and confidence interval where applicable
- failure rate and invalid-output rate
- median latency and estimated cost

## Contamination Control

Public tasks are useful for debugging but can be optimized against. Leaderboard claims should use holdout or time-released tasks, and should publish enough aggregate metadata to make the result auditable without leaking answers.
