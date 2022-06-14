from asyncore import write
from tkinter import font
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ('high_scores.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()
    
    def write_highscore(self):
        with open ('high_scores.txt','w') as file:
            file.write(f"{self.high_score}")