import time


def sleep_count(num):
    time.sleep(2)
    print('Number {} slept 2 seconds'.format(num))


if __name__ == '__main__':
    start_time = time.time()
    for _ in range(5):
        sleep_count(_)
    print("--- %s seconds ---" % (time.time() - start_time))
