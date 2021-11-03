import time


def output_computing_time(algorithm_name, start_time):
    print(algorithm_name + " computing time: " + str(time.time() - start_time))
