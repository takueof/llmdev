# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLM アプリケーション開発コースの学習用リポジトリ。

番号つきディレクトリで各トピックが整理されている。

## Development Setup

### パッケージマネージャー

このプロジェクトは `uv` を使用している。

`uv` の設定ファイルは @pyproject.toml である。

初回セットアップ：

```bash
uv sync
uv run -m ipykernel install --sys-prefix --name python3
```

新規シェルセッションにおける初期化：

```bash
. .venv/bin/activate
```

### Python バージョン

Python 3.12.x 以上 3.13.0 未満を必須とする。

Python 3.13.0 以降は使わないよう @.python-version と @uv.lock でロックしている。

### 環境変数の扱い

@.env で環境変数を管理している。

2つの環境変数にそれぞれ API キーが格納されている：

- `API_KEY`: [OpenAI Platform](https://platform.openai.com/api-keys) 用
- `TAVILY_API_KEY`: [Tavily](https://app.tavily.com/home) 用

## Testing

`pytest` を使用してテストを実行する。

## Type Checking

`ty` と `pyright` と `mypy` を順番に実行して厳格な型チェックを行う。

対象範囲は @pyproject.toml で設定されている。

## Linting

`ruff check --fix` を実行してリンティングを行う。

## Formatting

`ruff format` を実行してコード整形を行う。

## Running Applications

### Testing example

対象：@06_test/authenticator.py

### Flask Todo App

対象：@09_flask/app.py

アプリケーションには http://localhost:5000 からアクセスする。

### LLM App

対象：@16_llmapp/original/app.py

API キーを使う。

## Code Architecture

### 型アノテーション

すべてのコードは `mypy` によるチェックを通らなければならない。

### コードフォーマット

すべてのコードは `ruff format` によるコードフォーマットが実行されていなければならない。
