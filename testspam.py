import time
def taym():
  time.sleep(0.3)
def main():
  print("Welcome to SpamX")
  choice1 = input("""1. Spam
2. Exit
$ """) 
  if choice1 == "1":
    spam1 = input("""Input your spam text
  $ """)
    times = int(input("""How many times of spamming?
    $ """))
    secs = bool(input("""Input the seconds of pause in spamming
    $ """))
    for spamz in range(times):
         print(">>", spam1)
         time.sleep(secs)
    def ulet():
         print("""1. Go back
2. Exit """)
         awit = input("$ ")
         if awit == "1":
             main()
         elif awit == "2":
           exit("Goodbye!")
          
           exit()
         else:
           print("Syntax error!")
           ulet()
    ulet()
  elif choice1 =="2":
    taym()
    exit("Goodbye!")
  else:
    print("Syntax error!")
    taym()
    main()
main()
#Developed by raym huhu
