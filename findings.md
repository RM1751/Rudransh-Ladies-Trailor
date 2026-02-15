# 🔍 Rudransh Tailoring - Findings & Research

---

## Business Requirements

### Core Needs
1. **Product Showcase** - Gallery with categories (Blouse, Kurti, Salwar, Lehenga, Gown)
2. **Customer Booking** - Appointment form with detailed measurements
3. **WhatsApp Integration** - Direct chat link for customers
4. **Order Management** - Status tracking (basic for now)
5. **Photo Gallery** - Admin can upload/remove work samples

### Technical Constraints
- Static hosting preferred (can use Python Flask for backend)
- WhatsApp Business API not needed (using direct chat link)
- Image storage: Local filesystem
- No payment gateway integration

---

## WhatsApp Integration Research

**Method:** Direct WhatsApp Chat Link
- URL Format: `https://api.whatsapp.com/message/5ENPHPUVUVYOF1?autoload=1&app_absent=0`
- No API key required
- Opens WhatsApp web/app with pre-filled message
- Customer clicks to send

**Implementation:**
- Floating button on all pages (bottom-right)
- Fixed position, z-index: 9999
- Green color (#25D366 - WhatsApp brand color)
- Icon: WhatsApp logo SVG

---

## Measurement Form Fields

Based on tailoring requirements:

| Field | Type | Required |
|-------|------|----------|
| Customer Name | Text | Yes |
| Phone Number | Tel | Yes |
| Email | Email | No |
| Address | Textarea | Yes |
| Garment Type | Select | Yes |
| Style/Design | Text | No |
| Bust | Number | Yes |
| Waist | Number | Yes |
| Hip | Number | Yes |
| Shoulder | Number | Yes |
| Arm Length | Number | No |
| Garment Length | Number | Yes |
| Sleeve Length | Number | No |
| Neck Depth | Number | No |
| Special Instructions | Textarea | No |
| Preferred Delivery Date | Date | No |

---

## Design Decisions

### Color Palette
- **Primary:** #8B0000 (Dark Maroon - traditional)
- **Secondary:** #FFD700 (Gold - premium feel)
- **Accent:** #25D366 (WhatsApp Green)
- **Background:** #FFF8F0 (Cream)
- **Text:** #333333 (Dark Gray)

### Typography
- Headings: 'Playfair Display' or similar serif (elegant)
- Body: 'Inter' or 'Roboto' (readable)

### Layout
- Mobile-first responsive design
- Single-column on mobile
- 2-3 columns on desktop
- Max-width: 1200px

---

## Security Considerations

1. **Form Spam:** Add honeypot field + simple CAPTCHA
2. **File Upload:** Validate type, size, rename files
3. **Admin Panel:** Basic HTTP auth or simple password
4. **Data Privacy:** Don't log sensitive info

---

## Known Limitations

1. WhatsApp message will be pre-filled, customer must click send
2. No real-time order tracking (manual status updates)
3. No payment integration (cash on delivery)
4. Image storage is local (backup recommended)

---

## Useful Resources

- WhatsApp API docs: https://developers.facebook.com/docs/whatsapp/
- Flask documentation: https://flask.palletsprojects.com/
- Tailwind CSS (if used): https://tailwindcss.com/

---

## Questions Asked & Answered

| Question | Answer |
|----------|--------|
| Business Name | Rudransh Trailoring at doorStep |
| WhatsApp Number | +918840586403 |
| WhatsApp Link | https://api.whatsapp.com/message/5ENPHPUVUVYOF1?autoload=1&app_absent=0 |
| Image handling | Placeholders initially, admin upload/remove feature |
| Data delivery | WhatsApp message + Excel format option |
