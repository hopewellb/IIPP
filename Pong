# Baby's First Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0  
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2 
score1 = 0
score2 = 0
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global LEFT, RIGHT, ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]    
    if direction == False:
        ball_vel[0] = - (random.randrange(120, 240) / 60.0)
        ball_vel[1] = - (random.randrange(60, 180) / 60.0)
        print "ball velocity is " + str(ball_vel)
        print "spawn ball left"     
    elif direction == True:
        ball_vel[0] = random.randrange(120, 240) / 60.0
        ball_vel[1] = - (random.randrange(60, 180) / 60.0)
        print "ball velocity is " + str(ball_vel)
        print "spawn ball right"

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(random.choice([LEFT, RIGHT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, LEFT, RIGHT       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # ball bounces off top/bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # update paddle's vertical position, keeps paddle on the screen    
    # paddle 1 position
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel     
    else:
        paddle1_pos = HALF_PAD_HEIGHT
    if paddle1_pos + paddle1_vel > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    # paddle 2 position
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel     
    else:
        paddle2_pos = HALF_PAD_HEIGHT  
    if paddle2_pos + paddle2_vel > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    # draw paddle 1
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),(HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), 
                     HALF_PAD_WIDTH, "White")
    
    # draw paddle 2
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT),
                     (WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), 
                     HALF_PAD_WIDTH, "White") 
                             
    # determines whether paddle and ball collide, otherwise determines scores   
    if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
          if abs(paddle1_pos - ball_pos[1]) > HALF_PAD_HEIGHT + BALL_RADIUS:
            spawn_ball(RIGHT)
            score2 += 1
            print "score 2 is " +str(score2)
          else:
            ball_vel[0] = - ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1

    elif ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if abs(paddle2_pos - ball_pos[1]) > HALF_PAD_HEIGHT + BALL_RADIUS:
            spawn_ball(LEFT)
            score1 += 1
            print "score 1 is " + str(score1)       	
        else: 
            ball_vel[0] = - ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1   
    
    # draw scores
    canvas.draw_text(str(score1), [142, 55], 45, "White")
    canvas.draw_text(str(score2), [458, 55], 45, "White")
        
# moves paddles on keydown
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP["down"]:
         paddle2_vel = 4

# stops paddle velocity on keyup           
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# calls new game, resets scores to 0       
def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", restart, 200)


# start frame
new_game()
frame.start()
