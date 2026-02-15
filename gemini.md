# 🚀 Rudransh Tailoring - Project Constitution

> This file is LAW. It defines data schemas, behavioral rules, and architectural invariants.

---

## 📋 Project Overview

**Business Name:** Rudransh Trailoring at doorStep  
**WhatsApp Number:** +918840586403  
**WhatsApp Link:** https://api.whatsapp.com/message/5ENPHPUVUVYOF1?autoload=1&app_absent=0  
**Project Type:** Responsive Website with Booking Form + WhatsApp Integration  
**Tech Stack:** HTML, CSS, JavaScript (Frontend), Python (Backend for form processing)

---

## 📊 Data Schemas

### Schema 1: Customer Booking Form (Input)

```json
{
  "customer_name": "string (required)",
  "phone_number": "string (required, validated)",
  "email": "string (optional)",
  "address": "string (required)",
  "garment_type": "enum [Blouse, Kurti, Salwar Kameez, Lehenga, Gown, Other]",
  "style_preference": "string (e.g., Princess Cut, Simple Cut, etc.)",
  "measurements": {
    "bust": "number (inches/cm)",
    "waist": "number (inches/cm)",
    "hip": "number (inches/cm)",
    "shoulder": "number (inches/cm)",
    "arm_length": "number (inches/cm)",
    "length": "number (inches/cm)",
    "other_notes": "string"
  },
  "fabric_provided": "boolean",
  "pickup_required": "boolean",
  "delivery_required": "boolean",
  "preferred_date": "date",
  "special_instructions": "string (optional)",
  "submitted_at": "timestamp"
}
```

### Schema 2: Form Output Payload

```json
{
  "whatsapp_message": "formatted string for WhatsApp",
  "excel_row": "array format for CSV/Excel",
  "email_body": "HTML/text email format"
}
```

### Schema 3: Gallery Image (Admin Upload)

```json
{
  "image_id": "uuid",
  "file_name": "string",
  "file_path": "string (relative path)",
  "category": "enum [Blouse, Kurti, Salwar, Lehenga, Gown, Other]",
  "uploaded_at": "timestamp",
  "is_visible": "boolean"
}
```

---

## 🎨 Behavioral Rules

### UI/UX Rules
1. **Mobile-First:** Website must be fully responsive, optimized for mobile
2. **Color Theme:** Traditional Indian tailoring colors (Maroon, Gold, Cream/White accents)
3. **Font:** Clean, readable fonts (Inter or similar for body, decorative for headings)
4. **WhatsApp Button:** Fixed floating button on bottom-right, green color
5. **Loading States:** Show loading spinner during form submission

### Form Rules
1. **Validation:** All required fields must be validated before submission
2. **Phone Format:** Indian phone number validation (+91 or 10 digits)
3. **Measurement Units:** Allow both inches and cm with conversion
4. **File Upload:** Max 5MB per image, JPG/PNG only

### Security Rules
1. **No Sensitive Data:** Don't store payment info
2. **Rate Limiting:** Max 3 form submissions per IP per hour
3. **Input Sanitization:** Sanitize all text inputs

---

## 🚫 Do Not Rules
1. Do NOT store customer data permanently without consent
2. Do NOT auto-send WhatsApp messages (user must click to send)
3. Do NOT collect payment information
4. Do NOT use external tracking/analytics without permission

---

## 📁 File Structure

```
project/
├── index.html              # Homepage
├── about.html              # About page
├── gallery.html            # Gallery/Portfolio
├── booking.html            # Booking form page
├── contact.html            # Contact page
├── css/
│   └── styles.css          # Main stylesheet
├── js/
│   └── main.js             # Main JavaScript
├── tools/
│   └── form_processor.py   # Python backend for form processing
├── uploads/                # Image upload folder (admin)
├── .tmp/                   # Temporary files
├── architecture/           # SOP documentation
│   ├── form_handling.md
│   ├── image_upload.md
│   └── whatsapp_integration.md
├── gemini.md               # This file
├── task_plan.md            # Project phases
├── findings.md             # Research & discoveries
└── progress.md             # Progress tracking
```

---

## 🔧 Technical Invariants

1. **Frontend:** Pure HTML/CSS/JS (no frameworks for simplicity)
2. **Backend:** Python Flask (lightweight, easy to deploy)
3. **Image Storage:** Local filesystem (can migrate to cloud later)
4. **Form Delivery:** WhatsApp API link + optional email
5. **Admin Panel:** Simple password-protected page for image upload/remove

---

## 📅 Maintenance Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-02-15 | Initial creation | Project initialization |
