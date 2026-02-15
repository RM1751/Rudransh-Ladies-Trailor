"""
Image Manager for Rudransh Tailoring
Handles image uploads, storage, and deletion for gallery
"""

import os
import uuid
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from werkzeug.utils import secure_filename


class ImageManager:
    """Manage gallery images with file system storage"""
    
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    
    # Category mapping with icons
    CATEGORIES = {
        'blouse': {'name': 'Blouse', 'icon': '👔'},
        'kurti': {'name': 'Kurti', 'icon': '👗'},
        'salwar': {'name': 'Salwar Suit', 'icon': '🥻'},
        'lehenga': {'name': 'Lehenga', 'icon': '💃'},
        'gown': {'name': 'Gown', 'icon': '👰'},
        'other': {'name': 'Other', 'icon': '👘'}
    }
    
    def __init__(self, upload_folder: str = "../uploads", metadata_file: str = "image_metadata.json"):
        self.upload_folder = Path(upload_folder)
        self.metadata_file = Path(metadata_file)
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Create necessary directories if they don't exist"""
        self.upload_folder.mkdir(parents=True, exist_ok=True)
        
        # Create category subdirectories
        for category in self.CATEGORIES.keys():
            category_path = self.upload_folder / category
            category_path.mkdir(exist_ok=True)
    
    def allowed_file(self, filename: str) -> bool:
        """Check if file extension is allowed"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
    
    def validate_file(self, file_storage) -> tuple[bool, str]:
        """
        Validate uploaded file
        Returns: (is_valid, error_message)
        """
        if not file_storage or not file_storage.filename:
            return False, "No file provided"
        
        if not self.allowed_file(file_storage.filename):
            return False, f"Invalid file type. Allowed: {', '.join(self.ALLOWED_EXTENSIONS)}"
        
        # Check file size
        file_storage.seek(0, os.SEEK_END)
        file_size = file_storage.tell()
        file_storage.seek(0)
        
        if file_size > self.MAX_FILE_SIZE:
            max_mb = self.MAX_FILE_SIZE / (1024 * 1024)
            return False, f"File too large. Maximum size: {max_mb}MB"
        
        return True, ""
    
    def save_image(self, file_storage, category: str, title: str = "", 
                   description: str = "") -> Dict[str, Any]:
        """
        Save uploaded image to filesystem
        Returns: image metadata dict or error dict
        """
        # Validate category
        if category not in self.CATEGORIES:
            return {'success': False, 'error': f"Invalid category: {category}"}
        
        # Validate file
        is_valid, error = self.validate_file(file_storage)
        if not is_valid:
            return {'success': False, 'error': error}
        
        try:
            # Generate unique filename
            original_filename = secure_filename(file_storage.filename)
            file_ext = original_filename.rsplit('.', 1)[1].lower()
            unique_filename = f"{uuid.uuid4().hex}.{file_ext}"
            
            # Save to category folder
            category_path = self.upload_folder / category
            file_path = category_path / unique_filename
            
            file_storage.save(file_path)
            
            # Create metadata
            image_data = {
                'id': str(uuid.uuid4().hex),
                'title': title or original_filename,
                'description': description,
                'category': category,
                'filename': unique_filename,
                'original_filename': original_filename,
                'file_path': str(file_path),
                'file_size': os.path.getsize(file_path),
                'uploaded_at': datetime.now().isoformat(),
                'url': f"/uploads/{category}/{unique_filename}"
            }
            
            # Save to metadata
            self._save_metadata(image_data)
            
            return {'success': True, 'image': image_data}
            
        except Exception as e:
            return {'success': False, 'error': f"Failed to save image: {str(e)}"}
    
    def delete_image(self, image_id: str) -> Dict[str, Any]:
        """
        Delete image by ID
        Returns: result dict
        """
        try:
            metadata = self._load_metadata()
            
            # Find image
            image = None
            for img in metadata['images']:
                if img['id'] == image_id:
                    image = img
                    break
            
            if not image:
                return {'success': False, 'error': 'Image not found'}
            
            # Delete file
            file_path = Path(image['file_path'])
            if file_path.exists():
                file_path.unlink()
            
            # Remove from metadata
            metadata['images'] = [img for img in metadata['images'] if img['id'] != image_id]
            self._save_metadata_dict(metadata)
            
            return {'success': True, 'message': 'Image deleted successfully'}
            
        except Exception as e:
            return {'success': False, 'error': f"Failed to delete image: {str(e)}"}
    
    def get_images(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get all images, optionally filtered by category
        """
        metadata = self._load_metadata()
        images = metadata.get('images', [])
        
        if category and category != 'all':
            images = [img for img in images if img['category'] == category]
        
        # Sort by upload date (newest first)
        images.sort(key=lambda x: x.get('uploaded_at', ''), reverse=True)
        
        return images
    
    def get_image_by_id(self, image_id: str) -> Optional[Dict[str, Any]]:
        """Get single image by ID"""
        metadata = self._load_metadata()
        for img in metadata.get('images', []):
            if img['id'] == image_id:
                return img
        return None
    
    def get_categories(self) -> Dict[str, Dict[str, str]]:
        """Get all available categories"""
        return self.CATEGORIES
    
    def get_stats(self) -> Dict[str, Any]:
        """Get gallery statistics"""
        metadata = self._load_metadata()
        images = metadata.get('images', [])
        
        stats = {
            'total_images': len(images),
            'total_size': sum(img.get('file_size', 0) for img in images),
            'categories': {}
        }
        
        for category in self.CATEGORIES.keys():
            cat_images = [img for img in images if img['category'] == category]
            stats['categories'][category] = {
                'count': len(cat_images),
                'name': self.CATEGORIES[category]['name']
            }
        
        return stats
    
    def _load_metadata(self) -> Dict[str, Any]:
        """Load image metadata from JSON file"""
        try:
            if self.metadata_file.exists():
                with open(self.metadata_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
        
        return {'images': []}
    
    def _save_metadata(self, image_data: Dict[str, Any]):
        """Add image to metadata file"""
        metadata = self._load_metadata()
        metadata['images'].append(image_data)
        self._save_metadata_dict(metadata)
    
    def _save_metadata_dict(self, metadata: Dict[str, Any]):
        """Save metadata dict to JSON file"""
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)


# For direct testing
if __name__ == "__main__":
    manager = ImageManager()
    
    print("Image Manager Test")
    print("=" * 40)
    print(f"\nUpload folder: {manager.upload_folder.absolute()}")
    print(f"Metadata file: {manager.metadata_file}")
    print(f"\nAllowed extensions: {manager.ALLOWED_EXTENSIONS}")
    print(f"Max file size: {manager.MAX_FILE_SIZE / (1024*1024)}MB")
    
    print("\nCategories:")
    for key, value in manager.get_categories().items():
        print(f"  {value['icon']} {key}: {value['name']}")
    
    print("\nCurrent Stats:")
    stats = manager.get_stats()
    print(f"  Total images: {stats['total_images']}")
    print(f"  Total size: {stats['total_size'] / 1024:.2f} KB")
