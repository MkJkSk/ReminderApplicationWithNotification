import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
        title =" Drinking Water ",
        message = """Drinking water is essential to a healthy lifestyle""",
        app_icon = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\New\\Water.ico",
        timeout = 10
    )
    time.sleep(60*60)