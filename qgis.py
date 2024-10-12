uri = "styleUrl=https://geoobserver.de/download/versatiles_styles/colorful.json&type=xyz&url=https://tiles.versatiles.org/tiles/osm/%7Bz%7D/%7Bx%7D/%7By%7D&zmax=14&zmin=0&http-header:referer="

#####################################################################
esri_url = 'https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/{z}/{y}/{x}.pbf'
esri_coloredpencil = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_coloredpencil.json'
esri_nova= 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_nova.json'
esri_contour = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_contour.json'
esri_dark = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_dark.json'
esri_mordern_antique = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_modern_antique.json'
esri_night = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_night.json'
esri_topography = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_topography.json'
# esri_watercolor = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/esri_watercolor.json'
# esri_blueprint = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_blueprint.json'
# esri_dark_grey_base = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_darkgrey_base.json'
# esri_dark_grey_ref = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_darkgrey_ref.json'
# esri_osm_hybrid = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_hybrid_ref.json'
# esri_lightgrey = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_lightgrey_base.json'
# esri_relief = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_relief.json'
# esri_osm_standard = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_standard.json'
# esri_osm_street = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_street.json'

#####################################################################
# maplibre_url='https://demotiles.maplibre.org/tiles-omt/{z}/{x}/{y}.pbf'
# # maplibre_url = 'https://demotiles.maplibre.org/tiles/{z}/{x}/{y}.pbf'
# maplibre_world = 'https://raw.githubusercontent.com/thangqd/vstyles/main/maplibre/world.json'
# maplibre_omt = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/bright.json'
#####################################################################

#####################################################################
versatiles_url='https://tiles.versatiles.org/tiles/osm/{z}/{x}/{y}'
# maplibre_url = 'https://demotiles.maplibre.org/tiles/{z}/{x}/{y}.pbf'
versatiles_world = 'https://raw.githubusercontent.com/thangqd/vstyles/main/maplibre/world.json'
versatiles_omt = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/bright.json'
#####################################################################


uri = f"styleUrl={maplibre_omt}&type=xyz&url={maplibre_url}"

layer = QgsVectorTileLayer(uri,'Maplibre')
layer.loadDefaultStyle()

if layer.isValid():
    # Add the layer to the QGIS project
    QgsProject.instance().addMapLayer(layer)
    print("Layer added successfully!")
else:
    print("Failed to add the layer.")
