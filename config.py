from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = os.getenv("SESSION_NAME", "session")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
