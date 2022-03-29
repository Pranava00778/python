finalScores = {"Lata":0, "Golu":0,"Manoj":0}

for c in range(1,4):
    print("===============================")
    print("Game ROUND:",c)
    print("-------------------------------")

    lataScore = 0
    while lataScore <= 0 or lataScore > 10 : # This will keep asking for a number between 1 and 9
        lataScore = int(input("Enter Score of Lata (1-9): "))
    
    goluScore =0
    while goluScore <=0 or goluScore>10:
        goluScore = int(input("Enter Score of Golu (1-9): "))

    manScore=0
    while manScore <=0 or manScore > 10:    
        manScore = int(input("Enter Score of Manoj (1-9): "))

    finalScores["Lata"] = finalScores["Lata"] + lataScore
    finalScores["Golu"] = finalScores["Golu"] + goluScore
    finalScores["Manoj"] = finalScores["Manoj"] + manScore

orderedResults = sorted(finalScores, key=finalScores.get, reverse = True)
print('-------------------------------')
print("Final Scores are:", orderedResults ,finalScores)
print("😎 WINNER: ", orderedResults[0], " with score: ", finalScores[orderedResults[0]])
print("👍 Runner: ", orderedResults[1], " with score: ", finalScores[orderedResults[1]])
print('-------------------------------')
print('GAME OVER ---------------------')
print('-------------------------------')
