import { constructMapboxStyleFromEsri } from "esri-style-ft-mapbox-style";

// Specify the base URL of your Esri Vector Tile Service
const esriBaseUrl =
  "https://basemaps.arcgis.com/arcgis/rest/services/World_Contours_v2/VectorTileServer";

(async () => {
  try {
    // Convert the Esri style to a Mapbox-compatible style
    const mapboxStyle = await constructMapboxStyleFromEsri(esriBaseUrl);

    // Output the converted style
    console.log(
      "Converted Mapbox Style:",
      JSON.stringify(mapboxStyle, null, 2)
    );
  } catch (error) {
    console.error("Error converting Esri style to Mapbox style:", error);
  }
})();