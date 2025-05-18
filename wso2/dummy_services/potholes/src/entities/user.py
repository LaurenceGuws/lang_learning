from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db

@dataclass
class User:
    name: str
    email: str
    id: Optional[int] = None
    role: str = "citizen"
    created_at: Optional[datetime] = None
    
    @classmethod
    def from_row(cls, row):
        """Create a User instance from a database row."""
        if not row:
            return None
        return cls(
            id=row['id'],
            name=row['name'],
            email=row['email'],
            role=row['role'],
            created_at=datetime.fromisoformat(row['created_at']) if row['created_at'] else None
        )
    
    @classmethod
    def get_by_id(cls, user_id):
        """Get a user by ID."""
        row = db.get_by_id("users", user_id)
        return cls.from_row(row)
    
    @classmethod
    def get_all(cls):
        """Get all users."""
        rows = db.execute_query("SELECT * FROM users")
        return [cls.from_row(row) for row in rows]
    
    def save(self):
        """Save user to database."""
        if self.id:
            # Update existing user
            query = """
                UPDATE users 
                SET name = ?, email = ?, role = ?
                WHERE id = ?
            """
            db.execute_query(query, (self.name, self.email, self.role, self.id))
            return self.id
        else:
            # Insert new user
            query = """
                INSERT INTO users (name, email, role)
                VALUES (?, ?, ?)
            """
            self.id = db.execute_insert(query, (self.name, self.email, self.role))
            return self.id
            
    def delete(self):
        """Delete user from database."""
        if not self.id:
            return False
        query = "DELETE FROM users WHERE id = ?"
        db.execute_query(query, (self.id,))
        return True
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API responses."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
