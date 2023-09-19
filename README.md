# python_dropncatch #

## Introduction ##

The name of this game is "Escaping Bats: Gotham Edition". It was individually designed and implemented using Python with Processing 3. 

The main aim of this project was to systematically develop a mini-game using the programming methods introduced in-class. In essence, it is a drop and catch game.

In this README.md file, I am going to dive into the Game Design and Game Implementation.

## Game Design ##

Here, I will begin by briefly introducing the mini-game. This also includes the Game Storyboard and Psuedocode.

### Scenario ###

- Drop and Catch Game​
- Batman needs to avoid getting hit by the bats and the ground.​
- If he collides with a bat or the ground three times, the game will end.

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 30 51 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/7f069071-7da0-4eb1-aad6-839be1c48dda">
</p>

### Storyboard ###

The Storyboard has three main components.

#### 1. Welcome Page ####

- Display Instructions​
- Press any key to begin the game

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 34 53 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/7878a4d6-dd90-4d38-a4b8-3ae6929aac4f">
</p>

#### 2. Game Play ####

- The player has 3 lives​
- Bats will appear from the left of the screen and move towards the right ​
- The bats will spawn at random y positions​
- For every bat avoided, the “Bat Avoided: “ number will increase by 1

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 36 06 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/2235c798-5fae-4bf0-a299-26ffd2ea4373">
</p>

- Batman can move up by clicking the mouse to avoid colliding with the bat​

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 36 35 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/5bb29f42-3ec0-4a00-8d3d-432772324876">
</p>

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 36 59 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/6005ef83-e997-42fe-989a-fc31a56e6438">
</p>

- If batman collides with the bat, then he loses a life​

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 37 18 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/1592f240-f8f0-4a16-acf8-68a1a31574fc">
</p>

- If batman collides with the ground, then he loses a life​

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 37 40 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/4c30a929-e949-486c-8e68-2ae458ce5dc3">
</p>

#### 3. Game Over ####

- If batman loses all three lives, then the game is over​
- Words “GAME OVER!” are displayed​
- The restart and exit game buttons are displayed

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 38 53 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/a79676cf-8ee9-4f78-b533-b40519175acb">
</p>

**i. Restart Game**

- If the restart game button is pressed, the game will begin from scratch​
- The instructions will be displayed again​
- If a key is pressed, the game will begin

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 39 27 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/3175cc8d-2fd5-4cd2-abd1-135819699d79">
</p>

**ii. Exit Game**

- If the exit game button is pressed, then the game window will close​

<p align="center">
<img width="524" alt="Screenshot 2023-09-20 at 3 39 40 AM" src="https://github.com/zainkoreshi/python_dropncatch/assets/139840078/a6ec5024-bb72-4516-8773-bd8be9bcaf28">
</p>

### Pseudocode ###

The pseudocode of all three main components is displayed below.

#### 1. Welcome Page ####

```
def draw():​
    draw background image​
    display game instructions

def keyPressed():​
    start game if any key is pressed
```

#### 2. Game Play ####

```
def draw():​

  draw background image​
  draw batman in centre of screen​
  draw the bat at a random y value, but fixed x position (0)​
  display the number of lives​
  display the number of bats avoided​
  move batman downwards​
  move the bats from left to right​

  for the bat, ​
    if the bat exits from the right edge​
      new bat displayed at random y value​
    if the bat passes across without touching batman​
      increase the score​
    if batman collides with the bat​
      decrease the life​
      remove the bat​
      new bat displayed at random y value​
    if batman collides with the ground​
      decrease the life
      remove the bat​
      new bat displayed at random y value​

    if lives = 0​
      stop the bat​
      stop batman​
      move to game over

    def mousePressed():​
      move batman upwards
```

#### 3. Game Over ####

```
def draw():​
  display “GAME OVER!”​
  display restart button​
  display exit button​

def mousePressed():​
  if restart button is clicked:​
    restart the game​
  if exit button is clicked​
    close the window
```
