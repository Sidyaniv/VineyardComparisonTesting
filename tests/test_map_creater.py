import pytest
import folium

from app import map_creater
from configuration import get_data_conf as gdc


@pytest.mark.parametrize("lat, long", [(gdc['correct']['lat'][0], gdc['correct']['long'][0]),
                                       (gdc['correct']['lat'][1], gdc['correct']['long'][1]),
                                       (gdc['correct']['lat'][2], gdc['correct']['long'][2]),
                                       (gdc['correct']['lat'][3], gdc['correct']['long'][3]),
                                       (gdc['correct']['lat'][4], gdc['correct']['long'][4]),
                                      ])
def test_map_create(lat, long):
    """
    Тесты связанные с функцией map_create.
    Задаём корректные данные 
    
    """

    map_with_data = map_creater([lat,long])
    map_without_data = map_creater(None)
    assert isinstance(map_with_data, folium.folium.Map) 
    assert isinstance(map_without_data, folium.folium.Map)

@pytest.mark.parametrize("lat, long", [(gdc['uncorrect']['lat'][0], gdc['uncorrect']['long'][0]),
                                       (gdc['uncorrect']['lat'][1], gdc['uncorrect']['long'][1]),
                                       (gdc['uncorrect']['lat'][2], gdc['uncorrect']['long'][2]),
                                       (gdc['uncorrect']['lat'][3], gdc['uncorrect']['long'][3]),
                                       (gdc['uncorrect']['lat'][4], gdc['uncorrect']['long'][4]),
                                      ])
def test_map_create_uncorrect(lat, long):
    """
    Тесты связанные с функцией map_create.
    Задаём некорректные данные
    """

    map_with_data = map_creater([lat,long])
    assert isinstance(map_with_data, folium.folium.Map) 
