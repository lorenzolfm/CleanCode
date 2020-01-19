import requests

#Function that returns request object for a given URL
def get(url):
    request = requests.get(url)
    return request


#Function that returns request object for a given URL
def get(url):
    request = requests.get(url)
    return request.text


#======================================================
#A function that returns the factorial of n
def f(n):
    if n == 1:
        return n
    else:
        return n * f(n-1)
#vs

def factorialOf(number):
    if number == 1:
        return number
    else:
        return number * factorialOf(number - 1)

#=======================================================
#Function that detects collisions between enemies and players
def detect(self):
    #for each enemy in the enemies list
    for i in enemies.l:
        #if enemy and players hitbox are coliding
	if self.hb[1] <= i.hb[1] + i.hb[3] and self.hb[1] + self.hb[3] >= i.hb[1]:
            if self.hb[0] <= i.hb[0] + i.hb[2] and self.hb[0] + self.hb[2] >= i.hb[0]:
                #player got hit
                p.hit()
#vs

def detectCollisions(self):
    for enemy in enemies.enemies:
	if self.hitbox[1] <= enemy.hitbox[1] + enemy.hitbox[3] and self.hitbox[1] + self.hitbox[3] >= enemy.hitbox[1]:
            if self.hitbox[0] <= enemy.hitbox[0] + enemy.hitbox[2] and self.hitbox[0] + self.hitbox[2] >= enemy.hitbox[0]:
                player.hit()
