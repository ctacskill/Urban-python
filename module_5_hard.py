
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def get_password(self):
        return self.password
    def __str__(self):
        return self.nickname
    def __repr__(self):
        return self.nickname
    def __contains__(self, item):
        return item in self.nickname
    def __eq__(self, other):
        return self.nickname == other
    def get_age(self):
        return self.age
class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    def __contains__(self, item):
        return item.lower() in self.title.lower()
    def __eq__(self, other):
        return self.title == other
    def set_time_now(self):
        self.time_now += 1
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user.nickname not in self.users:
            self.users.append(user)
            self.current_user = user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.get_password():
                self.current_user = user
                return
        print('Такого пользователя не существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)


    def get_videos(self, stroka):
        stroka = stroka.lower()
        videos = []
        for video in self.videos:
            if stroka in video:
                videos.append(video)
        return videos
    def check_age(self, video):
        if self.current_user:
            if not video.adult_mode or self.current_user.get_age() >= 18:
                return True
            else:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


    def watch_video(self, video_name):
        from time import sleep
        for video in self.videos:
            if video_name == video and self.check_age(video):
                while video.time_now < video.duration:
                    video.set_time_now()
                    print(video.time_now, end=' ')
                print('Конец видео')

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



