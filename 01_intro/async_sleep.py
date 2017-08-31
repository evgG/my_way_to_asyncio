import time
import asyncio


async def sleep_count(num):
    await asyncio.sleep(2)
    print('Number {} slept 2 seconds'.format(num))


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*(sleep_count(_)
                                           for _ in range(5))))
    loop.close()
    print("--- %s seconds ---" % (time.time() - start_time))
