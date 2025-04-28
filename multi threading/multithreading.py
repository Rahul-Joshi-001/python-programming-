import multiprocessing  # Correct import statement
import time

def square():
    for i in range(5):
        time.sleep(1)  # Simulate delay
        print(f"square : {i*i}")

def cube():
    for i in range(5):
        time.sleep(1.5)  # Simulate delay
        print(f"cube : {i*i*i}")

if __name__ == "__main__":
    # Create two processes
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t0 = time.time()  # Start time for total execution

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    # Calculate and print the total execution time
    ftime = time.time() - t0
    print(f"Total execution time: {ftime} seconds")
