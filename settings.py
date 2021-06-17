import pygame
#Game settings, hardcoded data, renders/intializations

TITLE = 'Clicker Life Simulator'

#colours
GRAY = (175, 175, 175)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
SKYBLUE = (51,180,255)
GRASS = (0,170,0)

#screen size
WIDTH = 500
HEIGHT = 500

#initialize screen/pygame 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.font.init()
clock=pygame.time.Clock()
screen = pygame.display.get_surface()# Set up the user screen 

#set different fonts
myFont = pygame.font.SysFont('Comic Sans MS', 30)#main text
mySmallFont = pygame.font.SysFont('Comic Sans MS', 20)#Stats
TitleFont = pygame.font.SysFont("Comic Sans MS", 50) #TITLE

#start menu text
Title = TitleFont.render(TITLE,1,BLACK)
startText = myFont.render('Start',1,BLACK)


#school/ education() data
learnExp = 5 
schoolCost = 50000
schoolExp = 10000
educated = False

#player start stats
age = 18
retire = 60
exp = 0
money = 0
day = 0
workHour = 4
intrest = 0.05 #yearly intrest
click = False #check if buttons pressed
season = 1 

#job data from csv
jobData = open('jobData.csv','r') #open
jobDatas = jobData.readlines() #read
jobDatas.pop(0) #take off the title/label

jobs =[]
jobWages = []
jobExps = []
jobExpFactors=[]

jobIndex = 0 #for nagvigating what jobs available

#sort data into lists
for data in jobDatas:
  info=data.split(",")# split will split any string into a list by the specified character
  jobs.append(info[0])
  jobWages.append(int(info[1]))
  jobExps.append(int(info[2]))
  jobExpFactors.append(int(info[3]))


#stat bar coord
barSizeX = WIDTH//4 -10
barSizeY = HEIGHT//12
barX = 5
barY = HEIGHT- barSizeY*2 - 5

bar = pygame.Rect(0, barY - 5 ,WIDTH, barSizeY*2 + 15)

bar1 = pygame.Rect(barX, barY,barSizeX, barSizeY-5)
bar2 = pygame.Rect(barX+barSizeX+10, barY,barSizeX, barSizeY-5)
bar3 =  pygame.Rect(barX+barSizeX*2+20, barY,barSizeX*2+10, barSizeY-5)

bar4 = pygame.Rect(barX, barY + barSizeY ,barSizeX*2+10, barSizeY-5)
bar5 = pygame.Rect(barX+barSizeX*2+20, barY + barSizeY ,barSizeX*2+10, barSizeY-5)

#button sizes
button1X = 190
button1Y = 100

button2X = WIDTH - 200
button2Y = 80


#game button coords
#large
workX = WIDTH//2 - button1X - 10
workY = HEIGHT-220
schoolX = WIDTH//2 + 10
schoolY = HEIGHT -220
#small 
jobOfferX =  WIDTH//6
jobOfferY =  100

workImg = pygame.image.load('Images/workImg.png')#work pop up


#game button locations/size
work = pygame.Rect(workX,workY,button1X,button1Y)  
school = pygame.Rect(schoolX, schoolY,button1X,button1Y)
jobOffer = pygame.Rect(jobOfferX, jobOfferY,button2X,button2Y)

#render button text
workText = myFont.render("Work",1,BLACK)
learnText = myFont.render("Learn",1, BLACK)
clickedSchoolText = myFont.render(" + " + str(learnExp)+ ' exp',1, BLACK)

schoolText = myFont.render("4 year education",1, BLACK)
schoolText2 = myFont.render("EXP: +" + str(schoolExp), 1, BLACK)
schoolText3 = myFont.render("-$" + str(schoolCost) , 1, BLACK)


#START MENU data
#Start menu coords
startX = (WIDTH-button1X)//2
startY = (HEIGHT - 2*button1Y- button1Y)
quitX = startX
quitY = startY + button1Y +50
cursorY = startY #set cursor starting

startButton = pygame.Rect(startX,startY,button1X,button1Y) 
quitButton = pygame.Rect(quitX, quitY,button1X,button1Y)

#drawing coords
birdX = 50
birdY = 110

bunnyY = HEIGHT - 130

bunnyX = WIDTH
frame = 0   #animation frame start menu

cursor = pygame.image.load("Images/hand_cursor.png")