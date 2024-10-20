from pathlib import Path
from dbt.tests.fixtures.project import TestProjInfo
from dbt.tests.util import (
    run_dbt,
)

from dbt_native_artifacts_parser import read_sources


class TestSources:
    def test_results(self, project: TestProjInfo):
        run_dbt(["source", "freshness"])

        sources_path = Path(project.project_root) / "target" / "sources.json"
        assert sources_path.exists()
        assert sources_path.is_file()

        parsed = read_sources(sources_path)
        assert parsed is not None
