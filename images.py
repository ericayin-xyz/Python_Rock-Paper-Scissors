logo = """
______________________________________________________________________________________
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    _______     ______    ______   __   ___                                          
   /"      \   /    " \  /" _  "\ | "| /  ")                                         
  |:   ./   | // ____  \(: ( \___)(: |/   /                                          
  |_____/   )/  /    ) :)\/ \     |    __/                                           
   //      /(: (____/ // /   \ _  (/  _  \                                           
  |:  __   \ \        / (:   _) \ |: | \  \                                          
  |__|  \___) '\_____/   \_______)(__|  \__)                                         
     _______     __         _______    _______   _______                             
    |   __ "\   /""\       |   __ "\  /"     "| /"      \                            
    (. |__) :) /    \      (. |__) :)(: ______)|:        |                           
    |:  ____/ /' /\  \     |:  ____/  \     |  |_____/   )                           
    (|  /    //  __'  \    (|  /      // ___)_  //      /                            
   /|__/ \  /   /  \.  \  /|__/ \    (:      "||:  __   \                            
  (_______)(___/    \___)(_______)    \_______)|__|  \___)                           
    ________  ______    __      ________  ________   ______     _______    ________  
   /"       )/" _  "\  |" \    /"       )/"       ) /    " \   /"      \  /"       ) 
  (:   \___/(: ( \___) ||  |  (:   \___/(:   \___/ // ____  \ |:        |(:   \___/  
   \___  \   \/ \      |   |   \___  \   \___  \  /  /    ) :)|_____/   ) \___  \    
    __/  .\  //  \ _   |.  |    __/  .\   __/  .\(: (____/ //  /       /   __/  '\.   
   /" \   :)(:   _) \  /\  |\  /" \   :) /" \   :)\        /  |:  __   \  /" \   :)  
  (_______/  \_______)(__\_|_)(_______/ (_______/  .\_____/   |__|  \___)(_______/   

"""  



menu_image = {
1: """
 -------------- 
| 1. PLAYER-1  |  
 -------------- """,
2: """
 -------------- 
| 2. PLAYER-2  |  
 -------------- """,
3: """ 
 ---------------------- 
| 3. Difficulty Levels |  
 ---------------------- """,
4: """ 
 ------------ 
| 4. | EXIT  |  
 ------------ """
}




menu_image_line = """
   --------------       ---------------       ----------------------       ------------
--| 1. PLAYER-1  |-----|  2. PLAYER-2  |-----| 3. Difficulty Levels |-----| 4. | EXIT  |
   --------------       ---------------       ----------------------       ------------

"""

# print(menu_image[2])
# print(menu_image[3])
# print(menu_image[4])

scissors = """
                 ._____
            ____/    ___)______.
                         _______) 
                        ________)
            ___     (_____)
               ` ___(____)

"""

rock = """
                ._____
            ___/    ___)_.
                   (_______) 
                   (_______)
            __     (______)
               ` __(_____)
   
"""

paper = """
                ._____.
            ___/    ___)_____.
                        ______) 
                        _______)
            __         _______)
               \ .________)
   
"""

line = """
---- - -- - - - -- - -- - - -- - - -- - -- --- - -
"""

you = """
                                                 -----
                                                | YOU |
                                                 -----
"""

house = """
                                   /\.
                              /\  //\..
                       /\    //.\///\.\.       /\.
                      //.\  ///\////\.\.\ /\  //\..
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \.
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \.
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\.
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\.
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\.
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\.
  /^ ^  ^ ___ ^    ||___|___||||||||||||___|__|||      /||o||||||\.
 / ^   ^ /___\  ^  ||___|___||||||||||||___|__|||          | |
/ ^ ^ ^ <" | ">  ^ ||||||||||||||||||||||||||||||oooooooooo| |ooooooo
oooooooo(o_|_o)ooooooooooooooooooooooooooooooooooooooooooooooooooooooo
TTTTTTTTTu___uTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
  ====    ====    ====   ====    ====    ====    ====    ====    ====  

"""



win = """
                      __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
   oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
   oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
             *OOOOOOOOo           oOOOOOOOO*      
                 *OOOOOOOOOOOOOOOOOOOOO*          
                      ""ooooooooo""

"""

a = """
                                      
           .---.                      
          /. ./|  ,--,                
      .--'.  ' ;,--.'|         ,---,  
     /__./ \ : ||  |,      ,-+-. /  | 
 .--'.  '   \' .`--'_     ,--.'|'   | 
/___/ \ |    ' ',' ,'|   |   |  ,"' | 
;   \  \;      :'  | |   |   | /  | | 
 \   ;  `      ||  | :   |   | |  | | 
  .   \    .\  ;'  : |__ |   | |  |/  
   \   \   ' \ ||  | '.'||   | |--'   
    :   '  |--" ;  :    ;|   |/       
     \   \ ;    |  ,   / '---'        
      '---"      ---`-'               
                                

"""
# print(a)
lose = """
                      __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo                          
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo             
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo                  .---.   
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo                /. ./|   ,--,      
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo.           .--'.  ' ; ,--.'|          ,---,      
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo          /__./ \ : | |  |,       ,-+-. /  | 
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo      .--'.  '   \' . `--'_      ,--.'|'   | 
   oOOOOOOOOOOOOOOOOOo             oOOOOOOOOOOOOOOOOOo     /___/ \ |    ' ' ,' ,'|    |   |  ,"' | 
    *OOOOOOOOOOOOOO  oOOOOOOOOOOOOOo  OOOOOOOOOOOOOO*      ;   \  \;      : '  | |    |   | /  | | 
    *OOOOOOOOOOo  *OOOOOOOOOOOOOOOOOOO*  oOOOOOOOOOO*       \   ;  `      | |  | :    |   | |  | | 
     *OOOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOOO*         .   \    .\  ; '  : |__  |   | |  |/ 
      *OOOOOo  *OOOOOOOOOOOOOOOOOOOOOOOOO*  oOOOOO*           \   \   ' \ | |  | '.'| |   | |--'  
        *OO      OOOOOOOOOOOOOOOOOOOOOOO      OO*              :   '  |--"  ;  :    ; |   |/  
          *OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO*                \   \ ;     |  ,   /  '---' 
             *OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO*                    '---"       ---`-'      
                 *OOOOOOOOOOOOOOOOOOOOO*          
                      ""ooooooooo""

"""
