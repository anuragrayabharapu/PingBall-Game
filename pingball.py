from tkinter import * 
import random
import time 
class Ball():
    def __init__(self,tk, canvas, paddle, color):
        self.canvas = canvas
        self.tk=tk

        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100) 
        starts = [-3, -2, -1, 1, 2, 3] 
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.summ=3
        self.hit=0
    def score(self):
        
        score_label=Label(self.tk)
        #print(type(self.hit))
        score_text="score:"+str(self.hit)
        score_label.config(text= score_text,font=('courier',12,'bold'),foreground='black',background='#87CEFA')
        score_label.place(relx=0.0,rely=0.0,anchor='nw')
    def life(self):
        if self.summ==0:
            self.canvas.create_text(245,100,text="Game odipoyinav bro lite tisko", fill='red')
            time.sleep(3)
            self.tk.destroy()
            
        life_label=Label(self.tk)
        life_text="lifes:"+str(self.summ)
        life_label.config(text= life_text,font=('courier',12,'bold'),foreground='black',background='#87CEFA')
        life_label.place(relx=1.0,rely=0.0,anchor='ne')
        

    def reset_ball(self):
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id,245,100)
        reposition = [-3, -2, -1, 1, 2, 3] 
        random.shuffle(reposition)
        self.x = reposition[0]
        self.y = -3
        tk.update_idletasks() 
        tk.update()
        time.sleep(0.01)
                
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.hit=self.hit+1
                return True
        return False
    
    def draw(self):
        self.score()
        self.canvas.move(self.id, self.x, self.y) 
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.summ=self.summ-1
            self.life()            
            self.canvas.move(self.id,245, 100)
            del self.id
            self.reset_ball()
            paddle.reset_paddle()
            y=self.canvas.create_text(250,245,text="Game Over",font=('courier',15,'bold'), fill='black')
            tk.after(600,canvas.delete,y)
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3         
            
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def reset_paddle(self):
        self.canvas.move(self.id, 200, 300)
        del self.id
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill='blue')
        self.canvas.move(self.id, 200, 300)
        self.x = 0
    def draw(self):
        self.canvas.move(self.id, self.x, 0) 
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 2
        elif pos[2] >= self.canvas_width:
            self.x = -2        
    def turn_left(self, evt): 
        self.x = -3
    def turn_right(self, evt): 
        self.x = 3
def butttonn():
    #ball.score()
    ball.life()
    butttonn.btn=Button(tk,text='Play Game',bg='orange')
    butttonn.btn['command']=lambda binst=butttonn.btn: start(binst)
    butttonn.btn.place(relx=0.5,rely=0.5,anchor=CENTER)
    ball.hit_bottom=False
    
def start(binst):
    binst.destroy()
    while ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        if ball.hit_bottom==True:
            break
    if ball.hit_bottom==True:
        butttonn()   
    ball.hit_bottom=False
tk = Tk()
tk.title("Game") 
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0,background='#87CEFA') 
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue') 
ball = Ball(tk,canvas, paddle, 'red')
butttonn()



        
