import os

API_ID = API_ID = 20945078

API_HASH = os.environ.get("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7378826796))

LOG = -1002352077049

try:
    ADMINS=[]
    #auth_users id - 1234736828 1375282662
    for x in (os.environ.get("ADMINS", "7378826796").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
