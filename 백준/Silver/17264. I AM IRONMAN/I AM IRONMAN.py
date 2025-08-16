game_count, hacked_player = map(int, input().split())
Wpoint, Lpoint, target = map(int, input().split())
Wplayer = []
isIron = True
currScore = 0

for i in range(hacked_player):
    name, result = map(str, input().split())
    if result == "W":
        Wplayer.append(name)

for j in range(game_count):
    name = input()
    if Wplayer.count(name) != 0:
        currScore += Wpoint
        if currScore >= target:
            isIron = False
    else:
        if currScore <= Lpoint:
            currScore = 0
        else:
            currScore -= Lpoint

if isIron == True:
    print("I AM IRONMAN!!")
else:
    print("I AM NOT IRONMAN!!")