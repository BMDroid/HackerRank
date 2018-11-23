# https://www.hackerrank.com/challenges/angry-professor/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def angryProfessor(k, a):
    c = sum(list(map(lambda x: x <= 0, a)))
    print('NO' if c >= k else 'YES')
