"""
Flask Backend Server for Rudransh Tailoring
Provides API endpoints for booking form and image management
"""

import os
import sys
from datetime import datetime
from functools import wraps

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import RequestEntityTooLarge
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our modules
from form_processor import FormProcessor
from image_manager import ImageManager

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file upload

# Enable CORS for frontend access
CORS(app, resources={
    r"/api/*": {
        "origins": ["*"],
        "methods": ["GET", "POST", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Initialize managers
form_processor = FormProcessor(whatsapp_number=os.getenv('WHATSAPP_NUMBER', '918840586403'))
image_manager = ImageManager(
    upload_folder=os.getenv('UPLOAD_FOLDER', '../uploads'),
    metadata_file='image_metadata.json'
)

# Admin password from env
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Ravi@12345')


# ============== Helper Functions ==============

def require_auth(f):
    """Decorator to require admin authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'success': False, 'error': 'Authorization required'}), 401
        
        # Simple password check (in production, use proper JWT)
        if auth_header != f'Bearer {ADMIN_PASSWORD}':
            return jsonify({'success': False, 'error': 'Invalid credentials'}), 403
        
        return f(*args, **kwargs)
    return decorated


# ============== API Routes ==============

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Rudransh Tailoring API'
    })


# ============== Booking Routes ==============

@app.route('/api/booking/submit', methods=['POST'])
def submit_booking():
    """
    Submit a new booking
    POST /api/booking/submit
    Body: JSON with booking form data
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        # Process booking
        result = form_processor.process_booking(data)
        
        if result['success']:
            # Save to JSON file for records
            form_processor.save_booking_to_json(data)
            
            return jsonify({
                'success': True,
                'whatsapp_url': result['whatsapp_url'],
                'message': 'Booking processed successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': result['error']
            }), 400
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/booking/validate', methods=['POST'])
def validate_booking():
    """
    Validate booking form without submitting
    POST /api/booking/validate
    Body: JSON with booking form data
    """
    try:
        data = request.get_json()
        is_valid, error = form_processor.validate_form(data)
        
        return jsonify({
            'valid': is_valid,
            'error': error if not is_valid else None
        })
        
    except Exception as e:
        return jsonify({'valid': False, 'error': str(e)}), 500


@app.route('/api/booking/preview', methods=['POST'])
def preview_message():
    """
    Get WhatsApp message preview
    POST /api/booking/preview
    Body: JSON with booking form data
    """
    try:
        data = request.get_json()
        message = form_processor.format_whatsapp_message(data)
        
        return jsonify({
            'success': True,
            'message': message
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# ============== Gallery/Image Routes ==============

@app.route('/api/gallery/images', methods=['GET'])
def get_images():
    """
    Get all gallery images
    GET /api/gallery/images?category=all
    """
    try:
        category = request.args.get('category', 'all')
        images = image_manager.get_images(category)
        
        return jsonify({
            'success': True,
            'images': images,
            'count': len(images)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/gallery/upload', methods=['POST'])
# @require_auth  # Uncomment for production
def upload_image():
    """
    Upload new image to gallery
    POST /api/gallery/upload
    Form data: image (file), category, title, description
    """
    try:
        # Check if file is present
        if 'image' not in request.files:
            return jsonify({'success': False, 'error': 'No image file provided'}), 400
        
        file = request.files['image']
        category = request.form.get('category', 'other')
        title = request.form.get('title', '')
        description = request.form.get('description', '')
        
        # Save image
        result = image_manager.save_image(file, category, title, description)
        
        if result['success']:
            return jsonify({
                'success': True,
                'image': result['image'],
                'message': 'Image uploaded successfully'
            })
        else:
            return jsonify({'success': False, 'error': result['error']}), 400
            
    except RequestEntityTooLarge:
        return jsonify({'success': False, 'error': 'File too large (max 5MB)'}), 413
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/gallery/delete/<image_id>', methods=['DELETE'])
# @require_auth  # Uncomment for production
def delete_image(image_id):
    """
    Delete image by ID
    DELETE /api/gallery/delete/<image_id>
    """
    try:
        result = image_manager.delete_image(image_id)
        
        if result['success']:
            return jsonify(result)
        else:
            return jsonify(result), 404
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/gallery/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    return jsonify({
        'success': True,
        'categories': image_manager.get_categories()
    })


@app.route('/api/gallery/stats', methods=['GET'])
def get_stats():
    """Get gallery statistics"""
    return jsonify({
        'success': True,
        'stats': image_manager.get_stats()
    })


# ============== WhatsApp Routes ==============

@app.route('/api/whatsapp/link', methods=['GET'])
def get_whatsapp_link():
    """Get WhatsApp contact link"""
    return jsonify({
        'success': True,
        'link': os.getenv('WHATSAPP_LINK', 'https://wa.me/918840586403'),
        'number': os.getenv('WHATSAPP_NUMBER', '918840586403')
    })


# ============== Static File Serving ==============

@app.route('/uploads/<path:filename>')
def serve_upload(filename):
    """Serve uploaded images"""
    upload_folder = os.getenv('UPLOAD_FOLDER', '../uploads')
    return send_from_directory(upload_folder, filename)


# ============== Error Handlers ==============

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


@app.errorhandler(RequestEntityTooLarge)
def too_large(error):
    return jsonify({'success': False, 'error': 'File too large (max 5MB)'}), 413


# ============== Main Entry Point ==============

if __name__ == '__main__':
    print("=" * 50)
    print("🧵 Rudransh Tailoring - Flask Backend Server")
    print("=" * 50)
    print(f"\nEnvironment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"Debug mode: {os.getenv('FLASK_DEBUG', 'True')}")
    print(f"\nAvailable endpoints:")
    print(f"  Health:    http://127.0.0.1:5000/api/health")
    print(f"  Booking:   http://127.0.0.1:5000/api/booking/submit")
    print(f"  Gallery:   http://127.0.0.1:5000/api/gallery/images")
    print(f"  WhatsApp:  http://127.0.0.1:5000/api/whatsapp/link")
    print("\n" + "=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    )
