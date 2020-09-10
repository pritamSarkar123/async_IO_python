import asyncio
import time
import math
#consept: https://www.youtube.com/watch?v=tSLDcRkgTsY
def is_prime(value):
	return not any(value%i==0 for i in range(2,int(math.sqrt(value))+1))
async def find_largest_prime(upper_bound):
	print(f"Highest prime of {upper_bound}")
	for i in range(upper_bound-1,0,-1):
		if is_prime(i):
			print(f"Highest prime below {upper_bound} is {i}")
			return i
		if i<upper_bound-10:
			await asyncio.sleep(0.01)  #makes the function properly asynchronous
			#time.sleep(0.01)
	return None
async def main():
	t0=time.time()
	await asyncio.wait([
		find_largest_prime(2000000),
		find_largest_prime(10000),
		find_largest_prime(90000),
		find_largest_prime(1000000)
		])
	t1=time.time()
	print(f"time taken {(t1-t0)*1000} ms")

if __name__ == '__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(main())
	loop.close()