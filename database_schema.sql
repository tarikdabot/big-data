-- Create table for the processed e-commerce data
CREATE TABLE ecommerce_data (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP NOT NULL,
    event_type VARCHAR(50),
    product_id INT,
    category_id INT,
    category_code VARCHAR(50),
    brand VARCHAR(50),
    price NUMERIC,
    user_id INT,
    user_session VARCHAR(50),
    sentiment_score NUMERIC
);

-- Optionally, create indexes for performance optimization
CREATE INDEX idx_event_time ON ecommerce_data(event_time);
CREATE INDEX idx_user_id ON ecommerce_data(user_id);
