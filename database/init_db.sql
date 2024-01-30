-- Создание базы данных
CREATE DATABASE counter_db;

-- Подключение к базе данных
\c counter_db

-- Создание таблицы
CREATE TABLE counter_table (
  id SERIAL PRIMARY KEY,
  count INT NOT NULL
);