# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lyra", color="#ffa500", image="lyra")
define v = Character("Vergil", color="ff0000", image="vergil")
define m = Character("Maria", color="00ffff", image="maria")
define t = Character("Terry", color="0000ff", image="terry")
define b = Character("Benjamin", color="#964b00", image="benjamin")
define s = Character("Sakura", color="#ffc0cb", image="sakura")
define c = Character("Cole", color="#ffff00", image="cole")
define r = Character("Rachel", image="rachel")
define lo = Character("Logan", image="logan")
define ma = Character("Mason", image="mason")
define mi = Character("Milo", image="milo")
define li = Character("Liam", image="liam")
define g = Character("Guard", image="guard")
define g2 = Character("Guard", image="guard")
define k = Character("Dr. Westworth", image="kiara")
define mat = Character("Dr. Leonard", image="matt")
define va = Character("Dr. Montevero", image="valerie")


# The game starts here.

label start:
    
    camera:
        perspective True
        gl_depth True
        
    transform zbg:
        zpos -10000 zzoom True

    scene bg line at center, zbg
    
    play music free_time
    
    show lyra happy at center
    
    show guard:
        xalign 0.9 yalign 1.0 zpos -500

    l "Hi! I'm legendary TSC OC Lyra Iridi! Yahoo! Yippee!"
    v "Vergil Todsky"
    m "Maria Westworth"
    t "Terry Johnstone"
    b "Benjamin Hilbert"
    s "Sakura Takahashi"
    c "Cole Davis"

    return
