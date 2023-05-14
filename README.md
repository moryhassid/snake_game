# Snake game


<p align="center">
  <img src="images\animation_snake.gif" width="300">
</p


Welcome to my game, I have implemented the game "Snake".
Here you can see there are multiple stages of difficulties.
Moreover, I have added a scoreboard using pandas.

I have added a **"super-power"** for the snake, snake is rewarded after 4 points it earned,
so it will be able to jump from one screen's edge/boundary to the other.  


When executing the game you will be requested to enter your name,
afterwards a timer will start and your snake will need to eat all the apple
(red circle)


In the end of the game you will get your position in the scoreboard.

**Sketches and brainstorming**

## First Page:

In the page, we see the snake in several positions each position in a different 
time slice/slot. We can easily see the snake moves on the **horizontal axis**.

| Time Slice | Apple's Position | Snake head's position | Snake's length |
|------------|------------------|-----------------------|----------------|
| 1 sec      | (4,4)            | (4,6)                 | 1              |
| 2 sec      | (4,4)            | (4,5)                 | 1              |
| 3 sec      | -                | (4,4)                 | 2              |
| 4 sec      | (4,2)            | (4,3)                 | 2              |
| 5 sec      | -                | (4,2)                 | 3              |

is a single joint (head), 
in the time slice t=1sec we see the apple in position (4,4)

<p align="center">
  <img src="images\1.jpg" width="400">
</p>


## Second Page:

This page describes a more complex scenario
which the snake eats the apple and moves from the horizontal axis to the vertical axis.
Here we are exploring how the body of the snake (joints) should move in the game. 

| Time Slice | Apple's Position | Snake head's position | Snake's length |
|------------|------------------|-----------------------|----------------|
| 1 sec      | (4,5)            | (3,5)                 | 2              |
| 2 sec      | -                | (4,5)                 | 3              |
| 3 sec      | -                | (5,5)                 | 3              |
| 4 sec      | -                | (6,5)                 | 3              |

<p align="center">
  <img src="images\2.jpg" width="400">
</p>

Good Luck!
