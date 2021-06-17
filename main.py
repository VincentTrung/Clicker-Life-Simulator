import pygame
from time import *
from helper import *
from introFunctions import *

#start menu 
running = startMenu() 

#main game loop begins
while running:  
#Draw  #screen.fill(BG) #Background
  background(season(day))
  statBar(day, age, money, exp,jobs[jobIndex]) #stats
  
  #conditional buttons#
  colour = hovering(school, pygame.mouse.get_pos())
  if age <= 18: 
    createButton("School", colour, schoolX, schoolY, button1X, button1Y)
  elif not educated:
    createButton("", colour, schoolX, schoolY, button1X, button1Y)
    screen.blit(schoolText,(schoolX + button1X // 8, schoolY + button1Y // 4))
    screen.blit(schoolText2,(schoolX + button1X // 8, schoolY + button1Y // 4 + 25))
    screen.blit(schoolText3,(schoolX + button1X // 8, schoolY + button1Y // 4 + 50))
    
  if exp >= jobExps[1]:
    colour = hovering(jobOffer,pygame.mouse.get_pos())
    createButton("Job Offer", colour, jobOfferX, jobOfferY, button2X,button2Y)
    jobTitle = myFont.render(jobs[jobIndex+1],1,BLACK) #change title depending on exp
    screen.blit(jobTitle,(jobOfferX + button1X // 2, jobOfferY + button1Y // 4+25))
    
  #constant button #check hovered
  colour = hovering(work, pygame.mouse.get_pos())
  createButton("Work", colour, workX, workY, button1X, button1Y)

  pygame.display.flip() #actually draw


  #collect player action 
  for event in pygame.event.get():  
    if event.type == pygame.QUIT:
      running = False  #quit if player wants

    if event.type == pygame.MOUSEBUTTONDOWN:  #collect clicked coords
      buttonClick = pygame.mouse.get_pressed() #check what button
      mouse_pos = event.pos
      
      #check collisions on buttons
      #work button click
      if work.collidepoint(mouse_pos) and buttonClick[0] ==1:  
        #print('work')
        buttonPressed(mouse_pos, workX, workY, button1X, button1Y)
        money += pay(jobWages,jobIndex, workHour, mouse_pos)
        exp += jobExpFactors[jobIndex]
        click = True

      #school button click
      if age <= 18 and school.collidepoint(mouse_pos)and buttonClick[0] ==1: 
        #print('School')
        buttonPressed(mouse_pos, schoolX, schoolY, button1X, button1Y)
        exp += learnExp
        click = True
      elif school.collidepoint(mouse_pos)and buttonClick[0] ==1 and not educated:
        #print('educated')#post secondary
        createButton("", GREEN, schoolX, schoolY, button1X,button1Y)
        educated, age, money, exp = education(age,money,exp,schoolCost, schoolExp)
        click = True

      #job offer to level up when enough exp
      if exp >= jobExps[1] and jobOffer.collidepoint(mouse_pos) and buttonClick[0] ==1: 
        #print('applied')
        del jobExps[0] #dont need anymore
        jobIndex += 1 #update job
        createButton("", GREEN, jobOfferX, jobOfferY,button2X, button2Y)
        click = True
      
      if click == True: #check if any button pressed to update stats
        time.sleep(0.1)
        day, age, money, exp = timePass(day, age, money, exp, intrest)
      click = False
      
      clock.tick(60)
      pygame.display.flip()#draw changes
      #print(day, age, money, exp) #temporary 

      

#end game screen?
pygame.quit()#end of program