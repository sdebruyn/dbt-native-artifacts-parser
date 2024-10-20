from pathlib import Path
from dbt.tests.fixtures.project import TestProjInfo
from dbt.tests.util import (
    run_dbt,
)

from dbt_native_artifacts_parser import read_manifest


class TestManifest:
    def test_manifest(self, project: TestProjInfo):
        run_dbt(["ls"])

        manifest_path = Path(project.project_root) / "target" / "manifest.json"
        assert manifest_path.exists()
        assert manifest_path.is_file()

        parsed = read_manifest(manifest_path)
        assert parsed is not None
