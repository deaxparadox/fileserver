import os
import uvicorn


# fastapi app
from main import app


# SERVER CONFIGURATIONS

# Reload and worker configurations.
# 
# Rreload will not work with multiple workers, so
# set enable --reload=true with --workers=1 only.
# 
RELOAD = False
WORKERS = os.getenv("WORKERS")
if not WORKERS:
    WORKERS = 1
    RELOAD = True
else:
    WORKERS = int(WORKERS)


# PORT configuration
# 
PORT = os.getenv("PORT")
if not PORT:
    PORT = 9000
else:
    PORT = int(PORT)


# DOCKER CONFIGURATION
# 
DOCKER = os.getenv("DOCKER")
if DOCKER:
    HOST = os.getenv("HOST")

def main():
    if DOCKER:
        uvicorn.run(
            "main:app",
            port=PORT,
            workers=WORKERS,
            host=HOST
        )
    else:    
        uvicorn.run(
            "main:app",
            port=PORT,
            reload=RELOAD,
            workers=WORKERS,
        )
    
if __name__ == "__main__":
    main()