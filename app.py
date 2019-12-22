import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")

def Get_Color_From_Elevation(elevation):
    if elevation >= 3000.00:
        return "red"
    elif elevation >= 1000.00:
        return "orange"
    else:
        return "green"

def Get_Country_Color(pop):
    return "green"

def Add_Markers(feature_group, location_list):
    for item in location_list:
        feature_group.add_child(folium.Marker(location = item, popup="New Marker", icon=folium.Icon(color="blue")))


def Add_Markers_From_File(feature_group, file):
    name = list(file["NAME"])
    lat = list(file["LAT"])
    lon = list(file["LON"])
    elev = list(file["ELEV"])

    for name, lt, ln, el in zip(name, lat, lon, elev):
        ##feature_group.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color=Get_Color_From_Elevation(el))))
        feature_group.add_child(folium.CircleMarker(location=[lt, ln], popup=name,
         fill_color=Get_Color_From_Elevation(el), color="grey", fill_opacity = 0.7, radius=6))


myMap = folium.Map(location=[51.647924, -3.007263], zoom_start=12, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcano Locations in USA")
fgc = folium.FeatureGroup(name="Color Coded Countries based on their Pop")
#fg.add_child(folium.Marker(location=[51.647924, -3.007263], popup="Will's House", icon=folium.Icon(color="green")))

#Add_Markers(fg, [[51.64, -3.007], [51.23, -3.1], [51.5, -3.15]])
Add_Markers_From_File(fgv, volcanoes)

fgc.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()), 
style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

groups = [fgv, fgc]
for item in groups:
    myMap.add_child(item)

myMap.add_child(folium.LayerControl())

myMap.save("83Llanny.html")