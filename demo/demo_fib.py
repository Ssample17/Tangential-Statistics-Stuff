#Demonstration of fibonacci numbers produced by in-package function

import numpy as np
import TanStats as ts

if __name__ == "__main__":
    print("The function can compute fibonacci numbers via matrix multiplication.")
    a = np.sort(np.random.choice(range(4, 51), size=5))
    for i in a:
        print("The " + str(i) + "th fibonacci number is: " + str(ts.fib(int(i))))