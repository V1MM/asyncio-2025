import time
from datetime import timedelta
import asyncio
speed = 100
Judit_time = 5/speed
Oppent_time = 55/speed
opponents = 24
move_pairs = 30 


#My answer
async def game(x) :
   board_start_time = time.perf_counter()
   calulated_board_start_time = 0
   for i in range(move_pairs) :
      await asyncio.sleep(Judit_time)
      calulated_board_start_time =  calulated_board_start_time + Judit_time
      print(f'BORAD-{x+1} {i+1} Judith made move with {int(Judit_time*speed)} secs.')

      await asyncio.sleep(Judit_time)
      print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Oppent_time*speed)} secs.")
      calulated_board_start_time = calulated_board_start_time + Oppent_time
   print(f'BOARD-{x+1} - >>>>>>>>>>>>>>>>>>>>> Finish move in {(time.perf_counter() - board_start_time) *speed:.1f} secs')
   print(f'BOARD-{x+1} - >>>>>>>>>>>>>>>>>>>>> Finish move in {calulated_board_start_time*speed:.1f} secs (calculated)\n')
   return [(time.perf_counter() - board_start_time), calulated_board_start_time ]



async def main() :
    print(f"Number of games : {opponents} games.")
    print(f"Number of move : {move_pairs} pairs.")
    start_time = time.perf_counter()
    boards_time = 0
    calculated_borad_time = 0
    for borad in range(opponents) :
       boards_time += game(borad)[0]
       calculated_borad_time += game(borad)[1]
    
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(boards_time*speed) )} hr.")
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=round(calculated_borad_time*speed) )} hr.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__" :
   asyncio.run (main())

#Soloution
# async def game(x) :
#     board_start_time = time.perf_counter()
#     for i in range(move_pairs) :
#         time.sleep(Judit_time)
#         print(f"BOARD-{x+1} {i+1} Judith made a move with {int(Judit_time*speed)} secs.")

#         await asyncio.sleep(Oppent_time)
#         print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Oppent_time*speed)} secs.")
#     print(f"BOARD-{x+1} - >>>>>>>>>>>>> Finshed move in { (time.perf_counter() - board_start_time)* speed:.1f} secs. \n")
#     return [(time.perf_counter() - board_start_time)*speed]

# async def main():
#     tasks = []
#     for i in range(opponents) :
#         tasks += [game(i)]
#     await asyncio.gather(*tasks)
#     print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=speed*round(time.perf_counter() - start_time))} hr.")

# if __name__ == "__main__" :
#     start_time = time.perf_counter()
#     asyncio.run(main())
#     print(f"Finished in {round(time.perf_counter()-start_time)} secs.")
