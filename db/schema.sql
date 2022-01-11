CREATE DATABASE salaries;
\c salaries;

CREATE TABLE titles(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE technologies(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE salaries(
    id SERIAL PRIMARY KEY,
    english_level VARCHAR NOT NULL,
    average INTEGER NOT NULL,
    top INTEGER NOT NULL,
    bottom INTEGER NOT NULL,
    is_remote BOOLEAN DEFAULT FALSE,
    location VARCHAR,
    seniority SMALLINT NOT NULL,
    title_id INTEGER NOT NULL,
    FOREIGN KEY (title_id) REFERENCES titles ON DELETE CASCADE
);

CREATE TABLE salaries_technologies(
    salary_id INTEGER NOT NULL,
    technology_id INTEGER NOT NULL,
    PRIMARY KEY (salary_id, technology_id),
    FOREIGN KEY (salary_id) REFERENCES salaries ON DELETE CASCADE,
    FOREIGN KEY (technology_id) REFERENCES technologies ON DELETE CASCADE
);
