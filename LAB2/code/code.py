processes = [
    ["P1", 3, 5],
    ["P2", 2, 4],
    ["P3", 4, 3],
    ["P4", 1, 2],
    ["P5", 5, 3]
]

order = sorted(processes, key=lambda x: x[1])

result = {}
current_time = 0
execution = []

for p in order:
    pid = p[0]
    at = p[1]
    bt = p[2]

    if current_time < at:
        current_time = at

    ct = current_time + bt
    tat = ct - at
    wt = tat - bt

    current_time = ct

    result[pid] = [ct, tat, wt]
    execution.append(pid)


print("P_ID   AT   BT   CT   TAT   WT")

for p in processes:
    pid = p[0]
    at = p[1]
    bt = p[2]

    ct = result[pid][0]
    tat = result[pid][1]
    wt = result[pid][2]

    print(f"{pid:<7}{at:<5}{bt:<5}{ct:<5}{tat:<6}{wt}")


total_tat = 0
total_wt = 0

for p in processes:
    total_tat += result[p[0]][1]
    total_wt += result[p[0]][2]

avg_tat = total_tat / len(processes)
avg_wt = total_wt / len(processes)

print()
print("AVG TAT =", avg_tat)
print("AVG WT  =", avg_wt)

print()
print("Execution Sequence:")
print(" -> ".join(execution))