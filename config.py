import os
import secrets

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, 'encle.db')}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask Secret Key (세션, 플래시 메시지 등에 필요)
SECRET_KEY = secrets.token_hex(32)