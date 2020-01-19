def redrawScreen():
    screen.scrollScreen()
    displayObjects()
    displayInfo()
    pygame.display.update()

def displayObjects():
    player.draw()
    player.drawBullets()
    enemies.drawBullets()
    enemies.draw()
    enemies.drawUpgrades()

def displayInfo():
    text = font.render('Score: ' + str(player.score), 1, (0,0,0))
    screen.window.blit(text,(50,10))
    pygame.draw.rect(screen.window, (255,0,0), (200,10,50,10))
    pygame.draw.rect(screen.window, (0,255,0), (200,10,50 - ((0.25*50)*(5-player.hp)),10))

#=============================================================================================
def staticEventListener(*args):
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
            endGame()
	if event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_x:
		endGame()
	if args == ():
            if event.key == pygame.K_j:
		restartGame()
	if args:
            if event.key == pygame.K_c:
		pause = False

def endGame():
    global run,gameOver,newGame,pause
    run = gameOver = newGame = pause = False

def restartGame():
    global gameOver,newGame

    gameOver = False
    newGame = False
    player.hp = 5
    player.score = 0
    player.x = 212
    player.y = 400
    enemies.enemies.clear()

#=============================================================================================

def draw(self):
    for enemy in self.enemies:
        enemy.draw()

def drawBullets(self):
    for enemy in self.enemies:
	for bullet in enemy.bullets:
	    bullet.draw()

def drawUpgrades(self):
    for upgrade in self.upgrades:
	upgrade.draw()

#=============================================================================================

clock        = pygame.time.Clock()
font         = pygame.font.SysFont('arial',20, True)
shootSound   = pygame.mixer.Sound('soundEffects/tiro.wav')
crahsSound   = pygame.mixer.Sound('soundEffects/batida.wav')
upgradeSound = pygame.mixer.Sound('soundEffects/upgrade.wav')

#vs

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial',20, True)
shootSound = pygame.mixer.Sound('soundEffects/tiro.wav')
crahsSound = pygame.mixer.Sound('soundEffects/batida.wav')
upgradeSound = pygame.mixer.Sound('soundEffects/upgrade.wav')
