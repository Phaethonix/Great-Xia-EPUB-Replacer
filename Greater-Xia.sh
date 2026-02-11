#!/usr/bin/env bash

mkdir -p Novels Original_Novels

rm -rf "$(pwd)/script.log"
exec > >(tee -a "$(pwd)/script.log") 2>&1
set -x

for VAR in *.epub; do
  [ -e "$VAR" ] || continue

  echo "------------------------------------------------"
  echo "Processing: $VAR"
  folder_name=$(basename "${VAR%.epub}")
  rm -rf "Novels/$folder_name"
  rm -rf "$folder_name"
  echo "Unzipping $VAR..."
  mkdir -p "$folder_name"
  unzip -o "$VAR" -d "$folder_name"
  cat <<'EOF' >"$folder_name/zip-novel.sh"
#!/usr/bin/env bash
file=$(basename "$(pwd)")
zip -r "../${file}.epub" *
EOF
  chmod +x "$folder_name/zip-novel.sh"
  mv "$folder_name" "Novels/"
  novel="$(pwd)/Novels/$folder_name"
  echo "Removing Great-Xia.py on $novel"
  python "Great-Xia.py" "$novel"
  echo "Zipping back up..."
  cd "$novel"
  ./zip-novel.sh
  cd - >/dev/null
  mv "$VAR" "Original_Novels/"

  echo "Finished processing $VAR"
done

echo "All done."
