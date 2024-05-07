import os
import time

from replit import audio

print(
    "\033[34m",
    "\n\n\n\n------------------> 🎼 MyPOD MUSIC PLAYER 🎼 <----------------------",
    "\033[0m")
print("\nLoading...")
time.sleep(3)


def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback
  while True:
    # Start taking user input and doing something with it

    decide = (input(
        "\n-------> press 3 to pause OR (if song is over THEN ONLY press no)----> "
    ))

    if decide == "3":
      source.paused = True  # unpause the playback
      while True:
        while True:
          resume = input("\nwant to resume again? (yes or no)----> ")
          if resume == "yes":
            source.paused = False  # unpause the playbac
            break
            # continue
          elif resume == "no":
            print("\033[35m", "\n\n\npress 1 to play song AGAIN 😏😁 ")
            print("\npress 2 to exit ", "\033[0m")
            what_todo = int(input("\nWhat you want to do ? 🤔 (1 or 2)---> "))
            print("\033[32m", "\nENJOY 😎", "\033[0m")
            # take user's input
            while True:
              if what_todo == 1:
                play()
              elif what_todo == 2:
                print(
                    "\033[32m",
                    "\n\n------------------> Hope you ENJOYED 😄 <----------------------",
                    "\033[0m")
                time.sleep(2)
                exit()
              else:
                print("\033[31m", "\nyou can only input 1 or 2. TRY AGAIN ",
                      "\033[0m")

          decide = (input(
              "\n-------->press 3 to pause OR (if song is over THEN ONLY press no)----> "
          ))
          if decide == "3":
            source.paused = True  # unpause the playback
          elif decide == "no":
            break
          else:
            print(
                "\033[31m",
                "\nyou cannot type anything else rather than yes or no in lowercase. Please try again.",
                "\033[0m")
            continue
        break
    elif decide == "no":
      print("\033[35m", "\n\n\npress 1 to play song AGAIN")
      print("\npress 2 to exit ", "\033[0m")
      what_todo = int(input("\nWhat you want to do ? 🤔 (1 or 2)---> "))
      print("\033[32m", "\nENJOY 😎", "\033[0m")

      # take user's input
      while True:
        if what_todo == 1:
          play()
        elif what_todo == 2:
          print(
              "\033[32m",
              "\n\n------------------> Hope you ENJOYED 😄 <----------------------",
              "\033[0m")
          time.sleep(2)
          exit()
        else:
          print("\033[31m", "\nyou can only input 1 or 2. TRY AGAIN ",
                "\033[0m")


# play()
while True:
  # clear the screen
  os.system("clear")

  # Show the menu
  print("\033[34m", "---------------> 🎼 MyPOD Music Player 🎼 <---------------",
        "\033[0m")
  print("\033[31m","           <---------------------------------->\n\n","\033[0m")
  print(
      "\033[33m",
      "----------->makue sure you input only what is accepted from you.",
      "\033[0m")
  print(
    "\033[33m",
    "IF BY MISTAKELY YOU INPUT ANY WRONG INPUT according to requirements , ths progame shall not run correctly.",
    "\033[0m")
  
  print(
    "\033[33m",
    "then only KINDLY RUN THE PROGRAM AGAIN <-------------",
    "\033[0m")
  
  print("\033[35m", "\npress 1 to play song ")
  print("\npress 2 to exit ", "\033[0m")
  what_todo = int(input("\nWhat you want to do ? 🤔 (1 or 2)---> "))
  print("\033[32m", "\nENJOY 😎", "\033[0m")

  # take user's input
  while True:
    if what_todo == 1:
      play()
    elif what_todo == 2:
      print(
          "\033[32m",
          "\n\n------------------> Hope you ENJOYED 😄 <----------------------",
          "\033[0m")
      exit()
    else:
      print("\033[31m", "\nyou can only input 1 or 2. TRY AGAIN ", "\033[0m")

  # check whether you should call the play() subroutine depending on user's input
