CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(50),
    temperature NUMERIC(5, 2),
    humidity NUMERIC(5, 2),
    air_quality NUMERIC(5, 2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);