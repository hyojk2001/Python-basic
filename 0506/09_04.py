import asyncio

async def make_americano():
    print("Americano Start")
    await asyncio.sleep(3)
    print("Americano End")

async def make_latte():
    print("Latte Start")
    await asyncio.sleep(3)
    print("Latte End")

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    await asyncio.gather(
        coro1,
        coro2
    )

if __name__ == "__main__":      #이걸 하면 다른 파이썬에서 이 모듈을 끌어다 쓸 때, 위의 함수만 갖다 쓰고 22번째부터인 print문은 안 쓰는것이 가능하다.
    print("Main Start")
    asyncio.run(main())
    print("Main End")