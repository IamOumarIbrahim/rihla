# Paste this whole file into your PythonAnywhere WSGI configuration file
# (Web tab > Code > WSGI configuration file), replacing what is there.
# That file lives outside your git repository, so your secrets never go to GitHub.
import os
import sys

# 1. Change these four values
USERNAME = "yourusername"
os.environ["SECRET_KEY"] = "CHANGE-ME"
os.environ["ADMIN_EMAIL"] = "you@example.com"
os.environ["ADMIN_PASSWORD"] = "CHANGE-ME"

# 2. Leave the rest as it is
os.environ["RIHLA_ENV"] = "production"

backend = "/home/" + USERNAME + "/rihla/backend"
if backend not in sys.path:
    sys.path.insert(0, backend)

from app import app as application  # noqa: E402