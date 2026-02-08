import pytest
from tests.conftest import try_get_url


@pytest.mark.parametrize(
    'url, slug', [
        ('/category/category_slug/', 'category_slug'),
        ('/category/another_slug/', 'another_slug'),
    ]
)
def test_category_page_contents(client, url, slug):
    response = try_get_url(client, url)
    expected_slug = '<slug>'
    msg_url = url.replace(slug, expected_slug)
    found_slug_in_page_html = slug in response.content.decode()
    assert found_slug_in_page_html, (
        f'Убедитесь, что на странице {msg_url}'
        f'отображается текст {expected_slug}.'
    )
