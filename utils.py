import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from google.colab import drive
from google.colab import files
from oauth2client.client import GoogleCredentials
import zipfile


def my_auth():
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive_ = GoogleDrive(gauth)
    drive.mount(PATH,force_remount=True)
    return drive_
def upload_data():
  # 1. Authenticate and create the PyDrive client.
  drive_=my_auth()
  # 2. upload kaggle.json if it doesn't exist    
  if not os.path.exists('./kaggle.json'):
    files.upload()
  if not os.path.exists('./dataset_itr2'):
    !mkdir -p ~/.kaggle
    !cp kaggle.json ~/.kaggle/
    !ls ~/.kaggle
    !chmod 600 /root/.kaggle/kaggle.json  # set permission
    #3.download dataset from kaggle.com
    !kaggle datasets download -d saroz014/plant-diseases
  with zipfile.ZipFile("plant-diseases.zip") as zip_file:
              zip_file.extractall(os.getcwd())
  print("finished !")

def delete_ugly():
  i=0
  listdirs=os.listdir('./dataset_itr2/test')
  for dirpath,_,filenames in os.walk('./dataset_itr2/test'):
    for f in filenames:
      try:
        img=Image.open(os.path.abspath(os.path.join(dirpath, f)))
      except OSError:
        ++i
        os.remove(os.path.abspath(os.path.join(dirpath, f)))
  print("{} ugly files deleted from test".format(i))

