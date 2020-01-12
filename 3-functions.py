#Chapter 3: Functions
#Functions are the first line of organization in any program

#Small: The first rule of function is that they should be small. The second rule of functions is that
#they should be smaller than that

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
        b.destroy()
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

#Blocks within if, else, while statements and so on should be function calls
#Indent level of a function should not be greater than one or two

#------------------------------------------------------------------------------

#Do One Thing
#Functions should do one thing. They should do it well. They should do it only.
