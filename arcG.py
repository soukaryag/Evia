from arcgis.gis import GIS
from IPython.display import display

gis = GIS("https://python.playground.esri.com/portal", "arcgis_python", "amazing_arcgis_123")



wm_item = search_result[1]

from arcgis.mapping import WebMap
web_map_obj = WebMap(wm_item)
