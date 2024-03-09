from lab_3_task_4 import triganometry_array, m

triganometry_array[:, [int(i) for i in range(m)]] = triganometry_array[:, [1, 0, 3, 2]]  # надо что-то решить с последовательностью замены

print(triganometry_array)