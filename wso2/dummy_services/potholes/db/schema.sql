-- users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT DEFAULT 'citizen',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- potholes table
CREATE TABLE potholes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reported_by INTEGER NOT NULL,
    street_name TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    diameter_cm REAL,
    description TEXT,
    status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(reported_by) REFERENCES users(id)
);
