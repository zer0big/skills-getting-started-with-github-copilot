import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture()
def client():
    original_activities = copy.deepcopy(activities)

    try:
        yield TestClient(app)
    finally:
        activities.clear()
        activities.update(copy.deepcopy(original_activities))