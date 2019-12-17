#Chapter 3: Functions
#Functions are the first line of organization in any program

#Small: The first rule of function is that they should be small. The second rule of functions is that
#they should be smaller than that

def detectCollision(player, enemy):
    if player.x == enemy.x and player.y == enemy.y:
        player.hp -= 1
        enemy.destroy()
        spawnNewEnemy()
        if player.hp <= 0:
            print("Game Over. Try Again")
            runGame = False
            window.close()

#vs

def detectCollision(player, enemy):
    if playerIsHittingEnemy():
        destroyEnemyReduceHp()
        if player.hp <= 0:
            gameOver()

#Blocks within if, else, while statements and so on should be function calls
#Indent level of a function should not be greater than one or two

#------------------------------------------------------------------------------

#Do One Thing
#Functions should do one thing. They should do it well. They should do it only.
