import os
from app import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

@app.route('/')
def home():
    return "It Works"

if __name__ == '__main__': app.run(debug=True)
