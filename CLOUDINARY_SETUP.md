# ☁️ Cloudinary Setup Guide for Rudransh Tailoring

This guide helps you set up **Cloudinary** for permanent image storage so all visitors can see your uploaded images.

---

## 🎯 What is Cloudinary?

Cloudinary is a **free cloud service** that stores your images and delivers them fast to visitors worldwide.

### Benefits:
- ✅ **Permanent storage** - Images don't disappear when you clear browser
- ✅ **Global CDN** - Fast loading for visitors anywhere
- ✅ **Free tier** - 25GB storage + 25GB bandwidth per month
- ✅ **No GitHub needed** - Upload directly from admin panel
- ✅ **Auto-optimization** - Images are automatically optimized

---

## 📋 Setup Steps

### Step 1: Create Free Account

1. Go to: **https://cloudinary.com/users/register/free**
2. Sign up with:
   - Your email, or
   - Google account
3. Verify your email

---

### Step 2: Get Your Cloud Name

1. Go to Dashboard: **https://cloudinary.com/console**
2. Look for **"Cloud name"** at the top
   - Example: `rudransh-tailoring` or `dx1a2b3c4`
3. **Copy this name**

![Cloud Name Location](https://res.cloudinary.com/demo/image/upload/cloud_name_location.png)

---

### Step 3: Create Upload Preset

This allows your website to upload images without API keys:

1. In Cloudinary console, click **Settings** (gear icon) → **Upload**
2. Scroll down to **"Upload presets"**
3. Click **"Add upload preset"**
4. Fill these values:
   - **Preset name**: `rudransh_uploads`
   - **Signing Mode**: ☑️ **Unsigned**
   - **Folder**: `rudransh_gallery`
5. Click **Save**

![Upload Preset](https://res.cloudinary.com/demo/image/upload/upload_preset.png)

---

### Step 4: Update Your Website

1. Open file: `js/cloudinary-config.js`
2. Replace `YOUR_CLOUD_NAME` with your actual cloud name:

```javascript
const CLOUDINARY_CONFIG = {
    cloudName: 'rudransh-tailoring',  // <-- Replace this
    uploadPreset: 'rudransh_uploads',
    folder: 'rudransh_gallery'
};
```

3. **Save the file**

---

### Step 5: Deploy to Vercel

Push changes to GitHub (Vercel auto-deploys):

```bash
git add .
git commit -m "Configure Cloudinary for image uploads"
git push origin main
```

Or upload files manually to GitHub.

---

### Step 6: Test Upload

1. Go to your website: `https://your-site.vercel.app/admin.html`
2. Login with password: `Ravi@12345`
3. Select **"☁️ Cloudinary (Recommended)"** tab
4. Fill in image details
5. Click **"Open Cloudinary Upload"**
6. Select an image from your computer
7. Wait for upload to complete
8. Check your gallery page - image should appear!

---

## 🔍 Verification

### Check in Cloudinary Console:
1. Go to: **https://cloudinary.com/console**
2. Click **Media Library**
3. You should see your uploaded images in `rudransh_gallery` folder

### Check on Your Website:
1. Go to Gallery page
2. Uploaded images should appear in "Our Work" section
3. Images load fast from Cloudinary CDN

---

## 📊 Free Tier Limits

| Feature | Free Tier |
|---------|-----------|
| Storage | 25 GB |
| Bandwidth | 25 GB/month |
| Transformations | 25,000/month |
| Price | **FREE** |

> 💡 For a small tailoring business, this is more than enough!

---

## 🛠️ Troubleshooting

### "Cloudinary not configured" error
- Check that you updated `cloudName` in `js/cloudinary-config.js`
- Make sure you deployed the updated file to Vercel

### Upload fails
- Check internet connection
- Image must be under 5MB
- Try a different image format (JPG, PNG)

### Images not showing in gallery
- Clear browser cache (Ctrl+Shift+R)
- Check browser console for errors (F12 → Console)
- Verify images appear in Cloudinary Media Library

### "Upload preset not found"
- Make sure preset name is exactly: `rudransh_uploads`
- Check it's set to "Unsigned" mode
- Wait 1-2 minutes after creating preset

---

## 🎓 Alternative: Python Gallery Generator

If you prefer to add images manually to GitHub, use the Python script:

```bash
# Add images to images/ folder
cd tools/
python generate_gallery.py
```

This auto-generates gallery HTML from the `images/` folder.

---

## 📞 Need Help?

- **Cloudinary Docs**: https://cloudinary.com/documentation
- **Video Tutorial**: Search "Cloudinary upload widget setup" on YouTube
- **Contact me** for assistance!

---

## ✅ Summary

| Feature | Browser Storage | Cloudinary |
|---------|----------------|------------|
| Visibility | Only you | Everyone |
| Storage | Browser only | Cloud |
| Permanent | ❌ No | ✅ Yes |
| Speed | Good | Excellent (CDN) |
| Cost | Free | Free (25GB) |
| Setup | None | 5 minutes |

**Recommendation**: Use **Cloudinary** for production!
