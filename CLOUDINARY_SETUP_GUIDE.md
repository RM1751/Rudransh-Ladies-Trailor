# Cloudinary Setup Guide for Rudrans

## ✅ Your Cloudinary Account Details
- **Cloud Name:** `dbaduzib2` ✓
- **Status:** Configured in website

## ⚠️ Required: Create Upload Preset

You need to create an **upload preset** in Cloudinary to allow image uploads from your website.

### Steps to Create Upload Preset:

1. **Login to Cloudinary:** https://cloudinary.com/console

2. **Go to Settings:**
   - Click on the **Settings** icon (gear icon) in the top right
   - Or go directly to: https://cloudinary.com/console/settings/upload

3. **Navigate to Upload Tab:**
   - Click on **"Upload"** tab in the settings menu
   - Scroll down to **"Upload presets"** section

4. **Create New Upload Preset:**
   - Click **"Add upload preset"** button
   
5. **Configure the Preset:**
   
   | Setting | Value |
   |---------|-------|
   | **Preset name** | `rudransh_uploads` |
   | **Signing Mode** | `Unsigned` |
   | **Folder** | `rudransh_gallery` (optional) |

6. **Save the Preset:**
   - Click **"Save"** button

## 🧪 Test the Upload

1. Open your website's **Admin Panel** (`admin.html`)
2. Login with password
3. Go to **"Upload to Cloudinary"** section
4. Select a category, add title/description
5. Click **"Upload to Cloudinary"** button
6. Select an image and upload

## 🖼️ Your Uploaded Image

You already have this image in Cloudinary:
- **URL:** https://res.cloudinary.com/dbaduzib2/image/upload/v1773573175/Blouse-Thumbnail-Hindi_1_sfgxlk.png

This will automatically appear in your website's **Hero Slider** and **Gallery**!

## 🔧 Files Updated

- `js/cloudinary-config.js` - Cloud name updated to `dbaduzib2`
- `admin.html` - Upload check updated

## ❓ Troubleshooting

### "Upload preset not found" error?
- Make sure the preset name is exactly: `rudransh_uploads`
- Check that **Signing Mode** is set to **Unsigned**

### Images not showing in gallery?
- Upload images through the Admin Panel
- Images are stored in browser's localStorage
- Clear browser cache and refresh

### Need help?
- Cloudinary Docs: https://cloudinary.com/documentation
- Upload Widget Docs: https://cloudinary.com/documentation/upload_widget
