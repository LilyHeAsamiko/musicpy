# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:47:34 2024

@author: QinHeLily
"""
from musicpy import *
import mingus.extra.lilypond as mgLilyPond
from mingus import *

'''(Both of these examples are written without using advanced syntax, using advanced syntax makes the musicpy language look more compact)
detail see help(...)
'''
test = read(r"E:\musicpy\test.mid", split_channels=True)

#bar = mgLilyPond.from_Bar(test[0])
temp = containers
b = temp.Bar()
#b = [b+s for s in test[0]]
#for s in test[0]:b+str(s)[0]
for i in range(len(test[0])):
    b+str(test[0][i])[0]
mgLilyPond.from_Bar(b)
mgLilyPond.to_pdf(mgLilyPond.from_Bar(b),r"E:\musicpy\test")


a = (C(str(test[0][0])[0]+'maj9',3)/[2,3,4,1,5]) % (1/8,1/8)
b = (C(str(test[0][0])[0]+'maj9',3)/[2,3,4,1,5,2]) % (1/8, 1/8)
q = a + ~a[1:-1]
q2 = b + ~b[3:-1]
t = (q + q2) * 2
adding = chord(test[0][0:4]) % (1/2,1/2) * 2
t2 = t & adding
play(t2 + (t2 - 3), instrument=47)


#from mingus.midi import fluidsynth
tempC = containers
bc = tempC.Bar()
bct = bc
#b = [b+s for s in test[0]]
#for s in test[0]:b+str(s)[0]
for p in range(0,len(t2 + (t2 - 3)),4):
    bc = tempC.Bar()
    for i in range(len((t2 + (t2 - 3))))[p:p+4]:
        bc+str((t2 + (t2 - 3))[i])[0]
        bct+str((t2 + (t2 - 3))[i])[0]
    print(bc)
    print(mgLilyPond.from_Bar(bc))
#    mgLilyPond.to_pdf(mgLilyPond.from_Bar(bc),r"E:\musicpy\testc"+str(p/4))
#    midi_file_out.write_NoteContainer(r"E:\musicpy\ch"+str(p/4)+".testc.mid", bc, bpm=120, repeat=0, verbose=False)
    
#midi_file_out.write_NoteContainer(r"E:\musicpy\test.mid", bct)

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.containers.instrument import MidiInstrument
from mingus.midi import midi_file_out
for p in range(0,len(t2 + (t2 - 3)),4):
    bct = Bar()
    for i in range(len((t2 + (t2 - 3))))[p:p+4]:
        if len(str((t2 + (t2 - 3))[i])[0])==2:
            bct.place_notes(str((t2 + (t2 - 3))[i])[0]+'-'+str((t2 + (t2 - 3))[i])[1],4)
        elif len(str((t2 + (t2 - 3))[i])[0])==3:
            bct.place_notes(str((t2 + (t2 - 3))[i])[0:2]+'-'+str((t2 + (t2 - 3))[i])[2],4)
    print(bct)
    print(mgLilyPond.from_Bar(bct))
    i1=MidiInstrument()
    i1.instrument_nr=47
    t1=Track(i1)
    t1.add_bar(bct)
    midi_file_out.write_Track(r"E:\musicpy\ch"+str(p/4)+".testc.mid",t1)
    
    '''c=Composition()
    c.add_track(t1)
    c.add_track(...)
    midi_file_out.write_Composition("c.mid",c)'''

#write whole mid and export into mp3
write(t2 + (t2 - 3),bpm=120,channel=0,name=r"E:\musicpy\my first song test.mid",save_as_file=True)
from musicpy.daw import *
test_song = daw(1, name='my first song')
#test_song.load(0, 'piano') # load a folder named 'piano' with audio files as an instrument for the first channel

#test_song.instruments(47)
#test_song.instruments(0)
test_song.play(t2 + (t2 - 3))
test_song.load(0, r"E:\musicpy\my first song test.mid") # load an mdi file as an instrument for the first channel
test_piece = read(r"E:\musicpy\my first song test.mid", split_channels=True)
#export not working well
test_song.export(test_piece, channel_num = 1, mode = 'wav', filename="E:\musicpy\my first song test.wav",action ='play') # export a C major chord as a wav file, using instruments of channel 1
#make_mdi(path_of_instruments_folder, name_of_instruments_you_want_to_have)
print(test_song)
#instruments=['Acoustic Grand Piano', 'Electric Bass (finger)', 'Orchestral Harp', 'Synth Drum'],

'''test_song = daw(4, name='my first song')
new_piece = piece([t,adding, t2,  t2 - 3],
                  bpm=120,
                  start_times=[0, 0, 0, 0],
                  track_names=['piano', 'bass', 'harp', 'drum'],
                  daw_channels = [0,1,2,3])
test_song.play(new_piece) # play the piece type current_song
test_song.export(new_piece, action='play',filename='my first song.wav') # export the piece type current_song to


play(new_piece)'''

import os
from pydub import AudioSegment
def midi_to_mp3(midi_file, soundfont, mp3_file):
    # Convert MIDI to WAV using fluidsynth
    wav_file = mp3_file.replace('.mp3', '.wav')
    os.system(f'fluidsynth -ni {soundfont} {midi_file} -F {wav_file} -r 44100')
    # Convert WAV to MP3 using pydub
    audio = AudioSegment.from_wav(wav_file)
    audio.export(mp3_file, format='mp3')
    # Remove temporary WAV file
    os.remove(wav_file)
# Example usage:
midi_file = r"E:\musicpy\my first song test.mid"
soundfont = r"E:\GeneralUser_GS_1.471\GeneralUser GS 1.471\GeneralUser GS v1.471.sf2"
audio_file = r"E:\musicpy\my first song test musicpy.wav"
#midi_to_mp3(midi_file, soundfont, mp3_file)
from midi2audio import FluidSynth
fs = FluidSynth()
fs.midi_to_audio(midi_file, audio_file)




from musicpy import *
#duanwukuaile
pygame.init()
a = (C('F'+'maj9',3)/[2,3,4,1,5]) % (1/8,1/8)
b = (C('D'+'maj9',3)/[2,3,4,1,5,2]) % (1/8, 1/8)
q = a + ~a[1:-1]
q2 = b + ~b[3:-1]
t = (q + q2) * 2
adding = chord(['F4','D4','C4','C5'])% (1/2,1/4,1/4,1/2)+chord(['C5','F4','D4','E4'])%(1/4,1/4,1/4,1/4)+chord(['D4','C4','C5','C4'])%(1/4,1/4,1/4,1/4)+chord(['D4','C4','C4','F4#'])%(1/4,1/4,1/2,1/2)+chord(['C4','D4'])%(1/2,1/2)+C('G') 
t2 = t & adding

write(t2 + (t2 - 3),bpm=120,channel=0,name=r"E:\musicpy\dwkl\DWKL.mid",save_as_file=True)
play(t2 + (t2 - 3), instrument=47)

from mingus import *
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.containers.instrument import MidiInstrument
from mingus.midi import midi_file_out
import mingus.extra.lilypond as mgLilyPond

nps = Bar()
for p in range(0,len(adding)):
    print(str(adding.notes[p])[:len(str(adding.notes[p]))-1]+'-'+str(adding.notes[p])[-1])
    nps.place_notes(str(adding.notes[p])[:len(str(adding.notes[p]))-1]+'-'+str(adding.notes[p])[-1],1/(adding.interval[p] if adding.interval[p]>0 else 1))
    print(nps)
np
print(mgLilyPond.from_Bar(np))
mgLilyPond.to_pdf(mgLilyPond.from_Bar(np),r"E:\musicpy\dwkl\dwkladding.pdf")

c = Composition()
c.add_track(t2 + (t2 - 3))
#mgLilyPond.to_pdf(mgLilyPond.from_Composition(c),r"E:\musicpy\dwkl\dwkladding.pdf")
i = MidiInstrument()
i.midi_instr = 47
[i.can_play_notes(nt) for nt in (t2 + (t2 - 3)).notes] 

mgLilyPond.to_pdf(mgLilyPond.from_Track(t2 + (t2 - 3)),r"E:\musicpy\dwkl\dwkladding.pdf")


for p in range(0,len(adding),4):
    np = Bar()
    for i in range(len(adding))[p:min((p+4),len(adding))]:
        np.place_notes(str(adding[i])[:len(str(adding[i]))-1]+'-'+str(adding[i])[-1],1/adding.interval[i] if adding.interval[i]>0 else 1)
    print(mgLilyPond.from_Bar(np))
    print(np)
    mgLilyPond.to_png(mgLilyPond.from_Bar(np),r"E:\musicpy\dwkl\part"+str(p/4)+'.png')
    i1=MidiInstrument()
    i1.instrument_nr=47
    t1=Track(i1)
    t1.add_bar(np)
    midi_file_out.write_Track(r"E:\musicpy\dwkl\part"+str(p/4)+".mid",t1)


c_dwkl = midi_file_in.MIDI_to_Composition(read(r"E:\musicpy\dwkl\my first songDWKL.mid", split_channels=True))                                 
#This function can raise all kinds of exceptions (IOError, HeaderError, TimeDivisionError, FormatError), so be sure to try and catch.



import pygame
import numpy as np
from pygame.locals import *
import pygame.time

pygame.init()
# window create
screen = pygame.display.set_mode((960, 300))
pygame.display.set_caption("Let's Practice Piano!")

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
blue = (0,100,200)
green = (0,200,50)
red = (200,0,50)

pygame.font.init()
font = pygame.font.Font(None, 36)
#input_text = "E:\musicpy\test.mid"
#input_text = "E:\musicpy\chord test.mid"
text = '' 
textactive = False
input_rect = pygame.Rect(200,245,140,40)
color_ac=pygame.Color('green')
color_pc=pygame.Color('red') 
color=color_pc 
# note to keyboard
#textactive = True if using unicode text method
clock = pygame.time.Clock()

'''key_to_note = {
    pygame.K_a: 'C',
    pygame.K_s: 'D',
    pygame.K_d: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'A',
    pygame.K_j: 'B',
    pygame.K_w: 'C#',
    pygame.K_e: 'D#',
    pygame.K_t: 'F#',
    pygame.K_y: 'G#',
    pygame.K_u: 'A#',
}'''

key_to_octave = {
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_0: '0',
}

key_to_note01 = {
    pygame.K_a: 'A0',
    pygame.K_s: 'B0',
    pygame.K_w: 'A0#',
    pygame.K_d: 'C1',
    pygame.K_g: 'D1',
    pygame.K_f: 'E1',
    pygame.K_g: 'F1',
    pygame.K_h: 'G1',
    pygame.K_j: 'A1',
    pygame.K_k: 'B1',
    pygame.K_r: 'C1#',    
    pygame.K_t: 'D1#',
    pygame.K_u: 'F1#',
    pygame.K_i: 'G1#',
    pygame.K_o: 'A1#',
}

'''key_to_note = {
    pygame.K_a: 'C',
    pygame.K_s: 'D',
    pygame.K_d: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'A',
    pygame.K_j: 'B',
    pygame.K_w: 'C#',
    pygame.K_e: 'D#',
    pygame.K_t: 'F#',
    pygame.K_y: 'G#',    
    pygame.K_u: 'A#',
}'''

key_to_note78 = {
    pygame.K_a: 'C',
    pygame.K_s: 'D',
    pygame.K_d: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'A',
    pygame.K_j: 'B',
    pygame.K_k: 'C8',
    pygame.K_w: 'C#',
    pygame.K_e: 'D#',
    pygame.K_t: 'F#',
    pygame.K_y: 'G#',    
    pygame.K_u: 'A#',
}

#notes ={'C':32.70,'D':36.71,'E':41.20,'F':43.65,'G':49.00,'A':55.00,'B':61.74,'C#':34.65,'D#':38.89,'F#':46.25,'G#':51.91,'A#':58.27}
notes01 ={'A0':27.55,'B0':30.87,'A0#':29.36,'C':32.70,'D':36.71,'E':41.20,'F':43.65,'G':49.00,'A':55.00,'B':61.74,'C#':34.65,'D#':38.89,'F#':46.25,'G#':51.91,'A#':58.27}
notes78 ={'C':32.70,'D':36.71,'E':41.20,'F':43.65,'G':49.00,'A':55.00,'B':61.74,'C8':4186.11,'C#':34.65,'D#':38.89,'F#':46.25,'G#':51.91,'A#':58.27}


# keyboard
'''def draw_piano_keys(notes,octave):
    # C,D,E，F，G,A,B,C#,D#,F#,G#,A#
    # 0,1 2 3 4 5 6 7  8  9  10 11 
    # to position

    # 2:  0,1 X 3 4 5  <-   7 8 X 9 10 11

    # 2:  0,1,2 3,4 5,6 <- 0,1,2,3,4, 5, 6

    for i, note in enumerate(notes):
        if note =='Db':
            note = 'C#'
        if note =='Eb':
            note = 'D#'
        if note =='Gb':
            note = 'F#'
        if note =='Ab':
            note = 'G#'
        if note =='Bb':
            note = 'A#'
        width = 79
        height = 100
        if octave > 1:
            if note in ['C#','D#']:  #7,8 -> 0,1
                x = 35+ (i-7)* 80
                y = 0 
                color = gray if note_pressed[note] else black
            elif note in ['F#','G#','A#']:#9,10,11 -> 3,4,5
                x = 35 + (i-7+1) * 80 
                y = 0 
                color = gray if note_pressed[note] else black
            elif note in ['C','D','E','F','G','A','B']:
                x = i * 80
                y = 101
                color = gray if note_pressed[note] else white
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            text_surface = font.render(note, True, white)
            screen.blit(text_surface, (x + (width - text_surface.get_width()) / 2, y + (height - text_surface.get_height()) / 2))
'''
def draw_piano_keys01(notes01,octave):
    # A0,B0,A0#,C,D,E，F，G,A,B8,C#,D#,F#,G#,A#
    # 0, 1  2   3 4 5 6 7 8 9  10 11 12 13 14
    # to position

    # 1:  X 2,3,X 5 6 7   <-   X 10 11 X 12 13 14
    # 0:0                 <- 2  

    # 1:    2,3,4 5,6 7,8 <-     3,4,5,6,7,8，9
    # 0:0 1               <- 0 1
    for i, note in enumerate(notes01):
        if note =='Db':
            note = 'C#'
        if note =='Eb':
            note = 'D#'
        if note =='Gb':
            note = 'F#'
        if note =='Ab':
            note = 'G#'
        if note =='Bb':
            note = 'A#'
        if note =='B0b':
            note = 'A0#'
        width = 79
        height = 100
        if octave <= 1:
            if note in ['C1#','D1#']: #10,11 -> 2,3
                x = 35 + (i-3-7+2) * 80
                y=0
                color = gray if note01_pressed[note] else black
            elif note in ['F1#','G1#','A1#']: #12,13,14 -> 5,6,7
                x = 35 + (i-3-7+3) * 80
                y = 0
                color = gray if note01_pressed[note] else black
            elif note in ['C1','D1','E1','F1','G1','A1','B1']: #3-9 ->2-8 
                x = (i-1)*80
                y = 101
                color = gray if note01_pressed[note] else white
            elif note =='A0#': # 2->0
                x = 35 + (i-2) * 80 #35
                y = 0 
                color = gray if note01_pressed[note] else black
            elif note in ['A0','B0']: 
                x = i* 80
                y = 101
                color = gray if note01_pressed[note] else white
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        text_surface = font.render(note, True, white)
        screen.blit(text_surface, (x + (width - text_surface.get_width()) / 2, y + (height - text_surface.get_height()) / 2))

def draw_piano_keys78(notes78,octave):
    # C,D,E，F，G,A,B,C8，C#,D#,F#,G#,A#
    # 0,1 2 3 4 5 6 7  8  9  10 11 12
    # to position

    # 2:  0,1 X 3 4 5    <-  8 9 X 10 11 12

    # 2:  0,1,2 3,4 5,6 7 <- 0,1,2,3,4, 5, 6 7

    for i, note in enumerate(notes78):
        if note =='Db':
            note = 'C#'
        if note =='Eb':
            note = 'D#'
        if note =='Gb':
            note = 'F#'
        if note =='Ab':
            note = 'G#'
        if note =='Bb':
            note = 'A#'
        width = 79
        height = 100
        if octave > 1:
            if note in ['C#','D#']:  #8,9 -> 0,1
                x = 35+ (i-8)* 80
                y = 0 
                color = gray if note_pressed[note] else black
            elif note in ['F#','G#','A#']:#10,11，12 -> 3,4,5
                x = 35 + (i-8+1) * 80 
                y = 0 
                color = gray if note_pressed[note] else black
            elif note in ['C','D','E','F','G','A','B','C8']:
                x = i * 80
                y = 101
                color = gray if note_pressed[note] else white
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            text_surface = font.render(note, True, white)
            screen.blit(text_surface, (x + (width - text_surface.get_width()) / 2, y + (height - text_surface.get_height()) / 2))


N = ''
octave = 4

running = True
note_pressed = {note: False for note in notes78}
note01_pressed = {note: False for note in notes01}
try:
    while running:   
        if octave >2:
            note_pressed_copy = note_pressed
        else:
            note01_pressed_copy = note01_pressed
        #screen.fill(blue)
        #draw keyboard
        #draw_piano_keys(notes,octave)
        
        font = pygame.font.Font(None, 36)
    #    Ttext = font.render('Please input the midi file path(as C:/Users/XXX.mid):', True, black)
    #    text_rect = Ttext.get_rect()
    #    text_rect.center = (350, 275)
    #    screen.blit(Ttext, text_rect)
    #    pygame.display.flip()
            # Blit the input_box rect.
    #    pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]):
                x, y = pygame.mouse.get_pos()
                if 101 <= y <= 200:
                    key_index = x // 80                    
                    #to list index 
                    #   1:    2,3,4 5,6 7,8 ->     3,4,5,6,7,8,9
                    #   0:0 1               -> 0 1
                    # 2-8:0 1,2,3 4,5 6 7   -> 0,1,2,3,4,5,6 7
                    if octave == 1:
                        key_index += 1
                    if 0 <= key_index <10:
                        if octave >=2:
                            N = list(notes78.keys())[key_index]
                            if not note_pressed[N]:  # no repeat
                                print('N: ',N)
                                note_pressed[N] = True
                                play(chord(str(N)+str(octave))) if key_index <7 else play(chord(str(N).replace('8',str(octave+1))))
                        else:
                            N = list(notes01.keys())[key_index] 
                            if not note01_pressed[N]:  # no repeat
                                print('N: ',N)
                                note01_pressed[N] = True
                                play(chord(N))
                elif 0 <= y <= 100:
                    key_index = (x-35) //80
                    #  1:  X 2,3 X 5 6,7 ->     X 10 11 X 12 13 14
                    #  0:0               ->  2  
                    #2-8:0 1 X 3 4 5     ->  8  9  X 10 11 12
                    if octave >=2:
                        if key_index <2:
                            key_index += 8
                        else:
                            key_index += 7        
                    if octave ==1:
                        if key_index >= 2 and key_index <4:
                            key_index += 8
                        elif key_index>4:
                            key_index += 7        
                    if octave ==0:
                        key_index += 2
                    if key_index <= 14:
                        if octave >=2:
                            N = list(notes78.keys())[key_index]
                            if not note_pressed[N]:  # no repeat
                                note_pressed[N] = True
                                print(chord(N))
                                play(chord(str(N)+str(octave))) if key_index <12 else play(chord(str(N).replace('8',str(octave+1))))
                        else:
                            N = list(notes01.keys())[key_index]
                            if not note01_pressed[N]:  # no repeat
                                print('N: ',N)
                                print('Note: ',note(N))
                                note01_pressed[N] = True
                                play(chord(N))    
                elif y > 210:
                    #textactive = True
                    #text= ''
                    if input_rect.collidepoint(event.pos): 
                        textactive = True
    #                text_rect.move_ip(x - text_rect.width // 2, y - text_rect.height)  # to the text_rec
    #                pygame.draw.rect(screen, red, text_rect)  # draw red rec_text
    #                screen.blit(text, text_rect)  # show text on the rectangle
            elif event.type == pygame.MOUSEBUTTONUP:
                if octave >=2:               
                    note_pressed_copy = note_pressed
                    for N in note_pressed:
                        note_pressed[N] = False
                else:
                    note_pressed_copy =note01_pressed
                    for N in note01_pressed:
                        note01_pressed[N] = False
            elif event.type == pygame.KEYDOWN:
                if octave >=2:
                    print(textactive)
                    if textactive:                               
                        if event.key == pygame.K_RETURN:  # enter key event
                            print(text)
                            textactive = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    elif text =='':
                        if event.key in key_to_octave:
                            octave = int(key_to_octave[event.key])   
                            print(octave)
                        elif event.key in key_to_note78:
                            N = key_to_note78[event.key]
                            note_pressed[N] = True
                            play(chord(str(N)+str(octave))) if N!= 'C8' else play(chord(str(N).replace('8',str(octave+1))))
                if octave <2:
                    print(textactive)
                    if textactive:                               
                        if event.key == pygame.K_RETURN:  # enter key event
                            print(text)
                            textactive = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                    elif text =='':
                        if event.key in key_to_octave:
                            octave = int(key_to_octave[event.key])
                            print(octave)
                        elif event.key in key_to_note01:
                            N = key_to_note01[event.key]
                            note01_pressed[N] = True
                            play(chord(N))                
            elif event.type == pygame.KEYUP:
                if octave >=2:               
                    if textactive == False:
                        if text=='':
                            note_pressed_copy = note_pressed
                            if event.key in key_to_octave:
                                octave = int(key_to_octave[event.key])
                                print(octave)
                            elif event.key in key_to_note78:
                                N = key_to_note78[event.key]
                                note_pressed[N] = False
                        else:
                            t = read(text)
                            play(chord(t)[0])
                                
                elif octave <2:
                    if textactive == False:
                        if text=='':
                            note_pressed_copy = note01_pressed
                            if event.key in key_to_octave:
                                octave = int(key_to_octave[event.key])
                                print(octave)
                            elif event.key in key_to_note01:
                                N = key_to_note01[event.key]
                                note01_pressed[N] = False
                        else:
                            t = read(text)
                            play(chord(t)[0])
                
        screen.fill(blue)
        #draw keyboard
        #rint(note_pressed_copy)
        if octave <2:
            draw_piano_keys01(notes01,octave)
        else:
            draw_piano_keys78(notes78,octave)
            
        font = pygame.font.Font(None, 36)
        Ttext = font.render('Please input the midi file path(as C:/Users/XXX.mid):', True, black)
        text_rect = Ttext.get_rect()
        text_rect.center = (350, 275)
        screen.blit(Ttext, text_rect)
        pygame.display.flip()
    
        if textactive: 
            color=red 
        else: 
            color=green 
        
        pygame.draw.rect(screen,color,input_rect,2)
        text_surface = font.render(text,True,white) 
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))
        input_rect.w=max(200,text_surface.get_width() + 10) 
        
        fontObj = pygame.font.Font(None, 18)
        showtext= 'Note: '+str(N)+' at Octave '+str(octave)
        textSurfaceObj = fontObj.render(showtext,True,green)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (305, 220)
        screen.blit(textSurfaceObj, textRectObj)
        # Blit the input_box rect.
        pygame.display.flip()
        clock.tick(60)#ms
        
    
    #    textSurfaceObj0 = fontObj.render(text,True,black)
    ##    width = max(200, textSurfaceObj0.get_width()+10)
    #    input_box.w = width
            # Blit the text.
    #    screen.blit(textSurfaceObj0, textSurfaceObj0.get_rect(center=(35, 220)))
            # Blit the input_box rect.
    #    pygame.display.flip()
        
        # if midi uploaded uploaded
    #'''   try:'''
    #    if text and textactive==False:
    
        #for test:
        #text = "E:\musicpy\dwkl\my first songDWKL.mid"
#        while not event.key:
        if len(text)>0 and textactive==False:
            t = read(text)
#            pygame.mixer.init()
#            pygame.mixer.music.load(text)
#            pygame.mixer.music.play()
#            play(chord(t)[0])
##            while pygame.mixer.music.get_busy():
#                clock.tick(60)
            octave = int(str(t[0][0]).replace('#','')[-1])
            if octave >=2:    
                note_pressed = {note: False for note in notes78}
                #t = read(f'{input_text}')
                print(t[0])
                if len(t[0])==1:
                    note_pressed[t[0][0]] = True
                    draw_piano_keys78(note_pressed,octave)
                    pygame.display.flip()
    #                clock.tick(20)
                    play(t[0][0])
                    note_pressed = {note: False for note in notes78}
                    clock.tick(60)
                elif len(t[0])>1:
                    intervalinfo = chord(t)[0].interval #not chord(t[0]).interval which are all zeros
                    #with pure notes
                    event_key = pygame.K_9
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        else:
                            if 0 not in intervalinfo:
                                for c in t[0]:
                                    if event_key == pygame.K_9:
                                        note_pressed[c] = True
                                        pygame.mixer.init()
                                        play(c)
                                        draw_piano_keys78(note_pressed,int(str(c).replace('#','')[-1]))
                                        pygame.display.flip()
                                        note_pressed = {note: False for note in notes78}
                                        clock.tick(90)
                                event_key = pygame.K_9
                            #with chord
                            else:
                                i = 0
                                while i in range(len(t[0])):
                                    if event_key == pygame.K_9:
                                        if intervalinfo[i] !=  0 or i == len(t[0])-1:
    #                                        pygame.mixer.init()
                                            play(t[0][i])
                                            note_pressed[str(t[0][i])[0:len(str(t[0][i]))-1]] = True
                                            print(i,intervalinfo[i],t[0][i],note_pressed)
                                            draw_piano_keys78(note_pressed,int(str(t[0][i]).replace('#','')[-1]))
                                            pygame.display.flip()
                                            clock.tick(90)
                                            note_pressed = {note: False for note in notes78}
                                            i += 1
                                        else:
                                            for j in range(i,len(t[0])):
                                                note_pressed[str(t[0][j])[0:len(str(t[0][j]))-1]] = True
                                                if event_key == pygame.K_9:
                                                    if j == len(t[0])-1:
                                                        ch = t[0][i:]
                    #                                    CH=chord(notes=ch,interval=intervalinfo[0][i:j],start_time=0)
                    #                                    print(CH)
                                                        #pygame.mixer.init()
                                                        play(ch)
                                                        print(j,intervalinfo[j],t[0][j],note_pressed)
                                                        draw_piano_keys78(note_pressed,int(str(t[0][j]).replace('#','')[-1]))
                                                        pygame.display.flip()
                                                        clock.tick(90*len(ch))
                                                        note_pressed = {note: False for note in notes78}                                
                                                        i = j+1           
                                                    elif intervalinfo[j+1] !=  0:
                                                        #ch = [tc for tc in note_pressed if note_pressed[tc] is True]
                                                        ch = t[0][i:j+1]
                    #                                    CH=chord(notes=ch,interval=intervalinfo[0][i:j],start_time=0)
                    #                                    print(CH)
                                                        #pygame.mixer.init()
                                                        play(ch)
                                                        print(j,intervalinfo[j],t[0][j],note_pressed)
                                                        draw_piano_keys78(note_pressed,int(str(t[0][j]).replace('#','')[-1]))
                                                        pygame.display.flip()
                                                        clock.tick(90*len(ch))
                                                        note_pressed = {note: False for note in notes78}                                
                                                        i = j+1
                                                        break
                        text = ''
                        event_key = pygame.K_BREAK
            if octave <2:    
                        note01_pressed = {note: False for note in notes01}
                        if len(t[0])==1:
                            note01_pressed[t[0][0]] = True
                            draw_piano_keys01(note01_pressed,int(str(t[0][0]).replace('#','')[-1]))
                            pygame.display.flip()
            #                clock.tick(20)
                            pygame.mixer.init()
                            play(t[0][0])
                            note01_pressed = {note: False for note in notes01}
                            clock.tick(60)
                            event_key = pygame.K_BREAK
                        elif len(t[0])>1:
                            event_key = pygame.K_9
                            intervalinfo = chord(t)[0].interval #not chord(t[0]).interval which are all zeros
                            #with pure notes
                            if 0 not in intervalinfo:
                                for c in t[0]:
                                    if event_key == pygame.K_9:
                                        note01_pressed[c] = True
                                        pygame.mixer.init()
                                        play(c)
                                        draw_piano_keys01(note01_pressed,int(str(c).replace('#','')[-1]))
                                        pygame.display.flip()
                                        note01_pressed = {note: False for note in notes01}
                                        clock.tick(90)
                                event_key = pygame.K_BREAK
                            #with chord
                            else:
                                i = 0
                                while i in range(len(t[0])):
                                    if event_key == pygame.K_9:
                                        if intervalinfo[i] !=  0 or i == len(t[0])-1:
                                            pygame.mixer.init()
                                            play(t[0][i])
                                            note01_pressed[str(t[0][i])[0:len(str(t[0][i]))-1]] = True
                                            print(i,intervalinfo[i],t[0][i],note01_pressed)
                                            draw_piano_keys01(note01_pressed,int(str(t[0][i]).replace('#','')[-1]))
                                            pygame.display.flip()
                                            clock.tick(90)
                                            note01_pressed = {note: False for note in notes01}
                                            i += 1
                                        else:
                                            for j in range(i,len(t[0])):
                                                note01_pressed[str(t[0][j])[0:len(str(t[0][j]))-1]] = True
                                                if event_key == pygame.K_9:
                                                    if j == len(t[0])-1:
                                                        ch = chord(t)[0][i:]
                    #                                    CH=chord(notes=ch,interval=intervalinfo[0][i:j],start_time=0)
                    #                                    print(CH)
                                                        pygame.mixer.init()
                                                        play(ch)
                                                        print(j,intervalinfo[j],t[0][j],note01_pressed)
                                                        draw_piano_keys01(note01_pressed,int(str(t[0][j]).replace('#','')[-1]))
                                                        pygame.display.flip()
                                                        clock.tick(90*len(ch))
                                                        note01_pressed = {note: False for note in notes01}                                
                                                        i = j+1           
                                                    elif intervalinfo[j+1] !=  0:
                                                        #ch = [tc for tc in note_pressed if note_presse88d[tc] is True]
                                                        ch = chord(t[0])[i:j+1]
                    #                                    CH=chord(notes=ch,interval=intervalinfo[0][i:j],start_time=0)
                    #                                    print(CH)
                                                        pygame.mixer.init()
                                                        play(ch)
                                                        print(j,intervalinfo[j],t[0][j],note01_pressed)
                                                        draw_piano_keys01(note01_pressed,int(str(t[0][j]).replace('#','')[-1]))
                                                        pygame.display.flip()
                                                        clock.tick(90*len(ch))
                                                        note01_pressed = {note: False for note in notes01}                                
                                                        i = j+1
                                                        break
                        text = ''
                        event_key = pygame.K_BREAK
except Exception as e:
        print("Running failed: ", e)
        running = False
        pygame.quit()

pygame.display.update()
pygame.quit()

#"E:\musicpy\chord test.mid"