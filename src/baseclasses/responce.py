import json

from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessage

class Data: 
    def __init__(self, data) -> None:
        self.data = data
        self.data_json = data.json()
        self.data_status = data.status_code
    
    def validate(self, scheme):
        if isinstance(self.data_json, list):
            for region in self.data_json:
             validate(region, scheme)
        else:
            validate(self.data_json, scheme)

    def assert_isinstance(self, type):        
        assert isinstance(self.data, type), GlobalErrorMessage.INVALID_OUTPUT_FORMAT
        return self
    
    def assert_status(self, status):
        assert  self.data.status_code == status, GlobalErrorMessage.WRONG_STATUS_CODE
        return self

class GetData: 
    def __init__(self, data) -> None:
        self.data = data
    
    def validate(self, scheme):
        if isinstance(self.data, list):
            for region in self.data:
             validate(region, scheme)
        else:
            validate(self.data, scheme)

    def assert_isinstance(self, type):        
        assert isinstance(self.data, type), GlobalErrorMessage.INVALID_OUTPUT_FORMAT
        return self
    
    def asssert_equal(self, dataframe):
        data_str = str(type(self.data))
        assert data_str == dataframe,  GlobalErrorMessage.INVALID_OUTPUT_FORMAT
        return self




