from synthesizer import Player, Synthesizer, Waveform
import random
import time

#-------------------------
#  NOTE FREQUENCY TABLE
#-------------------------

# 3rd octave
c3 = 131
c_3 = 139
d3 = 147
d_3 = 156
e3 = 165
f3 = 175
f_3 = 185
g3 = 196
g_3 = 208
a3 = 220
a_3 = 233
b3 = 247

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

full_notes = {"C3":c3, "C#3":c_3, "D3":d3, "D#3":d_3, "E3":e3, "F3":f3, "F#3":f_3, "G3":g3, "G#3":g_3, "A3":a3, "A#3":a_3, "B3":b3,
              "C4":c4, "C#4":c_4, "D4":d4, "D#4":d_4, "E4":e4, "F4":f4, "F#4":f_4, "G4":g4, "G#4":g_4, "A4":a4, "A#4":a_4, "B4":b4,
              "C5":c5, "C#5":c_5, "D5":d5, "D#5":d_5, "E5":e5, "F5":f5, "F#5":f_5, "G5":g5, "G#5":g_5, "A5":a5, "A#5":a_5, "B5":b5}

c_major = {"C3":c3, "D3":d3, "E3":e3, "F3":f3, "G3":g3, "A3":a3, "B3":b3,
           "C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "B4":b4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "B5":b5}

c_minor = {"C3":c3, "D3":d3, "D#3":d_3, "F3":f3, "G3":g3, "G#3":g_3, "A#3":a_3,
           "C4":c4, "D4":d4, "D#4":d_4, "F4":f4, "G4":g4, "G#4":g_4, "A#4":a_4,
           "C5":c5, "D5":d5, "D#5":d_5, "F5":f5, "G5":g5, "G#5":g_5, "A#5":a_5}

d_minor = {"C3":c3, "D3":d3, "E3":e3, "F3":f3, "G3":g3, "A3":a3, "A#3":a_3,
           "C4":c4, "D4":d4, "E4":e4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "E5":e5, "F5":f5, "G5":g5, "A5":a5, "A#5":a_5}

g_minor = {"C3":c3, "D3":d3, "D#3":d_3, "F3":f3, "G3":g3, "A3":a3, "A#3":a_3,
           "C4":c4, "D4":d4, "D#4":d_4, "F4":f4, "G4":g4, "A4":a4, "A#4":a_4,
           "C5":c5, "D5":d5, "D#4":d_5, "F4":f5, "G4":g5, "A4":a5, "A#4":a_5}

f_minor = {"C3":c3, "C#3":c_3, "D#3":d_3, "F3":f3, "G3":g3, "G#3":g_3, "A#3":a_3,
           "C4":c4, "C#4":c_4, "D#4":d_4, "F4":f4, "G4":g4, "G#4":g_4, "A#4":a_4,
           "C5":c5, "C#5":c_5, "D#5":d_5, "F5":f5, "G5":g5, "G#5":g_5, "A#5":a_5}

chords = {"Full Notes":full_notes, "C Major":c_major, "C Minor":c_minor, "D Minor":d_minor, "G Minor":g_minor,
          "F Minor":f_minor}

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
#  DURATIONS AND REPEATS
#-------------------------

note_durations = {"1/4":1/4, "1/2": 1/2, "1":1, "2":2, "4":4}
bar_repeats = [2, 4]

#-------------------------
#       SETUP
#-------------------------
player = Player()
player.open_stream()
synth1 = Synthesizer(osc1_waveform = Waveform.sine, osc1_volume=1.0,
                     use_osc2=True, osc2_waveform=Waveform.square, osc2_volume=0.3)

# print the seed, so we can replay the song
# if we ever want to
randseed = random.randint(0, 2**31)
random.seed(randseed)
print("Seed:", randseed)

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

note_jump_limit = 2.2 # times the frequency of last note

durations_current = []

# ratio of silences to notes
silence_percent = 1

# ratio of non-repeated bars to all bars
# (set to 100 or above to inhibit repeated bars)
non_repeat_percent = 55

music_length = 250 # num. of bars
print("Length:", music_length, "bars")

bar_num = 0

#-------------------------
#    GENERATE AND PLAY
#-------------------------

for l in range(0, music_length):

    while durations_current == [] or sum(durations_current) < scale:
        next_duration = random.choice(list(note_durations.keys()))
        next_duration_value = note_durations.get(next_duration)
        
        if sum(durations_current) + next_duration_value <= scale:
            durations_current.append(next_duration_value)

    notes_current = []
    notes_current_names = []

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
        while note_last == None or (note_current == note_last or
                                    note_current - note_last >= note_last * (note_jump_limit - 1) or
                                    note_last - note_current >= note_last / (note_jump_limit - 1)):
            note_current_name = random.choice(list(chord_current.keys()))
            note_current = chord_current.get(note_current_name)
            if note_last == None:
                break

        if not silence:
            note_last = note_current
            notes_current.append(note_current)
            notes_current_names.append(note_current_name)
            
        else:
            notes_current.append("silence")
            notes_current_names.append("silence")

    print("\n" + str(notes_current_names) + "\n" + str(durations_current))

    if random.uniform(0, 100) > non_repeat_percent:
        bar_repeat_current = random.choice(bar_repeats)
    else:
        bar_repeat_current = 1
        
    print("Bar Repeat:", bar_repeat_current)

    for bar_repeat in range(bar_repeat_current):
        bar_num += 1
        print("Bar #" + str(bar_num))
        for i in range(len(durations_current)):
            if not notes_current[i] == "silence":
                player.play_wave(synth1.generate_constant_wave(notes_current[i], durations_current[i] * 60/bpm_current))
            else:
                time.sleep(durations_current[i] * 60/bpm_current)

    durations_current = []
