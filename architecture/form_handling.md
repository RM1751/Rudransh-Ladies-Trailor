# SOP: Form Handling & WhatsApp Integration

## Purpose
Handle customer booking form submissions and send data to WhatsApp.

## Input
- Customer fills booking form on `booking.html`
- Form data: name, phone, address, garment type, measurements, etc.

## Process

### Step 1: Form Validation
```javascript
// Validate required fields
// Validate phone number (10 digits, starts with 6-9)
// Show error if validation fails
```

### Step 2: Data Collection
```javascript
// Collect all form fields into object
// Convert to WhatsApp message format
```

### Step 3: WhatsApp Message Generation
```
Format:
*New Booking - Rudransh Tailoring*
*Date:* [timestamp]

*Customer Details:*
👤 Name: [name]
📞 Phone: [phone]
🏠 Address: [address]

*Order Details:*
👗 Garment Type: [type]
📏 Measurements: [measurements]
...
```

### Step 4: WhatsApp URL Generation
```
https://wa.me/918840586403?text=[encoded_message]
```

### Step 5: Open WhatsApp
- Open URL in new tab
- WhatsApp opens with pre-filled message
- Customer clicks send

## Output
- WhatsApp opens with formatted booking details
- Customer sends message to complete booking

## Error Handling
- Invalid phone: Show alert
- Missing required fields: Highlight fields in red
- Network issues: Show error message

## Edge Cases
- Phone number with spaces/dashes: Strip non-digits
- Empty optional fields: Skip in message
- Very long text: WhatsApp handles truncation
