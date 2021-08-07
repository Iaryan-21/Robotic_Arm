from tkinter import *
from tkinter import filedialog
import serial
import time

port_opened=False

def set_port():
    global port_opened,arduino
    com_port = port_input.get()
    arduino=serial.Serial(com_port,9600)
    port_opened=True
    print("COM port is"+com_port)
def send_positions(position):
    message = "{0:0=3d}".format(position[0])+"{0:0=3d}".format(position[1]) +"{0:0=3d".format(position[2])+"{0:0=3d}".format(position[4])+"\n"
    arduino.write(str,encode(message))
    print(message, end='')
    time.sleep(0.2)
saved_positions = []
def save_positions():
    saved_positions.append([servoA_slider.get(),servoB_slider.get(),servoC_slider.get(),servoD_slider.get(),servoE_slider.get(),])    
    print("saved positions: "+str(saved_positions))
def play_positions():
    for position in saved_positions:
        print("playing: "+str(position))
        send_positions(position);
        time.sleep(1)
def clear_all_positions():
    global saved_positions
    saved_positions = []
    print("cleared all positions")
def clear_last_positions():
    global saved_positions
    saved_positions = []
    print("saved positions: "+str(saved_positions))            
def open_file():
    global saved_positions
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select the File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file = open(filename, "r")
    data=file.read()
    saved_positions=eval(data)
    file.close()
    print("opened: "+filename)

def save_file():
    save_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    save_file.write(str(saved_positions))
    save_file.close()
    print("saved file")

def instructions():
    print("1.) Set the Arduino's COM port and click Enter. This can be found in Device Manager in Windows")
    print("2.) Move the arm's servos using the sliders")
    print("3.) To record a position, click on Record Position")
    print("4.) To replay the recorded positions, click on Replay Positions")
    print("\nTo save what you've recorded, got to File > Save File.")
    print("To open a previously saved file, got to File > Open File.")



window = Tk()
window.title("Robot Arm Controller")
window.minsize(355,300)

port_label=Label(window,text="Set Port:");
port_label.place(x=10,y=10);
port_input=Entry(window)
port_input.place(x=10,y=35)
port_button=Button(window, text="Enter", command=set_port)
port_button.place(x=135, y=32)

servoA_slider = Scale(window, from_=180, to=0)
servoA_slider.place(x=0, y= 100)
servoA_label=Label(window,text="Servo A")
ServoA_label.place(x=10, y=80)

servoB_slider = Scale(window, from_=180, to=0)
servoB_slider.place(x=70, y= 100)
servoB_label=Label(window,text="Servo B")
ServoB_label.place(x=80, y=80)

servoC_slider = Scale(window, from_=180, to=0)
servoC_slider.place(x=140, y= 100)
servoC_label=Label(window,text="Servo C")
ServoC_label.place(x=150, y=80)

servoD_slider = Scale(window, from_=180, to=0)
servoD_slider.place(x=210, y= 100)
servoD_label=Label(window,text="Servo D")
ServoD_label.place(x=220, y=80)

servoE_slider = Scale(window, from_=180, to=0)
servoE_slider.place(x=280, y= 100)
servoE_label=Label(window,text="Servo E")
ServoE_label.place(x=290, y=80)

save_button=Button(window, text"Record Position", command=save_positions)
clear_button.place(x=10,y=220)

clear_button=Button(window, text"Clear Last Position", command=clear_last_positions)
clear_button.place(x=120, y=220)

clear_button=Button(window, text"Clear All Position", command=clear_all_positions)
clear_button.place(x=120, y=255)

play_button=Button(window, text="Replay Positions", command=play_positions, height=3)
play_button.place(x=250, y=220)

menubar= Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File", command=open_file)
filemenu.add_command(label="Save File", command=save_file)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label ="Clear last Position", command=clear_last_positions)
editmenu.add_command(label ="Clear all Position", command=clear_all_positions)
editmenu.add_command(label = "Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Way of deploying", command=instructions)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
while True:
    window.update()
    if(port_opened):
        send_positions([servoA_slider.get(), servoB_slider.get(), servoC_slider.get(), servoD_slider.get(),servoE_slider.get()]) 
