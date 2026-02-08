# import os
from pathlib import Path

import pytest
from django.template import TemplateDoesNotExist


@pytest.fixture()
def urlpatterns(imports_by_full_name):
    urlpattern_paths = [
        'pages.urls.urlpatterns', 'blog.urls.urlpatterns']
    urlpattern_vals = [imports_by_full_name[path] for path in urlpattern_paths]
    expected_names = [
        ('about', 'rules'),
        ('index', 'post_detail', 'category_posts'),
    ]
    expected_views = [
        ('pages.views.about', 'pages.views.rules'),
        ('blog.views.index', 'blog.views.post_detail',
         'blog.views.category_posts'),
    ]
    return zip(
        urlpattern_paths, urlpattern_vals, expected_names, expected_views)


@pytest.fixture()
def settings_app_name():
    return 'blogicum'


@pytest.fixture()
def root_dir():
    return str(Path(__file__).parent.parent)


@pytest.fixture()
def project_dirname():
    return 'blogicum'


@pytest.fixture()
def posts():
    return EXPECTED_POSTS


EXPECTED_POSTS = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]


def try_get_url(client, url: str):
    try:
        response = client.get(url)
    except TemplateDoesNotExist as err:
        raise AssertionError(
            f'При загрузке страницы по адресу `{url}` возникла ошибка. '
            'Убедитесь, что указанный для страницы шаблон существует '
            'и находится в правильной директории.'
        ) from err
    except TypeError as err:
        raise AssertionError(
            f'При загрузке страницы по адресу `{url}` '
            'возникла ошибка TypeError. '
            'Убедитесь, что используете Path Converter '
            'для приведения параметра строки запроса к нужному типу.'
        ) from err
    except Exception as err:
        raise AssertionError(
            f'При попытке загрузки страницы по адресу `{url}` возникла ошибка:'
            f' {err}'
        ) from err
    else:
        if response.status_code < 300:
            return response
        raise AssertionError(
            f'При попытке загрузки страницы по адресу `{url}` возникла ошибка:'
            f' {response}'
        )


class _TestModelAttrs:
    """Класс для проверки атрибутов моделей."""

    def test_model_attrs(self, model_name, field_name, expected_value,
                         attr_name, model_admin=None):
        if model_admin:
            model = model_admin
        else:
            from django.apps import apps
            model = apps.get_model('blog', model_name)

        field = model._meta.get_field(field_name)
        value = getattr(field, attr_name)
        assert value == expected_value, (
            f'Проверьте, что для поля `{field_name}` модели `{model_name}` '
            f'атрибут `{attr_name}` имеет значение `{expected_value}`.'
        )
