from msilib.schema import SelfReg
import tkinter as Tk
from typing import Self
from PIL import ImageTk,Image
import time,random,math

shift = 0
shift_dir = 0
circle_row = 0
circle_nr = 0
clock = 0
lives = 3
HS_game = 0
enemy_matrix = [[3,3,3,3,3,3,3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1]]
enemies = []
shots = []
enemy_shots=[]
SI_houses = []
tank_move = "STOP"
tank_pos = 320
Game_run = True

    
class Mainmenu:
    def __init__(self, parent, *args, **kwargs):
        self.master = parent
        self.frame = Tk.Frame(self.master,height=400,width=640,bg="black",fg="green")
        self.NewGame_btn = Tk.Button(self,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="New Game",command=self.newGame)
        self.NewGame_btn.pack()
        self.QuitGame_btn = Tk.Button(self,borderwidth=0,font="arial 35 italic", fg="Green",bg="black",text="Quit Game",command=self.quitGame)
        self.QuitGame_btn.pack()
        self.Frame.pack()
    
    def newGame(self):
        global Game_run,shift,shift_dir,clock,lives,HS_game,lives_c_Label
        shift = 0
        shift_dir = 0
        clock = 0
        lives = 3
        lives_c_Label = []
        self.master.update()
        
    def quitGame(self):
        self.master.destroy()
        
        
