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
    """Тест проверяющий создание карты с помощью map_creater
       Задаём корректные данные 

    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    map_with_data = map_creater([lat,long])
    map_without_data = map_creater(None)
    assert isinstance(map_with_data, folium.folium.Map) 
    assert isinstance(map_without_data, folium.folium.Map)

@pytest.mark.parametrize("lat, long", [(gdc['incorrect']['lat'][0], gdc['incorrect']['long'][0]),
                                       (gdc['incorrect']['lat'][1], gdc['incorrect']['long'][1]),
                                       (gdc['incorrect']['lat'][2], gdc['incorrect']['long'][2]),
                                       (gdc['incorrect']['lat'][3], gdc['incorrect']['long'][3]),
                                       (gdc['incorrect']['lat'][4], gdc['incorrect']['long'][4]),
                                      ])
def test_map_create_incorrect(lat, long):
    """Тест проверяющий создание карты с помощью map_creater.
       Задаём некорректные данные

    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """

    map_with_data = map_creater([lat,long])
    assert isinstance(map_with_data, folium.folium.Map) 
  