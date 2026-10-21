# Drug Discovery File-Format Parser

This is a high-performance file-format parser designed specifically for molecular screening and cheminformatics applications, providing a streaming architecture and robust validation capabilities to ensure data integrity. Built from the ground up in pure Python, it offers a seamless development experience with comprehensive testing and documentation in place. With its focus on correctness and usability, this project aims to streamline your drug discovery workflows.

## What makes it unique

Combines molecular screening and cheminformatics with a streaming parser with a validating reader and friendly error messages — a niche where few ready-made tools exist.

## Features

- **`drug_discovery_parser/parser.py`** — The core parsing logic for the file format.
- **`drug_discovery_parser/reader.py`** — A validating reader that ensures parsed data is correct.
- **`drug_discovery_parser/errors.py`** — Friendly error messages for common parsing errors.
- **`drug_discovery_parser/streaming_parser.py`** — A streaming parser for large files, built on top of the core parser.
- **`drug_discovery_parser/tests.py`** — Unit tests and integration tests for the file-format parser.
- **`drug_discovery_parser/docs.py`** — Documentation generation and metadata management.

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/drug-discovery-parser.git
cd drug-discovery-parser

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
drug-discovery-parser/
├── drug_discovery_parser/
│   ├── parser.py
│   ├── reader.py
│   ├── errors.py
│   ├── streaming_parser.py
│   ├── tests.py
│   ├── docs.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **drug-discovery** · Archetype: **parser** ·
Built autonomously by JARVIS on 2026-10-20. MIT licensed.
