# Rudrans Ladies Tailoring at Doorstep

A responsive website for Rudrans Ladies Tailoring business with booking form, gallery, and admin panel.

## 🌐 Live Website

**Deployed URL:** [Your Vercel/Netlify URL]

## 📱 Features

- **Responsive Design** - Works on mobile, tablet, and desktop
- **Image Gallery** - Click any image to view details and book order
- **Booking Form** - Complete measurement form with WhatsApp integration
- **Admin Panel** - Upload and manage gallery images
- **WhatsApp Integration** - Direct chat and order submission via WhatsApp

## 🔑 Admin Access

To access the admin panel:
1. Go to: `yourwebsite.com/admin.html`
2. Default Password: `Ravi@12345`
3. You can change the password after logging in

## ⚠️ Important: Image Storage Limitation

**Current Setup:** Images are stored in browser's `localStorage`

### What This Means:
- ✅ Images uploaded on **your computer** will show on **your computer**
- ❌ Images will **NOT** show on customer's phones or other devices
- ❌ Images will **NOT** show if browser cache is cleared
- ❌ Images are limited to ~5MB total storage

### Solutions for Production:

#### Option 1: Use Sample Images Only (Current)
The website includes sample placeholder images that work for all users.

#### Option 2: Add Real Images via Code (Recommended)
To add your real work photos that show for everyone:

1. Rename your images: `blouse1.jpg`, `kurti1.jpg`, etc.
2. Place them in the `images/` folder
3. Update `gallery.html` to reference these files:

```html
<div class="gallery-item">
    <img src="images/blouse1.jpg" alt="Princess Cut Blouse">
</div>
```

#### Option 3: Use Cloud Storage (Advanced)
Upload images to:
- Google Drive (public links)
- Cloudinary (free tier)
- AWS S3
- Imgur

Then update the image URLs in the gallery.

## 🚀 Deployment

### Deploy to Vercel:
```bash
npm i -g vercel
vercel
```

### Deploy to Netlify:
1. Push code to GitHub
2. Connect repository to Netlify
3. Auto-deploy on every push

## 📞 Contact

- **Phone:** +91 88405 86403
- **WhatsApp:** https://wa.me/918840586403

## 📝 Updates

### 2026-02-15
- ✅ Fixed WhatsApp links for mobile compatibility
- ✅ Added image click-to-order modal
- ✅ Added password reset functionality

## 🔧 Tech Stack

- HTML5
- CSS3
- JavaScript (Vanilla)
- localStorage (for admin images - device specific)

---

**Note:** For a fully functional image gallery across all devices, consider upgrading to a backend with database storage.
