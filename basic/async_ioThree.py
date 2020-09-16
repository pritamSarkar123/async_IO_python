import asyncio
import time

def is_palindrom(num):
    old_num=num
    new_num=0
    while num:
        new_num=new_num*10+(num%10)
        num=num//10
    if old_num==new_num:
        return True
    else:
        return False
async def largest_palindrom(upper_bound):
    print(f"Highest palindrom of {upper_bound}")
    min_difference=upper_bound
    max_palindrom=None
    for i in range(upper_bound+1):
        if is_palindrom(i) and upper_bound-i<min_difference:
            min_difference=upper_bound-i
            max_palindrom=i
        if i%100==0:
            await asyncio.sleep(0.001)
    print(f"Highest palindrom of {upper_bound} is {max_palindrom}")
    return max_palindrom
async def main():
    t0=time.time()
    r1=loop.create_task(largest_palindrom(200000))
    r2=loop.create_task(largest_palindrom(10000))
    r3=loop.create_task(largest_palindrom(90000))
    r4=loop.create_task(largest_palindrom(50000))
    await asyncio.wait([r1,r2,r3,r4])
    t1=time.time()
    print(f"Time taken {(t1-t0)} s")
    return r1,r2,r3,r4
if __name__=="__main__":
    try:
        loop=asyncio.get_event_loop()
        r1,r2,r3,r4=loop.run_until_complete(main())
        print(r1.result(),r2.result(),r3.result(),r4.result())
    except Exception as e:
        pass
    finally:
        loop.close()
    