#!/bin/bash
rm -f pothole.db
sqlite3 pothole.db < schema.sql
echo "SQLite database created."

