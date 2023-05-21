import os
from dotenv import load_dotenv, find_dotenv

from dts import create_app

load_dotenv(find_dotenv())

env_name = os.environ.get("DEVELOPMENT_MODE")
app = create_app(env_name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
