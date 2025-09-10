import os
import uuid
from datetime import datetime
from pathlib import Path
from mimetypes import guess_extension

# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {
    # Images
    'image/png': '.png',
    'image/jpeg': '.jpg',
    'image/jpg': '.jpg',
    'image/gif': '.gif',
    # Documents
    'application/pdf': '.pdf',
    'application/msword': '.doc',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',
    'application/vnd.ms-excel': '.xls',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': '.xlsx',
    'text/plain': '.txt',
}

# Maximum file sizes (in bytes)
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB for images
MAX_DOCUMENT_SIZE = 10 * 1024 * 1024  # 10MB for documents

# Base upload directories (relative to the project root)
UPLOAD_FOLDERS = {
    'images': 'static/uploads/images',
    'documents': 'static/uploads/documents',
    'resumes': 'static/uploads/resumes',
    'avatars': 'static/uploads/avatars',
}

# Create upload directories if they don't exist
for folder in UPLOAD_FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

def is_allowed_file(file_type: str, category: str) -> bool:
    """Check if the file type is allowed for the given category."""
    if category == 'image':
        return file_type.startswith('image/')
    elif category == 'document':
        return file_type.startswith('application/') or file_type == 'text/plain'
    return False

def generate_unique_filename(file_type: str, original_filename: str = '') -> str:
    """Generate a unique filename with the correct extension."""
    # Try to get extension from file type first
    extension = ALLOWED_EXTENSIONS.get(file_type)
    
    # If no extension from file type, try to get from original filename
    if not extension and original_filename:
        extension = os.path.splitext(original_filename)[1].lower()
    
    # If still no extension, use a default
    if not extension:
        extension = guess_extension(file_type) or '.bin'
        # Fix common extensions
        if extension == '.jpe' or extension == '.jpeg':
            extension = '.jpg'
    
    # Generate a unique filename with timestamp and UUID
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4().hex)[:8]
    
    return f"{timestamp}_{unique_id}{extension}"

def save_uploaded_file(file, file_category: str = 'images') -> str:
    """
    Save an uploaded file to the server.
    
    Args:
        file: The file object from the upload
        file_category: The category of the file ('images', 'documents', 'resumes', 'avatars')
        
    Returns:
        str: The path to the saved file relative to the project root
    """
    try:
        # Determine the file type and validate
        file_type = file.type.lower()
        
        # Set max size based on file category
        max_size = MAX_IMAGE_SIZE if file_category in ['images', 'avatars'] else MAX_DOCUMENT_SIZE
        
        # Check file type
        if not is_allowed_file(file_type, 'image' if file_category in ['images', 'avatars'] else 'document'):
            raise ValueError(f"File type {file_type} not allowed for {file_category}")
        
        # Check file size
        if file.size > max_size:
            raise ValueError(f"File size exceeds maximum allowed size of {max_size/1024/1024}MB")
        
        # Generate a unique filename
        filename = generate_unique_filename(file_type, file.filename)
        
        # Get the upload directory for the file category
        upload_dir = UPLOAD_FOLDERS.get(file_category, UPLOAD_FOLDERS['images'])
        
        # Ensure the directory exists
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save the file
        file_path = os.path.join(upload_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(file.read())
        
        # Return the relative path
        return os.path.join(upload_dir, filename).replace('\\', '/')
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return None

def delete_file(file_path: str) -> bool:
    """
    Delete a file from the server.
    
    Args:
        file_path: Path to the file to delete (relative to project root or absolute)
        
    Returns:
        bool: True if the file was deleted or didn't exist, False otherwise
    """
    try:
        # Convert to absolute path if it's relative
        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)
        
        # Check if the file is within one of our upload directories
        is_in_upload_dir = False
        for folder in UPLOAD_FOLDERS.values():
            abs_folder = os.path.abspath(folder)
            if os.path.commonpath([abs_folder]) == os.path.commonpath([abs_folder, os.path.abspath(file_path)]):
                is_in_upload_dir = True
                break
        
        # Only allow deleting files within our upload directories
        if not is_in_upload_dir:
            print(f"Security: Attempted to delete file outside upload directory: {file_path}")
            return False
        
        # Delete the file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        return True
    except Exception as e:
        print(f"Error deleting file {file_path}: {str(e)}")
        return False
