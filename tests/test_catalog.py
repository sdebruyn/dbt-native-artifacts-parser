from pathlib import Path
from dbt.tests.fixtures.project import TestProjInfo
from dbt.tests.util import (
    run_dbt,
)

from dbt_native_artifacts_parser import read_catalog


class TestCatalog:
    def test_catalog(self, project: TestProjInfo):
        project.run_sql(
            "create schema my_schema; create table my_schema.my_table (id int);"
        )
        run_dbt(["run"])
        catalog = run_dbt(["docs", " generate"])
        assert catalog is not None

        catalog_path = Path(project.project_root) / "target" / "catalog.json"
        assert catalog_path.exists()
        assert catalog_path.is_file()

        parsed = read_catalog(catalog_path)
        assert parsed is not None
