import fungsiDasar as fd

def list_game():
     global _possession,_gamedata,_loggedUser
     username = _loggedUser[0]
     x =fd.len(_possession) 
     k= fd.len(_gamedata)
     t=0 
     if(x==0):
         print()
         print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
         return 
     for m in range (x):
             if(_possession[m][1]==username):
                 for j in range (k):
                     if(_possession[m][0]==_gamedata[j][0]):
                         print()
                         t+=1
                         print(t,end=". ")
                         print(_gamedata[j][0],end=" | ")
                         print(_gamedata[j][1],end=" | ")
                         print(_gamedata[j][2],end=" | ")
                         print(_gamedata[j][3],end=" | ")
                         print(_gamedata[j][4],end="")
                 

                         