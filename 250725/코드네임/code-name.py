MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = [Agent(codenames[i], scores[i]) for i in range(MAX_N)]

agents.sort(key=lambda x: x.score)

print(agents[0].codename, agents[0].score)