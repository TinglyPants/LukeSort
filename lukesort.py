# quicksort display and demo
import random, math
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption("Quicksort")

pygame.mixer.init(channels=2, size=-16, buffer=512)
pygame.mixer.set_num_channels(16)

beeps = [pygame.mixer.Sound("a.wav"),
         pygame.mixer.Sound("b.wav"),
         pygame.mixer.Sound("c.wav"),
         pygame.mixer.Sound("d.wav"),
         pygame.mixer.Sound("e.wav"),
         pygame.mixer.Sound("f.wav"),
         pygame.mixer.Sound("g.wav"),
         pygame.mixer.Sound("h.wav")]

[i.set_volume(0.1) for i in beeps]

victory = pygame.mixer.Sound("victory.wav")

def displayArray(arr, markerIndex):
    screen.fill((0,0,0))
    for i in range(len(arr)):
        if i == markerIndex:
            colour = (255, 0, 0)
            beeps[math.floor((i*8)/1000)].play()
            pygame.time.delay(50)
        else:
            colour = (255,255,255)
        bar = pygame.Rect((i, 400-arr[i]), (1,arr[i]))
        pygame.draw.rect(screen, colour, bar)
           
    pygame.display.flip()

def checkArray(arr):
    for i in range(len(arr)):
        bar = pygame.Rect((i, 400-arr[i]), (1,arr[i]))
        pygame.draw.rect(screen,(0,255,0), bar)
        beeps[math.floor((i*8)/1000)].play()
        pygame.time.delay(10)
        pygame.display.flip()
    pygame.time.delay(200)
    victory.play()
    pygame.time.delay(5000)


def partition(arr, low, high):
    pivot = arr[high]
    l_sublist = []
    r_sublist = []

    # need to modify arr in place!
    for j in range(low, high):
        if arr[j] <= pivot:
            l_sublist.append(arr[j])
        else:
            r_sublist.append(arr[j])
           
    arr[low:high+1] = l_sublist + [pivot] + r_sublist
   

    displayArray(arr, low + len(l_sublist))

    return low + len(l_sublist)
       
def quicksort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        quicksort(arr, start, pIndex-1)
        quicksort(arr, pIndex+1, end)

       
t = [round((400*i)/1000) for i in range(1000)]
random.shuffle(t)
quicksort(t, 0, 1000-1)

checkArray(t)