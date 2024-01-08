import turtle as t
starting_positions=[(0,0),(-20,0),(-40,0)]
move_distance=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
  def __init__(self): 
    self.segments=[]
    self.create_snake()
    
    
  def create_snake(self):
      for i in starting_positions:
        self.add_segment(i)
        
  def add_segment(self,i):
    timmy=t.Turtle("square")
    timmy.color("white")
    timmy.penup()
    timmy.goto(i)
    self.segments.append(timmy)
    
  def extend(self):
    #we add segment after each time when food is eaten  
    self.add_segment(self.segments[-1].position())
    #position is method in turtle returns its position
  def move(self):
      for seg in range(len( self.segments)-1 ,0 ,-1 ):
           x= self.segments[seg-1].xcor()
           y= self.segments[seg-1].ycor()
           self.segments[seg].goto(x,y)
      self.segments[0].forward(move_distance)
  def up(self):
    if(self.segments[0].heading()!=DOWN):
      self.segments[0].setheading(UP)
     
  def down(self):
    if(self.segments[0].heading()!=UP):
      self.segments[0].setheading(DOWN)
     
  def left(self):
     if(self.segments[0].heading()!=RIGHT):
      self.segments[0].setheading(LEFT)
     
  def right(self):
     if(self.segments[0].heading()!=LEFT):
        self.segments[0].setheading(RIGHT) 
  def reset(self):
    for seg in self.segments:
      seg.goto(1000,1000)
    self.segments.clear()
    self.create_snake()
    