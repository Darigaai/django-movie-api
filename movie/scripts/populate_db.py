import datetime
from django.contrib.auth import get_user_model
from users.models import User  # Можно было бы использовать get_user_model() напрямую
from movie.models import Genre, Actor, Movie  # Предполагаем, что модели в приложении main

# exec(open('populate_db.py').read())

def run():
    # 1. Создаём (или получаем) пользователя «admin», к которому привяжем все фильмы
    admin_user, _ = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'password': 'admin'  # Для реального проекта используйте более сложный пароль
        }
    )

    # 2. Создаём (или получаем) список основных жанров (название на русском, slug на английском)
    genre_names = [
        ('Драма', 'drama'),
        ('Криминал', 'crime'),
        ('Боевик', 'action'),
        ('Комедия', 'comedy'),
        ('Триллер', 'thriller'),
        ('Научная фантастика', 'sci-fi'),
        ('Фэнтези', 'fantasy'),
        ('Приключения', 'adventure'),
        ('Мультфильм', 'animation'),
        ('Биография', 'biography'),
        ('Мелодрама', 'romance'),
        ('Вестерн', 'western')
    ]
    genre_objects = {}
    for g_name, g_slug in genre_names:
        obj, _ = Genre.objects.get_or_create(title=g_name, slug=g_slug) #slug=g_slug
        
        genre_objects[g_name] = obj

    # 3. Создаём (или получаем) список актёров и режиссёров (Actor).
    #    В модели Movie у нас ManyToManyField(Actor) для поля directors и actors.
    #    При желании можно было бы добавить поля: дата рождения, биография и т.п.
    #    Здесь же просто создаём объекты с полем name.
    actor_names = [
        'Фрэнк Дарабонт',
        'Фрэнсис Форд Коппола',
        'Кристофер Нолан',
        'Квентин Тарантино',
        'Дэвид Финчер',
        'Роберт Земекис',
        'Мартин Скорсезе',
        'Ридли Скотт',
        'Тим Роббинс',
        'Морган Фриман',
        'Аль Пачино',
        'Мэрлон Брандо',
        'Кристиан Бейл',
        'Хит Леджер',
        'Брэд Питт',
        'Эдвард Нортон',
        'Том Хэнкс',
        'Леонардо Ди Каприо',
        'Киану Ривз',
        'Лоренс Фишбёрн',
        'Гэри Олдман',
        'Роберт Де Ниро',
        'Джоди Фостер',
        'Энтони Хопкинс',
        'Пон Джун-хо',
        'Джейми Фокс',
        'Сэмюэл Л. Джексон'
        # Можно добавить больше при желании
    ]
    actor_objects = {}
    for name in actor_names:
        actor_obj, _ = Actor.objects.get_or_create(name=name)
        actor_objects[name] = actor_obj

    # 4. Подготавливаем список из 20 фильмов с информацией на русском языке.
    #    Каждый словарь содержит:
    #       - title (название на русском)
    #       - description (краткое описание)
    #       - year (год)
    #       - country (страна)
    #       - world_premiere (дата мировой премьеры в формате datetime.date)
    #       - budget, fees_in_usa, fees_in_world (числовые поля)
    #       - directors (список имён режиссёров из actor_names)
    #       - actors (список имён актёров из actor_names)
    #       - genres (список жанров из списка выше: «Драма», «Криминал» и т.д.)
    movies_data = [
        {
            'title': 'Побег из Шоушенка',
            'description': 'История о том, как два осуждённых сближаются за долгие годы тюремной жизни...',
            'year': 1994,
            'country': 'США',
            'world_premiere': datetime.date(1994, 9, 22),
            'budget': 25000000,
            'fees_in_usa': 28341469,
            'fees_in_world': 58341469,
            'directors': ['Фрэнк Дарабонт'],
            'actors': ['Тим Роббинс', 'Морган Фриман'],
            'genres': ['Драма', 'Криминал']
        },
        {
            'title': 'Крёстный отец',
            'description': 'Влиятельный глава мафиозного клана постепенно передаёт дела своему сыну...',
            'year': 1972,
            'country': 'США',
            'world_premiere': datetime.date(1972, 3, 24),
            'budget': 6000000,
            'fees_in_usa': 134966411,
            'fees_in_world': 246120986,
            'directors': ['Фрэнсис Форд Коппола'],
            'actors': ['Мэрлон Брандо', 'Аль Пачино'],
            'genres': ['Криминал', 'Драма']
        },
        {
            'title': 'Тёмный рыцарь',
            'description': 'Бэтмен сталкивается с тяжелейшим психологическим испытанием в борьбе с Джокером...',
            'year': 2008,
            'country': 'США',
            'world_premiere': datetime.date(2008, 7, 18),
            'budget': 185000000,
            'fees_in_usa': 534858444,
            'fees_in_world': 1004000000,
            'directors': ['Кристофер Нолан'],
            'actors': ['Кристиан Бейл', 'Хит Леджер', 'Гэри Олдман'],
            'genres': ['Боевик', 'Криминал', 'Драма']
        },
        {
            'title': 'Криминальное чтиво',
            'description': 'Переплетённые истории двух наёмных убийц, боксера, гангстера и его жены...',
            'year': 1994,
            'country': 'США',
            'world_premiere': datetime.date(1994, 10, 14),
            'budget': 8000000,
            'fees_in_usa': 107928762,
            'fees_in_world': 213928762,
            'directors': ['Квентин Тарантино'],
            'actors': ['Джон Траволта', 'Сэмюэл Л. Джексон', 'Ума Турман'],
            'genres': ['Криминал', 'Драма']
        },
        {
            'title': 'Бойцовский клуб',
            'description': 'Страдающий от бессонницы клерк и продавец мыла основывают подпольный бойцовский клуб...',
            'year': 1999,
            'country': 'США',
            'world_premiere': datetime.date(1999, 10, 15),
            'budget': 63000000,
            'fees_in_usa': 37030102,
            'fees_in_world': 100853753,
            'directors': ['Дэвид Финчер'],
            'actors': ['Брэд Питт', 'Эдвард Нортон'],
            'genres': ['Драма']
        },
        {
            'title': 'Форрест Гамп',
            'description': 'Трогательная история добродушного Форреста, чья жизнь пересекается с важными событиями в истории США...',
            'year': 1994,
            'country': 'США',
            'world_premiere': datetime.date(1994, 7, 6),
            'budget': 55000000,
            'fees_in_usa': 330000000,
            'fees_in_world': 678000000,
            'directors': ['Роберт Земекис'],
            'actors': ['Том Хэнкс', 'Гэри Синиз'],  # Можно было добавить больше актёров
            'genres': ['Драма', 'Мелодрама']
        },
        {
            'title': 'Начало',
            'description': 'Вор проникает в сны людей, чтобы красть их идеи, но получает последний и самый сложный заказ...',
            'year': 2010,
            'country': 'США',
            'world_premiere': datetime.date(2010, 7, 16),
            'budget': 160000000,
            'fees_in_usa': 292576195,
            'fees_in_world': 836848102,
            'directors': ['Кристофер Нолан'],
            'actors': ['Леонардо Ди Каприо', 'Джозеф Гордон-Левитт'],  # Гордон-Левитта лучше тоже в список актёров выше при желании
            'genres': ['Боевик', 'Научная фантастика', 'Приключения']
        },
        {
            'title': 'Матрица',
            'description': 'Обычный программист Нео узнаёт, что реальность — это иллюзия, и вступает в борьбу с системой...',
            'year': 1999,
            'country': 'США',
            'world_premiere': datetime.date(1999, 3, 31),
            'budget': 63000000,
            'fees_in_usa': 171479930,
            'fees_in_world': 466364845,
            'directors': ['Лана Вачовски', 'Лилли Вачовски'],
            'actors': ['Киану Ривз', 'Лоренс Фишбёрн'],
            'genres': ['Боевик', 'Научная фантастика']
        },
        {
            'title': 'Славные парни',
            'description': 'История Генри Хилла и его жизни в мафии: дружба, предательства и попытки «завязать»...',
            'year': 1990,
            'country': 'США',
            'world_premiere': datetime.date(1990, 9, 19),
            'budget': 25000000,
            'fees_in_usa': 46836394,
            'fees_in_world': 46836394,
            'directors': ['Мартин Скорсезе'],
            'actors': ['Роберт Де Ниро', 'Рэй Лиотта', 'Джо Пески'],  # Этих актёров тоже можно добавить в actor_names
            'genres': ['Криминал', 'Драма']
        },
        {
            'title': 'Семь',
            'description': 'Два детектива — новичок и ветеран — преследуют жестокого серийного убийцу, наказывающего людей за грехи...',
            'year': 1995,
            'country': 'США',
            'world_premiere': datetime.date(1995, 9, 22),
            'budget': 33000000,
            'fees_in_usa': 100125643,
            'fees_in_world': 327311859,
            'directors': ['Дэвид Финчер'],
            'actors': ['Брэд Питт', 'Морган Фриман', 'Кевин Спейси'],  # Кевина Спейси тоже можно добавить в actor_names
            'genres': ['Криминал', 'Драма', 'Триллер']
        },
        {
            'title': 'Молчание ягнят',
            'description': 'Молодой курсант ФБР просит помощи у заключённого маньяка, чтобы найти другого серийного убийцу...',
            'year': 1991,
            'country': 'США',
            'world_premiere': datetime.date(1991, 2, 14),
            'budget': 19000000,
            'fees_in_usa': 130742922,
            'fees_in_world': 272742922,
            'directors': ['Джонатан Демме'],
            'actors': ['Джоди Фостер', 'Энтони Хопкинс'],
            'genres': ['Триллер', 'Криминал']
        },
        {
            'title': 'Город Бога',
            'description': 'Судьбы двух мальчишек расходятся в трущобах Рио: один становится фотографом, другой — наркобароном...',
            'year': 2002,
            'country': 'Бразилия',
            'world_premiere': datetime.date(2002, 8, 30),
            'budget': 3300000,
            'fees_in_usa': 7563397,
            'fees_in_world': 30338359,
            'directors': ['Фернанду Мейреллиш', 'Катя Лунд'],
            'actors': ['Александре Родригес', 'Леандро Фирмину'],
            'genres': ['Криминал', 'Драма']
        },
        {
            'title': 'Зелёная миля',
            'description': 'История надзирателей блока смертников, жизнь которых меняется с приходом таинственного узника...',
            'year': 1999,
            'country': 'США',
            'world_premiere': datetime.date(1999, 12, 10),
            'budget': 60000000,
            'fees_in_usa': 136801374,
            'fees_in_world': 286801374,
            'directors': ['Фрэнк Дарабонт'],
            'actors': ['Том Хэнкс', 'Майкл Кларк Дункан'],
            'genres': ['Криминал', 'Драма', 'Фэнтези']
        },
        {
            'title': 'Интерстеллар',
            'description': 'Группа исследователей отправляется через червоточину в космосе, чтобы найти новый дом для человечества...',
            'year': 2014,
            'country': 'США',
            'world_premiere': datetime.date(2014, 11, 7),
            'budget': 165000000,
            'fees_in_usa': 188020017,
            'fees_in_world': 701729206,
            'directors': ['Кристофер Нолан'],
            'actors': ['Мэттью МакКонахи', 'Анн Хэтэуэй'],  # Их можно тоже включить в actor_names
            'genres': ['Научная фантастика', 'Приключения', 'Драма']
        },
        {
            'title': 'Унесённые призраками',
            'description': 'Девочка попадает в магический мир духов и ищет путь домой, сталкиваясь с множеством испытаний...',
            'year': 2001,
            'country': 'Япония',
            'world_premiere': datetime.date(2001, 7, 20),
            'budget': 19000000,
            'fees_in_usa': 10049886,
            'fees_in_world': 274925095,
            'directors': ['Хаяо Миядзаки'],
            'actors': ['Руми Хираи', 'Мию Ирино'],
            'genres': ['Мультфильм', 'Фэнтези']
        },
        {
            'title': 'Спасти рядового Райана',
            'description': 'Во время Второй мировой отряд солдат отправляется за линию фронта, чтобы найти и вернуть домой рядового...',
            'year': 1998,
            'country': 'США',
            'world_premiere': datetime.date(1998, 7, 24),
            'budget': 70000000,
            'fees_in_usa': 216540909,
            'fees_in_world': 481840909,
            'directors': ['Стивен Спилберг'],
            'actors': ['Том Хэнкс', 'Мэтт Деймон'],
            'genres': ['Драма', 'Боевик']
        },
        {
            'title': 'Король Лев',
            'description': 'Юный лев Симба становится мишенью для злого дяди, который хочет захватить власть в саванне...',
            'year': 1994,
            'country': 'США',
            'world_premiere': datetime.date(1994, 6, 24),
            'budget': 45000000,
            'fees_in_usa': 422783777,
            'fees_in_world': 968483777,
            'directors': ['Роджер Аллерс', 'Роб Минкофф'],
            'actors': ['Мэтью Бродерик', 'Джеймс Эрл Джонс'],
            'genres': ['Мультфильм', 'Приключения', 'Драма']
        },
        {
            'title': 'Пианист',
            'description': 'Польский еврей и талантливый пианист пытается выжить в условиях немецкой оккупации...',
            'year': 2002,
            'country': 'Франция/Польша/Великобритания/Германия',
            'world_premiere': datetime.date(2002, 5, 24),
            'budget': 35000000,
            'fees_in_usa': 32572576,
            'fees_in_world': 120072577,
            'directors': ['Роман Полански'],
            'actors': ['Адриен Броуди'],
            'genres': ['Биография', 'Драма']
        },
        {
            'title': 'Паразиты',
            'description': 'Семья, живущая на социальном дне, проникает в дом богатой семьи. Жадность и классовые различия приводят к трагедии...',
            'year': 2019,
            'country': 'Республика Корея',
            'world_premiere': datetime.date(2019, 5, 30),
            'budget': 11400000,
            'fees_in_usa': 53236963,
            'fees_in_world': 263969463,
            'directors': ['Пон Джун-хо'],
            'actors': ['Сон Кан Хо', 'Чхве У Шик'],
            'genres': ['Триллер', 'Драма']
        },
        {
            'title': 'Джанго освобождённый',
            'description': 'Освобождённый раб и немецкий охотник за головами отправляются на поиски жены главного героя...',
            'year': 2012,
            'country': 'США',
            'world_premiere': datetime.date(2012, 12, 25),
            'budget': 100000000,
            'fees_in_usa': 162805434,
            'fees_in_world': 426074373,
            'directors': ['Квентин Тарантино'],
            'actors': ['Джейми Фокс', 'Леонардо Ди Каприо', 'Сэмюэл Л. Джексон'],
            'genres': ['Драма', 'Вестерн']
        },
    ]

    # 5. Создаём объекты Movie и заполняем их данными, указывая admin_user как автора.
    #    Затем устанавливаем связи ManyToMany (actors, directors, genres).
    for m_data in movies_data:
        movie_obj = Movie.objects.create(
            title=m_data['title'],
            description=m_data['description'],
            year=m_data['year'],
            country=m_data['country'],
            world_premiere=m_data['world_premiere'],
            budget=m_data['budget'],
            fees_in_usa=m_data['fees_in_usa'],
            fees_in_world=m_data['fees_in_world'],
            user=admin_user  # Привязка к пользователю (ForeignKey)
        )

        # Привязываем режиссёров
        director_list = []
        for d_name in m_data['directors']:
            # Если режиссёр не найден в actor_objects, создаём «на лету»
            d_obj, _ = Actor.objects.get_or_create(name=d_name)
            director_list.append(d_obj)
        movie_obj.directors.set(director_list)

        # Привязываем актёров
        actors_list = []
        for a_name in m_data['actors']:
            a_obj, _ = Actor.objects.get_or_create(name=a_name)
            actors_list.append(a_obj)
        movie_obj.actors.set(actors_list)

        # Привязываем жанры
        genres_list = []
        for g_name in m_data['genres']:
            # Если жанр уже есть в словаре genre_objects — используем его
            if g_name in genre_objects:
                genres_list.append(genre_objects[g_name])
            else:
                # Если жанра нет, создаём новый (сделаем slug на латинице)
                slug = g_name.lower()
                g_obj, _ = Genre.objects.get_or_create(name=g_name, slug=slug)
                genres_list.append(g_obj)
        movie_obj.genres.set(genres_list)

        print(f"Создан фильм: {movie_obj.title}")

    print("Готово! 20 фильмов добавлены (либо уже существовали).")