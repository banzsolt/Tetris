import block
import bord
import time
import random
import translator
import datetime
import RPi.GPIO as GPIO

__author__ = 'Zsolti'

Matrix = [[1 for y in range(10)] for x in range(11)]
speed = None
main_board = bord.Bord(8, 10)
the_translator = translator.Translator(10,8,Matrix)
dead = False
current_brick = block.Block(0, main_board.y / 2)
processes = []

right_timout = datetime.datetime.now()
left_timeout = datetime.datetime.now()
down_timeout = datetime.datetime.now()
rotate_timeout = datetime.datetime.now()

sensitivity = 0.2

def set_initial_setting():
    global speed
    speed = 1
    main_board = bord.Bord(8, 10)
    current_brick = block.Block(0, main_board.y / 2)

def show_matrix(matrix):
    global Matrix, the_translator, main_board
    timeout = time.time() + 1
    while 1:
        if time.time() > timeout:
            for x in range (0, len(matrix)):
                print (str(matrix[x][0]) + str(matrix[x][1]) + str(matrix[x][2]) + str(matrix[x][3]) + str(matrix[x][4]) + str(matrix[x][5]) + str(matrix[x][6]) + str(matrix[x][7]) + str(matrix[x][8]) + str(matrix[x][9]))
            print
            break  
        check_left()
        check_right()
        check_down()
        the_translator.output_to_gpio()
    
    

def check_left():
    global safe_left, main_board, left_timeout
    if GPIO.input(40) == 1:
        if main_board._last_block is None:
            return
        if left_timeout + datetime.timedelta(seconds = sensitivity) > datetime.datetime.now():
            return
        
        left_timeout = datetime.datetime.now()
        current_brick = main_board._last_block
        colide = False
        current_x = 0
        for possition in range(current_brick.x, current_brick.x + current_brick.height()):
            if current_brick.shape[current_x][0] == 1:
                if main_board.matrix[int(possition)][int(current_brick.y - 1)] == 1:
                    colide = True
            current_x += 1
    
        if colide:
            return
        else:
            main_board.new_block(current_brick, int(current_brick.x), int(current_brick.y -1))
    the_translator.output_to_gpio()
        
def check_right():
    global safe_right, main_board, right_timout
    if GPIO.input(38) == 1:
        if main_board._last_block is None:
            return
        if right_timout + datetime.timedelta(seconds = sensitivity) > datetime.datetime.now():
            return
        
        right_timout = datetime.datetime.now()
        current_brick = main_board._last_block
        colide = False
        current_x = 0
        for possition in range(current_brick.x, current_brick.x + current_brick.height()):
            if current_brick.shape[current_x][current_brick.width()-1] == 1:
                if main_board.matrix[int(possition)][int(current_brick.y + current_brick.width())] == 1:
                    colide = True
            current_x += 1

        if colide:
            return
        else:
            main_board.new_block(current_brick, int(current_brick.x), int(current_brick.y +1))
    the_translator.output_to_gpio()


def check_down():
    global down_timeout
    #main_board.next_step()
    #global main_board
    if GPIO.input(36) == 1:
        print("36")
        if down_timeout + datetime.timedelta(seconds = sensitivity) > datetime.datetime.now():
            return
        down_timeout = datetime.datetime.now()
        main_board.next_step()
        print("36")
        
        
def check_rotate():
    global rotate_timeout
    #main_board.next_step()
    #global main_board
    if GPIO.input(37) == 1:
        print("32")
        if rotate_timeout + datetime.timedelta(seconds = sensitivity) > datetime.datetime.now():
            return
        rotate_timeout = datetime.datetime.now()
        main_board.next_step()
        print("32")
    



def change_matrix():
    global Matrix, main_board, dead, current_brick
    print("I am here")
    show_matrix(main_board.matrix)
    
    while not dead:
        the_block = block.Block(0,random.randint(1, 4))
        current_brick = the_block
        print("new block")
        main_board.new_block(the_block, the_block.x, the_block.y)
        the_translator.set_matrix(main_board.matrix)
        colide = False
        while not colide:
            #show_matrix(main_board.matrix)
            timeout = time.time() + 1
            while 1:
                if time.time() > timeout:
                    break
                #main_board.new_block(main_board._last_block, main_board._last_block.x, main_board._last_block.y)
                the_translator.output_to_gpio()
                show_matrix(main_board.matrix)
            colide = main_board.next_step()
        main_board.check_row_filled()
        for y in range (1, main_board.width()):
            if main_board.matrix[0][y] == 1:
                dead = True
                break
        if dead:
            print("you are dead!!")
    

def start():
    global the_translator, Matrix, processes
    change_matrix()

if __name__ == '__main__':
    start()



