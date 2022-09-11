# Escape from Hakurei shrine v0.00

# Introduce
 This program is Text adventure.
 Input text command to escape the shrine.
 Resourse is Touhou project.

## 1. How to execute game.py
 1. Open command prompt.
 2. Input the text ``python game.py -`` + mode\
 modes can be ``e``, ``k``, ``j``, ``c``, ``r`` \
 mode can be omitted and language can be English automatly.
 -e: Execute program by English.\
 -k: Execute program by Korean.\
 -j: Execute program by Japanese. (did not made.)\
 -c: Execute program by Chinese. (did not made.)\
 -r: Execute program by Russian (did not made.)\
 \
 **ex)** ``python game.py -e``

## 2. Structure of the program (did not made.)
 ``[mrskr|usrf] $ ``\
 mrskr: account name\
   It can be mrskr, kcysn, skyiz, hctylp, rimhk\
 usrf: account right\
   \_adm (admin): Can use all command\
   usrg (guest user): Can use some command\
   usrf (friend user): Can use command more than guest.\
 \
 **ex)**\
 ``[mrskr|usrf] $ open closet``\
 ``[kcysn|usrg] $ unzip rainbow-box 3146``\
 \
## 3. Login from starting game (did not made.)
 ``$ login -e mrskr``\
 login: the command\
 -e: difficulty. It can be e(Easy), n(Normal), h(Hard), l(Lunartic)\
 If mode was omitted, mode can be easy automatly.
 mrskr: account name\
 \
 To logout, input ``logout`` on command.\
 **Warning!** Going is Disappear if you have logout.
