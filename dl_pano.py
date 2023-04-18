import os
import time
import json
from streetlevel import streetview
import mpmath as mp  # ignore

# Set the bounding box
bb = {
    'lat_max': 47.56766766393,
    'lat_min': 47.54585741600579,
    'lon_max': 7.609428116347839,
    'lon_min': 7.57658226490531
}

# Set json info file name
dataset = 'basel'
json_name = 'dataset_info.json'


def get_tiles(north, south, east, west):
    # Generate a grid of points within the bounding box
    step_size = 0.001
    points = []
    for lat in range(int((north - south) / step_size)):
        lat = south + lat * step_size
        for lon in range(int((east - west) / step_size)):
            lon = west + lon * step_size
            points.append((lat, lon))
    # Get map tiles from the point grid
    zoom = 17
    tiles = []
    for point in points:
        lat_rad = mp.radians(point[0])
        n = 2 ** zoom

        xtile = n * ((point[1] + 180) / 360)
        ytile = n * \
            (1 - (mp.log(mp.tan(lat_rad) + mp.sec(lat_rad)) / mp.pi)) / 2
        tile = ('%d' % (xtile), '%d' % (ytile))
        if tile not in tiles:
            tiles.append(tile)
    return tiles, points


# get a list of panoramas from tiles
response = get_tiles(bb['lat_max'], bb['lat_min'],
                     bb['lon_max'], bb['lon_min'])
print(f'Points found: {len(response[1])}')
panoramas = []

for tile in response[0]:
    panoramas_tile = streetview.get_coverage_tile(tile[0], tile[1], None)
    if panoramas is not []:
        panoramasN = panoramas_tile
        for panoN in panoramasN:
            if panoN not in panoramas:
                panoramas.append(panoN)
    else:
        panoramas.append(panoramas_tile)
print(len(panoramas))

# # get a list of panoramas from point grid
# for point in response[1]:
#     panoramas_point = streetview.get_coverage_tile_by_latlon(
#         point[0], point[1])
#     if panoramas is not []:
#         panoramasN = panoramas_point
#         for panoN in panoramasN:
#             if panoN not in panoramas:
#                 panoramas.append(panoN)
#     else:
#         panoramas.append(panoramas_point)
#     os.system('clear')
#     print(len(panoramas))
#     print(point)

# Open existing json info file / create new list
if (os.path.exists(f'{dataset}/{json_name}')):
    with open(f'{dataset}/{json_name}', "r") as file:
        pano_json = json.load(file)
elif (os.path.exists(dataset)):
    pano_json = []
else:
    os.mkdir(dataset)
    pano_json = []

# get info for each / download / export json
for pano in panoramas:
    if (os.path.exists(f'{dataset}/{pano.id}.jpg') == False):
        os.system('clear')
        print(f"Done {panoramas.index(pano)} of {len(panoramas)}")
        try:
            pano = streetview.find_panorama(pano.lat, pano.lon)
            print(f"Panorama lat/lon: {pano.lat}/{pano.lon}")
            print(f"Panorama id: {pano.id}")
            print(f"Panorama date: {pano.month}/{pano.year}")
            streetview.download_panorama(pano, f'{dataset}/{pano.id}.jpg')
            info = {
                'id': pano.id,
                'lat': pano.lat,
                'lon': pano.lon,
                'date': f'{pano.month}/{pano.year}',
                'bounding_box': bb
            }
            pano_json.append(info)
        except:
            print("Got an error, saving...")
            jsonString = json.dumps(pano_json)
            with open(f'{dataset}/{json_name}', 'w') as outfile:
                outfile.write(jsonString)
            print("Waiting 20 seconds...")
            time.sleep(20)

jsonString = json.dumps(pano_json)
with open(f'{dataset}/{json_name}', 'w') as outfile:
    outfile.write(jsonString)
