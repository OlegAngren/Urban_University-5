import hashlib
import time


class User:
    """
    Класс User управляет данными о пользователе.

    Атрибуты:
        nickname (str): Имя пользователя.
        password (int): Хэшированный пароль.
        age (int): Возраст пользователя.

    Методы:
        _hash_password(password): Приватный метод для хэширования пароля.
    """
    def __init__(self, nickname, password, age):
        """
        Инициализирует пользователя с указанными данными.

        Args:
            nickname (str): Имя пользователя.
            password (str): Пароль в виде строки.
            age (int): Возраст пользователя.
        """
        self.nickname = nickname
        self.password = self._hash_password(password)  # Пароль сохраняется в хэшированном виде
        self.age = age

    @staticmethod
    def _hash_password(password):
        """
        Приватный метод для хэширования пароля.

        Args:
            password (str): Пароль в виде строки.

        Returns:
            int: Хэшированный пароль.
        """
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        """
        Возвращает строковое представление объекта User.

        Returns:
            str: Имя пользователя.
        """
        return self.nickname


class Video:
    """
    Класс Video управляет данными о видео.

    Атрибуты:
        title (str): Название видео.
        duration (int): Продолжительность в секундах.
        time_now (int): Текущая секунда просмотра.
        adult_mode (bool): Ограничение по возрасту (по умолчанию False).
    """
    def __init__(self, title, duration, adult_mode=False):
        """
        Инициализирует видео с указанными данными.

        Args:
            title (str): Название видео.
            duration (int): Продолжительность в секундах.
            adult_mode (bool): Ограничение по возрасту.
        """
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        """
        Возвращает строковое представление объекта Video.

        Returns:
            str: Название видео.
        """
        return self.title


class UrTube:
    """
    Основной класс платформы UrTube.

    Атрибуты:
        users (list): Список зарегистрированных пользователей.
        videos (list): Список загруженных видео.
        current_user (User): Текущий авторизованный пользователь.
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Авторизует пользователя, если введены правильные данные.

        Args:
            nickname (str): Имя пользователя.
            password (str): Пароль.

        Если пользователь найден, устанавливается current_user.
        """
        hashed_password = User._hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Неверные логин или пароль.")

    def register(self, nickname, password, age):
        """
        Регистрирует нового пользователя.

        Args:
            nickname (str): Имя пользователя.
            password (str): Пароль.
            age (int): Возраст.

        Если пользователь уже существует, регистрация не выполняется.
        """
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        """Выходит из текущего аккаунта."""
        self.current_user = None

    def add(self, *videos):
        """
        Добавляет видео в список, если их названия уникальны.

        Args:
            *videos (Video): Видео для добавления.
        """
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_query):
        """
        Ищет видео по названию, не учитывая регистр.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список найденных названий.
        """
        return [video.title for video in self.videos if search_query.lower() in video.title.lower()]

    def watch_video(self, title):
        """
        Воспроизводит видео, если пользователь авторизован и соблюдены ограничения.

        Args:
            title (str): Название видео.
        """
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(1, video.duration + 1):
            print(second, end=" ", flush=True)
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0


# Тестирование
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
