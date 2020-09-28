""" Example pylib functions"""

import pandas as pd
import numpy as np
from geoid.acs import Tract, Block, AcsGeoid

race_map = {
    'OTHER': 'other',
    np.nan: 'unknown',
    None: 'unknown',
    'WHITE': 'nhwhite',
    'HISPANIC': 'hisp',
    'BLACK': 'black',
    'MIDDLE EASTERN': 'white',
    'PACIFIC ISLANDER': 'nhopi',
    'CHINESE': 'asian',
    'JAPANESE': 'asian',
    'OTHER ASIAN': 'asian',
    'FILIPINO': 'asian',
    'ASIAN INDIAN': 'asian',
    'GUAMANIAN': 'nhopi',
    'VIETNAMESE': 'asian',
    'HAWAIIAN': 'nhopi',
    'INDIAN': 'asian',
    'CAMBODIAN': 'asian',
    'KOREAN': 'asian',
    'SAMOAN': 'nhopi',
    'LAOTIAN': 'asian',
    'EAST AFRICAN': 'black'
}

def clean_crime(resource, doc, env, *args, **kwargs):
    """ An example row generator function.

    Reference this function in a Metatab file as the value of a Datafile:

            Datafile: python:pylib#row_generator

    The function must yield rows, with the first being headers, and subsequenct rows being data.

    :param resource: The Datafile term being processed
    :param doc: The Metatab document that contains the term being processed
    :param args: Positional arguments passed to the generator
    :param kwargs: Keyword arguments passed to the generator
    :return:


    The env argument is a dict with these environmental keys:

    * CACHE_DIR
    * RESOURCE_NAME
    * RESOLVED_URL
    * WORKING_DIR
    * METATAB_DOC
    * METATAB_WORKING_DIR
    * METATAB_PACKAGE

    It also contains key/value pairs for all of the properties of the resource.

    """
    
    def mk_tract_geoid(v):

        if v is None or v is np.nan:
            return None
        else:
            return str(Tract(6, 73, int(v) ))

    def mk_bg_geoid(r):

        if r.censusTract is None or r.censusTract is np.nan or r.censusBlock is None or r.censusBlock is np.nan:
            return None
        else:
            return str(Block(6, 73, int(r.censusTract), int(r.censusBlock) ))

    df = doc.reference('op_sd_crime_csv').dataframe()
    
    
    df['censusTract'] = df.censusTract.apply(lambda v: v.replace("'",'') if v not in [None, np.nan] else None)
    df['censusBlock'] = df.censusBlock.apply(lambda v: v.replace("'",'') if v not in [None, np.nan] else None)
    
    df['census_race'] = df.Race.replace(race_map)
    df['tract_geoid'] = df.censusTract.apply(mk_tract_geoid)
    df['block_geoid'] = df.apply(mk_bg_geoid, axis=1)

    df['activityDate'] = pd.to_datetime(df['activityDate'])
    df['year'] = df.activityDate.dt.year

    blks = doc.reference('census_blocks').dataframe().rename(columns={'geoid':'block_geoid'})
    blks.head()

    return df.merge(blks, on='block_geoid', how='left')
    

