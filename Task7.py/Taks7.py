chocolate = [int num() for num in input().split(', ')]
milk = deque ([int num() for num in input().split(', ')])

total = 0

while chocolate and milk and totalk < 5:
    if chocolate[-1] and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolate[-1] == milk[0]:
        total += 1
        chocolate.pop()
        milk.popleft()

