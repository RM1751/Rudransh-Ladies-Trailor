"""
Form Processor for Rudransh Tailoring
Handles booking form submissions and generates WhatsApp messages
"""

import json
import urllib.parse
from datetime import datetime
from typing import Dict, Any


class FormProcessor:
    """Process booking form data and generate WhatsApp messages"""
    
    def __init__(self, whatsapp_number: str = "918840586403"):
        self.whatsapp_number = whatsapp_number
        
    def validate_form(self, data: Dict[str, Any]) -> tuple[bool, str]:
        """
        Validate booking form data
        Returns: (is_valid, error_message)
        """
        required_fields = ['name', 'phone', 'address', 'garment_type']
        
        for field in required_fields:
            if not data.get(field) or not str(data[field]).strip():
                return False, f"{field.replace('_', ' ').title()} is required"
        
        # Validate phone number (Indian format)
        phone = str(data['phone']).strip()
        phone_digits = ''.join(filter(str.isdigit, phone))
        
        if len(phone_digits) < 10:
            return False, "Phone number must have at least 10 digits"
        
        if len(phone_digits) > 10:
            # Remove country code if present
            if phone_digits.startswith('91') and len(phone_digits) == 12:
                phone_digits = phone_digits[2:]
            else:
                return False, "Invalid phone number format"
        
        # Check if phone starts with valid digit (6-9)
        if phone_digits[0] not in '6789':
            return False, "Phone number must start with 6, 7, 8, or 9"
        
        return True, ""
    
    def format_whatsapp_message(self, data: Dict[str, Any]) -> str:
        """
        Format form data into a WhatsApp message
        """
        now = datetime.now().strftime("%d/%m/%Y, %I:%M:%S %p")
        
        message = f"""*New Booking - Rudransh Tailoring*
*Date:* {now}

*Customer Details:*
👤 Name: {data.get('name', 'N/A')}
📞 Phone: {data.get('phone', 'N/A')}
🏠 Address: {data.get('address', 'N/A')}
📧 Email: {data.get('email', 'Not provided')}

*Order Details:*
👗 Garment Type: {data.get('garment_type', 'N/A')}
✂️ Style/Design: {data.get('style', 'Not specified')}
📏 Measurements:
"""
        
        # Add measurements if provided
        measurements = [
            ('Bust', data.get('bust')),
            ('Waist', data.get('waist')),
            ('Hip', data.get('hip')),
            ('Shoulder', data.get('shoulder')),
            ('Arm Length', data.get('arm_length')),
            ('Garment Length', data.get('garment_length')),
            ('Sleeve Length', data.get('sleeve_length')),
            ('Neck Depth', data.get('neck_depth')),
        ]
        
        for label, value in measurements:
            if value:
                message += f"   • {label}: {value} inches\n"
        
        if not any(v for _, v in measurements):
            message += "   • No measurements provided\n"
        
        # Additional information
        message += f"""
*Additional Info:*
📝 Special Instructions: {data.get('instructions', 'None')}
📅 Preferred Delivery: {data.get('delivery_date', 'Not specified')}

Thank you for choosing Rudransh Tailoring! 🙏
Please confirm my booking."""
        
        return message
    
    def generate_whatsapp_url(self, data: Dict[str, Any]) -> str:
        """
        Generate WhatsApp URL with pre-filled message
        """
        message = self.format_whatsapp_message(data)
        encoded_message = urllib.parse.quote(message)
        return f"https://wa.me/{self.whatsapp_number}?text={encoded_message}"
    
    def process_booking(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a complete booking
        Returns: {
            'success': bool,
            'error': str (if failed),
            'whatsapp_url': str (if success),
            'message': str (formatted message)
        }
        """
        # Validate form
        is_valid, error = self.validate_form(data)
        if not is_valid:
            return {
                'success': False,
                'error': error,
                'whatsapp_url': None,
                'message': None
            }
        
        # Clean phone number
        phone = str(data['phone']).strip()
        phone_digits = ''.join(filter(str.isdigit, phone))
        if len(phone_digits) == 12 and phone_digits.startswith('91'):
            phone_digits = phone_digits[2:]
        data['phone'] = phone_digits
        
        # Generate WhatsApp URL and message
        whatsapp_url = self.generate_whatsapp_url(data)
        message = self.format_whatsapp_message(data)
        
        return {
            'success': True,
            'error': None,
            'whatsapp_url': whatsapp_url,
            'message': message
        }
    
    def save_booking_to_json(self, data: Dict[str, Any], filename: str = "bookings.json") -> bool:
        """
        Save booking data to a JSON file for record keeping
        """
        try:
            # Add timestamp
            data['submitted_at'] = datetime.now().isoformat()
            data['status'] = 'pending'
            
            # Load existing bookings
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    bookings = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                bookings = []
            
            # Add new booking
            bookings.append(data)
            
            # Save back to file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(bookings, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving booking: {e}")
            return False


# For direct testing
if __name__ == "__main__":
    processor = FormProcessor()
    
    # Test data
    test_data = {
        'name': 'Priya Sharma',
        'phone': '9876543210',
        'email': 'priya@example.com',
        'address': '123 Main Street, Mumbai',
        'garment_type': 'Blouse',
        'style': 'Princess Cut',
        'bust': '36',
        'waist': '30',
        'hip': '38',
        'shoulder': '14',
        'arm_length': '22',
        'garment_length': '24',
        'sleeve_length': '6',
        'neck_depth': '8',
        'instructions': 'Need urgently for event',
        'delivery_date': '2026-02-20'
    }
    
    result = processor.process_booking(test_data)
    
    if result['success']:
        print("✅ Booking processed successfully!")
        print(f"\nWhatsApp URL:\n{result['whatsapp_url']}")
        print(f"\nMessage Preview:\n{result['message']}")
    else:
        print(f"❌ Error: {result['error']}")
