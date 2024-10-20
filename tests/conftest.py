from pathlib import Path
from typing import Any
import pytest

pytest_plugins: list[str] = ["dbt.tests.fixtures.project"]


@pytest.fixture(scope="class")
def dbt_profile_target(project_root: Any) -> dict[str, Any]:
    return {
        "type": "duckdb",
        "path": str(Path(project_root) / "db.duckdb"),
    }


@pytest.fixture(scope="class")
def models() -> dict[str, Any]:
    return {"first.sql": "select 1 as id"}
