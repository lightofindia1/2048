'''
Name: 2048
Version: 1.0
Author: Manikiran
Last Date Modified: 10/1/2015
'''
import pygame,sys,random
rc=random.choice
class Menu(object):
    def __init__(self):
        screen=pygame.display.set_mode((220,220))
        menu=["Start Game","Credits","Exit"]
        counter=0
        title=myfont_42.render("2048",1,(255,255,255))
        while 1:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif e.key==pygame.K_UP:
                        if counter>0:
                            counter-=1
                        else:
                            counter=len(menu)-1
                    elif e.key==pygame.K_DOWN:
                        if counter<len(menu)-1:
                            counter+=1
                        else:
                            counter=0
                    elif e.key==pygame.K_RETURN:
                        if counter==0:
                            Game()
                        elif counter==1:
                            Credits()
                        else:
                            pygame.quit()
                            sys.exit()

            screen.fill((0,0,0))
            screen.blit(title,(110-title.get_width()/2,30))
            for i in range(len(menu)):
                if counter==i:
                    cols=(200,0,0)
                else:
                    cols=(255,130,40)
                txt=myfont.render(menu[i],1,cols)
                screen.blit(txt,(110-txt.get_width()/2,100+i*30))
            pygame.display.flip()
class Gameover(object):
    def __init__(self,highscore):
        screen=pygame.display.set_mode((220,220))
        title=myfont.render("Highscore",1,(255,255,255))
        hs=myfont_42.render(str(highscore),1,(255,255,255))
        con=myfont_20.render("Press any key for Menu",1,(255,255,255))
        while 1:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type==pygame.KEYDOWN:
                    Menu()
            screen.fill((0,0,0))
            screen.blit(title,(110-title.get_width()/2,10))
            screen.blit(hs,(110-hs.get_width()/2,50))
            screen.blit(con,(110-con.get_width()/2,180))
            pygame.display.flip()
class Game(object):
    def __init__(self):
        screen=pygame.display.set_mode((220,220))
        pos=[(7,7),(7,59),(7,111),(7,163),(59,7),(59,59),(59,111),(59,163),(111,7),(111,59),(111,111),(111,163),(163,7),(163,59),(163,111),(163,163)]
        vals=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
        vals[rc(range(4))][rc(range(4))]=rc([2,4])
        def checkmoves():
            for i in range(4):
                for j in range(4):
                    if vals[i][j]==None:
                        return False
                    elif j>1 and vals[i][j-1]==vals[i][j]:
                        return False
                    elif j<3 and vals[i][j+1]==vals[i][j]:
                        return False
                    elif i>1 and vals[i-1][j]==vals[i][j]:
                        return False
                    elif i<3 and vals[i+1][j]==vals[i][j]:
                        return False
            return True
        while 1:
            if checkmoves():
                hs=0
                for i in vals:
                    for j in i:
                        if j>hs:
                            hs=j
                Gameover(hs)
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP:
                        tk=0
                        for k in range(4):
                            for i in range(1,4):
                                for j in range(4):
                                    if vals[j][i]:
                                        if vals[j][i-1]==vals[j][i]:
                                            vals[j][i-1]=vals[j][i]+vals[j][i-1]
                                            vals[j][i]=None
                                            tk=1
                                        elif vals[j][i-1]==None:
                                            vals[j][i-1]=vals[j][i]
                                            vals[j][i]=None
                                            tk=1
                        while tk:
                            i,j=rc(range(4)),rc(range(4))
                            if not vals[i][j]:
                                vals[i][j]=rc([2,4])
                                tk=0
                    elif e.key==pygame.K_DOWN:
                        tk=0
                        for k in range(4):
                            for i in range(3):
                                for j in range(4):
                                    if vals[j][i]:
                                        if vals[j][i+1]==vals[j][i]:
                                            vals[j][i+1]=vals[j][i]+vals[j][i+1]
                                            vals[j][i]=None
                                            tk=1
                                        elif vals[j][i+1]==None:
                                            vals[j][i+1]=vals[j][i]
                                            vals[j][i]=None
                                            tk=1
                        while tk:
                            i,j=rc(range(4)),rc(range(4))
                            if not vals[i][j]:
                                vals[i][j]=rc([2,4])
                                tk=0
                    elif e.key==pygame.K_RIGHT:
                        tk=0
                        for k in range(4):
                            for i in range(4):
                                for j in range(3):
                                    if vals[j][i]:
                                        if vals[j+1][i]==vals[j][i]:
                                            vals[j+1][i]=vals[j][i]+vals[j+1][i]
                                            vals[j][i]=None
                                            tk=1
                                        elif vals[j+1][i]==None:
                                            vals[j+1][i]=vals[j][i]
                                            vals[j][i]=None
                                            tk=1
                        while tk:
                            i,j=rc(range(4)),rc(range(4))
                            if not vals[i][j]:
                                vals[i][j]=rc([2,4])
                                tk=0
                    elif e.key==pygame.K_LEFT:
                        tk=0
                        for k in range(4):
                            for i in range(4):
                                for j in range(1,4):
                                    if vals[j][i]:
                                        if vals[j-1][i]==vals[j][i]:
                                            vals[j-1][i]=vals[j][i]+vals[j-1][i]
                                            vals[j][i]=None
                                            tk=1
                                        elif vals[j-1][i]==None:
                                            vals[j-1][i]=vals[j][i]
                                            vals[j][i]=None
                                            tk=1
                        while tk:
                            i,j=rc(range(4)),rc(range(4))
                            if not vals[i][j]:
                                vals[i][j]=rc([2,4])
                                tk=0
                    elif e.key==pygame.K_r:
                        Game()
                    elif e.key==pygame.K_ESCAPE:
                        Menu()
            screen.fill((0,0,0))
            pygame.draw.rect(screen,(0,0,0),(0,0,210,210),5)
            for i in pos:
                pygame.draw.rect(screen,(255,255,255),(i[0],i[1],50,50))
            for i in range(4):
                for j in range(4):
                    if vals[i][j]:
                        temp=myfont.render(str(vals[i][j]),1,(0,0,0))
                        p=i*4+j
                        screen.blit(temp,(pos[p][0]+25-temp.get_width()/2,pos[p][1]+25-temp.get_height()/2))
            pygame.display.flip()
class Credits(object):
    def __init__(self):
        screen=pygame.display.set_mode((220,220))
        title=myfont_42.render("2048",1,(255,255,255))
        name=myfont.render("Manikiran",1,(255,255,255))
        clas=myfont.render("XII C 8",1,(255,255,255))
        school1=myfont.render("Delhi Public School",1,(255,255,255))
        school2=myfont.render("Bangalore South",1,(255,255,255))
        while 1:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif e.type==pygame.KEYDOWN:
                    Menu()
            screen.fill((0,0,0))
            screen.blit(title,(110-title.get_width()/2,10))
            screen.blit(name,(110-name.get_width()/2,90))
            screen.blit(clas,(110-clas.get_width()/2,120))
            screen.blit(school1,(110-school1.get_width()/2,150))
            screen.blit(school2,(110-school2.get_width()/2,180))
            pygame.display.flip()
if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("2048")
    myfont=pygame.font.SysFont("Arial",25)
    myfont_20=pygame.font.SysFont("Arial",20)
    myfont_42=pygame.font.SysFont("Arial",42)
    Menu()
