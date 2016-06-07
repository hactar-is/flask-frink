from flask_frink.connection import RethinkFlask
from flask.ext.security import Security

db = RethinkFlask()
security = Security()
