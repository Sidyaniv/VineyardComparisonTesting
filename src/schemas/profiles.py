PROFILE_JSON_SCHEME = {
    'type': 'object',
    'properties': {
        'region': {'type': 'string'},
        'mean_elevation': {'type': 'number'},
         'mean_temp': {'type': 'number'},
         'mean_soil_content_%': {
                                'type': 'object',
                                'properties': {
                                                'Clay': {'type': 'number'},
                                                'Sand': {'type': 'number'},
                                                'Organic Matter': {'type': 'number'}, 
                                                'Other': {'type': 'number'}
                                              }
                                },
         'avg_diurnal_range': {'type': 'number'},
    }
}