CREATE TABLE IF NOT EXISTS powers (
    id SERIAL PRIMARY KEY,
    sender_phone VARCHAR(20),
    recipient_name TEXT,
    recipient_phone VARCHAR(20),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
