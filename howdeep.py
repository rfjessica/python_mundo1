from pygame import mixer
mixer.init()
mixer.music.load('beegees.mp3')
mixer.music.play()
while mixer.music.get_busy():pass
