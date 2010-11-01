#Prefixes and their meanings.

PREFIX_LIST = ['M', # M-Route
               'S', # Deluxe
               'X', # Express
               'L', # LSS
               'W'] # AC Volvo

SUFFIX_LIST = ['EXT','EX','ET','XT','EXN','X', # Extension
               'CUT','CU','CT','CUNS', # Cut Service
               'NS','NH', # Night Service
               'FS']

#Prefixes and suffixes that should not be removed from display name
SUFFIX_KEEPERS = ['EXT','EX','EX','ET','XT','EXN','X',
                  'CUT','CU','CT']
PREFIX_KEEPERS = ['M']

#Aliases To Ext And Cut That Should Be Replaced By ' Ext' And ' Cut'
EXT_ALIASES = ['EXT','EX','EX','ET','XT','EXN','X']
CUT_ALIASES = ['CUT','CU','CT']
