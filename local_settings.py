
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "44c28db6-1c0c-432a-9b22-daeef7b93716608eaa37-f79e-475d-9a1e-88099e9b18a11f709b01-5a9d-4633-86ef-42a21923931d"
NEVERCACHE_KEY = "d203c531-d727-4282-a095-9c3a43c52f9e4a965d5c-80d7-424c-974b-d01812956611edf69497-42f7-4ecf-9207-0ee7d7409a9a"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
