#consept
#https://www.youtube.com/watch?v=BI0asZuqFXM&t=1068s
import asyncio
import time
import math
def is_prime(value):
	return not any(value%i==0 for i in range(2,int(math.sqrt(value))+1))

async def find_largest_prime(upper_bound):
	print(f"Highest prime of {upper_bound}")
	for i in range(upper_bound-1,0,-1):
		if is_prime(i):
			print(f"Highest prime below {upper_bound} is {i}")
			return i
		if i<upper_bound-10:
			await asyncio.sleep(0.01) #makes the function properly asynchronous
			#time.sleep(0.01)
	return None

async def main():
	t0=time.time()
	l1=loop.create_task(find_largest_prime(2000000))
	l2=loop.create_task(find_largest_prime(10000))
	l3=loop.create_task(find_largest_prime(90000))
	l4=loop.create_task(find_largest_prime(1000000))
	await asyncio.wait([l1,l2,l3,l4]) #l1->l2->l3->l4 one complets then other ,iff not await asyncio.sleep(0.01) is used
	t1=time.time()	
	print(f"time taken {(t1-t0)*1000} ms")
	return l1,l2,l3,l4

if __name__ == '__main__':
	try:
		loop=asyncio.get_event_loop()
		#loop.set_debug() #if debug is required
		l1,l2,l3,l4=loop.run_until_complete(main())
		print(l1.result())
		print(l2.result())
		print(l3.result())
		print(l4.result())
	except Exception as e:
		pass
	finally:
		loop.close()