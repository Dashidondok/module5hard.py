
class User:
    '''
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    '''
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname
    def get_info(self):
        return self.nickname, self.password

class Video:
    '''
    Класс Видео содержащий атрибуты: Заголовок, продолжительность, секунда остановки, ограничение по возрасту
    '''
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class UrTube:
    '''
    Класс UrTube содержащий атрибуты: Список объектов User, Список объектов Video, Текущий пользователь
    '''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    '''ищем пользователя в users с такими же логином и паролем'''
    def log_in(self, login, password):
        for user in self.users:
            if (login, hash(password)) == user.get_info():
                self.current_user = user
                return user


    '''добавляем пользователя в список, если пользователя не существует'''
        def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    '''сброс текущего пользователя на None'''
    def log_out(self):
        self.current_user = None

    '''добавляем в videos, если с таким же названием видео ещё не существует'''
    def add(self, *videos: Video):
        for Video in videos:
            if Video.title not in self.videos:
                self.videos.append(Video)

    '''принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово'''
    def get_videos(self, search):
        titles = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)
        return titles

    '''принимает название фильма, если не находит точного совпадения(вплоть до пробела), 
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
    После текущее время просмотра данного видео сбрасывается. 
    Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. 
    В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
    Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. 
    Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    После воспроизведения нужно выводить: "Конец видео"'''
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age <= 18:
                    while video.time_now > video.duration:
                        video.time_now =+ 1
                        print(video.time_now, end = ' ')
                        time.sleep(1)
                    video.time_now = 0
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

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