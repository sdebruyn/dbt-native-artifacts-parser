# dbt-native-artifacts-parser

An artifact parser for dbt using dbt-core's built-in classes.

## Why

The other artifact parsers available often had their own custom classes and complex implementations. This will just use the actual classes which dbt Core uses to write and read the artifacts. It's basically a simple wrapper to make those functions more accessible. If you ignore the checks and error handling, the actual code is less than 10 lines.

## Installation

```bash
pip install dbt-native-artifacts-parser
```

## Usage

```python
from dbt_native_artifacts_parser import read_manifest

manifest = read_manifest('path/to/manifest.json')
```

```python
from dbt_native_artifacts_parser import read_results

run_results = read_results('path/to/run_results.json')
```

```python
from dbt_native_artifacts_parser import read_catalog

catalog = read_catalog('path/to/catalog.json')
```

```python
from dbt_native_artifacts_parser import read_sources

sources = read_sources('path/to/sources.json')
``` 

## License

MIT
