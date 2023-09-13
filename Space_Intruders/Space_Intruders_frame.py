
import tkinter as Tk
from PIL import ImageTk,Image
import time,random,math,os

shift = 0
shift_dir = 0
circle_row = 0
circle_nr = 0
clock = 0
lives = 3
HS_game = 0
win_lose = 0
enemy_matrix = [[3,3,3,3,3,3,3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1]]
enemies = []
shots = []
enemy_shots=[]
SI_houses = []
player_char = []
tank_move = "STOP"
tank_pos = 320
Game_run = None

class Highscore:
    def __init__(self,parent):
        super().__init__()
        global strt_time,HS_game
        self.master = parent
        self.master.geometry("800x640")
        self.frame = Tk.Frame(self.master,bg="black")
        HS_board = self.round_rectangle(40, 40, 800, 640, radius=20, fill="green")
        Hs_data  = self.HS_table()
        for data in range(len(Hs_data())):
            temp_data = Hs_data[data]
            sepr = temp_data.find(" ")
            temp_player = temp_data[:sepr]
            temp_score = temp_data[sepr:]
            temp_player_lbl = Tk.Label(self.master,text=temp_player)
            temp_player_lbl.place(x=100,y=40 + 20 * data)
            temp_score_lbl = Tk.Label(self.master,text=temp_score)
            temp_score_lbl.place(x=100,y=40 + 20 * data)
        self.replay_btn = Tk.Button(self.master,image=pics[29],borderwidth=0,compound="bottom",command=self.replay)
        self.quit_btn = Tk.Button(self.master,image=pics[30],borderwidth=0,compound="bottom",command=self.quit)
        
        self.frame.pack()
        


    def round_rectangle(x1, y1, x2, y2, radius, **kwargs):
        
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        return Tk.Canvas.create_polygon(points, **kwargs, smooth=True)
    
    def HS_table():
        data = os.open("HS_Score.csv")
        scores = []
        i = 0
        while i <= len(data):
            x =  data.find(",")
            score = data[i:x]
            scores.append(score)
            i = x
        return scores

    
class Mainmenu:
    def __init__(self, parent, *args, **kwargs):
        self.master = parent
        self.master.geometry("400x350+20+20")
        self.frame = Tk.Frame(self.master,bg="black")
        self.NewGame_btn = Tk.Button(self.master,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="New Game",command=self.newGame)
        self.NewGame_btn.pack(fill='both',expand=False)
        self.OptionsGame_btn = Tk.Button(self.master,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="Options",command=self.quitGame)
        self.OptionsGame_btn.pack(fill='both',expand=False)
        self.CreditsGame_btn = Tk.Button(self.master,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="Credits",command=self.quitGame)
        self.CreditsGame_btn.pack(fill='both',expand=False)
        self.QuitGame_btn = Tk.Button(self.master,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="Quit Game",command=self.quitGame)
        self.QuitGame_btn.pack(fill='both',expand=False)
        self.frame.pack()
    
    def newGame(self):
        global Game_run,shift,shift_dir,clock,lives,HS_game,lives_c_Label
        shift = 0
        shift_dir = 0
        clock = 0
        lives = 3
        lives_c_Label = []
        Game_session = Tk.Toplevel()
        Game(Game_session)
        Game_run = Game_session
        self.master.update()
        
    def quitGame(self):
        self.master.destroy()
        
        
