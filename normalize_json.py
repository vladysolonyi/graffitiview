import os
import json

# Config
dataset = 'basel_preprocess'
json_name = 'output_json.json'
minify = False

if (os.path.exists(f'{dataset}/{json_name}')):
    # container for normalized json
    new_pano_json = []

    with open(f'{dataset}/{json_name}', "r") as file:
        pano_json = json.load(file)

    # remove duplicates and remove not existing
    for pano in pano_json:
        id = pano['id']
        # pano['objects'] = []
        # and os.path.exists(f'{dataset}/{id}.jpg'):
        if pano not in new_pano_json:
            new_pano_json.append(pano)
        else:
            print("Duplicate found!")

    # write the file
    if minify:
        ind = None
    else:
        ind = 4
    jsonString = json.dumps(new_pano_json, indent=ind)
    with open(f'{dataset}/normalized_{json_name}', 'w') as outfile:
        outfile.write(jsonString)

    print('Done!')
else:
    print("Path not found!")
