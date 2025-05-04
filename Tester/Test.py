import os
import subprocess

# this class is used to test the functionality of the program
class Test():

    def run_fibonacci(self, n):
        if n <= 0:
            return "Invalid input. n must be a positive integer."
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.run_fibonacci(n - 1) + self.run_fibonacci(n - 2)
     
    def run_cpu_test(self, threads=4):
        output = subprocess.check_output(f'sysbench cpu --time=30 --threads={threads} run | grep "total number of"', shell=True, text=True)
        return output.split(':'[::-1])[1].strip()
