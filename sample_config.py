import os


class Config(object):
    BOT_TOKEN = "5483813124:AAEPqJcVjFq3h7NG7rrcsGYPtGJKeDdAiE0"
    API_ID = "9501538"
   
    API_HASH = "adb8864f52095ff4ca53e847a9250dac"
    
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5483813124:AAEPqJcVjFq3h7NG7rrcsGYPtGJKeDdAiE0")

    APP_ID = int(os.environ.get("APP_ID", "9501538")

    API_HASH = os.environ.get("API_HASH", "adb8864f52095ff4ca53e847a9250dac")
