import pytest
import json

from cloud import get_data
from configuration import get_data_conf as gdc

@pytest.fixture
def make_profile_json():
    p = open('profiles.json')
    profiles = json.load(p)
    return profiles

@pytest.fixture
def get_data_soil_dict():
    clay = get_data(gdc['correct']['param'][1])
    sand = get_data(gdc['correct']['param'][0])
    orgc = get_data(gdc['correct']['param'][2])
    soil_list = [clay, sand, orgc]
    return soil_list

