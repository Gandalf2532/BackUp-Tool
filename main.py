import datetime as dt
from backup import backupfolder_and_zip

SOURCE = r"Pfad\zur\Quelle"
TARGET = r"Pfad\zum\Zielordner"

current_date = dt.datetime.now()
formatted_date = current_date.strftime("%d.%m-%H.%M")
BACKUP_ZIP_NAME = f"{formatted_date}Uhr.zip"

backupfolder_and_zip(SOURCE, TARGET, BACKUP_ZIP_NAME)