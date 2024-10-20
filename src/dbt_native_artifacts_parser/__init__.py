from pathlib import Path
from dbt.contracts.graph.manifest import Manifest
from dbt.artifacts.schemas.manifest import WritableManifest
from dbt.artifacts.exceptions import IncompatibleSchemaError
from dbt.artifacts.schemas.run import RunResultsArtifact
from dbt.artifacts.schemas.freshness import FreshnessExecutionResultArtifact
from dbt.artifacts.schemas.catalog import CatalogArtifact


def read_manifest(manifest_path: str) -> Manifest:
    manifest_path = Path(manifest_path)

    if not manifest_path.exists():
        raise ValueError(f"Manifest file not found at {manifest_path}")

    if not manifest_path.is_file():
        raise ValueError(f"Manifest path is not a file: {manifest_path}")

    try:
        writable_manifest = WritableManifest.read_and_check_versions(str(manifest_path))
        manifest = Manifest.from_writable_manifest(writable_manifest)
    except IncompatibleSchemaError as exc:
        exc.add_filename(str(manifest_path))
        raise

    return manifest


def read_results(results_path: str) -> RunResultsArtifact:
    results_path = Path(results_path)

    if not results_path.exists():
        raise ValueError(f"Results file not found at {results_path}")

    if not results_path.is_file():
        raise ValueError(f"Results path is not a file: {results_path}")

    try:
        return RunResultsArtifact.read_and_check_versions(str(results_path))
    except IncompatibleSchemaError as exc:
        exc.add_filename(str(results_path))
        raise


def read_sources(sources_path: str) -> FreshnessExecutionResultArtifact:
    sources_path = Path(sources_path)

    if not sources_path.exists():
        raise ValueError(f"Sources file not found at {sources_path}")

    if not sources_path.is_file():
        raise ValueError(f"Sources path is not a file: {sources_path}")

    try:
        return FreshnessExecutionResultArtifact.read_and_check_versions(
            str(sources_path)
        )
    except IncompatibleSchemaError as exc:
        exc.add_filename(str(sources_path))
        raise


def read_catalog(catalog_path: str) -> CatalogArtifact:
    catalog_path = Path(catalog_path)

    if not catalog_path.exists():
        raise ValueError(f"Catalog file not found at {catalog_path}")

    if not catalog_path.is_file():
        raise ValueError(f"Catalog path is not a file: {catalog_path}")

    try:
        return CatalogArtifact.read_and_check_versions(str(catalog_path))
    except IncompatibleSchemaError as exc:
        exc.add_filename(str(catalog_path))
        raise
