from os import environ 

class Config:
    API_ID = environ.get("API_ID", "32557254")
    API_HASH = environ.get("API_HASH", "448bb61d4711ef33afff691ac1bb0931")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8651739298:AAF244rm6XZrG9zKkILeBp_IcvbMDqhozv0") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
