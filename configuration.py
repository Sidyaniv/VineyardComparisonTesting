


get_data_conf = {
                'snippets': ( "OpenLandMap/SOL/SOL_SAND-WFRACTION_USDA-3A1A1A_M/v02",
                            "OpenLandMap/SOL/SOL_CLAY-WFRACTION_USDA-3A1A1A_M/v02",
                            "OpenLandMap/SOL/SOL_ORGANIC-CARBON_USDA-6A1C_M/v02", 
                            "NRCan/CDEM",
                            "OpenLandMap/CLM/CLM_LST_MOD11A2-DAYNIGHT_M/v01"
                            ),
                'scale_factors': (1 * 0.01,
                                 1 * 0.01, 
                                 5 * 0.001, 
                                 1, 
                                 0.02
                                 ),
                'uncorrect': {
                    'param': ("s", 3, (1,2,3), {'e':1}, None),
                    'lat': ('21','21','-1902',None,'24'),
                    'long': ('91.02',None,'0','221232','abcd'),
                },
                'correct': {
                    'param':("sand", "clay", "orgc", "elev", "diurnal"),
                    'lat': (57.70414723434193,
                            62.70414723434193,
                            56.70414723434193,
                            55.70414723434193,
                            50.70414723434193,
                            ),
                    'long': (-120.28125000000001,
                             -115.28125000000001,
                             -108.28125000000001,
                             -100.28125000000001,
                             -90.28125000000001, 
                            )
                    
                }

}