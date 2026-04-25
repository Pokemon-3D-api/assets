import os
import sys
import json
import requests
import time
import re

def download_model(item, api_token):
    url = item['url']
    model_id = str(item['id'])
    category = item['category']
    
    if item.get('custom_name'):
        final_filename = item['custom_name']
    elif item.get('suffix'):
        final_filename = f"{model_id}{item['suffix']}"
    else:
        final_filename = model_id

    paths_to_clean = [
        f"models/glb/{category}/{final_filename}.glb",
        f"models/opt/{category}/{final_filename}.glb"
    ]
    
    for path in paths_to_clean:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"🗑️ Deleted existing file: {path}")
            except Exception as e:
                print(f"⚠️ Could not delete {path}: {e}")

    match = re.search(r"([a-f0-9]{32})", url)
    if not match:
        print(f"❌ Invalid Sketchfab URL: {url}")
        return False
    sketch_id = match.group(1)

    headers = {"Authorization": f"Token {api_token}"}
    api_url = f"https://api.sketchfab.com/v3/models/{sketch_id}/download"
    
    try:
        res = requests.get(api_url, headers=headers).json()
        download_url = res.get('glb', {}).get('url') or res.get('gltf', {}).get('url')
        
        if not download_url:
            print(f"❌ No downloadable GLB/GLTF found for {final_filename}")
            return False

        dest_dir = f"models/glb/{category}"
        os.makedirs(dest_dir, exist_ok=True)
        
        print(f"⬇️ Fetching fresh {final_filename} into {category}...")
        file_data = requests.get(download_url).content
        with open(f"{dest_dir}/{final_filename}.glb", 'wb') as f:
            f.write(file_data)
        return True
    except Exception as e:
        print(f"⚠️ Error downloading {final_filename}: {e}")
        return False

def main():
    api_token = os.getenv("SKETCHFAB_API_TOKEN")
    map_path = 'scripts/model_map.json'

    if not api_token:
        print("❌ SKETCHFAB_API_TOKEN not found in environment.")
        return

    if not os.path.exists(map_path):
        print("❌ model_map.json not found.")
        return

    with open(map_path, 'r') as f:
        try:
            mapping = json.load(f)
        except json.JSONDecodeError:
            print("❌ Invalid JSON in model_map.json")
            return
    
    if not mapping:
        print("Empty queue. Nothing to do.")
        return

    for item in mapping:
        download_model(item, api_token)
        time.sleep(1) 
        
    with open(map_path, 'w') as f:
        json.dump([], f, indent=2)
    print("🧹 Queue processed and model_map.json reset.")

if __name__ == "__main__":
    main()