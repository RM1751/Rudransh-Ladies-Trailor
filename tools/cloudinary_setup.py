#!/usr/bin/env python3
"""
Cloudinary Setup Helper for Rudransh Tailoring
Helps configure Cloudinary for image hosting
"""

import os
from pathlib import Path


def create_cloudinary_html():
    """Create cloudinary-config.js template"""
    js_content = '''/**
 * Cloudinary Configuration
 * Get these values from your Cloudinary Dashboard:
 * https://cloudinary.com/console
 */

const CLOUDINARY_CONFIG = {
    // Your Cloudinary cloud name
    cloudName: 'dbaduzib2',
    
    // Upload preset (create one in Cloudinary settings)
    uploadPreset: 'rudransh_uploads',
    
    // API Key (for signed uploads - optional)
    apiKey: 'YOUR_API_KEY',
    
    // Folder path in Cloudinary
    folder: 'rudransh_gallery'
};

// Make available globally
window.CLOUDINARY_CONFIG = CLOUDINARY_CONFIG;
'''
    
    with open('../js/cloudinary-config.js', 'w') as f:
        f.write(js_content)
    
    print("✅ Created: js/cloudinary-config.js")


def print_setup_instructions():
    """Print Cloudinary setup instructions"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║              CLOUDINARY SETUP INSTRUCTIONS                       ║
╚══════════════════════════════════════════════════════════════════╝

📝 Step 1: Create Cloudinary Account
   1. Go to: https://cloudinary.com/users/register/free
   2. Sign up with email or Google account
   3. It's FREE for up to 25GB storage!

📝 Step 2: Get Your Cloud Name
   1. Go to Dashboard: https://cloudinary.com/console
   2. Look for "Cloud name" (e.g., "rudransh-tailoring")
   3. Copy this value

📝 Step 3: Create Upload Preset
   1. Go to Settings → Upload
   2. Scroll to "Upload presets" section
   3. Click "Add upload preset"
   4. Set:
      - Name: rudransh_uploads
      - Signing Mode: Unsigned
      - Folder: rudransh_gallery
   5. Click Save

📝 Step 4: Update Configuration
   1. Open: js/cloudinary-config.js
   2. Replace 'YOUR_CLOUD_NAME' with your actual cloud name
   3. Save the file

📝 Step 5: Test Upload
   1. Go to admin.html
   2. Login with password: Ravi@12345
   3. Try uploading an image
   4. Check Cloudinary Media Library to verify

═══════════════════════════════════════════════════════════════════

✨ BENEFITS OF CLOUDINARY:
   ✅ Images stored permanently (not just in browser)
   ✅ Automatic image optimization
   ✅ Fast global CDN delivery
   ✅ Works on all devices
   ✅ No GitHub needed for image uploads

═══════════════════════════════════════════════════════════════════
    """)


def main():
    print("=" * 60)
    print("☁️  Cloudinary Setup for Rudransh Tailoring")
    print("=" * 60)
    
    # Create config file
    create_cloudinary_html()
    
    # Print instructions
    print_setup_instructions()


if __name__ == '__main__':
    main()
