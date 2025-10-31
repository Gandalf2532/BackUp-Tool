import datetime as dt
from backup import backupfolder_and_zip
from time import sleep

#0: einaml
#1: alle x sekunden

ART_DES_AUSFUEHRENS = 0 
TIME_TO_SLEEP = 600

SOURCE = r"Pfad\zur\Quelle"
TARGET = r"Pfad\zum\Zielordner"

current_date = dt.datetime.now()
formatted_date = current_date.strftime("%d.%m-%H.%M")
BACKUP_ZIP_NAME = f"{formatted_date}Uhr.zip"

match ART_DES_AUSFUEHRENS:
    case 0: 
        backupfolder_and_zip(SOURCE, TARGET, BACKUP_ZIP_NAME)
    case 1:
        while True:
            backupfolder_and_zip(SOURCE, TARGET, BACKUP_ZIP_NAME)
            sleep(TIME_TO_SLEEP)
    case _:
        print("Valide ART_DES_AUSFUEHRENS angeben!")