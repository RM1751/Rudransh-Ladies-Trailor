/**
 * Cloudinary Configuration
 * Get these values from your Cloudinary Dashboard:
 * https://cloudinary.com/console
 * 
 * SETUP INSTRUCTIONS:
 * 1. Sign up at https://cloudinary.com/users/register/free
 * 2. Go to Dashboard to get your Cloud name
 * 3. Create an upload preset (Settings → Upload → Add preset)
 * 4. Set the values below
 */

const CLOUDINARY_CONFIG = {
    // Your Cloudinary cloud name (from Dashboard)
    cloudName: 'YOUR_CLOUD_NAME',
    
    // Upload preset name (create in Settings → Upload)
    uploadPreset: 'rudransh_uploads',
    
    // Folder path in Cloudinary (optional)
    folder: 'rudransh_gallery'
};

// Make available globally
window.CLOUDINARY_CONFIG = CLOUDINARY_CONFIG;
