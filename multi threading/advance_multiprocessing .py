from concurrent.futures import ProcessPoolExecutor
import time


def square(no):
    time.sleep(1)
    return f"squre is : {no * no}"
num = [1,2,3,4,5,6]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=2) as exe:
        result = exe.map(square,num)

    for el in result:
        print(el)