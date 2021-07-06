#!/usr/bin/python
# -*- coding: utf-8 -*-

from pytunegen.constants import *
import random
import time

class TuneGen:
    """Tune generator"""

    def __init__(self, seed):
        if seed:
            self.randseed = seed
        else:
            self.randseed = random.randint(0, 2**31)
        random.seed(self.randseed)
        # get random bpm, scale, chord, silence percent, length
        self.bpm_current = bpms[random.randint(0, len(bpms) - 1)]
        self.scale = random.randint(1, 8)
        self.chord_current_name = random.choice(list(chords.keys()))
        self.chord_current = chords.get(self.chord_current_name)

    def generate(self):
        durations_current = []
        bar_num = 0
        tune_group = []

        while True:

            while durations_current == [] or sum(durations_current) < self.scale:
                next_duration = random.choice(list(note_durations.keys()))
                next_duration_value = note_durations.get(next_duration)
                
                if sum(durations_current) + next_duration_value <= self.scale:
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
                    note_current_name = random.choice(list(self.chord_current.keys()))
                    note_current = self.chord_current.get(note_current_name)
                    if note_last == None:
                        break

                if not silence:
                    note_last = note_current
                    notes_current.append(note_current)
                    notes_current_names.append(note_current_name)
                    
                else:
                    notes_current.append("silence")
                    notes_current_names.append("silence")

            
            if random.uniform(0, 100) > non_repeat_percent:
                bar_repeat_current = random.choice(bar_repeats)
            else:
                bar_repeat_current = 1

            group = TuneGroup(notes_current_names, durations_current, bar_repeat_current)
            
            for bar_repeat in range(bar_repeat_current):
                bar_num += 1
                for i in range(len(durations_current)):
                    group.tunes.append(Tune(notes_current[i], durations_current[i], notes_current[i] == "silence"))
            
            tune_group.append(group)

            durations_current = []
            if bar_num >= music_length:
                return tune_group

class TuneGroup:
    """Representation of a tune group"""

    def __init__(self, note_names, durations, bar_repeat):
        self.note_names = note_names
        self.durations = durations
        self.bar_repeat = bar_repeat
        self.tunes = []

class Tune:
    """Representation of a single tune"""
    
    def __init__(self, note, duration, silence):
        self.note = note
        self.duration = duration
        self.silence = silence
