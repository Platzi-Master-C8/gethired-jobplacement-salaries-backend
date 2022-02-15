import os


MOCK_DATA = True if os.environ.get("MOCK_DATA") else False
DB_HOST = os.environ.get("DB_HOST", "db")
DB_DATABASE = os.environ.get("DB_DATABASE", "salaries")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
