import time
from datetime import timedelta
speed = 10000
Judit_time = 5/speed
Oppent_time = 55/speed
opponents = 24
move_pairs = 30 

Number_of_Games = 24
Number_of_Move = 30
#Answer for me
for i in range(1,Number_of_Games+1) :
    for j in range(1,Number_of_Move+1) :
      print(f'BOARD-{i} {j} Judith made a move with {Judit_time} secs.') 
      time.sleep(5)
      print(f'BOARD-{i} {j} Opponent made a move with {Oppent_time} secs.') 
      time.sleep(55)


#Solution of Teacher Red
# def game(x) :
#    board_start_time = time.perf_counter()
#    calulated_board_start_time = 0
#    for i in range(move_pairs) :
#       time.sleep(Judit_time)
#       calulated_board_start_time =  calulated_board_start_time + Judit_time
#       print(f'BORAD-{x+1} {i+1} Judith made move with {int(Judit_time*speed)} secs.')

#       time.sleep(Oppent_time)
#       print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Oppent_time*speed)} secs.")
#       calulated_board_start_time = calulated_board_start_time + Oppent_time
#    print(f'BOARD-{x+1} - >>>>>>>>>>>>>>>>>>>>> Finish move in {(time.perf_counter() - board_start_time) *speed:.1f} secs')
#    print(f'BOARD-{x+1} - >>>>>>>>>>>>>>>>>>>>> Finish move in {calulated_board_start_time*speed:.1f} secs (calculated)\n')
#    return [(time.perf_counter() - board_start_time), calulated_board_start_time ]



# if __name__ == "__main__" :
#     print(f"Number of games : {opponents} games.")
#     print(f"Number of move : {move_pairs} pairs.")
#     start_time = time.perf_counter()
#     boards_time = 0
#     calculated_borad_time = 0
#     for borad in range(opponents) :
#        boards_time += game(borad)[0]
#        calculated_borad_time += game(borad)[1]
    
#     print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(boards_time*speed) )} hr.")
#     print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(calculated_borad_time*speed) )} hr.")
#     print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

