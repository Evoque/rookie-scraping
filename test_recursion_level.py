'''
测试递归深度(书上说默认1000)
'''

import time

count = 0
def recursion():
    global count
    time.sleep(0.01)
    count += 1
    print(f'count: {count}')
    recursion()
    
    
recursion()