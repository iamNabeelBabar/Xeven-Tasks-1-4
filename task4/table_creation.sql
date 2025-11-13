
CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);


CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customers(customer_id),
  product_name VARCHAR(100),
  amount DECIMAL(10,2)
);

