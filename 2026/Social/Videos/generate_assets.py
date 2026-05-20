import os

# ==========================================
# CONFIGURATION
# ==========================================
# 1. Change this to match your target GitHub repository path for this specific campaign
GITHUB_BASE_URL = "https://github.com/ApprovalPage/SNCGG-CreativeLibrary/blob/main/2026/Social/"

# 2. Allowed file extensions for main assets
ASSET_EXTENSIONS = ('.mp4', '.png', '.jpg', '.jpeg', '.gif')
# ==========================================

def generate_html_blocks():
    # Look at the directory where the script is running
    current_dir = os.getcwd()
    thumbs_dir = os.path.join(current_dir, 'thumbs')
    
    # Get all files in the current directory
    files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]
    
    html_output = []
    
    for file in sorted(files):
        # Skip the script itself or non-asset files
        if not file.lower().endswith(ASSET_EXTENSIONS) or file == 'generate_assets.py':
            continue
            
        filename_without_ext, ext = os.path.splitext(file)
        
        # Build the URL for the main asset
        main_asset_url = f"{GITHUB_BASE_URL}{file}?raw=true"
        
        # Determine the thumbnail path (checks for .png or .jpg in the thumbs folder)
        thumb_file = f"{filename_without_ext}.png"
        if not os.path.exists(os.path.join(thumbs_dir, thumb_file)):
            thumb_file = f"{filename_without_ext}.jpg" # fallback check
            
        thumb_url = f"{GITHUB_BASE_URL}thumbs/{thumb_file}?raw=true"
        
        # Generate the HTML block matching your exact layout
        block = f'''            <div class="asset-item" onclick="openModal('{main_asset_url}')">
                <img class="asset-thumbnail" src="{thumb_url}">
                <div class="asset-caption">{filename_without_ext}</div>
            </div>'''
        
        html_output.append(block)
    
    # Write the results to a text file
    output_file = "generated_html.txt"
    with open(output_file, "w") as out:
        out.write("\n".join(html_output))
        
    print(f"Success! {len(html_output)} HTML asset blocks generated inside '{output_file}'.")

if __name__ == "__main__":
    generate_html_blocks()