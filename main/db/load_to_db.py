import json
# from pathlib import Path
from main.models import BranchModel
from mkapi.settings import BASE_DIR
import logging

logger = logging.getLogger(__name__)

path_to_json = BASE_DIR / "main/uploads/Branches.json"

with open(path_to_json, encoding='utf-8-sig') as json_file:
    jsonObject = json.load(json_file)


def insert_row(json_object_row):
    return {'city_ru': json_object_row['city']['ru'],
            'city_kz': json_object_row['city']['kz'],
            'region_ru': json_object_row['region']['ru'],
            'region_kz': json_object_row['region']['kz'],
            'address_ru': json_object_row['address']['ru'],
            'address_kz': json_object_row['address']['kz'],
            'area_ru': json_object_row['area']['ru'],
            'area_kz': json_object_row['area']['kz'],
            'lng': json_object_row['lng'],
            'lat': json_object_row['lat'],
            'newbranch': json_object_row['newbranch'],
            'alias': json_object_row['alias'],
            'londonfix3': json_object_row['londonfix3'],
            'phone': json_object_row['phone'],
            'Whatsapp': json_object_row['Whatsapp'],
            'Vyhodnye': json_object_row['Vyhodnye'],
            'RezhimRabotyLeto': json_object_row['RezhimRabotyLeto'],
            'RezhimRabotyZima': json_object_row['RezhimRabotyZima'],
            'Uslugi': json_object_row['Uslugi'],
            'VIP': json_object_row['VIP'],
            'BranchNumber': json_object_row['BranchNumber']
            }


# check for empty DB
is_exist_rows = BranchModel.objects.exists()

if is_exist_rows:
    try:
        objects_from_table = BranchModel.objects.all()

    except Exception as e:
        logger.warning(f"At create was raise exception: {e}", exc_info=True)

else:
    try:
        insert_objects = []

        for obj in jsonObject['branches']:
            insert_objects.append(insert_row(obj))

        bulk_create_objects = [BranchModel(**vals) for vals in insert_objects]
        BranchModel.objects.bulk_create(bulk_create_objects)
        logger.debug("Branches was created successfully!")

    except Exception as e:
        logger.warning(f"At create was raise exception: {e}", exc_info=True)
