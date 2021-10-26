import librosa
import IPython.display as ipd
from os import listdir
import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

tempos = []
temposms = []
index = 0
sounds = []

pygame.mixer.init()

for f in listdir("songs"):
    if(f.endswith(".wav") or f.endswith(".mp3")):
        fpath = "songs/" + f
        print(fpath)
        x, sr = librosa.load(fpath)
        ipd.Audio(x, rate=sr)
        tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')
        print(tempo)
        tempos.append(tempo)
        temposms.append(int(60000/tempo))
        soundObj = pygame.mixer.Sound(fpath)
        sounds.append(soundObj)
        pygame.mixer.music.queue(fpath)

print(temposms)

screen = pygame.display.set_mode((56, 56))
clock = pygame.time.Clock()
FPS = 1000/(temposms[index]) * 4
print(FPS)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image .fill(WHITE)

sounds[0].play()

closed = pygame.image.load("popcat1.png")
open = pygame.image.load("popcat2.png")
closedrect = closed.get_rect()
openrect = open.get_rect()

opened = False

while True:
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                   break

    FPS = 1000/(temposms[index]) * 4
    print(FPS)
    clock.tick(FPS)
    if(not pygame.mixer.get_busy()):
        index += 1
        if(index > len(sounds) - 1):
            index = 0
        sounds[index].play()

    opened = not opened

    screen.fill(BLACK)
    if(opened):
        screen.blit(open, openrect)
    else:
        screen.blit(closed, closedrect)
    pygame.display.update()  # Or pygame.display.flip()
