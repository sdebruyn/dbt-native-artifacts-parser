from pathlib import Path
from dbt.tests.fixtures.project import TestProjInfo
from dbt.tests.util import (
    run_dbt,
)

from dbt_native_artifacts_parser import read_results


class TestResults:
    def test_results(self, project: TestProjInfo):
        run_dbt(["run"])

        results_path = Path(project.project_root) / "target" / "run_results.json"
        assert results_path.exists()
        assert results_path.is_file()

        parsed = read_results(results_path)
        assert parsed is not None
