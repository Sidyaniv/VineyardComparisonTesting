import pytest
import folium

from app import map_creater
from configuration import get_data_conf as gdc


@pytest.mark.parametrize("lat, long", [(gdc['correct']['lat1'][0], gdc['correct']['long1'][0]),
                                       (gdc['correct']['lat1'][1], gdc['correct']['long1'][1]),
                                       (gdc['correct']['lat1'][2], gdc['correct']['long1'][2]),
                                       (gdc['correct']['lat1'][3], gdc['correct']['long1'][3]),
                                       (gdc['correct']['lat1'][4], gdc['correct']['long1'][4]),
                                       (gdc['correct']['lat2'][0], gdc['correct']['long2'][0]),
                                       (gdc['correct']['lat2'][1], gdc['correct']['long2'][1]),
                                       (gdc['correct']['lat2'][2], gdc['correct']['long2'][2]),
                                       (gdc['correct']['lat2'][3], gdc['correct']['long2'][3]),
                                       (gdc['correct']['lat2'][4], gdc['correct']['long2'][4]),
                                       (gdc['correct']['lat2'][5], gdc['correct']['long2'][5]),
                                       (gdc['correct']['lat2'][6], gdc['correct']['long2'][6]),
                                       (gdc['correct']['lat2'][7], gdc['correct']['long2'][7]),
                                       (gdc['correct']['lat2'][8], gdc['correct']['long2'][8])

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

@pytest.mark.parametrize("lat, long", [(gdc['incorrect']['lat1'][0], gdc['incorrect']['long1'][0]),
                                       (gdc['incorrect']['lat1'][1], gdc['incorrect']['long1'][1]),
                                       (gdc['incorrect']['lat1'][2], gdc['incorrect']['long1'][2]),
                                       (gdc['incorrect']['lat1'][3], gdc['incorrect']['long1'][3]),
                                       (gdc['incorrect']['lat1'][4], gdc['incorrect']['long1'][4]),
                                       (gdc['incorrect']['lat2'][0], gdc['incorrect']['long2'][0]),
                                       (gdc['incorrect']['lat2'][1], gdc['incorrect']['long2'][1]),
                                       (gdc['incorrect']['lat2'][2], gdc['incorrect']['long2'][2]),
                                       (gdc['incorrect']['lat2'][3], gdc['incorrect']['long2'][3]),
                                       (gdc['incorrect']['lat2'][4], gdc['incorrect']['long2'][4])
                                      ])
def test_map_create_incorrect(lat, long):
    """Тест проверяющий создание карты с помощью map_creater.
       Задаём некорректные данные

    Args:
        lat (float | int): географическая долгота (если float, то до 6 знаков после запятой)
        long (float | int): географическая широта (если float, то до 6 знаков после запятой)
    """
    

    # if isinstance(float(lat), (int, float)) and isinstance(float(long), (int, float)):
    map_with_data = map_creater([lat,long])
    assert isinstance(map_with_data, folium.folium.Map) 
    # else:
    #     with pytest.raises(ValueError):
    #         map_with_data = map_creater([lat,long])