========================================
HOW TO ADD YOUR IMAGES - 3 METHODS
========================================

========================================
METHOD 1: CLOUDINARY (EASIEST - RECOMMENDED)
========================================
Upload images directly from Admin Panel to Cloudinary cloud storage.

STEPS:
1. Go to: https://your-site.vercel.app/admin.html
2. Login with password: Ravi@12345
3. Select "☁️ Cloudinary (Recommended)" tab
4. Click "Open Cloudinary Upload"
5. Select your image and upload
6. Done! Image appears instantly on your website

SETUP REQUIRED (One-time):
- See: CLOUDINARY_SETUP.md in root folder
- Or visit: https://cloudinary.com/users/register/free

BENEFITS:
✅ Images visible to ALL visitors immediately
✅ No GitHub needed
✅ Fast global CDN delivery
✅ FREE up to 25GB

========================================
METHOD 2: PYTHON GALLERY GENERATOR
========================================
Auto-generate gallery from images in this folder.

STEPS:
1. Add images to this folder (images/)
2. Run the Python script:
   
   cd tools/
   python generate_gallery.py

3. Script will auto-update gallery.html
4. Push to GitHub:
   
   git add .
   git commit -m "Added gallery images"
   git push origin main

5. Vercel auto-deploys in ~1 minute

BENEFITS:
✅ No manual HTML editing
✅ Images stored in GitHub (permanent)
✅ Works offline

========================================
METHOD 3: MANUAL GITHUB UPLOAD
========================================
Upload images directly via GitHub website.

STEPS:
1. Go to: https://github.com/YOUR_USERNAME/Rudransh-Ladies-Trailor
2. Navigate to: images/ folder
3. Click: "Add file" → "Upload files"
4. Upload your images
5. Commit changes
6. Vercel auto-deploys

BENEFITS:
✅ No command line needed
✅ Works from any device
✅ Images in version control

========================================
IMAGE NAMING GUIDE
========================================
Use descriptive names so they're auto-categorized:

  blouse-design-1.jpg    → Category: Blouse
  blouse-princess.jpg    → Category: Blouse
  kurti-anarkali.jpg     → Category: Kurti
  salwar-punjabi.jpg     → Category: Salwar Suit
  lehenga-bridal.jpg     → Category: Lehenga
  gown-evening.jpg       → Category: Gown

Supported formats: .jpg, .jpeg, .png, .webp
Recommended size: 800x1000px, under 1MB

========================================
NEED HELP?
========================================
WhatsApp: +91 88405 86403
Email: Check your business contact

========================================
