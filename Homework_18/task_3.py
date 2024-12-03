from contextlib import contextmanager

@contextmanager
def database_connection():
    start = print("Opening database connection...")
    yield
    end = print("Closing database connection...")
    
    
with database_connection():
    print("Performing database operations...")