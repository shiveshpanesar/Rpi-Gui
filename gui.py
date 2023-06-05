import tkinter as tk
# import ultrasonic as us
import colour as col
from datetime import datetime
root = tk.Tk()
root.attributes('-fullscreen', True)  # Set the window to fullscreen mode

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

width = root.winfo_screenwidth()  
height = root.winfo_screenheight() 

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def getData(val):
	per = (round(val)/800)*100
	if(per>100):
		per=100
	per=100-per
	if(per>70):
		color=col.red()
	else:
		color=col.blue()
	return per,color
	
def bar(x1,x2,tankName,textX):

	#val= map_value(us.u(TRIG=6,ECHO=5), 2, 20, 0, 800)
	val=0
	val= map_value(10, 2, 20, 0, 800)
	y1 = val 
	y2 = height 
	
	per,color=getData(val)
	print(per)
	text = tankName+str(round(per))+" %"  # The text to be displayed
	
	canvas.create_rectangle(x1, y1, x2, y2, fill=color) 
	canvas.create_text(textX, 600, text=text, font=("Arial", 40), fill="black")


def update():
	canvas.delete("all")
	now = datetime.now()

	current_time = now.strftime("%d/%m/%Y, %H:%M:%S")
	canvas.create_text(1400, 20, text=current_time, font=("Arial", 20), fill="black")
	bar(0,width//2,"Tank 1- ",300)
	bar(width//2,width,"Tank 2- ",1000)
	
	root.after(50, update) 

update()
root.mainloop()
