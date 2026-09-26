CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    join_date DATETIME
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT,
    title VARCHAR(150),
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users VALUES (1, 'Alice Johnson', 'alice@example.com', '2026-09-01 10:00:00');
INSERT INTO users VALUES (2, 'Ben Smith', 'ben@example.com', '2026-09-02 11:00:00');
INSERT INTO users VALUES (3, 'Carla Davis', 'carla@example.com', '2026-09-03 12:00:00');
INSERT INTO users VALUES (4, 'Daniel Lee', 'daniel@example.com', '2026-09-04 13:00:00');
INSERT INTO users VALUES (5, 'Emma Wilson', 'emma@example.com', '2026-09-05 14:00:00');
INSERT INTO users VALUES (6, 'Frank Brown', 'frank@example.com', '2026-09-06 15:00:00');
INSERT INTO users VALUES (7, 'Grace Miller', 'grace@example.com', '2026-09-07 16:00:00');
INSERT INTO users VALUES (8, 'Henry Taylor', 'henry@example.com', '2026-09-08 17:00:00');
INSERT INTO users VALUES (9, 'Isabella Moore', 'isabella@example.com', '2026-09-09 18:00:00');
INSERT INTO users VALUES (10, 'Jack Anderson', 'jack@example.com', '2026-09-10 19:00:00');

INSERT INTO posts VALUES (1, 1, 'First Post', 'This is Alice''s first post.');
INSERT INTO posts VALUES (2, 2, 'Hello World', 'Ben is sharing his first post.');
INSERT INTO posts VALUES (3, 3, 'Data Science', 'Carla is learning about data science.');
INSERT INTO posts VALUES (4, 1, 'Another Post', 'Alice is writing another post.');
INSERT INTO posts VALUES (5, 4, 'SQL Practice', 'Daniel is practicing SQL.');
INSERT INTO posts VALUES (6, 5, 'College Life', 'Emma is writing about college life.');
INSERT INTO posts VALUES (7, 6, 'Python Tips', 'Frank is sharing some Python tips.');
INSERT INTO posts VALUES (8, 7, 'My Project', 'Grace is working on a new project.');
INSERT INTO posts VALUES (9, 8, 'Database Basics', 'Henry is learning about databases.');
INSERT INTO posts VALUES (10, 9, 'Final Post', 'Isabella is sharing her latest post.');
