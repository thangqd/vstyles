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
esri_blueprint = 'https://raw.githubusercontent.com/thangqd/vstyles/main/esri/osm_blueprint.json'
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
versatiles_colorful = 'https://raw.githubusercontent.com/thangqd/vstyles/main/versatiles/colorful.json'
versatiles_eclipse = 'https://raw.githubusercontent.com/thangqd/vstyles/main/versatiles/eclipse.json'
versatiles_neutrino = 'https://raw.githubusercontent.com/thangqd/vstyles/main/versatiles/neutrino.json'
#####################################################################

#####################################################################
vgrid_url='https://map-api-new.sovereignsolutions.net/sovereign/v20240410/vietnam/{z}/{x}/{y}.pbf'
vgrid_bright = 'https://raw.githubusercontent.com/thangqd/vstyles/main/vstyles/bright/style.json'
#####################################################################

#####################################################################
omt_basic = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/basic.json'
omt_dark = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/dark.json'
omt_fiord = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/fiord.json'
omt_liberty = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/osmliberty.json'
omt_liberty_topo = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/osmlibertytopo.json'
mot_positron = 'https://raw.githubusercontent.com/thangqd/vstyles/main/openmaptiles/positron.json'
# mot_terrain = 'https://raw.githubusercontent.com/thangqd/vstyles/refs/heads/main/openmaptiles/terrain.json'
mot_toner = 'https://raw.githubusercontent.com/thangqd/vstyles/refs/heads/main/openmaptiles/toner.json'
#####################################################################

#####################################################################
ne_shaded_relief = 'https://klokantech.github.io/naturalearthtiles/tiles/natural_earth_2_shaded_relief.raster/{z}/{x}/{y}.png'
ne_blended_relief = 'https://naturalearthtiles.roblabs.com/tiles/natural_earth_cross_blended_hypso_shaded_relief.raster/{z}/{x}/{y}.png'
ne_grey_relief =  'https://map-api-new.sovereignsolutions.net/sovereign/v20240410/ne_grey/{z}/{x}/{y}.png'
dem = 'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'
#####################################################################

uri = f"styleUrl={mot_toner}&type=xyz&url={vgrid_url}"

layer = QgsVectorTileLayer(uri,'Maplibre')
layer.loadDefaultStyle()

if layer.isValid():
    # Add the layer to the QGIS project
    QgsProject.instance().addMapLayer(layer)
    print("Layer added successfully!")
else:
    print("Failed to add the layer.")
