import pytest
import ee
from jsonschema import validate

from cloud import get_data
from src.schemas.get import GET_SOIL_PROPERTIES_IMAGE_SCHEME

from configuration import get_data_conf as gdc
from src.enums.global_enums import GlobalErrorMessage
 
 
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
    assert isinstance(dataset, ee.image.Image), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE 

    dataset_info = dataset.getInfo()
    validate(dataset_info, GET_SOIL_PROPERTIES_IMAGE_SCHEME)


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
    with pytest.raises(AssertionError): 
        assert isinstance(dataset, ee.image.Image), GlobalErrorMessage.GET_DATA_ERROR_MESSAGE 






# Проверка функции get_elevation на валидность, наличие данных 

