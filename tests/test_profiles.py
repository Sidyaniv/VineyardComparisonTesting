import pytest
import ee
from jsonschema import validate

from src.schemas.profiles import PROFILE_JSON_SCHEME
from src.enums.global_enums import GlobalErrorMessage
from data_analysis import make_profile_comparative_json, get_location_temp, get_location_diurnal_range
from configuration import get_data_conf as gdc

def test_make_profile_json(make_profile_json):
    """Тест на валидность данных, полученных из функции make_profile_comparative_json

    Args:
        make_profile_json (fixture)
    """

    profiles = make_profile_comparative_json(make_profile_json)
    for region in profiles:
        validate(region, PROFILE_JSON_SCHEME)

# def test_comparison():
#     pass
@pytest.mark.parametrize("lat, long", [(gdc['correct']['lat'][0], gdc['correct']['long'][0]),
                                       (gdc['correct']['lat'][1], gdc['correct']['long'][1]),
                                       (gdc['correct']['lat'][2], gdc['correct']['long'][2]),
                                       (gdc['correct']['lat'][3], gdc['correct']['long'][3]),
                                       (gdc['correct']['lat'][4], gdc['correct']['long'][4]),
                                      ])
def test_get_location_correct_data(lat, long):
    """Тест обратботки корректно полученных данных (в зоне покрытия EarthEngine)
    
    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    temp = get_location_temp(lat, long)
    assert isinstance(temp,  int | float ), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE


@pytest.mark.parametrize("lat, long", [(gdc['uncorrect']['lat'][0], gdc['uncorrect']['long'][0]),
                                       (gdc['uncorrect']['lat'][1], gdc['uncorrect']['long'][1]),
                                       (gdc['uncorrect']['lat'][2], gdc['uncorrect']['long'][2]),
                                       (gdc['uncorrect']['lat'][3], gdc['uncorrect']['long'][3]),
                                       (gdc['uncorrect']['lat'][4], gdc['uncorrect']['long'][4]),
                                      ])
def test_get_location_uncorrect_data(lat, long):
    """Тест обратботки некорректно полученных данных (вне зоны покрытия EarthEngine)
    
    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    
    if lat is not None and long is not None:
        with pytest.raises(ee.ee_exception.EEException):
            get_location_temp(lat, long), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
    else:
        with pytest.raises(KeyError):
            get_location_temp(lat, long), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE

