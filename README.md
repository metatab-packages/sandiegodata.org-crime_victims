# San Diego Crime Incidents with Victim Descriptions


There are important national conversations going on about criminal justice
reform, aligning resources towards prevention and community support rather than
primarily for policing, and calls to Defund or Abolish the Police. These are
all valuable discussions about the communities in which we want to live. An
important voice in that conversation is the voice of victims of crime. The data
below is a complete data set for victims of violent crime from ARJIS (Automated
Regional Justice Information System) for San Diego County, the nation's fifth
largest County, from 2016 through 2020. The complete data set, a cleaned
version of the data, a data dictionary, the Public Records Act request on which
the data was based and several maps are provided for review. A full
conversation requires diverse voices and will help ensure that resources are
realigned in a way that furthers the dual aims of equity and safety in our
communities. 


The file has multiple rows per incident, one for each suspect or
victim. The primary key ``pk`` links records together into a single crime incident. 

## Processing

The data presented here are a processed version of the file received from San 
Diego County through a Public Records Act request. The processing includes:

* Converting the tract identifier to a formal ACS format tract geoid
* Converting the block identifier to a formal ACS format block geoid
* Adding the position of the centroid of the tracts, in WKT format
* Adding the Census internal point location, for the block, in WGS 84 latitude and longitude. 
* Recording the race field to the Census race / ethinicity scheme. 

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
