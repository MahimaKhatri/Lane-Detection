from app import app

# Checks if the run.py is executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True)