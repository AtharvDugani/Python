import asyncio

async def Task1():
    print("Task 1 is started!!")
    await asyncio.sleep(3)
    print("Task 1 is completed!!")
    return("Task1")

async def Task2():
    print("Task 2 is started!!")
    await asyncio.sleep(2)
    print("Task 2 is completed!!")
    return("Task2")

async def Task3():
    print("Task 3 is started!!")
    await asyncio.sleep(1)
    print("Task 3 is completed!!")  
    return("Task3")

async def main():
    # with the help of gather function
    # result = await asyncio.gather(
    #     Task1(),
    #     Task2(),
    #     Task3()
    # )
    # print(result)

    # With the help of create_task method of asyncio 
    t1 = asyncio.create_task(Task1())
    t2 = asyncio.create_task( Task2())
    t3 = asyncio.create_task( Task3())
    await t1
    await t2
    await t3
asyncio.run(main())