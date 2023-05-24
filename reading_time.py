import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" Reading Time ",
        message = """Books are windows to new worlds, where imagination 
        takes flight and knowledge finds its voice.""",
        app_icon = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\New\\Reading.ico",
        timeout = 10
    )
    time.sleep(60*60)
    