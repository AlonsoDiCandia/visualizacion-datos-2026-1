import geopandas as gpd
import json

r08 = gpd.read_file("/Users/alonsodicandia/UFSM/2026/visualizacion de datos/clase 7/manzanas_r08.gpkg")
r08 = r08.to_crs(epsg=4326)

geojson_str = r08.to_json()

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>Manzanas R08</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <style>
    body {{ margin: 0; padding: 0; }}
    #map {{ height: 100vh; width: 100vw; }}
  </style>
</head>
<body>
  <div id="map"></div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>
    const manzanasData = {geojson_str};

    const map = L.map("map").setView([-37.5, -72.0], 8);

    L.tileLayer("https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{
      attribution: "© OpenStreetMap contributors © CARTO",
      maxZoom: 19,
    }}).addTo(map);

    L.geoJSON(manzanasData, {{
      style: {{
        color: "white",
        weight: 0.3,
        fillColor: "steelblue",
        fillOpacity: 0.5,
      }},
      onEachFeature: function(feature, layer) {{
        const p = feature.properties;
        layer.bindPopup(`
          <b>${{p.COMUNA}}</b><br>
          Personas: ${{p.n_per}}<br>
          Hogares: ${{p.n_hog}}<br>
          Viviendas: ${{p.n_vp}}
        `);
      }}
    }}).addTo(map);
  </script>
</body>
</html>"""

with open("/Users/alonsodicandia/UFSM/2026/visualizacion de datos/clase 7/mapa.html", "w") as f:
    f.write(html)

print("mapa.html generado OK")
