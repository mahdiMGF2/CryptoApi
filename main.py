import uvicorn
import os,dotenv

env_path = os.path.join(os.path.dirname(__file__), "app", ".env")
dotenv.load_dotenv(dotenv_path=env_path)


if __name__ == "__main__":
    uvicorn.run('app.config:app', host=os.getenv('Host'), port=int(os.getenv('Port')), reload=True)