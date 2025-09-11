import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """SQLite database manager for job advertisements and images"""
    
    def __init__(self, db_path: str = "advertisement_manager.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        # Jobs table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                employment_type TEXT NOT NULL,
                location TEXT NOT NULL,
                salary_min INTEGER DEFAULT 0,
                salary_max INTEGER DEFAULT 0,
                currency TEXT DEFAULT 'USD',
                posted_by TEXT NOT NULL,
                date_posted TEXT NOT NULL,
                application_deadline TEXT NOT NULL,
                job_status TEXT DEFAULT 'Active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Images table (for job flyers/attachments)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER,
                name TEXT NOT NULL,
                content BLOB,
                content_type TEXT,
                size INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE CASCADE
            )
        """)
        
        # Companies table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                website TEXT,
                logo_image_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (logo_image_id) REFERENCES images (id)
            )
        """)
        
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    
    def add_job(self, job_data: Dict[str, Any]) -> int:
        """Add a new job to the database"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        try:
            cur.execute("""
                INSERT INTO jobs (
                    title, description, category, employment_type, location,
                    salary_min, salary_max, currency, posted_by, date_posted,
                    application_deadline, job_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                job_data.get('title', ''),
                job_data.get('description', ''),
                job_data.get('category', 'Technology'),
                job_data.get('employment_type', 'Full-time'),
                job_data.get('location', ''),
                job_data.get('salary_min', 0),
                job_data.get('salary_max', 0),
                job_data.get('currency', 'USD'),
                job_data.get('posted_by', ''),
                job_data.get('date_posted', datetime.now().strftime('%Y-%m-%d')),
                job_data.get('application_deadline', datetime.now().strftime('%Y-%m-%d')),
                job_data.get('job_status', 'Active')
            ))
            
            job_id = cur.lastrowid
            conn.commit()
            logger.info(f"Job added successfully with ID: {job_id}")
            return job_id
            
        except Exception as e:
            conn.rollback()
            logger.error(f"Error adding job: {e}")
            raise
        finally:
            conn.close()
    
    def get_jobs(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get all jobs from database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dict-like access
        cur = conn.cursor()
        
        try:
            if status:
                cur.execute("SELECT * FROM jobs WHERE job_status = ? ORDER BY created_at DESC", (status,))
            else:
                cur.execute("SELECT * FROM jobs ORDER BY created_at DESC")
            
            jobs = [dict(row) for row in cur.fetchall()]
            logger.info(f"Retrieved {len(jobs)} jobs from database")
            return jobs
            
        except Exception as e:
            logger.error(f"Error retrieving jobs: {e}")
            return []
        finally:
            conn.close()
    
    def get_job_by_id(self, job_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific job by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        try:
            cur.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
            row = cur.fetchone()
            return dict(row) if row else None
            
        except Exception as e:
            logger.error(f"Error retrieving job {job_id}: {e}")
            return None
        finally:
            conn.close()
    
    def update_job(self, job_id: int, job_data: Dict[str, Any]) -> bool:
        """Update an existing job"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        try:
            cur.execute("""
                UPDATE jobs SET
                    title = ?, description = ?, category = ?, employment_type = ?,
                    location = ?, salary_min = ?, salary_max = ?, currency = ?,
                    posted_by = ?, date_posted = ?, application_deadline = ?,
                    job_status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (
                job_data.get('title', ''),
                job_data.get('description', ''),
                job_data.get('category', 'Technology'),
                job_data.get('employment_type', 'Full-time'),
                job_data.get('location', ''),
                job_data.get('salary_min', 0),
                job_data.get('salary_max', 0),
                job_data.get('currency', 'USD'),
                job_data.get('posted_by', ''),
                job_data.get('date_posted', datetime.now().strftime('%Y-%m-%d')),
                job_data.get('application_deadline', datetime.now().strftime('%Y-%m-%d')),
                job_data.get('job_status', 'Active'),
                job_id
            ))
            
            success = cur.rowcount > 0
            conn.commit()
            logger.info(f"Job {job_id} updated successfully: {success}")
            return success
            
        except Exception as e:
            conn.rollback()
            logger.error(f"Error updating job {job_id}: {e}")
            return False
        finally:
            conn.close()
    
    def delete_job(self, job_id: int) -> bool:
        """Delete a job and its associated images"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        try:
            # Delete associated images first
            cur.execute("DELETE FROM images WHERE job_id = ?", (job_id,))
            # Delete the job
            cur.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
            
            success = cur.rowcount > 0
            conn.commit()
            logger.info(f"Job {job_id} deleted successfully: {success}")
            return success
            
        except Exception as e:
            conn.rollback()
            logger.error(f"Error deleting job {job_id}: {e}")
            return False
        finally:
            conn.close()
    
    def save_image(self, job_id: Optional[int], name: str, content: bytes, content_type: str = None) -> int:
        """Save an image to the database"""
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        try:
            cur.execute("""
                INSERT INTO images (job_id, name, content, content_type, size)
                VALUES (?, ?, ?, ?, ?)
            """, (job_id, name, content, content_type, len(content)))
            
            image_id = cur.lastrowid
            conn.commit()
            logger.info(f"Image saved successfully with ID: {image_id}")
            return image_id
            
        except Exception as e:
            conn.rollback()
            logger.error(f"Error saving image: {e}")
            raise
        finally:
            conn.close()
    
    def get_image(self, image_id: int) -> Optional[Dict[str, Any]]:
        """Get an image by ID"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        try:
            cur.execute("SELECT * FROM images WHERE id = ?", (image_id,))
            row = cur.fetchone()
            return dict(row) if row else None
            
        except Exception as e:
            logger.error(f"Error retrieving image {image_id}: {e}")
            return None
        finally:
            conn.close()
    
    def get_job_images(self, job_id: int) -> List[Dict[str, Any]]:
        """Get all images for a specific job"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        try:
            cur.execute("SELECT * FROM images WHERE job_id = ?", (job_id,))
            images = [dict(row) for row in cur.fetchall()]
            return images
            
        except Exception as e:
            logger.error(f"Error retrieving images for job {job_id}: {e}")
            return []
        finally:
            conn.close()

# Create global database instance
db_manager = DatabaseManager()
