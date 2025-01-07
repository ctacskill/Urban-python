import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование!')
    balls = 5
    delay = 0 - power + 6 # ну мы считаем, что сила  максимальная 5, поэтому так. Была бы  сила
                          # другой формула бы поменялась
    for set in range(1, balls + 1):
        await asyncio.sleep(delay)
        print(f'Силач {name}, поднял {set} шар')

    print(f'Силач {name} закончил соревнование!')


async def start_tournnament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournnament())


