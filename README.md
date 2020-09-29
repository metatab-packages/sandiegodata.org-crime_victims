# San Diego Crime Incidents with Demographic Descriptions

This dataset describes crime incidents from 2016 to 2020, with demographic
information for both the victims and suspects. The file has multiple rows per 
incident, one for each suspect or victim. The primary key ``pk`` links records 
together into a single crime incident. The dataset is derived from data acquired for a 
PRA request and is processed to standardize geographic identifiers and racial categories. 

Refer to the [source dataset](https://data.sandiegodata.org/dataset/arjis-org-crime-victims-pra/) 
for the original data and the PRA request used to acquire it. 

## Processing

The data presented here are a processed version of the file received from ARJIS 
through a Public Records Act request. The processing includes:

* Converting the tract identifier to a formal ACS format tract geoid
* Converting the block identifier to a formal ACS format block geoid
* Adding the position of the centroid of the tracts, in WKT format
* Adding the Census internal point location, for the block, in WGS 84 latitude and longitude. 
* Recording the race field to the Census race / ethinicity scheme. 

Additiona processing that was performed on the upstream data, which came directly
from ARJIS, includes: 

* Created "year" field
* Deleted MACRStatus from years 2017-2020
* Combined years into 1 file
* Deleted partial August cases to have complete month
* Deleted 2 ARJIS and 1 DA as AGENCY records
* Deleted incident type (all were crime case), highcharge (all were 1) and  role (all were incident)
* ALLYRS_NOSUSP includes only victims, victim/witnesses and blank (property?) in the person role
* UNIQUECASE includes unique case numbers (no matter how many victims)

### Race recode

The ``race`` field of the original data includes many names of regions,
countries or ethnicities. The ``census_race_eth`` field is a recode of the
``race`` field to use the race/ethnicity scheme used by the Census. The codes
used are:

* nhwhite: Non Hispanic White
* hispanic: Hispanic, of any race
* black: Black or African-American
* asian: Asian
* nhopi: Native Hawaiian or Pacific Islander. 

This file does not include any records that would be classified as the
remaining census race codes, such as American Indian or Alaskan Native. These
are the translations from the values in the ``race`` field to those of the
``census_race`` field:

* OTHER: other
* none: unknown
* WHITE: nhwhite
* HISPANIC: hisp
* BLACK: black
* MIDDLE EASTERN: white
* PACIFIC ISLANDER: nhopi
* CHINESE: asian
* JAPANESE: asian
* OTHER ASIAN: asian
* FILIPINO: asian
* ASIAN INDIAN: asian
* GUAMANIAN: nhopi
* VIETNAMESE: asian
* HAWAIIAN: nhopi
* INDIAN: asian
* CAMBODIAN: asian
* KOREAN: asian
* SAMOAN: nhopi
* LAOTIAN: asian
* EAST AFRICAN: black


For the 2020 census, Filipinos may be classified as Pacific Islanders, rather
than Asian, as they had been in previous years. Because this data was collected 
before this transition, Filipinos are classified as Asians.