#HsMenu = Tk.Toplevel(root=root).pack(side="top", fill="both", expand=True)
## def GameWindow and hide it may be lock timers !!!
## Class Rework Version
class Game:
    def __init__(self,parent):
        super().__init__()
        global strt_time,pics,player_char
        self.master = parent
        self.master.geometry("800x680")
        self.frame = Tk.Frame(self.master,height=680,width=800,padx=40,pady=40,bg="black")
        for house in range(4):
            t_house = Tk.Label(self.master,image=pics[9],borderwidth=0,height=18,width=12)
            t_house_x = 60 + 180 * house
            t_house_state = 4
            t_house.place(x=t_house_x,y=550)
            temp = [t_house,t_house_x,550,t_house_state,[t_house_x,568,t_house_x+12,568]]
            SI_houses.append(temp)
        for row in range(len(enemy_matrix)):
            for col in range(len(enemy_matrix[row])):
                if enemy_matrix[row][col] == 3:
                    enemy = Tk.Label(self.master,image=pics[26],borderwidth=0,)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                if enemy_matrix[row][col] == 2:
                    enemy = Tk.Label(self.master,image=pics[19],borderwidth=0)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                if enemy_matrix[row][col] == 1:
                    enemy = Tk.Label(self.master,image=pics[24],borderwidth=0)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                print(enemy_meta)
        
        self.heroTank = Tk.Label(self.master,image=pics[5],borderwidth=0)
        self.heroTank.place(x=320,y=600)
        player_char.append(self.heroTank)
        player_char.append(0)
        strt_time = time.strftime("%H:%M:%S")

        self.HUD_Frame = Tk.LabelFrame(self.master,height=20,width=640,background="Black",borderwidth=0)
        self.HUD_Frame.pack(side="top",fill="both",expand=False)
        self.HS_Label = Tk.Label(self.HUD_Frame,font="arial 15 bold",text="000000",foreground="grey",background="black")
        self.HS_Label.pack(side="left")
        self.Killcount_Lable= Tk.Label(self.HUD_Frame,font="arial 15 bold",text="0",foreground="white",background="black",image=pics[25],compound="left")
        self.Killcount_Lable.pack(side="left")

        for i in range(3):
            Lives_Label = Tk.Label(self.HUD_Frame,image=pics[28],borderwidth=0)
            Lives_Label.pack(side="right")
            lives_c_Label.append(Lives_Label)

        self.frame.pack()
        self.moveEnemy()
        self.moveShot()
        self.shotEnemy()
        self.UpdateLabels()
        return
    

    def UpdateLabels(self):
        global lives,strt_time,enemies,lives_c_Label,HS_Label,win_lose
        act_time = time.strftime("%H:%M:%S")
        act_time_h = int(act_time[0:2])
        strt_time_h = int(strt_time[0:2])
        act_time_min = int(act_time[3:5])
        strt_time_min = int(strt_time[3:5])
        act_time_sec = int(act_time[6:8])
        strt_time_sec = int(strt_time[6:8])
        if strt_time_h == act_time_h:
            game_time_h = 0
        if strt_time_h < act_time_h:
            game_time_min = act_time_min + 60*(act_time_h-strt_time_h)
        else:
            game_time_min = act_time_min-strt_time_min
        if strt_time_min < act_time_min:
            game_time_sec = act_time_sec + 60*(act_time_min-strt_time_min) + 360 * game_time_h
        else:
            game_time_sec = act_time_sec-strt_time_sec + 60 * game_time_h
        HS = str(game_time_sec * 5)
        self.HS_Label.configure(text=HS)
        KillCount = str(48 - len(enemies))
        self.Killcount_Lable.configure(text=KillCount)
        for l in range(len(lives_c_Label)):
            n = len(lives_c_Label)
        if n-l > lives:
            lives_c_Label[n-l].destroy()
    
        #HS Screen back to Mainmenu if Enemy got 2 mutch time kill all enemies or lost all lives or houses
        if KillCount == 48 :
            win_lose = 1
            Hs_window = Tk.Toplevel()
            Highscore(Hs_window)
            self.master.destroy()
        if lives == 0:
            Hs_window = Tk.Toplevel()
            Highscore(Hs_window)
            self.master.destroy()
        self.master.update_idletasks()
        self.master.after(1000,self.UpdateLabels)
        return
    
    def moveShot(self):
        global shots,enemies,enemy_matrix,Game_run
        shift = 0
        kills = ["None"]
        if shift == 0:
            for shot in range(len(shots)):
                t_shot = shots[shot]
                t_shot[0].place_forget()
                shift=1
        if shift == 1:
            for shot in range(len(shots)):
                temp_shot = shots[shot]
                t_shot_x = temp_shot[1]
                t_shot_y = temp_shot[2] - 5
                temp_shot[0].place(x=t_shot_x,y=t_shot_y)
                shots[shot] = [temp_shot[0],t_shot_x,t_shot_y]
                for confl in range(len(enemies)):
                    temp_ene = enemies[confl]
                    r2 = (temp_ene[1] - t_shot_x) * (temp_ene[1] - t_shot_x) + (temp_ene[2] - t_shot_y) * (temp_ene[2] - t_shot_y)
                    if r2 <= 40:
                        m = confl%12
                        n = int(confl/12) * 1
                        if enemy_matrix[n][m] == 3:
                            temp_ene[0].configure(image=pics[25])
                        if enemy_matrix[n][m] == 2:
                            temp_ene[0].configure(image=pics[18])
                        if enemy_matrix[n][m] == 1:
                            temp_ene[0].configure(image=pics[23])
                        temp_ene[3] = "Dead"
                        enemies[confl] = temp_ene
                        kills = shots[shot]
                        shots[shot][0].configure(image=pics[27])
                    shift=0
            if kills[0] != "None":    
                shots.remove(kills)
                kills[0].destroy()
                    
        self.master.update_idletasks() 
        self.master.after(100,self.moveShot)
        return
    
    def shotEnemy(self):
        global enemy_shots,clock,tank_pos,circle_row,circle_nr,SI_houses,lives,Game_run
        shift = clock%2
            
        if shift == 0:
            for shot in range(len(enemy_shots)):
                temp_shot = enemy_shots[shot]
                temp_shot[0].place_forget()
        if shift == 1:
            for shot in range(len(enemy_shots)):
                temp_shot = enemy_shots[shot]
                temp_shot[1] = int(temp_shot[1] + 5 * math.cos(temp_shot[3]))
                temp_shot[2] = int(temp_shot[2] + 5 * math.sin(temp_shot[3]))
                temp_shot[0].place(x=temp_shot[1],y=temp_shot[2])
                if temp_shot[1] < 0:
                    temp_shot[0].destroy()
                    enemy_shots.remove(temp_shot)
                    break
                if temp_shot[2] > 660:
                    temp_shot[0].destroy()
                    enemy_shots.remove(temp_shot)
                    break
                else:
                    enemy_shots[shot] = temp_shot
                print(temp_shot)
            for shot in range(len(enemy_shots)):
                temp = enemy_shots[shot]
                for confl in range(len(SI_houses)):
                    temp_spot_x = (int(temp[1] + 5 * math.sin(temp[3])) - SI_houses[confl][4][0]) * SI_houses[confl][4][2]
                    temp_spot_y = (int(temp[2] + 5 * math.cos(temp[3])) - SI_houses[confl][4][1]) * SI_houses[confl][4][3]
                    r = math.sqrt(math.pow(temp_spot_x,2)+math.pow(temp_spot_y,2))
                    t_r_x = tank_pos - temp_spot_x
                    t_r_y = 600 - temp_spot_y
                    r_tank = math.sqrt(math.pow(t_r_x,2)+math.pow(t_r_y,2))
                    if r_tank < 5:
                        self.heroTank.configure(image=pics[7])
                        lives = lives - 1
                    if r !=0:
                        continue
                    if SI_houses[confl][3] == 4:
                        SI_houses[confl][0].configurate(image=pics[10])
                        SI_houses[confl][3] = 3
                    if SI_houses[confl][3] == 3:
                        SI_houses[confl][0].configurate(image=pics[11])
                    SI_houses[confl][3] = 2
                    if SI_houses[confl][3] == 2:
                        SI_houses[confl][0].configurate(image=pics[12])
                        SI_houses[confl][3] = 1
                    if SI_houses[confl][3] == 1:
                        SI_houses[confl][0].destroy()
                    temp[0].destroy()
                        
        self.master.update_idletasks()
        self.master.after(100,self.shotEnemy)
        return
    
    def moveEnemy(self):
        global shift,enemies,circle_nr,tank_move,tank_pos,shift_dir,circle_row,loaded,clock,Game_run,enemy_shots
        kills = []
        if shift == 0:
            for data in range(len(enemies)):
                temp_enemy = enemies[data]
                temp_enemy[0].place_forget()
        if shift == 1:
            for ene in range(len(enemies)):
                temp_remov = enemies[ene]
                if temp_remov[3] == "Dead":
                    kills.append(enemies[ene])
            for kill in range(len(kills)):
                enemies.remove(kills[kill])
                kills[kill][0].destroy()
            for data in range(len(enemies)):
                temp = enemies[data]
                print(enemies[data])
                if shift_dir == 0:
                    temp_x = temp[1] + 5
                if shift_dir == 1:
                    temp_x = temp[1] - 5
                temp_y = temp[2] + circle_row
                temp[0].place(x=temp_x,y=temp_y)
                temp[1] = temp_x
                enemies[data] = temp
            if circle_nr >= 100 and shift_dir == 0:
                shift_dir = 1
                circle_row = circle_row + 1
            if circle_nr < 0 and shift_dir == 1:
                shift_dir = 0
                circle_row = circle_row + 1
            if shift_dir == 1:
                circle_nr = circle_nr - 1    

            if shift_dir == 0:
                circle_nr = circle_nr + 1
        clock = clock + 1        
        shift = clock%2
        if len(enemy_shots) < 3 :
            n = random.randint(0,1)
            if n == 1:
                temp_shot_x = 140 + circle_nr
                temp_shot_y = 43 + circle_row
                temp_spot_x = self.heroTank.winfo_rootx() - temp_shot_x
                temp_spot_y = 600 - temp_shot_y
                temp_shot_ang = math.tan((temp_spot_y/temp_spot_x)) + math.pi
                temp_pic = Image.open("SI_Alienshot_1.png")
                temp_ang_pic = temp_pic.rotate(temp_shot_ang)
                ## Time 2 wonder ^^
                e_fire = len(enemy_shots)
                temp_path = "alienshot"+ str(e_fire) + ".png"
                temp_ang_pic.save(temp_path)
                load = Image.open(temp_path)
                temp_shot_pic = ImageTk.PhotoImage(load)
                temp_shot = []
                temp_enemy_shot = Tk.Label(self.master,image=temp_shot_pic,borderwidth=0)
                temp_enemy_shot.place(x=temp_shot_x,y=temp_shot_y)
                temp_shot.append(temp_enemy_shot)
                temp_shot.append(temp_shot_x)
                temp_shot.append(temp_shot_y)
                temp_shot.append(temp_shot_ang)
                temp_shot.append(temp_shot_pic)
                enemy_shots.append(temp_shot)
        self.master.update_idletasks()
        self.master.after(1000,self.moveEnemy)
        return
    
