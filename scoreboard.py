from turtle import Turtle ,Screen
class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    self.high=0
    self.hideturtle()
    self.penup()
    self.color("white")
    self.scoreboard()
  def scoreboard(self):
    self.clear()
    self.goto(0,270) 
    self.message1=f"Score : {self.score} High Score: {self.high}"
    self.write(self.message1,move=False,align="center", font=('Courier', 15, 'bold'))
  def reset(self):
    # self.clear()
    if(self.high<self.score):
      self.high=self.score
    self.score=0
    self.scoreboard()
  def scoreincrement(self):
    self.score+=1
    self.scoreboard()
  # def game_over(self):
  #   self.goto(0,0) 
  #   self.write("GAME OVER",move=False,align="center", font=('Courier', 15, 'bold'))
    
    
    
    
