import pyperclip
import sched, time

s = sched.scheduler(time.time, time.sleep)

def algo(sc): 

    find = ""
    clipboard = pyperclip.paste()

    #---------DataBsae-------------------------------------------------!
    db = ["activebits","compare","islower","lastrune","printstr","swap",
    "atoibase","concatparams","isnegative","lastword","revparams","teste",
    "atoi","concat","isnumeric","pointone","rot13","tolower",
    "basicatoi2","countdown","isprime","printcomb2","rot14","toupper",
    "basicatoi", "countif","isprintable", "printcombn","sortintegertable","unmatch",
    "basicjoin", "doop","issorted","printcomb","sortparams",
    "capitalize","enigma","isupper","printnbrbase","splitwhitespaces",
    "collatzcountdown","firstrune","iterativefactorial","printnbr","strlen",
    "compact","isalpha","join","printparams","strrev"]

    #-------Search---------------------------------------!
    for i in db:
        if (clipboard == i):
            find = clipboard + ".txt"

    #--------Algo Search & Answer Past ---------------------!
    if (find != ""):
        lol = "DataBase/" + find
        answer = open(lol, "r")
        rd = answer.read()
        pyperclip.copy(rd)

    #----- Dont touch --------------------------------------!
    sc.enter(0.1, 1, algo, (sc,))

s.enter(0.1, 1, algo, (s,))
s.run()

