from configparser import ConfigParser
parser = ConfigParser()
parser.read("config.ini")

POSTGRES_ADDRESS    =        parser["POSTGRES"]["POSTGRES_ADDRESS"]
POSTGRES_PORT       = int(   parser["POSTGRES"]["POSTGRES_PORT"]     )
POSTGRES_DB         =        parser["POSTGRES"]["POSTGRES_DB"]

TABLE_SUBMISSIONS   =        parser["POSTGRES"]["TABLE_SUBMISSIONS"]
TABLE_INDEXES       =        parser["POSTGRES"]["TABLE_INDEXES"]
TABLE_ASSOCIATIONS  =        parser["POSTGRES"]["TABLE_ASSOCIATIONS"]

TABLE_CLASSES       =        parser["POSTGRES"]["TABLE_CLASSES"]
TABLE_OFFERINGS     =        parser["POSTGRES"]["TABLE_OFFERINGS"]
TABLE_ASSIGNMENTS   =        parser["POSTGRES"]["TABLE_ASSIGNMENTS"]

TABLE_USERS         =        parser["POSTGRES"]["TABLE_USERS"]

#TODO: VERY BAD, CHANGE LATER
POSTGRES_USER       =        parser["POSTGRES"]["POSTGRES_USER"]
POSTGRES_PASS       =        parser["POSTGRES"]["POSTGRES_PASS"]

DATABASE_MANAGER    =        parser["POSTGRES"]["DATABASE_MANAGER"]

BACKEND_ADDRESS     =        parser["BACKEND"]["BACKEND_ADDRESS"]