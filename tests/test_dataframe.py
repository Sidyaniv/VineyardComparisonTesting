import pytest
import ee

from data_analysis import queried_df, calculate_soil_mean
from src.schemas.get import GET_SOIL_PROPERTIES_IMAGE_SCHEME

from configuration import get_data_conf as gdc
from src.enums.global_enums import GlobalErrorMessage

def test_correct_output_data():
    
    pass