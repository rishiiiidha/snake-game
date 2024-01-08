from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
mysrc=Screen()
mysrc.setup(width=600,height=600)
mysrc.bgcolor("black")
mysrc.title("SNAKE GAME")
mysrc.tracer(0) #off
snake=Snake()
foood=Food()
score=Scoreboard()
count=0
mysrc.listen()
mysrc.onkey(snake.up,"Up")
mysrc.onkey(snake.down,"Down")
mysrc.onkey(snake.left,"Left")
mysrc.onkey(snake.right,"Right")
game=True
while game:
  mysrc.update() #will update after each variation made like a picutre picutre repeats m
  time.sleep(0.1) # 1 second delay 
  snake.move()
  #collision with food 
  #comparing distance between one turtle to other turtle using distance attritbute
  if(snake.segments[0].distance(foood)<15):
    foood.refresh()
    snake.extend()
    score.scoreincrement()
  if snake.segments[0].xcor()<-290 or  snake.segments[0].xcor()>290 or snake.segments[0].ycor()<-290 or snake.segments[0].ycor()> 290:
    snake.reset()
    score.reset()
  #detect collision with tail
  #if head collides with anysegment game over
  for segment in snake.segments[1:]:
    if(snake.segments[0].distance(segment)<10):
      snake.reset()
      score.reset()
 
   
mysrc.exitonclick()
