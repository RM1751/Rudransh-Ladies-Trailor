# SOP: WhatsApp Integration

## Purpose
Enable direct WhatsApp communication with customers.

## Method
Using WhatsApp Click-to-Chat API (no API key needed)

## Implementation

### Floating Button
- Fixed position: bottom-right corner
- Color: #25D366 (WhatsApp brand color)
- Icon: WhatsApp SVG logo
- Link: https://api.whatsapp.com/message/5ENPHPUVUVYOF1?autoload=1&app_absent=0

### Form Submission
- Generate pre-filled message
- Open wa.me link with encoded message
- Customer clicks send in WhatsApp

## URL Formats

### Direct Chat (Floating Button)
```
https://api.whatsapp.com/message/5ENPHPUVUVYOF1?autoload=1&app_absent=0
```

### Pre-filled Message (Form Submission)
```
https://wa.me/918840586403?text=Hello%20I%20want%20to%20book...
```

## Message Formatting
- Use `*` for bold: `*text*`
- Use `_` for italic: `_text_`
- Use `~` for strikethrough: `~text~`
- Use newline: `\n`
- URL encode special characters

## Example Message
```
*New Booking - Rudransh Tailoring*
*Date:* 15/02/2026, 2:30:00 pm

*Customer Details:*
👤 Name: Priya Sharma
📞 Phone: 9876543210
🏠 Address: 123 Main Street

*Order Details:*
👗 Garment Type: Blouse
✂️ Style: Princess Cut
📏 Measurements:
   • Bust: 36 inches
   • Waist: 30 inches
   • Hip: 38 inches

*Additional Info:*
🧵 Fabric Provided: No
🚚 Pickup Required: Yes
📦 Delivery Required: Yes

Thank you for choosing Rudransh Tailoring! 🙏
```

## Testing
1. Open website on mobile
2. Click WhatsApp button
3. Should open WhatsApp app with pre-filled message
4. On desktop: Opens WhatsApp Web

## Notes
- Customer must have WhatsApp installed
- Phone number must include country code
- Works internationally
- Free to use (no API costs)
