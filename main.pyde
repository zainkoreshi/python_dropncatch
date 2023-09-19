def setup():
    global batman, bat, gotham, exitButton, restartButton
    global batmanX, batmanY, batmanW, batmanH
    global posGotham, speedGotham
    global stageNum
    global lives, score
    global numBats, bat
    global batW, batH, batX, batY, batDx, batDy
    global heart
    global heartW, heartH, heartX, heartY, heartDx, heartDy
    global heartVisible
    
    # size of the window
    size(750, 500)
    
    # load images
    batman = loadImage("batman.png")
    gotham = loadImage("gotham.png")
    exitButton = loadImage("exit.png")
    restartButton = loadImage("restart.png")
    
    # batman dimensions
    batmanX = 345
    batmanY = 220
    batmanW = 60
    batmanH = 90
    
    # to make background/gotham move
    posGotham = 0
    speedGotham = -0.75
    
    # stageNum controls the stage
    #  0: Welcome page
    #  1: Game Play   
    #  2: Game Over  
    stageNum = 0
    
    # beginning number of lives
    lives = 3
    score = 0
    
    # load bats, bat dimensions and speed
    numBats = 10
    bat = []
    batW = []
    batH = []
    batX = []
    batY = []
    batDx = []
    batDy = []
    for i in range(numBats): 
        scale = random(0.01, 0.02)
        bat.append(loadImage("bat" + str(i)+".png"))
        batW.append(bat[i].width * scale)
        batH.append(bat[i].height * scale)
        batX.append(random(-width/2, 0))
        batY.append(random(0, height-batH[i]))
        batDx.append(random(0.1, 0.5))
        batDy.append(random(-0.5, 0.5))
        
    # load hearts, heart dimensions and speed
    heart = loadImage("heart0.png")
    scale = 0.01
    heartW = heart.width * scale
    heartH = heart.height * scale
    heartX = random(-width/2, 0)
    heartY = random(0, height-heartH)
    heartDx = random(0.1, 0.5)
    heartDy = random(-0.5, 0.5)
    heartVisible = False
                    
def draw():
    global posGotham
    
    # to make background/gotham move
    image(gotham, posGotham, 0, width, height*1.15)
    image(gotham, width+posGotham, 0, width, height*1.15)
    posGotham = posGotham + speedGotham
    if (posGotham <= -width):
        posGotham = 0
    
    # the different stages of the game
    if (stageNum == 0):
        drawWelcome()
    elif (stageNum == 1) :
        drawGamePlay()
    elif (stageNum == 2) :
        drawGameOver()
        
def drawWelcome():
    global stageNum
    
    # game instructions
    fill(0)
    rect(5, 10, 100, 20)
    rect(5, 30, 330, 20)
    rect(5, 50, 397, 20)
    rect(5, 70, 273, 20)
    rect(5, 90, 380, 20)
    fill(255)
    textSize(15)
    textAlign(LEFT, TOP)
    text("How to play:", 10, 10)
    text("- Click on the mouse to make Batman jump.", 10, 30)
    text("- Do not collide with white bats or touch the ground.", 10, 50)
    text("- Collect hearts to gain an extra life.", 10, 70)
    text("- You have three lives, try to score as many points!", 10, 90)
    
    # game name
    fill(0)
    rect(70, 155, 610, 60)
    fill(255)
    textSize(40)
    textAlign(CENTER)
    text("Escaping Bats: Gotham Edition", width/2, 200)
    
    # draw batman
    image(batman, batmanX, batmanY, batmanW, batmanH)
    
    # how to begin playing
    fill(0)
    rect(565, 470, 180, 20)
    fill(255)
    textSize(15)
    textAlign(RIGHT, TOP)
    text("Press any key to begin!", 740, 470)
    
    # move to next stage
    if keyPressed == True:
        stageNum = stageNum + 1
        
