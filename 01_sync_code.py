import urllib.request
import json
import time

base_url = 'http://jsonplaceholder.typicode.com/{}'
categories = ['users', 'posts', 'comments', 'albums']
# categories = ['users', 'posts', 'comments', 'albums', 'photos', 'todos']
# categories = ['users']


def category_to_json_list(category):
    url = base_url.format(category)
    html = urllib.request.urlopen(url).read().decode()
    json_list = json.loads(html)
    return json_list


def get_id_from_json(json_):
    return json_['id']


def category_get_by_id(category, json_):
    url = base_url.format(category) + '/{}'.format(get_id_from_json(json_))
    html = urllib.request.urlopen(url).read().decode()
    return json.loads(html)


if __name__ == '__main__':
    final_data = []
    print('Starting...')
    start = time.time()
    for cat in categories:
        print('Fetching {}'.format(cat))
        for j in category_to_json_list(cat):
            final_data.append(category_get_by_id(cat, j))
    print(final_data)
    print('All data fetched in {:3.2f}'.format(time.time() - start))
