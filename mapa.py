import geopandas as gpd
import folium
import os

output = "/Users/alonsodicandia/UFSM/2026/visualizacion de datos/clase 7/manzanas_r08.gpkg"

print("Cargando manzanas región 08...")
r08 = gpd.read_file(output)

# Convertir a WGS84 si es necesario
r08 = r08.to_crs(epsg=4326)

# Centro del mapa en la región 08
centro = [r08.geometry.centroid.y.mean(), r08.geometry.centroid.x.mean()]

m = folium.Map(location=centro, zoom_start=8, tiles="OpenStreetMap")

folium.GeoJson(
    r08,
    style_function=lambda x: {
        "fillColor": "steelblue",
        "color": "white",
        "weight": 0.3,
        "fillOpacity": 0.5,
    }
).add_to(m)

html_out = "/Users/alonsodicandia/UFSM/2026/visualizacion de datos/clase 7/mapa_r08.html"
m.save(html_out)
print(f"Mapa guardado en: {html_out}")