def rechts(event):
    global tank_move,tank_pos,Game_run,player_char
    if Game_run != None:
        shift = 0
        tank_move = "RIGHT"
        tank_pos = tank_pos + 5
    if shift == 0:
        player_char[0].place_forget()
        shift = 1
    if shift == 1 and player_char[1] == 0: 
        player_char[0].configure(image=pics[5])
        player_char[0].place(x=tank_pos,y=600)
        player_char[1] = 1
        shift = 0
    if shift == 1 and player_char[1] == 1: 
        player_char[0].configure(image=pics[6])
        player_char[0].place(x=tank_pos,y=600)
        player_char[1] = 0
        shift = 0
    print(tank_move)
    return

def links(event):
    global tank_move,tank_pos,Game_run,player_char
    if Game_run != None:
        shift = 0
        tank_move = "Left"
        tank_pos = tank_pos - 5
    if shift == 0:
        player_char[0].place_forget()
        shift = 1
    if shift == 1 and player_char[1] == 0: 
        player_char[0].configure(image=pics[5])
        player_char[0].place(x=tank_pos,y=600)
        player_char[1] = 1
        shift = 0
    if shift == 1 and player_char[1] == 1: 
        player_char[0].configure(image=pics[6])
        player_char[0].place(x=tank_pos,y=600)
        player_char[1] = 0
        shift = 0
    print(tank_move)
    return   

