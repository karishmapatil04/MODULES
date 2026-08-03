# Job Sequencing Problem – Loss Minimization using Backtracking

def calculateLoss(order, time, loss):
    total_loss = 0
    current_time = 0

    for job in order:
        current_time += time[job]
        total_loss += loss[job] * current_time

    return total_loss


def backtrack(order, used, n, time, loss):
    global min_loss, best_order

    if len(order) == n:
        total = calculateLoss(order, time, loss)
        if total < min_loss:
            min_loss = total
            best_order = order[:]
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            order.append(i)
            backtrack(order, used, n, time, loss)
            order.pop()
            used[i] = False


# Main Program
n = int(input("Enter number of jobs: "))

time = []
loss = []

for i in range(n):
    t = int(input(f"Enter processing time of Job {i+1}: "))
    l = int(input(f"Enter loss per unit time of Job {i+1}: "))
    time.append(t)
    loss.append(l)

min_loss = float('inf')
best_order = []

used = [False] * n

backtrack([], used, n, time, loss)

print("\nOptimal Job Sequence:")
for job in best_order:
    print("Job", job + 1, end=" ")

print("\nMinimum Total Loss:", min_loss)