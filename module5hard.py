import time

class User:
  """
  Создаем класс User и определяем его атрибуты, а также определяем спец.методы для класса:
  __init__ - конструктор класса, вызывается при создании
  __eq__ - для сравнения никнеймов
  __str__ - для вывода названия в виде строки
  
  """

  def __init__(self, nickname: str, password: int, age: int):
    self.nickname = nickname
    self.password = password
    self.age = age

  def __eq__(self, other):
    return self.nickname == other.nickname


class Video:
  """
  Создаем класс Video и определяем его атрибуты, а также определяем спец.методы для класса:
  __init__ - конструктор класса, вызывается при создании
  __eq__ - для сравнения названий видео
  __containse__ - для упрощения поиска названия видео в списке

  """
  def __init__(self, title: str, duration: int, adult_mode = bool(False)):
    self.title = title
    self.duration = duration
    self.time_now = 0
    self.adult_mode = adult_mode
    
  def __eq__(self, other):
    return self.title == other.title

  def __contains__(self, other):
    return self.title in other.title


class UrTube:
  """
  Создаем класс UrTube и определяем его атрибуты - списки (users, videos, current_user), а также определяем спец.метод для класса и функции:
  __init__ - конструктор класса, вызывается при создании
  log_in - для "входа" пользователя (сравнение имени и пароля с имющимся в списке)
  register - для регистрации нового пользователя (внесение в список users)
  log_ot - для "выхода" пользователя (current_user = None)
  add - для добавления видео в список videos
  get_videos - для вывода списка видео
  watch_video - для просмотра видео (отсчет времени просмотра)

  """
  def __init__(self):
    self.users = []
    self.videos = []
    self.current_user = None
  
  def log_in(self, nickname: str, password: int):
    for i in self.users:
      if i.nickname == nickname and i.password == password:
        self.current_user = i
        return
   
  def register(self, nickname: str, password: int, age: int):
    password = hash(password)
    for i in self.users:
        if i.nickname == i.nickname:
          print(f'Пользователь с никнеймом {nickname} уже существует')
          return
    Nuser = User(nickname, password, age)
    self.users.append(Nuser)
    self.current_user = Nuser    
  
  def log_out(self):
    self.current_user = None
  
  def add(self, *args):
    for i in args:
      if i not in self.videos:
        self.videos.append(i)
      else:
        print(f'Видео с названием {i.title} уже существует')
  
  def get_videos(self, title: str):
    listOfVideos = []
    for i in self.videos:
      if title.lower() in i.title.lower():
        listOfVideos.append(i)
    return listOfVideos 
  
  def watch_video(self, title: str):
    if self.current_user:
      for i in self.videos:
        if i.adult_mode and self.current_user.age < 18:
          print('Вам нет 18 лет, пожалуйста покиньте страницу')
          return
        if i in i.title:
          for j in range(i.duration):
            print(f'{i} ')
            time.sleep(1)
            i.time_now += 1
          i.time_now = 0
          print('Конец видео')
    else:
      print('Войдите в аккаунт, чтобы смотреть видео')    
        

for __name__ in '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
    ur.add(v1, v2)

# Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
  
# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

