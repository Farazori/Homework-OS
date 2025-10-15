n = int(input("Enter number of processes: "))
CS = int(input("Context switch time (enter 0 if none): "))
processes = []

for i in range(n):
    print(f"\nProcess {i+1}:")
    arrival = int(input("Arrival Time: "))
    burst = int(input("Burst Time: "))
    processes.append([f"P{i+1}", arrival, burst])

processes.sort(key=lambda x: x[1])

min_arrival = processes[0][1]
if min_arrival != 0:
    for p in processes:
        p[1] -= min_arrival

time = 0
total_wait = 0
gantt = []

print("\nFCFS Scheduling Result:")
print("Process | Arrival | Burst | Start | Finish | Waiting")

for p in processes:
    start = max(time, p[1])
    finish = start + p[2]
    waiting = start - p[1]
    total_wait += waiting
    time = finish
    if p != processes[-1]:
        time += CS

    gantt.append((p[0], start, finish))

    print(f"{p[0]:>7} | {p[1]:>7} | {p[2]:>5} | {start:>5} | {finish:>6} | {waiting:>7}")

avg_wait = total_wait / n
print(f"\nAverage Waiting Time: {avg_wait:.2f}")


# Gantt Chart
print("\n📊 Gantt Chart:")
for g in gantt:
    print(" ", "-" * (g[2] - g[1]), end="")
print()
for g in gantt:
    print(f"|{g[0]:^{g[2] - g[1]}}", end="")
print("|")
for g in gantt:
    print(" ", "-" * (g[2] - g[1]), end="")
print()
for g in gantt:
    print(f"{g[1]:>2}", end=" " * (g[2] - g[1]))
print(f"{gantt[-1][2]:>2}")
