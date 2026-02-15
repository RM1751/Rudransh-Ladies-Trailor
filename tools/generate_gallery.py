#!/usr/bin/env python3
"""
Gallery Generator for Rudransh Tailoring
Automatically generates gallery HTML from images in the images/ folder
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Category mapping based on filename keywords
CATEGORY_KEYWORDS = {
    'blouse': ['blouse', 'blouses', 'choli'],
    'kurti': ['kurti', 'kurtis', 'kurta'],
    'salwar': ['salwar', 'suit', 'punjabi', 'patiala'],
    'lehenga': ['lehenga', 'lehengas', 'bridal'],
    'gown': ['gown', 'gowns', 'dress', 'evening'],
}

# Category display names
CATEGORY_NAMES = {
    'blouse': 'Blouse',
    'kurti': 'Kurti',
    'salwar': 'Salwar Suit',
    'lehenga': 'Lehenga',
    'gown': 'Gown',
    'other': 'Other'
}

# Category icons
CATEGORY_ICONS = {
    'blouse': '👔',
    'kurti': '👗',
    'salwar': '🥻',
    'lehenga': '💃',
    'gown': '👰',
    'other': '👘'
}


def detect_category(filename):
    """Detect category based on filename keywords"""
    filename_lower = filename.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in filename_lower for keyword in keywords):
            return category
    return 'other'


def format_title(filename):
    """Convert filename to readable title"""
    # Remove extension
    name = Path(filename).stem
    # Replace separators with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    # Capitalize words
    return name.title()


def scan_images_folder(images_path='../images'):
    """Scan images folder and return list of image data"""
    images_path = Path(images_path)
    
    if not images_path.exists():
        print(f"❌ Images folder not found: {images_path}")
        return []
    
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG'}
    images = []
    
    for file in images_path.iterdir():
        if file.is_file() and file.suffix in valid_extensions:
            # Skip README and other non-image files
            if file.name.startswith('README'):
                continue
                
            category = detect_category(file.name)
            title = format_title(file.name)
            
            images.append({
                'filename': file.name,
                'path': f'images/{file.name}',
                'category': category,
                'title': title,
                'description': f'Beautiful custom {CATEGORY_NAMES.get(category, "garment")} by Rudransh Tailoring'
            })
    
    # Sort by category then filename
    images.sort(key=lambda x: (x['category'], x['filename']))
    return images


def generate_gallery_html(images):
    """Generate gallery HTML from images list"""
    if not images:
        return "<!-- No images found in images/ folder -->"
    
    html_parts = []
    
    for img in images:
        icon = CATEGORY_ICONS.get(img['category'], '👘')
        html_parts.append(f'''                <!-- {img['title']} -->
                <div class="gallery-item" data-category="{img['category']}" onclick="openFileModal('{img['path']}', '{img['category']}', '{img['title']}', '{img['description']}')">
                    <div class="gallery-image-wrapper">
                        <img src="{img['path']}" alt="{img['title']}" loading="lazy">
                    </div>
                    <div class="gallery-info">
                        <h4>{img['title']}</h4>
                        <p>{img['description']}</p>
                        <p style="color: var(--primary); font-size: 0.85rem; margin-top: 8px;">👆 Click to view & order</p>
                    </div>
                </div>''')
    
    return '\n'.join(html_parts)


def update_gallery_html(images, gallery_path='../gallery.html'):
    """Update gallery.html with generated HTML"""
    gallery_path = Path(gallery_path)
    
    if not gallery_path.exists():
        print(f"❌ Gallery file not found: {gallery_path}")
        return False
    
    # Read existing gallery.html
    with open(gallery_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate new gallery HTML
    gallery_html = generate_gallery_html(images)
    
    # Find the adminGallery div and replace its content
    import re
    
    # Pattern to match the adminGallery div content
    pattern = r'(<div class="gallery-grid" id="adminGallery">)(.*?)(</div>)'
    
    replacement = f'''\1
                    <!-- Auto-generated gallery - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -->
                    <p style="color: #666; text-align: center; grid-column: 1/-1; padding: 10px; font-size: 0.9rem;">
                        🖼️ Showing {len(images)} design(s)
                    </p>
{gallery_html}
                \3'''
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True


def generate_json_manifest(images, output_path='../images/gallery-manifest.json'):
    """Generate JSON manifest for images"""
    manifest = {
        'generated_at': datetime.now().isoformat(),
        'total_images': len(images),
        'images': images
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Manifest saved: {output_path}")


def print_stats(images):
    """Print statistics about images"""
    if not images:
        print("\n📊 No images found!")
        return
    
    print(f"\n📊 Found {len(images)} image(s):")
    print("-" * 40)
    
    by_category = {}
    for img in images:
        cat = img['category']
        by_category[cat] = by_category.get(cat, 0) + 1
    
    for cat, count in sorted(by_category.items()):
        icon = CATEGORY_ICONS.get(cat, '👘')
        print(f"  {icon} {CATEGORY_NAMES.get(cat, cat)}: {count}")


def main():
    """Main function"""
    print("=" * 50)
    print("🖼️  Rudransh Tailoring - Gallery Generator")
    print("=" * 50)
    
    # Scan images folder
    print("\n🔍 Scanning images/ folder...")
    images = scan_images_folder()
    
    # Print stats
    print_stats(images)
    
    if not images:
        print("\n⚠️  No images found. Add images to the 'images/' folder first.")
        return
    
    # Generate JSON manifest
    print("\n📝 Generating manifest...")
    generate_json_manifest(images)
    
    # Update gallery.html
    print("\n🔄 Updating gallery.html...")
    if update_gallery_html(images):
        print("✅ Gallery updated successfully!")
    else:
        print("❌ Failed to update gallery.html")
    
    print("\n" + "=" * 50)
    print("Next steps:")
    print("  1. Review the changes in gallery.html")
    print("  2. Commit and push to GitHub:")
    print("     git add .")
    print("     git commit -m 'Update gallery with new images'")
    print("     git push origin main")
    print("  3. Vercel will auto-deploy in ~1 minute")
    print("=" * 50)


if __name__ == '__main__':
    main()
