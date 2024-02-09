import pytest
import ee
import requests

from cloud import get_data

from src.schemas.get import GET_SOIL_PROPERTIES_IMAGE_SCHEME, GET_ELEVATION_SCHEME
from configuration import get_data_conf as gdc
from src.baseclasses.responce import GetData, Data

 
 
@pytest.mark.parametrize('param', [(gdc['correct']['param'][0]),
                                  (gdc['correct']['param'][1]), 
                                  (gdc['correct']['param'][2]), 
                                  (gdc['correct']['param'][3]), 
                                  (gdc['correct']['param'][4])
                                 ]
                        )
def test_positive_data_getting (param):
    """
    Позитивные сценарии проверки данных, полученных из функции get_data().
    Проверка на валидацию данных, полученных из функции get_info, 
    с использованием JSON-схемы
    Аргументы:
        param (str):  "sand" | "clay" | "orgc" | "elev" | "diurnal"
    """ 
    
    dataset = get_data(param)
    dataset_class = GetData(dataset)
    dataset_class.assert_isinstance(ee.image.Image)

    dataset_info = dataset.getInfo()
    dataset_info_class = GetData(dataset_info)
    dataset_info_class.validate(GET_SOIL_PROPERTIES_IMAGE_SCHEME)


@pytest.mark.parametrize('param', [(gdc['incorrect']['param'][0]),
                                  (gdc['incorrect']['param'][1]), 
                                  (gdc['incorrect']['param'][2]), 
                                  (gdc['incorrect']['param'][3]), 
                                  (gdc['incorrect']['param'][4])
                                 ]
                        )
def test_negative_data_getting (param):
    """
    Негативные сценарии проверки данных, полученных из функции get_data()
    
    Аргументы:
        param (str):  "sand" | "clay" | "orgc" | "elev"
    """ 
    dataset = get_data(param)
    dataset_class = GetData(dataset)

    with pytest.raises(AssertionError):
        dataset_class.assert_isinstance(ee.image.Image) 


@pytest.mark.parametrize("lat, long", [(gdc['correct']['lat1'][0], gdc['correct']['long1'][0]),
                                       (gdc['correct']['lat1'][1], gdc['correct']['long1'][1]),
                                       (gdc['correct']['lat1'][2], gdc['correct']['long1'][2]),
                                       (gdc['correct']['lat1'][3], gdc['correct']['long1'][3]),
                                       (gdc['correct']['lat1'][4], gdc['correct']['long1'][4]),
                                       (gdc['incorrect']['lat2'][0], gdc['incorrect']['long2'][0]),
                                       (gdc['incorrect']['lat2'][1], gdc['incorrect']['long2'][1]),
                                       (gdc['incorrect']['lat2'][2], gdc['incorrect']['long2'][2]),
                                       (gdc['incorrect']['lat2'][3], gdc['incorrect']['long2'][3]),
                                       (gdc['incorrect']['lat2'][4], gdc['incorrect']['long2'][4])
                                      ])
def test_elevation_request(lat, long):
    """Проверка статус кода запроса и валидации ответа функции get_elevation

    Args:
         Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    
    url_point = f'http://geogratis.gc.ca/services/elevation/cdem/altitude?lat={lat}&lon={long}'
    result = requests.get(url = url_point)
    responce = Data(result)
    responce.assert_status(200).validate(GET_ELEVATION_SCHEME)

