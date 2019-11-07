#0: house, 1: school, 2: hospital, 3: bar, 4: church, 5: theatre, 6: cinema

buildings = ['house', 'school', 'hospital', 'bar', 'church', 'theatre', 'cinema']

graph_buildings = [
    [0, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1]
]

for row in range(7):
    print(buildings[row], ':')
    for col in range(7):
        if graph_buildings[row][col] == 1:
            print(buildings[row], "<------>", buildings[col])