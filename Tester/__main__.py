from Tester.Data import Data
from Tester.Test import Test
import threading, time, json, os

def main():
    global result, kill_thread
    result = {
        "Frequency": 0,
        "Temperature_min": 0,
        "Temperature_max": 0,
        "Temperature_avg": [],
        "Fibonacci": 0,
        "cpu_test_single_thread": 0,
        "cpu_test_multi_thread": 0
    }
    test = Test()
    t1 = threading.Thread(target=get_data, daemon=True)
    t1.start()
    start_time = time.time()
    test.run_fibonacci(40)
    result["Fibonacci"] = round(time.time() - start_time, 2)
    result["cpu_test_single_thread"] = test.run_cpu_test(threads=1)
    result["cpu_test_multi_thread"] = test.run_cpu_test(threads=4)
    kill_thread = True
    t1.join()
    result["Temperature_avg"] = round(sum(result["Temperature_avg"]) / len(result["Temperature_avg"]), 2)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(BASE_DIR, 'data.json'), "r+") as f:
        file_data = json.load(f)
        file_data["tests"].append(result)
        f.seek(0)
        json.dump(file_data, f, indent=4)
    print("Test finished. Data saved in data.json")

def get_data():
    global result, kill_thread
    data = Data()
    result["Temperature_min"] = data.get_cpu_temp()
    kill_thread = False
    while not kill_thread:
        temp = data.get_cpu_temp()
        if temp < result["Temperature_min"]:
            result["Temperature_min"] = temp
        if temp > result["Temperature_max"]:
            result["Temperature_max"] = temp
        result["Temperature_avg"].append(temp)
        time.sleep(1)

    