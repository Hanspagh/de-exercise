import pandas as pd


# All segments maersk operates
# ['segment_index', 'segment_origin_geo', 'segment_destination_geo',
#  'segment_service', 'segment_vessel', 'segment_dep_voyage',
#  'segment_dep_time', 'segment_arr_time', 'segment_transport_mode']
segments = pd.read_parquet("../data/segments.parquet")

# All maersk sites in the world
# ['siteid', 'code', 'status', 'name', 'site_type']
site_ids_to_geo_codes = pd.read_csv("../data/geo_siteid_to_code.csv")

# Mapping table site_code to region
# ['city', 'city_name', 'country_code', 'country', 'cluster_code',
#       'cluster', 'region_code', 'region']
geo_codes = pd.read_csv("../data/geo_sitecode_to_region.csv")
