lyric1 = "Na"
lyric2 = "Hey"
lyric3 = "Goodbye!"
masterpiece = " "

def song(lyric, repeat, masterpiece):
    for i in range (1, repeat+1):
        masterpiece = masterpiece + lyric + " "
        if i == repeat:
            print(masterpiece)

song(lyric1, 4, masterpiece)
song(lyric1, 4, masterpiece)
song(lyric2, 3, masterpiece)
song(lyric3, 1, masterpiece)
    
