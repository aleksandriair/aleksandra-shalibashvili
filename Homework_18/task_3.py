def database_connection():
    print("Opening database connection...")
    yield
    print("Closing database connection...")

# Example usage
with database_connection():
    print("Performing database operations...")