#HsMenu = Tk.Toplevel(root=root).pack(side="top", fill="both", expand=True)
## def GameWindow and hide it may be lock timers !!!
## Class Rework Version
class Game:
    def __init__(self,parent):
        global strt_time
        self.master = parent
        self.frame = Tk.Frame(self.master,height=680,width=800,padx=40,pady=40,bg="black")
        self.alienhouse_dmg_1 = Tk.PhotoImage(file="SI_Alienhouse_dmg_1.png")
        self.alienhouse_dmg_2 = Tk.PhotoImage(file="SI_Alienhouse_dmg_2.png")
        self.alienhouse_full = Tk.PhotoImage(file="SI_Alienhouse_full.png")
        self.alienshot_1 = Tk.PhotoImage(file="SI_Alienshot_1.png")
        self.alienshot_2 = Tk.PhotoImage(file="SI_Alienshot_2.png")
        self.cannon_1 = Tk.PhotoImage(file="SI_Cannon_1.png")
        self.cannon_2 = Tk.PhotoImage(file="SI_Cannon_2.png")
        self.cannon_1_hit = Tk.PhotoImage(file="SI_Cannon_1_hit.png")
        self.cannon_2_hit = Tk.PhotoImage(file="SI_Cannon_2_hit.png")
        self.humanhouse_dmg_1 = Tk.PhotoImage(file="SI_Humanhouse_dmg_1.png")
        self.humanhouse_dmg_2 = Tk.PhotoImage(file="SI_Humanhouse_dmg_2.png")
        self.humanhouse_dmg_3 = Tk.PhotoImage(file="SI_Humanhouse_dmg_3.png")
        self.humanhouse_full = Tk.PhotoImage(file="SI_Humanhouse_full.png")
        self.humanshot = Tk.PhotoImage(file="SI_Humanshot.png")
        self.humanspaceship_1 = Tk.PhotoImage(file="SI_Humanspaceship_1.png")
        self.humanspaceship_2 = Tk.PhotoImage(file="SI_Humanspaceship_2.png")
        self.humanspaceship_1_hit = Tk.PhotoImage(file="SI_Humanspaceship_1_hit.png")
        self.humanspaceship_2_hit = Tk.PhotoImage(file="SI_Humanspaceship_2_hit.png")
        self.marksman_dead = Tk.PhotoImage(file="SI_Marksman_dead.png")
        self.marksman = Tk.PhotoImage(file="SI_Marksman_normal.png")
        self.miniboss_dead = Tk.PhotoImage(file="SI_Miniboss_dead.png")
        self.miniboss = Tk.PhotoImage(file="SI_Miniboss_full.png")
        self.miniboss_half = Tk.PhotoImage(file="SI_Miniboss_half.png")
        self.soldier_dead = Tk.PhotoImage(file="SI_Soldier_dead.png")
        self.soldier = Tk.PhotoImage(file="SI_Soldier_normal.png")
        self.tank_dead = Tk.PhotoImage(file="SI_Tank_dead.png")
        load = Image.open("SI_crap.png")
        self.tank = ImageTk.PhotoImage(load)
        load = Image.open("SI_blank.png")
        self.blank = ImageTk.PhotoImage(load)
        load = Image.open("SI_Lives.png")
        self.liveheart = ImageTk.PhotoImage(load)
        for house in range(4):
            t_house = Tk.Label(self,image=self.humanhouse_full,borderwidth=0)
            t_house_x = 60 + 180 * house
            t_house_state = 4
            t_house.place(x=t_house_x,y=550)
            temp = [t_house,t_house_x,550,t_house_state,[t_house_x,568,t_house_x+12,568]]
            SI_houses.append(temp)
        for row in range(len(enemy_matrix)):
            for col in range(len(enemy_matrix[row])):
                if enemy_matrix[row][col] == 3:
                    enemy = Tk.Label(self,image=self.tank,borderwidth=0,)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                if enemy_matrix[row][col] == 2:
                    enemy = Tk.Label(self,image=self.marksman,borderwidth=0)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                if enemy_matrix[row][col] == 1:
                    enemy = Tk.Label(self,image=self.soldier,borderwidth=0)
                    enemy.place(x = 40 + col * 20, y = 40 + row * 15)
                    cord_x = 40 + col * 20
                    cord_y = 40 + row * 15
                    enemy_meta = [enemy,cord_x,cord_y,"Alive"]
                    enemies.append(enemy_meta)
                print(enemy_meta)
        
        self.heroTank = Tk.Label(self,image=self.cannon_1,borderwidth=0)
        self.heroTank.place(x=320,y=600)
        self.bind("<Right>",self.rechts)
        self.bind("<Left>",self.links)
        self.bind("<space>",self.shot)
        strt_time = time.strftime("%H:%M:%S")
        
        HUD_Frame = Tk.LabelFrame(self,height=20,width=640,background="Black",borderwidth=0)
        HUD_Frame.pack(side="top",fill="both",expand=False)
        HS_Label = Tk.Label(HUD_Frame,font="arial 15 bold",text="000000",foreground="grey",background="black")
        HS_Label.pack(side="left")
        Killcount_Lable= Tk.Label(HUD_Frame,font="arial 15 bold",text="0",foreground="white",background="black",image=self.soldier,compound="left")
        Killcount_Lable.pack(side="left")

        for i in range(3):
            Lives_Label = Tk.Label(HUD_Frame,image=self.liveheart,borderwidth=0)
            Lives_Label.pack(side="right")
            lives_c_Label.append(Lives_Label)
        for x in range(15):
            ene_shot = Tk.Label(self,image=self.alienshot_1,borderwidth=0)
            ene_shot_x = 0
            temp_shot = random.randint(100,3600)
            enemy_shots.append([ene_shot,0,0,0,temp_shot,0.0,self.alienshot_1])
        self.frame.pack()
        self.moveEnemy()
        self.moveShot()
        self.shotEnemy()
        self.UpdateLabels()
        self.master.mainloop()
        return
    

    def UpdateLabels(self):
        global lives,strt_time,enemies,lives_c_Label,HS_lable
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

        self.update_idletasks()
        self.after(1000,self.UpdateLabels)
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
                            temp_ene[0].configure(image=self.tank_dead)
                        if enemy_matrix[n][m] == 2:
                            temp_ene[0].configure(image=self.marksman_dead)
                        if enemy_matrix[n][m] == 1:
                            temp_ene[0].configure(image=self.soldier_dead)
                        temp_ene[3] = "Dead"
                        enemies[confl] = temp_ene
                        kills = shots[shot]
                        shots[shot][0].configure(image=self.blank)
                    shift=0
                if kills[0] != "None":    
                    shots.remove(kills)
                    kills[0].destroy()
                    
        self.update_idletasks() 
        self.after(100,self.moveShot)
        return
    
    def shotEnemy(self):
        global enemy_shots,clock,tank_pos,circle_row,circle_nr,SI_houses,lives,Game_run
        shift = clock%2
        clock_s = clock * 10

        for shot in range(len(enemy_shots)):
            temp_shot = enemy_shots[shot]
            temp_shot_time = temp_shot[4]
            temp_shot_state = temp_shot[3]
            if temp_shot_state == 1:
                continue
            if temp_shot_time > clock_s: 
                temp_shot[3] = 1
                temp_shot_x = 140 + circle_nr
                temp_shot_y = 43 + circle_row
                temp_spot_x = self.heroTank.winfo_rootx() - temp_shot_x
                temp_spot_y = 600 - temp_shot_y
                temp_shot_ang = math.degrees(math.tan((temp_spot_y/temp_spot_x)))
                temp_shot[0].place(x=temp_shot_x,y=temp_shot_y)
                temp_pic = Image.open("SI_Alienshot_1.png")
                temp_ang_pic = temp_pic.rotate(temp_shot_ang)
                temp_shot_pic = ImageTk.PhotoImage(temp_ang_pic)
                temp_shot[1] = temp_shot_x
                temp_shot[2] = temp_shot_y
                temp_shot[5] = temp_shot_ang
                temp_shot[6] = temp_shot_pic
                enemy_shots[shot] = temp_shot
                enemy_shots[shot][0].configure(image=enemy_shots[shot][6])
                print(temp_shot[4])
            
        if shift == 0:
            for shot in range(len(enemy_shots)):
                temp_shot = enemy_shots[shot]
                temp_shot[0].place_forget()
        if shift == 1:
            for shot in range(len(enemy_shots)):
                temp_shot = enemy_shots[shot]
                if temp_shot[3] == 1:
                    temp_shot[1] = int(temp_shot[1] + 5 * math.sin(temp_shot[5]))
                    temp_shot[2] = int(temp_shot[2] + 5 * math.cos(temp_shot[5]))
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
                    temp_spot_x = (int(temp[1] + 5 * math.sin(temp[5])) - SI_houses[confl][4][0]) * SI_houses[confl][4][2]
                    temp_spot_y = (int(temp[2] + 5 * math.cos(temp[5])) - SI_houses[confl][4][1]) * SI_houses[confl][4][3]
                    r = math.sqrt(math.pow(temp_spot_x,2)+math.pow(temp_spot_y,2))
                    t_r_x = tank_pos - temp_spot_x
                    t_r_y = 600 - temp_spot_y
                    r_tank = math.sqrt(math.pow(t_r_x,2)+math.pow(t_r_y,2))
                    if r_tank < 5:
                        self.heroTank.configure(image=self.cannon_1_hit)
                        lives = lives - 1
                    if r !=0:
                        continue
                    if SI_houses[confl][3] == 4:
                        SI_houses[confl][0].configurate(image=self.humanhouse_dmg_3)
                        SI_houses[confl][3] = 3
                    if SI_houses[confl][3] == 3:
                        SI_houses[confl][0].configurate(image=self.humanhouse_dmg_2)
                    SI_houses[confl][3] = 2
                    if SI_houses[confl][3] == 2:
                        SI_houses[confl][0].configurate(image=self.humanhouse_dmg_1)
                        SI_houses[confl][3] = 1
                    if SI_houses[confl][3] == 1:
                        SI_houses[confl][0].destroy()
                    temp[0].destroy()
                        
        self.update_idletasks()
        self.after(100,self.shotEnemy)
        return
    
    def moveEnemy(self):
        global shift,enemies,circle_nr,tank_move,tank_pos,shift_dir,circle_row,loaded,clock,Game_run
        kills = []
        if shift == 0 and loaded:
            for data in range(len(enemies)):
                temp_enemy = enemies[data]
                temp_enemy[0].place_forget()
        if shift == 1 and loaded:
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
        self.update_idletasks()
        self.after(1000,self.moveEnemy)
        return
    
    def rechts(event,self):
        global tank_move,tank_pos
        shift = 0
        tank_move = "RIGHT"
        tank_pos = tank_pos + 5
        if shift == 0:
            self.heroTank.place_forget()
            shift = 1
        if shift == 1: 
            self.heroTank.place(x=tank_pos,y=600)
            shift = 0
        print(tank_move)
        return

    def links(event,self):
        global tank_move,tank_pos
        shift = 0
        tank_move = "LEFT"
        tank_pos = tank_pos - 5
        if shift == 0:
            self.heroTank.place_forget()
            shift = 1
        if shift == 1: 
            self.heroTank.place(x=tank_pos,y=600)
            shift = 0
        print(tank_move)
        return

    def shot(event,self):
        global tank_pos,shots
        shot = Tk.Label(self,image=self.humanshot,borderwidth=0)
        shot.place(x=tank_pos,y=600)
        gen_shot = [shot,tank_pos,600]
        shots.append(gen_shot)
        return
    
def main():
    root = Tk.Tk()
    Mainmenu(root).pack()
    root.mainloop()
    return
