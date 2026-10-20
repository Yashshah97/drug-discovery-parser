# Architecture Plan

- `drug_discovery_parser/parser.py` — The core parsing logic for the file format.
- `drug_discovery_parser/reader.py` — A validating reader that ensures parsed data is correct.
- `drug_discovery_parser/errors.py` — Friendly error messages for common parsing errors.
- `drug_discovery_parser/streaming_parser.py` — A streaming parser for large files, built on top of the core parser.
- `drug_discovery_parser/tests.py` — Unit tests and integration tests for the file-format parser.
- `drug_discovery_parser/docs.py` — Documentation generation and metadata management.
