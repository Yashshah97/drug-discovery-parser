"""Demo for Drug Discovery File-Format Parser."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import drug_discovery_parser

print("Drug Discovery File-Format Parser", "v" + drug_discovery_parser.__version__)
print("modules:", [m for m in dir(drug_discovery_parser) if not m.startswith('_')])
