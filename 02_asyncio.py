import urllib.request
import json
import time
import asyncio

base_url = 'http://jsonplaceholder.typicode.com/{}'
categories = ['users', 'posts', 'comments', 'albums']
# categories = ['users']
# categories = ['users', 'posts', 'comments', 'albums', 'photos', 'todos']

final_data = []


def category_to_json_list(category):
    url = base_url.format(category)
    html = urllib.request.urlopen(url).read().decode()
    json_list = json.loads(html)
    return json_list


def get_id_from_json(json_):
    return json_['id']


async def category_get_by_id(category, json_):
    # print(category, json_)
    url = base_url.format(category) + '/{}'.format(get_id_from_json(json_))
    html = urllib.request.urlopen(url).read().decode()
    return json.loads(html)


async def get_all_in_category(category, json_list):
    # print("json list: {}".format(json_list))
    coroutines = [category_get_by_id(category, json_item)
                  for json_item in json_list]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        final_data.append(item.result())


if __name__ == '__main__':
    print('Starting...')
    start = time.time()
    event_loop = asyncio.get_event_loop()
    try:
        for cat in categories:
            print('Fetching {}'.format(cat))
            j_lst = category_to_json_list(cat)
            event_loop.run_until_complete(get_all_in_category(cat, j_lst))
    finally:
        event_loop.close()
    print(final_data)
    # print(len(final_data))
    print('All data fetched in {:3.2f}'.format(time.time() - start))
