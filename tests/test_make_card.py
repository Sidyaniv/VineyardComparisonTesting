import pytest

from data_analysis import make_card_chart
from tests.test_dataframe import test_correct_output_data
# from src.schemas.get import 
from configuration import get_data_conf as gdc
from src.baseclasses.responce import GetData
from data_analysis import make_profile_comparative_json



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
def test_card_chart(get_data_soil_dict, long, lat):
    """Проверка функции make_card_chart на корректность данных на выходе.
       На выходе должен получаться объект класса pandas.core.frame.DataFrame.
       На вход используются корректные данные

    Args:
        get_data_soil_dict (_type_): _description_
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """

    df = test_correct_output_data(get_data_soil_dict, long, lat)
    dataframe_class = GetData(df)
    type_obj = "<class 'pandas.core.frame.DataFrame'>"
    dataframe_class.asssert_equal(type_obj)
