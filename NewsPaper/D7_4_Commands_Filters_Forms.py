# D7_2Проект News Portal
# # Доработайте ваш сайт с новостями:
#
# Задание -Добавьте постраничный вывод на основной странице новостей, чтобы на одной странице было не больше 10новостей,
#     и были видны номера лишь ближайших страниц, а также возможность перехода к первой или последней странице.

# |1|  D7_2 корректно настроим шаблон:
# |постраничный вывод|
# --настройка APP_DIRS должна быть выставлена в True;
#-- переходим в файл models.py в модели Post меняем функцию __str__
# def __str__(self):
#     return f'{self.heading} {self.text_post[:100]} '
#-- файл шаблона должен лежать в соответствующей папке внутри папки приложения.
# Переходим в файл NewsPaper/news/views.py
# вписывываем  идобавляем строку paginate_by = 10 в представление PostsList
# Переходим в файл templates/posts.html
# добавляем блок пагинации

# Задание-Добавьте страничку /news/search.
#         На ней должна быть реализована возможность пользователя искать новости по определённым критериям.
#
#         Критерии должны быть следующие:
#                 позже какой-либо даты;
#                 по названию;
#                 по имени пользователя автора;
#                 всё вместе.
#
# ВЫПОЛНЕНИЕ Для начала поставим дополнительные пакеты через pip:
# # python -m pip install django-filter
#
# Не забываем вписать ‘django_filters’ в INSTALLED_APPS в настройках, чтобы получить доступ к фильтрам в приложении.
# Теперь надо создать файл filters.py в директории simple_app/ в той же папке, где лежат наши модели и всё остальное.
# Заполняем файл

# Переходим в файл NewsPaper/news/views.py
# Создаем новый класс class PostsSearchList(ListView):
# обавляем функцию def get_context_data(self, **kwargs):

# Создаем папки news/search в NewsPaper/templates и отдельный файл шаблона posts_filters, для странички search
# наполняем файл нового шаблона posts_filters
# <!-- Перед таблицей добавим форму для поиска -->
# <!-- поменяем posts на filter.qs, т. к. теперь мы забираем уже отобранную по каким-то параметрам информацию -->
# обавляем url для странички /news/search/
# Проверяем страничку, должна работать

# Переходим в файл NewsPaper/news/views.py
# Фильтрация готова. С остальными полями надо быть осторожнее. Они ищут только точное совпадение.
# Такой вариант может не подходить для каких-нибудь интернет-магазинов, но отлично подойдёт, например,
# для журнала сотрудников (не наш случай).
# Давайте отредактируем фильтр новостей и сделаем из него более подходящий нам вариант:
# heading_post = CharFilter(field_name='heading', lookup_expr='icontains', label='Заголовок')
# author_post = CharFilter(field_name='author__user__username', lookup_expr='icontains', label='Имя пользователя')
# create_time_post = DateFilter(field_name='create_time', lookup_expr='gte', label='Дата(+)')

# Примеры поиска:
# заголовок---Новость или Статья
# Имя пользовтеля---- sasha или dima
# Дата форма записи ---2021-11-28


# Мы подробнее остановимся на работе с ModelForms. Эта штука позволяет нам быстро и удобно создавать HTML-формы на
# основе самой модели. Давайте добавим в наше приложение news файл forms.py.
# создал  class PostForm(ModelForm):
# Создаем шаблон post_create.html директории templates/news/

# Правим шаблон posts_filters.html:
# - подправил заголовки странички, перенес поиск, немного преобразовал...

# Правим шаблон posts.html:
# -(<a href="{% url 'post' post.id %}">{{ post.heading|truncatewords:2|censor:'***'}}</a>)

# Переходим в views.py создаем дженерик Create и подправили PostDetail

# Пропишем дополнительные пути в urls.py   и дописал ко всем свои name=

# добавим одну хитрость в наш models.py .
# def get_absolute_url(self):
# # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
#     return f'/products/{self.id}'

# Переходим в views.py создаем дженерик Delete Update

# Добавить новый шаблон по адресу news/product_delete.html

# Правим шаблон posts.html:
# Добавим ссылки на редактирование, создание  и удаление на главную страницу и переход на страницу search
# <a href="{% url 'post_update' post.id %}"><u>Редактировать</u></a>
# <a href="{% url 'post_delete' post.id %}"><u> Удалить </u></a>
# <a href="{% url 'post_create' %}">Добавить новый пост</a> <br>
# <a href="search/">| Поиск |</a>

# Пропишем оставшиеся пути в urls.py
#  один из примеров path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
# Удаление объектов as_view() ВАЖНО "()" ОБРАЩАТЬ ВНИМАЕ НА СКОБКИ  () ВАЖНО!!!!# !!




