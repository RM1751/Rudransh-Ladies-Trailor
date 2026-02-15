# SOP: Image Upload & Gallery Management

## Purpose
Allow admin to upload and manage gallery images.

## Input
- Admin logs into `admin.html`
- Selects image file (JPG/PNG, max 5MB)
- Selects category
- Adds title and description

## Process

### Step 1: Authentication
- Check password: `rudransh123`
- Store login state in sessionStorage

### Step 2: File Selection
- Click upload area or drag-drop
- Validate file type: image/*
- Validate file size: < 5MB
- Show preview

### Step 3: Metadata Entry
- Select category from dropdown
- Enter title
- Enter description (optional)

### Step 4: Storage
```javascript
// Current: localStorage (browser-based)
// Structure:
{
  id: timestamp,
  title: "...",
  description: "...",
  category: "blouse",
  dataUrl: "base64...",
  uploadedAt: "..."
}
```

### Step 5: Gallery Display
- Load images from localStorage
- Filter by category
- Display in grid layout

### Step 6: Deletion
- Click delete button on image
- Confirm dialog
- Remove from localStorage
- Refresh grid

## Output
- Images saved to localStorage
- Gallery displays uploaded images
- Can filter by category

## Limitations
- localStorage has ~5MB limit
- Images are base64 encoded (larger size)
- Data lost if browser cache cleared

## Future Enhancement
- Move to server-side storage
- Use actual file system or cloud storage
- Add image compression
