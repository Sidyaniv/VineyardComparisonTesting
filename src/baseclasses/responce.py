from jsonschema import validate


class Responce: 
    def __init__(self, responce) -> None:
        self.responce = responce
    
    def validate(self, scheme):
        if isinstance(self.responce, list):
            for region in prof:
             validate(region, scheme)
        else:
            validate(self.responce, scheme)

    
        