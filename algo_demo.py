import random
from adt import LinkedList
import time
from tqdm import tqdm

num_items = 1024*1024
l = LinkedList()
s = 0
print(time.time())
for i in tqdm(range(num_items)):
    l.append(random.randint(0, num_items))
    s = l.size()
print(time.time())

