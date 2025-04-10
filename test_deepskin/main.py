import uvicorn

from api.my_env import my_env

import os
import uvicorn

def main():
    """Launch the FastAPI application through ASGI Uvicorn"""
    port = int(os.environ.get("PORT", 8000))  # Render attribue ce port dynamiquement
    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=port
    )

if __name__ == '__main__':
    main()
