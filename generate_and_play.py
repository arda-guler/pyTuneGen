from synthesizer import Player, Synthesizer, Waveform
import random
import time

#-------------------------
#  NOTE FREQUENCY TABLE
#-------------------------

# 4th octave
c4 = 262
c_4 = 277
d4 = 294
d_4 = 311
e4 = 330
f4 = 349
f_4 = 370
g4 = 392
g_4 = 415
a4 = 440
a_4 = 466
b4 = 494

# 5th octave
c5 = 523
c_5 = 554
d5 = 587
d_5 = 622
e5 = 659
f5 = 698
f_5 = 740
g5 = 784
g_5 = 831
a5 = 880.00
a_5 = 932
b5 = 988

# chords

full_notes = {"C4":c4, "C#4":c_4, "D4":d4, "D#4":d_4, "E4":e4, "F4":f4, "F#4":f_4, "G4":g4, "G#4":g_4, "A4":a4, "A#4":a_4, "B4":b4,
         "C5":c5, "C#5":c_5, "D5":d5, "D#5":d_5, "E5":e5, "F5":f5, "F#5":f_5, "G5":g5, "G#5":g_5, "A5":a5, "A#5":a_5, "B5":b5}

c_major = {"C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "B4":b4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "B5":b5}

d_minor = {"C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "A#5":a_5}

g_minor = {"C4":c4, "D4":d4, "D#4":d_4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "D#4":d_5, "F4":f5, "G4":g5, "A4":a5, "A#4":a_5}

chords = {"Full Notes":full_notes, "C Major":c_major, "D Minor":d_minor, "G Minor":g_minor}

#-------------------------
#       BPM PRESETS
#-------------------------
bpm_slowest = 30
bpm_slow = 60
bpm_slowish = 90
bpm_normal = 120
bpm_fastish = 160
bpm_fast = 180
bpm_fastest = 210

bpms = [bpm_slowest, bpm_slow, bpm_slowish, bpm_normal, bpm_fastish, bpm_fast, bpm_fastest]

#-------------------------
#     NOTE DURATIONS
#-------------------------

note_durations = {"1/4":1/4, "1/2": 1/2, "1":1, "2":2, "4":4}

#-------------------------
#       SETUP
#-------------------------
player = Player()
player.open_stream()
synth1 = Synthesizer(osc1_waveform = Waveform.sine, osc1_volume=1.0,
                     use_osc2=True, osc2_waveform=Waveform.square, osc2_volume=0.3)

#-------------------------
#       PLAY
#-------------------------

# get random bpm, scale, chord, silence percent, length
bpm_current = bpms[random.randint(0, len(bpms) - 1)]
print("BPM: " + str(bpm_current))

scale = random.randint(1, 8)
print("Scale: " + str(scale) + "/4")

chord_current_name = random.choice(list(chords.keys()))
chord_current = chords.get(chord_current_name)
print("Chord:", chord_current_name)

# This next value ensures that the generator
# doesn't jump between notes of very different
# pitches. I could allow a real musician to do that
# but this script probably should not. ( ◡‿◡ *)

note_jump_limit = 600 # Hertz

silence_percent = 2

music_length = 250 # num. of bars
print("Length:", music_length, "bars")

for i in range(0, music_length):

    # divide the next bar into notes of various lengths
    durations_current = []

    while durations_current == [] or sum(durations_current) < scale:
        next_duration = random.choice(list(note_durations.keys()))
        next_duration_value = note_durations.get(next_duration)
        
        if sum(durations_current) + next_duration_value <= scale:
            durations_current.append(next_duration_value)

    print("\n         Bar #" + str(i+1) + ": " + str(durations_current))

    note_last = None
    note_current_name = None
    note_current = None

    for duration in durations_current:
        
        silence = False

        # sometimes put silence instead of a note
        # because sometimes silence tells more than a C4
        if random.randint(1, 100) < silence_percent:
            silence = True

        # make sure the upcoming note in the bar is not the same
        # with the previous one, and also make sure we don't jump
        # between high and low notes too aggressively
        while note_last == None or (note_current == note_last or abs(note_current - note_last) >= note_jump_limit):
            note_current_name = random.choice(list(chord_current.keys()))
            note_current = chord_current.get(note_current_name)
            if note_last == None:
                break

        note_last = note_current

        if not silence:
            print("\nNote: " + str(note_current_name))
        else:
            print("\nSilence")
            
        print("Duration: " + str(duration))

        if not silence:
            player.play_wave(synth1.generate_constant_wave(note_current, duration * 60/bpm_current))
        else:
            time.sleep(duration * 60/bpm_current)
    

