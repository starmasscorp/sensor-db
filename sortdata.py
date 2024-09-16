import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# Create a new table
c.execute('''
CREATE TABLE IF NOT EXISTS sensor_readings (
    channel_no INTEGER,
    sensor_id TEXT,
    reading REAL,
    temperature REAL,
    remarks TEXT
)
''')

# Data extracted from your image
data = [
    (701, 'BSM-301', 5682.6, 26.9, 'CH11x'),
    (702, 'CSM-302', 5655.3, 26.2, None),
    (703, 'CSM-303', 5078.5, 26.3, None),
    # Add other entries similarly...
    (717, 'MSM-304', 5206.8, 23.2, None)
]

# Insert data into the table
c.executemany('INSERT INTO sensor_readings (channel_no, sensor_id, reading, temperature, remarks) VALUES (?, ?, ?, ?, ?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()
