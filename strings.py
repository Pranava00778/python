msgStartGame ="Game Started!"
msgEndGame="Game Over!"
msgScore="You scored %s points!"
print(msgStartGame)
print(msgScore % 87)
print(msgEndGame)
print(id(msgStartGame)) # Address of Memory Location 
print(hex(id(msgStartGame))) # Hexadecimal of Memory Location