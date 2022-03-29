lataFinalScore=0
goluFinalScore=0
manFinalScore=0

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

    lataFinalScore = lataFinalScore + lataScore
    goluFinalScore = goluFinalScore + goluScore
    manFinalScore = manFinalScore + manScore


print("Final Scores are: Lata-%d Golu-%d Manoj-%d"  % (lataFinalScore,goluFinalScore,manFinalScore))
print('-------------------------------')
print('GAME OVER ---------------------')
print('-------------------------------')
