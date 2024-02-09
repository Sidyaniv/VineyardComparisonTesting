import pytest
import ee
from jsonschema import validate

from src.schemas.profiles import PROFILE_JSON_SCHEME
from src.enums.global_enums import GlobalErrorMessage
from data_analysis import make_profile_comparative_json, get_location_temp, get_location_diurnal_range
from cloud import get_data, local_profile
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
@pytest.mark.parametrize("param, lat, long", [
                                              (gdc['correct']['param'][0], gdc['correct']['lat1'][1], gdc['correct']['long1'][1]),
                                              (gdc['correct']['param'][1], gdc['correct']['lat1'][2], gdc['correct']['long1'][2]),
                                              (gdc['correct']['param'][2], gdc['correct']['lat1'][3], gdc['correct']['long1'][3]),
                                              (gdc['correct']['param'][3], gdc['correct']['lat1'][4], gdc['correct']['long1'][4]),
                                              (gdc['correct']['param'][4], gdc['correct']['lat2'][0], gdc['correct']['long2'][0]),
                                              (gdc['correct']['param'][0], gdc['correct']['lat2'][1], gdc['correct']['long2'][1]),
                                              (gdc['correct']['param'][1], gdc['correct']['lat2'][2], gdc['correct']['long2'][2]),
                                              (gdc['correct']['param'][2], gdc['correct']['lat2'][3], gdc['correct']['long2'][3]),
                                              (gdc['correct']['param'][3], gdc['correct']['lat2'][4], gdc['correct']['long2'][4]),
                                              (gdc['correct']['param'][4], gdc['correct']['lat2'][5], gdc['correct']['long2'][5]),
                                              (gdc['correct']['param'][0], gdc['correct']['lat2'][6], gdc['correct']['long2'][6]),
                                              (gdc['correct']['param'][1], gdc['correct']['lat2'][7], gdc['correct']['long2'][7]),
                                              (gdc['correct']['param'][2], gdc['correct']['lat2'][8], gdc['correct']['long2'][8]),
                                              (gdc['correct']['param'][3], gdc['correct']['lat2'][9], gdc['correct']['long2'][9]),
                                              (gdc['correct']['param'][0], gdc['incorrect']['lat2'][1], gdc['incorrect']['long2'][1]),
                                              (gdc['correct']['param'][1], gdc['incorrect']['lat2'][2], gdc['incorrect']['long2'][2]),
                                              (gdc['correct']['param'][2], gdc['incorrect']['lat2'][3], gdc['incorrect']['long2'][3]),
                                              (gdc['correct']['param'][3], gdc['incorrect']['lat2'][4], gdc['incorrect']['long2'][4])
                                             
                                             ])
def test_local_profile(param, lat, long):
    """Тест на работоспособность функции local_profile и её взаимодействие с функцией get_data

    Args:
        param (str): может быть одно из следующих значений:
                        "sand"     - Sand fraction
                        "clay"     - Clay fraction
                        "orgc"     - Organic Carbon fraction
                        "elev"     - DEM Elevation
        lat (int | float): географическая широта
        long (int | float):  географическая долгота
    """

    dataset = get_data(param)
    poi = (long, lat)
    buffer = 1000
    profile = local_profile(dataset=dataset, poi=poi, buffer=buffer)
    if profile == 'No data :(':
        assert True
    else:    
        assert isinstance(profile, dict)


@pytest.mark.parametrize("lat, long", [(gdc['correct']['lat1'][0], gdc['correct']['long1'][0]),
                                       (gdc['correct']['lat1'][1], gdc['correct']['long1'][1]),
                                       (gdc['correct']['lat1'][2], gdc['correct']['long1'][2]),
                                       (gdc['correct']['lat1'][3], gdc['correct']['long1'][3]),
                                       (gdc['correct']['lat1'][4], gdc['correct']['long1'][4]),
                                       (gdc['correct']['lat2'][0], gdc['correct']['long2'][0]),
                                       (gdc['correct']['lat2'][1], gdc['correct']['long2'][1]),
                                       (gdc['correct']['lat2'][2], gdc['correct']['long2'][2]),
                                       (gdc['correct']['lat2'][3], gdc['correct']['long2'][3]),
                                       (gdc['correct']['lat2'][4], gdc['correct']['long2'][4])
                                      ])
def test_get_location_correct_data(lat, long):
    """Тест обратботки данных полученных корректно (в зоне покрытия EarthEngine)
       Тестирование двух функций:  get_location_temp и get_location_diurnal_range

    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    temp = get_location_temp(lat, long)
    assert isinstance(temp,  (int, float) ), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE

    range = get_location_diurnal_range(lat, long)
    try:
        assert isinstance(range,  (int, float) ), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
    except AssertionError:
        assert isinstance(range, str), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE


@pytest.mark.parametrize("lat, long", [(gdc['incorrect']['lat1'][0], gdc['incorrect']['long1'][0]),
                                       (gdc['incorrect']['lat1'][1], gdc['incorrect']['long1'][1]),
                                       (gdc['incorrect']['lat1'][2], gdc['incorrect']['long1'][2]),
                                       (gdc['incorrect']['lat1'][3], gdc['incorrect']['long1'][3]),
                                       (gdc['incorrect']['lat1'][4], gdc['incorrect']['long1'][4])
                                      ])
def test_get_location_incorrect_data(lat, long):
    """Тест обратботки данных полученных некорректно (вне зоны покрытия EarthEngine)
    
    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    
    if lat is not None and long is not None:
        with pytest.raises(ee.ee_exception.EEException):
            get_location_temp(lat, long)
            range = get_location_diurnal_range(lat, long)
            try:
                assert isinstance(range,  (int, float) ), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
            except AssertionError:
                assert isinstance(range, str), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
    else:
        with pytest.raises(KeyError):
            get_location_temp(lat, long)
            range = get_location_diurnal_range(lat, long)
            try:
                assert isinstance(range,  (int, float) ), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
            except AssertionError:
                assert isinstance(range, str), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE
   