def drawGamePlay():
    global stageNum
    global lives, score
    global batmanX, batmanY
    global heart
    global heartW, heartH, heartX, heartY, heartDx, heartDy
    global heartVisible

    # move to next stage
    if lives == 0:
        stageNum = stageNum + 1
    else:
        # draw batman
        image(batman, batmanX, batmanY, batmanW, batmanH)
        
        # batman falls
        batmanY = batmanY + 1
        
        # lift batman
        if batmanY > 0:
            if mousePressed == True:
                batmanY = batmanY - 2
                        
        # bats move
        for i in range(numBats):
            image(bat[i], batX[i], batY[i], batW[i], batH[i])
            batX[i] = batX[i] + batDx[i]
            batY[i] = batY[i] + batDy[i]
        
            if (batY[i] < 0):
                batY[i] = 0
                batDy[i] = -batDy[i]
            elif (batY[i] + batH[i] > height):
                batY[i] = height - batH[i]
                batDy[i] = -batDy[i]
                
            if (batX[i] > width):
                scale = random(0.01, 0.02)
                batW[i] = bat[i].width * scale
                batH[i] = bat[i].height * scale
                batX[i] = -batW[i]
                batY[i] = random(0, height-batH[i])
                batDx.append(random(0.1, 0.5))
                batDy.append(random(-0.5, 0.5))
                
            # when to deduct lives
            # colliding with bat or ground
            if (batY[i] + batH[i] >= batmanY and batY[i] <= batmanY + batmanH and batX[i] + batW[i] >= batmanX and batX[i] <= batmanX + batmanW) or (batmanY + batmanH == height):
                lives = lives - 1
                batmanX = 345
                batmanY = 220
                
            # code for score
            score = score + batW[i] * batH[i] * 0.000005
             
        # if score becomes multiple of 25 then heart comes
        if int(score) % 25 == 0 and int(score) != 0:
             heartVisible = True
             
        if heartVisible == True:
            image(heart, heartX, heartY, heartW, heartH)
            heartX = heartX + heartDx
            heartY = heartY + heartDy
        
            if (heartY < 0):
                heartY = 0
                heartDy = - heartDy
            elif (heartY + heartH > height):
                heartY = height - heartH
                heartDy = - heartDy
                
            # colliding with heart adds life and makes heart disappear
            if (heartY + heartH >= batmanY and heartY <= batmanY + batmanH and heartX + heartW >= batmanX and heartX <= batmanX + batmanW):
                lives = lives + 1
                heartX = - width
                
                # image effect
                for y in range(0, batman.height, 1):
                    for x in range(0, batman.width, 1):
                        # get colour values
                        r = red(batman.get(x, y))
                        g = green(batman.get(x, y))
                        b = blue(batman.get(x, y))
                        
                        ''' image processing goes here '''
                        r = g
                        g = b
                        b = r
                        
                        # set new colour to the pixel
                        batman.set(x, y, color(r, g, b))
                        
                    #display the image
                    image(batman, batmanX, batmanY, batmanW, batmanH)
                    
                heartVisible = False
                    
        # display lives and score
        fill(0)
        rect(5, 10, 85, 20)
        rect(5, 30, 85, 20)
        fill(255)
        textSize(15)
        textAlign(LEFT, TOP)
        text("Lives:" + str(lives), 10, 10)
        text("Score:" + str(int(score)), 10, 30)
        
def drawGameOver():
    # display game over
    fill(255, 0, 0)
    textSize(100)
    textAlign(CENTER)
    text("GAME OVER!", width/2, height/3)
    
    # display score
    fill(0, 255, 0)
    textSize(50)
    textAlign(CENTER)
    text("Your score: " + (str(int(score))), width/2, height/2)
    
    # display restart and end game button
    fill(0, 255, 0)
    rect(width/2 - 225, height/3 * 2 - 25, 150, 150)
    image(restartButton, width/2 - 225, height/3 * 2 - 25, 150, 150)
    
    fill(255, 0, 0)
    rect(width/2 + 75, height/3 * 2 - 25, 150, 150)
    image(exitButton, width/2 + 75, height/3 * 2 - 25, 150, 150)

    # code for next steps
    if mousePressed == True:
        # if restart button pressed
        if mouseX > width/2 - 225 and mouseX < width/2 - 225 + 150 and mouseY > height/3 * 2 - 25 and mouseY < height/3 * 2 - 25 + 150:
            setup(),
        # if end game button pressed
        elif mouseX > width/2 + 75 and mouseX < width/2 + 75 + 150 and mouseY >  height/3 * 2 - 25 and mouseY <  height/3 * 2 - 25 + 150:
            exit()
