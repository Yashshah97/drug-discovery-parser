# Usage

```python
import drug_discovery_parser
```

Each module is self-contained; see docstrings for the API:

- `drug_discovery_parser.parser` — The core parsing logic for the file format.
- `drug_discovery_parser.reader` — A validating reader that ensures parsed data is correct.
- `drug_discovery_parser.errors` — Friendly error messages for common parsing errors.
- `drug_discovery_parser.streaming_parser` — A streaming parser for large files, built on top of the core parser.
- `drug_discovery_parser.tests` — Unit tests and integration tests for the file-format parser.
- `drug_discovery_parser.docs` — Documentation generation and metadata management.
