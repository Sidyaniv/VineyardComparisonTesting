GET_SOIL_PROPERTIES_IMAGE_SCHEME = {
    'type': 'object',
    'properties':{
        'args': {
                type: 'object', 'minimum': 2
                },
    }
}  

GET_ELEVATION_SCHEME = {
    'type': 'object',
    'properties': {
        'altitude':{'type': 'number'}
    },
    'required': ['altitude']    
}
