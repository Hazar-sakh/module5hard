import time

class User:
  def __init__(self, nickname, password, age):
    self.nickname = str()
    self.password = str()
    self.age = int(0)






class Video:
  def __init__(self, title, duration, time_now, adult_mode):
    self.title = str(None)
    self.duration = int(0)
    self.time_now = int(0)
    self.adult_mode = bool(False)






class UrTube:
  def __init__(self, users, videos, current_user):
    self.users = []
    self.videos = []
    self.current_user = None

  def __log_in__(self, nickname, password):
    for i in self.users:
      if i.nickname == nickname and i.password == password:
        self.current_user = i
      else:
        self.current_user = None

  def __register__(self, nickname, password, age):
    if nickname.User not in self.users:
      self.users.append(User(nickname, password, age))
    else:
      print(f'Пользователь с никнеймом {nickname} уже существует')

  def __log_out__(self):
    self.current_user = None

  def __add__(self, title, duration, time_now, adult_mode):
    for i in self.videos:
      i.title = i.title.lower()
      if i.title == title.Video.lower():
        print(f'Видео с названием {title} уже существует')
        return
      else:
        self.videos.append(Video(title, duration, time_now, adult_mode))

  def __get_videos__(self, title):
    listOfVideos = []
    for i in self.videos:
      if i.title.lower() == title.lower():
        listOfVideos.append(i)
    return listOfVideos
    
  def __watch_video__(self, title):
    if self.current_user != None:
      for i in self.videos:
        if i.title == title:
          if (i.adult_mode == True and self.current_user.age >= 18) or (i.adult_mode == False):
            timeline = []
            for i in timeline:
              if i != duration.Video:
                timeline.append(i)
            for i in timeline:
              if i != duration.Video:
                print(i)
                time.sleep(1)
                return
             
  
          else:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
          return
    else:
      print('Войдите в аккаунт, чтобы смотреть видео')    
