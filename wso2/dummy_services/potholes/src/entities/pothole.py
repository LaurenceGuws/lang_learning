from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any, List
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db
from entities.user import User

@dataclass
class Pothole:
    street_name: str
    reported_by: int
    id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    diameter_cm: Optional[float] = None
    description: Optional[str] = None
    status: str = "open"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_row(cls, row):
        """Create a Pothole instance from a database row."""
        if not row:
            return None
            
        return cls(
            id=row['id'],
            reported_by=row['reported_by'],
            street_name=row['street_name'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            diameter_cm=row['diameter_cm'],
            description=row['description'],
            status=row['status'],
            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else None,
            updated_at=datetime.fromisoformat(row['updated_at']) if row['updated_at'] else None
        )
    
    @classmethod
    def get_by_id(cls, pothole_id):
        """Get a pothole by ID."""
        row = db.get_by_id("potholes", pothole_id)
        return cls.from_row(row)
    
    @classmethod
    def get_all(cls):
        """Get all potholes."""
        rows = db.execute_query("SELECT * FROM potholes")
        return [cls.from_row(row) for row in rows]
    
    @classmethod
    def get_by_status(cls, status):
        """Get potholes by status."""
        query = "SELECT * FROM potholes WHERE status = ?"
        rows = db.execute_query(query, (status,))
        return [cls.from_row(row) for row in rows]
    
    @classmethod
    def get_by_reporter(cls, user_id):
        """Get potholes reported by a specific user."""
        query = "SELECT * FROM potholes WHERE reported_by = ?"
        rows = db.execute_query(query, (user_id,))
        return [cls.from_row(row) for row in rows]
    
    def save(self):
        """Save pothole to database."""
        now = datetime.now().isoformat()
        
        if self.id:
            # Update existing pothole
            query = """
                UPDATE potholes 
                SET street_name = ?, reported_by = ?, latitude = ?, 
                    longitude = ?, diameter_cm = ?, description = ?, 
                    status = ?, updated_at = ?
                WHERE id = ?
            """
            params = (
                self.street_name, self.reported_by, self.latitude,
                self.longitude, self.diameter_cm, self.description,
                self.status, now, self.id
            )
            db.execute_query(query, params)
            return self.id
        else:
            # Insert new pothole
            query = """
                INSERT INTO potholes (
                    street_name, reported_by, latitude, longitude,
                    diameter_cm, description, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            params = (
                self.street_name, self.reported_by, self.latitude,
                self.longitude, self.diameter_cm, self.description,
                self.status
            )
            self.id = db.execute_insert(query, params)
            return self.id
            
    def delete(self):
        """Delete pothole from database."""
        if not self.id:
            return False
        query = "DELETE FROM potholes WHERE id = ?"
        db.execute_query(query, (self.id,))
        return True
    
    def get_reporter(self):
        """Get the user who reported this pothole."""
        return User.get_by_id(self.reported_by)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "street_name": self.street_name,
            "reported_by": self.reported_by,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "diameter_cm": self.diameter_cm,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