def shot(event):
    global tank_pos,shots,Game_run
    if Game_run != None:
        shot = Tk.Label(Game_run,image=pics[13],borderwidth=0)
        shot.place(x=tank_pos,y=600)
        gen_shot = [shot,tank_pos,600]
        shots.append(gen_shot)
    return
 
    

# Main starts here
root = Tk.Tk()
pics = []
load = Image.open("SI_Alienhouse_full.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Alienhouse_dmg_1.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Alienhouse_dmg_2.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Alienshot_1.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Alienshot_2.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Cannon_1.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Cannon_2.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Cannon_1_hit.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Cannon_2_hit.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanhouse_full.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanhouse_dmg_1.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)        
load = Image.open("SI_Humanhouse_dmg_2.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanhouse_dmg_3.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanshot.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanspaceship_1.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanspaceship_2.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanspaceship_1_hit.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Humanspaceship_2_hit.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Marksman_dead.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Marksman_normal.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Miniboss_dead.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Miniboss_half.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Miniboss_dead.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Soldier_dead.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Soldier_normal.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Tank_dead.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Tank_normal.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_blank.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Lives.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_replay.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
load = Image.open("SI_Quit.png")
load_temp = ImageTk.PhotoImage(load)
pics.append(load_temp)
root.bind("<Right>",rechts)
root.bind("<Left>",links)
root.bind("<space>",shot)
Mainmenu(root)
root.mainloop()




