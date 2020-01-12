def detect(a, b):
    if a.x == b.x and a.y == b.y:
        a.hp -= 1
        b.delete()
        if a.hp <= 0:
            runBool = False
            w.close()

#vs

def detectCollision(player, enemy):
    if player.x == enemy.x and player.x == enemy.y:
        player.hp -= -1
        enemy.destroy()
        if player.hp <= 0:
            runGame = False
            window.close()

#vs

def detectCollisionBetweenPlayerAndEnemy(player,enemy):
    if playerIsHittingEnemy():
        ReducePlayerHp()
        enemy.destroy()
        if player.health <= 0:
            gameOver()

#--------------------------------------------------------

def redrawGameScreen():
    drawObjects()
    drawBackground()

def drawObjects():
    drawPlayer()
    drawEnemies()

def drawPlayer():
    x,y = getPlayerPosition
    draw(player,x,y)

def drawEnemies():
    for enemy in enemies:
        drawEnemy()

#--------------------------------------------------------

def assertEquals(expected, actual):
    if expected == actual: return True
    else: return False

#--------------------------------------------------------

def makeCircle(x,y,radius):
    pass

#vs

def makeCircle(center,radius):
    pass

#--------------------------------------------------------

def write(something):

#vs

def writeField(name)

#--------------------------------------------------------

def checkPassword(username,password):
    user = User.findByName(username)
    if user:
        if user.password == password:
            Session.initialize()
            return True
        else:
            return False

#--------------------------------------------------------

def displayGameOverMessage():
    return "Game Over!"

def displayWelcomeMessage():
    return "Welcome!"

#vs

def display(message):
    return message
