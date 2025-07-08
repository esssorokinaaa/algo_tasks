def josephus_simple(n, k):
    people = list(range(n))
    index = 0
    
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    
    return people[0]

josephus_simple(13, 3)
