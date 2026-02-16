import os
import re
import sys

# I forced Claude to do this don't mind the comments

def replace_unwanted_content(file_path):
    unwanted_contents = [
        'Great Xia',
        'Huaxia',
        'Dragon Country',
        'Xia Country',
        'Huaguo'
        #up to you
        #'China',
        
    ]

    # Read the file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

    original_content = content
    replaced_count = 0

    # Debug: Print file info
    print(f"  File content length: {len(content)} characters")

    # Replace each unwanted content
    for unwanted in unwanted_contents:
        print(f"  Looking for: '{unwanted}'")

        # Debug: Check if term exists in content at all
        if unwanted in content:
            print(f"  ✓ Found '{unwanted}' in content!")
        else:
            print(f"  ✗ '{unwanted}' not found in content")
            # Let's try to find similar text
            if 'Great Xia' in content:
                print("  But 'Great Xia' was found - might be formatting differences")
            if 'Cucktopia' in content:
                print("  But 'Cucktopia' was found - might be formatting differences")

        # Simple direct replacement (most reliable)
        if unwanted in content:
            new_content = content.replace(unwanted, 'Cucktopia')
            replacements = content.count(unwanted)
            content = new_content
            replaced_count += replacements
            print(f"  → Replaced {replacements} occurrences using direct replacement")
        else:
            # Try regex patterns as fallback
            patterns = []

            # For text with parentheses, be more careful with word boundaries
            # Don't use \b around parentheses - they mess up word boundaries
            patterns = [
                # Match HTML comments containing the unwanted content
                re.compile(r'<!--\s*' + re.escape(unwanted) + r'\s*-->', re.IGNORECASE),
                # Match the exact term without word boundaries (safer for parentheses)
                re.compile(re.escape(unwanted), re.IGNORECASE),
                # Try with flexible spacing inside parentheses
                re.compile(r'Great Xia\s*\(\s*Great\s+Xia\s*\)', re.IGNORECASE)
            ]

            for i, pattern in enumerate(patterns):
                matches = pattern.findall(content)
                if matches:
                    content = pattern.sub('Cucktopia', content)
                    replaced_count += len(matches)
                    print(f"  → Found and replaced using pattern {i+1}: {len(matches)} occurrences")
                    break

    # Write back to file if changes were made
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ File updated successfully")
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")
            return 0
    else:
        print(f"  → No changes made to file")

    return replaced_count

def process_directory(directory):
    total_files = 0
    total_replaced = 0

    # Find all .xhtml files
    xhtml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xhtml'):
                xhtml_files.append(os.path.join(root, file))

    if not xhtml_files:
        print(f"No .xhtml files found in directory: {directory}")
        return

    print(f"Found {len(xhtml_files)} .xhtml files to process")
    print("-" * 50)

    for file_path in xhtml_files:
        print(f"Processing: {file_path}")
        replaced = replace_unwanted_content(file_path)
        total_files += 1
        total_replaced += replaced

        if replaced > 0:
            print(f"✓ Replaced {replaced} terms in {os.path.basename(file_path)}")
        else:
            print(f"○ No replacements needed in {os.path.basename(file_path)}")
        print()

    print("-" * 50)
    print(f"Finished processing {total_files} files. Total terms replaced: {total_replaced}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Great-Xia.py <directory>")
        print("Example: python Great-Xia.py /path/to/your/novel/folder")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    print(f"Starting to process directory: {directory}")
    print("Replacing unwanted terms...")
    print("=" * 50)

    process_directory(directory)

if __name__ == "__main__":
    main()
