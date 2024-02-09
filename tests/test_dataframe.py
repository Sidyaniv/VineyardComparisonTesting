import pytest
import ee

from data_analysis import queried_df, calculate_soil_mean
from cloud import local_profile
from src.schemas.get import GET_SOIL_PROPERTIES_IMAGE_SCHEME

from configuration import get_data_conf as gdc
from src.enums.global_enums import GlobalErrorMessage

@pytest.mark.parametrize('long, lat', [
                                        (gdc['correct']['long1'][0], gdc['correct']['lat1'][0]),
                                        (gdc['correct']['long1'][1], gdc['correct']['lat1'][1]),
                                        (gdc['correct']['long1'][2], gdc['correct']['lat1'][2]),
                                        (gdc['correct']['long1'][3], gdc['correct']['lat1'][3]),
                                        (gdc['correct']['long1'][4], gdc['correct']['lat1'][4]),
                                        (gdc['correct']['long2'][4], gdc['correct']['lat2'][4]),
                                        (gdc['correct']['long2'][5], gdc['correct']['lat2'][5]),
                                        (gdc['correct']['long2'][6], gdc['correct']['lat2'][6]),
                                        (gdc['correct']['long2'][7], gdc['correct']['lat2'][7]),
                                        (gdc['correct']['long2'][8], gdc['correct']['lat2'][8]),
                                        (gdc['correct']['long2'][9], gdc['correct']['lat2'][9]),
                                      ])
def test_correct_output_data(get_data_soil_dict, long, lat ):
    """Проверка функции queried_df на корректность данных на выходе 
       и на взаимодействие с функцией local_profile .
       На выходе должен получаться объект класса pandas.core.frame.DataFrame.
       На вход используются корректные данные

    Args:
        get_data_current_soil (fixture): Создаёт список из трёх вызывов функции 
        get_data с разными параметрами: 
        [get_data('clay'), get_data('sand'), get_data('orgc')]

        lat (int | float): географическая широта
        long (int | float):  географическая долгота
    """

    coordinates_tuple = (long, lat)
    local_profiles = []

    for current_soil in get_data_soil_dict:
        current_soil_local_profile = local_profile(current_soil, coordinates_tuple, 1000)
        local_profiles.append(current_soil_local_profile)

    df = queried_df(local_profiles[0], local_profiles[1], local_profiles[2])
    df_str = str(type(df))
    assert df_str == "<class 'pandas.core.frame.DataFrame'>"
    return df


@pytest.mark.parametrize("long, lat", [
                                        (gdc['incorrect']['long1'][0], gdc['incorrect']['lat1'][0]),
                                        (gdc['incorrect']['long1'][1], gdc['incorrect']['lat1'][1]),
                                        (gdc['incorrect']['long1'][2], gdc['incorrect']['lat1'][2]),
                                        (gdc['incorrect']['long1'][3], gdc['incorrect']['lat1'][3]),
                                        (gdc['incorrect']['long1'][4], gdc['incorrect']['lat1'][4]),  
                                        (gdc['incorrect']['long2'][0], gdc['incorrect']['lat2'][0]),
                                        (gdc['incorrect']['long2'][1], gdc['incorrect']['lat2'][1]),
                                        (gdc['incorrect']['long2'][2], gdc['incorrect']['lat2'][2]),
                                        (gdc['incorrect']['long2'][3], gdc['incorrect']['lat2'][3]),
                                        (gdc['incorrect']['long2'][4], gdc['incorrect']['lat2'][4]),
                                      ])
def test_incorrect_output_data(get_data_soil_dict, long, lat):
    """Проверка функции queried_df на корректность исключений при взаимодействии с функцией local_profile.
       В качестве некорректных данных используются числа в формате строки и точки, которые находятся на воде 

    Args:
        get_data_current_soil (fixture): Создаёт список из трёх вызывов функции 
        lat (int | float): географическая широта
        long (int | float):  географическая долгота
    """
    try:
        with pytest.raises(KeyError):
            test_correct_output_data(get_data_soil_dict, long, lat)
    except(ee.ee_exception.EEException):
        with pytest.raises(ee.ee_exception.EEException):
            test_correct_output_data(get_data_soil_dict, long, lat)

@pytest.mark.parametrize('long, lat', [
                                        (gdc['correct']['long1'][0], gdc['correct']['lat1'][0]),
                                        (gdc['correct']['long1'][1], gdc['correct']['lat1'][1]),
                                        (gdc['correct']['long1'][2], gdc['correct']['lat1'][2]),
                                        (gdc['correct']['long1'][3], gdc['correct']['lat1'][3]),
                                        (gdc['correct']['long1'][4], gdc['correct']['lat1'][4]),
                                        (gdc['correct']['long2'][4], gdc['correct']['lat2'][4]),
                                        (gdc['correct']['long2'][5], gdc['correct']['lat2'][5]),
                                        (gdc['correct']['long2'][6], gdc['correct']['lat2'][6]),
                                        (gdc['correct']['long2'][7], gdc['correct']['lat2'][7]),
                                        (gdc['correct']['long2'][8], gdc['correct']['lat2'][8]),
                                        (gdc['correct']['long2'][9], gdc['correct']['lat2'][9]),
                                      ])
def test_calculating_soil_mean(get_data_soil_dict, long, lat):
    """Проверка функции calculate_soil_mean на корректность данных на выходе 
       и на взаимодействие с функцией local_profile .
       На выходе должен получаться объект класса pandas.core.frame.DataFrame.
       На вход используются корректные данные


    Args:
        get_data_soil_dict (_type_): _description_
        long (_type_): _description_
        lat (_type_): _description_
    """
    df = test_correct_output_data(get_data_soil_dict, long, lat)
    calculate_soil_mean(df)
    df_str = str(type(df))
    assert df_str == "<class 'pandas.core.frame.DataFrame'>"
# Несмотря на правильные входные данные, функция calculate_soil_mean обрабатывает их с ошибкой: KeyError
