#!/bin/bash

SRC_DIR="models/glb"
DEST_DIR="models/opt"
ERROR_FILE="scripts/error.txt"

> "$ERROR_FILE"

echo "🔄 Checking GLB files for optimization..."
modified=false

find "$SRC_DIR" -type f -name "*.glb" | while read -r glb_file; do
  relative_folder=$(dirname "${glb_file#$SRC_DIR/}") 
  filename=$(basename -- "$glb_file")
  
  opt_file="$DEST_DIR/$relative_folder/$filename"
  mkdir -p "$DEST_DIR/$relative_folder"
  echo "🛠️ Processing: $filename"
  
  npx gltf-transform resize "$glb_file" "$opt_file" --width 1024 --height 1024 && \
  npx gltf-transform optimize "$opt_file" "$opt_file" --compress draco --texture-compress webp

  if [ $? -ne 0 ]; then
    echo "❌ Failed to optimize: $glb_file"
    echo "$glb_file" >> "$ERROR_FILE"
  else
    modified=true
    echo "✅ Successfully optimized $filename to $opt_file"
  fi
done

if [ "$modified" = true ]; then
  if [ -s "$ERROR_FILE" ]; then
    echo "⚠️ Optimization completed with errors. Check $ERROR_FILE."
  else
    echo "✅ Optimization completed successfully!"
  fi
else
  echo "✨ No new files found in $SRC_DIR to process."
fi