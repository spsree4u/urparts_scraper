
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# DB
DB_PATH = str(BASE_DIR / "db.sqlite3")

# URLs
BASE_URL = "https://www.urparts.com/index.cfm/page/catalogue/"
