#!/usr/bin/python
# -*- coding: utf-8 -*-

from pytunegen.constants import *
import random
import time

class TuneGen:
    """Tune generator"""

    def __init__(self, seed = None, music_length = 50,
                 scale = None, bpm = None, time_sig = None,
                 note_jump_limit = 2.2, silence_percent = 1,
                 non_repeat_percent = 65):
        if seed:
            self.randseed = seed
        else:
            self.randseed = random.randint(0, 2**31)
        random.seed(self.randseed)
        
        # times the frequency of last note
        self.note_jump_limit = note_jump_limit
        
        # ratio of silences to notes
        self.silence_percent = silence_percent
        
        # ratio of non-repeated bars to all bars
        # (set to 100 or above to inhibit repeated bars)
        self.non_repeat_percent = non_repeat_percent
        
        # number of bars
        self.music_length = music_length
        
        # get bpm, time signature, scale, silence percent, length
        if bpm:
            self.bpm_current = int(bpm)
        else:
            self.bpm_current = bpms[random.randint(0, len(bpms) - 1)]

        if time_sig:
            if int(time_sig[2]) <= 0 or not (int(time_sig[2]) % 2) == 0:
                print("pyTuneGen Error: Illegal time signature.")
                print("Lower time signature must be a positive even integer.")
                return -1
            self.time_sig_upper = int(time_sig[0])
            self.time_sig_lower = int(time_sig[2])
            self.time_sig = int(time_sig[0])/int(time_sig[2])
        else:
            self.time_sig_upper = random.randint(1, 8)
            self.time_sig_lower = 4 # this can be hard-coded for now
            self.time_sig = self.time_sig_upper / self.time_sig_lower
            
        self.time_sig_display = (str(self.time_sig_upper) + "/" +
                                 str(self.time_sig_lower))
        
        if scale:
            self.scale_current_name = scale
            self.scale_current = scales.get(self.scale_current_name)
        else:
            self.scale_current_name = random.choice(list(scales.keys()))
            self.scale_current = scales.get(self.scale_current_name)

    def generate(self):
        durations_current = []
        bar_num = 0
        music = []

        while True:

            duration_selection_loop = 0
            while durations_current == [] or sum(durations_current) < self.time_sig:
                duration_selection_loop += 1
                next_duration = random.choice(list(note_durations.keys()))
                next_duration_value = note_durations.get(next_duration)
                
                if (sum(durations_current) + next_duration_value <= self.time_sig and not
                    (duration_selection_loop <= 15 and next_duration_value <= 0.125)):
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
                if random.randint(1, 100) < self.silence_percent:
                    silence = True

                # make sure the upcoming note in the bar is not the same
                # with the previous one, and also make sure we don't jump
                # between high and low notes too aggressively
                while note_last == None or (note_current == note_last or
                                            note_current - note_last >= note_last * (self.note_jump_limit - 1) or
                                            note_last - note_current >= note_last / (self.note_jump_limit - 1)):
                    note_current_name = random.choice(list(self.scale_current.keys()))
                    note_current = self.scale_current.get(note_current_name)
                    if note_last == None:
                        break

                if not silence:
                    note_last = note_current
                    notes_current.append(note_current)
                    notes_current_names.append(note_current_name)
                    
                else:
                    notes_current.append("silence")
                    notes_current_names.append("silence")

            
            if random.uniform(0, 100) > self.non_repeat_percent:
                bar_repeat_current = random.choice(bar_repeats)
            else:
                bar_repeat_current = 1

            bar = Bar(notes_current_names, durations_current, bar_repeat_current)
            
            for bar_repeat in range(bar_repeat_current):
                bar_num += 1
                for i in range(len(durations_current)):
                    bar.notes.append(Note(notes_current[i], durations_current[i], notes_current[i] == "silence"))
            
            music.append(bar)

            durations_current = []
            if bar_num >= self.music_length:
                return music

class Bar:
    """Representation of a single bar"""

    def __init__(self, note_names, durations, bar_repeat):
        self.note_names = note_names
        self.durations = durations
        self.bar_repeat = bar_repeat
        self.notes = []

class Note:
    """Representation of a single note"""
    
    def __init__(self, pitch, duration, silence):
        self.pitch = pitch
        self.duration = duration
        self.silence = silence
