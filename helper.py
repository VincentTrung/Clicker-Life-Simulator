from settings import *

#The functions that will be used to help game overall

#Draw functions#
#stat bar 
def statBar(day, age, money, exp, job):
  pygame.draw.rect(screen, BLACK, bar)

  pygame.draw.rect(screen, BLUE, bar1)
  screen.blit(myFont.render('Day: '+str(day),1,BLACK),(barX+10,barY+10))

  pygame.draw.rect(screen, BLUE, bar2)
  screen.blit(myFont.render('Age: '+ str(age),1,BLACK),(barX+barSizeX+30,barY+10))
  
  pygame.draw.rect(screen, BLUE, bar3)
  screen.blit(myFont.render("Job: "+ job,1,BLACK), (barX+barSizeX*2+30, barY+10))

  pygame.draw.rect(screen, BLUE, bar4)
  screen.blit(myFont.render("Money: " + str(round(money,2)),1,BLACK),(barX+10, barY+barSizeY +10))

  pygame.draw.rect(screen, BLUE, bar5)
  screen.blit(myFont.render("EXP: " + str(exp),1,BLACK),(barX+barSizeX*2+30, barY+barSizeY +10))

#seasonal backgrounds
def background(season):
    global frame
    if frame < 3:
        frame += 1
    else:
        frame -= 3
    if season == 1 or season == 2: #summer and fall don't animation
      frame = 0
    Season = pygame.image.load("Images/seasons/season-"+str(season)+str(frame)+".png")
    screen.blit(Season,(0,0))

#create a button with outline and maybe text
def createButton(text, colour, x,y, buttonX, buttonY):
  Text = myFont.render(text,1,BLACK)

  button = pygame.Rect(x,y,buttonX,buttonY)  
  outline = pygame.Rect(x-5,y-5,buttonX+10,buttonY+10)
  pygame.draw.rect(screen, BLACK, outline)  #outline
  pygame.draw.rect(screen, colour, button)  #inside

  screen.blit(Text, (x + buttonX // 3,  y + buttonY // 3))

#change colour when hovering
def hovering(Object, hover_pos):
  if Object.collidepoint(hover_pos):
    return GRAY
  else:
    return WHITE

#animate clicking button
def buttonPressed(mouse_pos, X,Y,buttonX, buttonY):
  createButton("", GREEN, X, Y, buttonX,buttonY)
  pygame.display.update()


#calculation functions#
#find season based on DOY
def season(day):
  if day < 92:
    season = 0
  elif day < 184:
    season = 1
  elif day < 276:
    season = 2
  else:
    season = 3
  return season

#one time function for choosing post secondary option
def education(age,money,exp,schoolCost, schoolExp):
    global educated
    money -= schoolCost
    age += 4
    exp += schoolExp 
    educated = True
    return educated, age, money, exp

#update stats as time passes
def timePass(day, age, money, exp,intrest):
    day += 1
    if day == 365:
      age += 1
      day = 0
      if age >= retire: #end game for retirment
        running = False
        return running
    else:
      intrest = 0
    intrest = abs(money) * intrest #annual intrest on debt
    money -= intrest
    return day, age, money, exp

#calculate pay for work depending on age/job
def pay(jobWages,jobIndex,workHour,mouse_pos):
  clickedWorkText = myFont.render(" +$" + str(jobWages[jobIndex]*workHour),1, BLACK)
  screen.blit(workImg,mouse_pos)
  screen.blit(clickedWorkText, mouse_pos)
  if age >= 18:
    workHour = 8
  return jobWages[jobIndex] * workHour