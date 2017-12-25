CREATE TABLE "User" (
  id  VARCHAR(100) PRIMARY KEY,
  username VARCHAR(30) UNIQUE,
  email VARCHAR(30) UNIQUE,
  password VARCHAR(250),
  is_admin BOOLEAN
);
