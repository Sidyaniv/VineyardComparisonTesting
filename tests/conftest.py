import pytest
import json

@pytest.fixture
def make_profile_json():
    p = open('profiles.json')
    profiles = json.load(p)
    return profiles