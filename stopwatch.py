# Baby's First "Stopwatch: The Game"
import simplegui

# define global variables
total_ticks = 0
total_stops = 0
total_wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = str(t // 600)
    b = str((((t // 10) % 60) // 10))
    c = str((((t // 10) % 60) % 10))
    d = str(t % 10)
    return a + ":" + b + c + "." + d   

# starts timer    
def start():
    timer.start()

# stops timer, tallys counters    
def stop():
    global total_stops, total_ticks, total_wins, timer_running
    if timer.is_running() == True and total_ticks % 10 == 0:
        timer.stop()
        total_stops += 1
        total_wins += 1
    elif timer.is_running() == True:
        timer.stop()
        total_stops += 1
    else:
        timer.stop()
       
# resets timer / global variables to 0        
def reset():
    global total_stops, total_ticks, total_wins
    total_ticks = 0
    total_stops = 0
    total_wins = 0
    timer.stop()

# event handler for timer with 0.1 sec interval
def tick():
    global total_ticks
    total_ticks += 1
 
# draw handler
def draw_handler(canvas):
    global total_ticks, total_stops, total_wins
    counter = str(total_wins) + "/" + str(total_stops)
    canvas.draw_text(format(total_ticks), [85, 125], 35, "White")
    canvas.draw_text(counter, [185, 30], 35, "Green")
        
# create frame
f = simplegui.create_frame("Stopwatch!", 250, 250)

# register event handlers
timer = simplegui.create_timer(100, tick)
f.set_draw_handler(draw_handler)
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)

# start frame
f.start()
