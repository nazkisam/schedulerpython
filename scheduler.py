import os
import shutil
import datetime
import schedule
import time


source_dir = r"C:\Users\DELL\Pictures\Camera Roll"
destination_dir = r"C:\Users\DELL\Pictures\Saved Pictures"

def copy_folder_to_directory(source,dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest,str(today))
  "Backups/11-23-2023"
   
  try:
    shutil.copytree(source, dest_dir)
    print(f'Folder copied to:{dest_dir}')
  except FileExistsError:
    print(f'Folder exists in {dest}')

schedule.every().day.at("17:49").do(lambda: copy_folder_to_directory(source_dir,destination_dir))

while True:
  schedule.run_pending()
  time.sleep(60)

   
