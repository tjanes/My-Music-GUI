try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk

from PIL import ImageTk, Image

class Note:
    # all possible, valid notes
    validNotes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
    'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
    def __init__(self, note):                           # note constructor
        self.setNote(note)                              # note value is a string
    def isValid(self):                           
        if (self.noteVal in self.validNotes):           # check note validity
            return True                                 # note is valid
        else:
            return False                                # note is not valid
    def setNote(self, n):                               # set note value if input is valid
        if (n in self.validNotes):                      # check note validity
            self.noteVal = n                            # set note
        else:
            print("Note is not valid...")
    def getNote(self):
        return self.noteVal                             # return note value to user

class Mode:
    # all possible, valid modes
    validModes = [
    'Ionian', 'Major', 'major', 'Dorian', 'Phrygian', 'Lydian', 
    'Mixolydian', 'Aeolian', 'Minor', 'minor', 'Locrian' ]
    def __init__(self, mode):                           # note constructor
        self.setMode(mode)
    def isValid(self):                           
        if (self.modeVal in self.validModes):           # check note validity
            return True                                 # note is valid
        else:
            return False                                # note is not valid
    def setMode(self, m):                               # set note value if input is valid
        if (m in self.validModes):                      # check note validity
            self.modeVal = m                            # set note
        else:
            print("Note is not valid...")
    def getMode(self):
        return self.modeVal                             # return mode value to user

class MyScale:
    steps = {                                           # dictionary mapping mode names to scale step values
        'Ionian'    : 'WWHWWWH',
        'Major'     : 'WWHWWWH',
        'major'     : 'WWHWWWH',
        'Dorian'    : 'WHWWWHW',
        'Phrygian'  : 'HWWWHWW',
        'Lydian'    : 'WWWHWWH',
        'Mixolydian': 'WWHWWHW',
        'Aeolian'   : 'WHWWHWW',
        'Minor'     : 'WHWWHWW',
        'minor'     : 'WHWWHWW',
        'Locrian'   : 'HWWHWWW'
    }
    def __init__(self, note, mode):                     # constructor to set the scale item (list of notes)
        self.myScale = self.setScale(note, mode)
    def setScale(self, n, m):                           # set scale using input root and scale mode
        if (n.isValid() and m.isValid()):               # run if input is valid
            self.root = n                               # set note 
            self.mode = m                               # set mode
        else:
            print("Error...")
            return None
        self.s = (self.steps).get((self.mode).modeVal)  # get the steps from "steps" dictionary
        return self.scaleIter()                         # return the scale

    def getScaleString(self):                           # iterate through scale item and concatenate with ',' to get one string
        retScale = ""
        count = 0
        for item in self.myScale:
            if (count < len(self.myScale) - 1):
                retScale += item + ", "
            else:
                retScale += item
            count += 1
        return retScale

    def getScaleList(self):                             # return the scale list as a list
        return self.myScale

    def scaleIter(self):                                # iterate through steps to get the scale
        root = self.root
        rootVal = root.noteVal
        validNotes = root.validNotes

        # create the scale
        notes = [rootVal]
        index = validNotes.index(rootVal)
        for step in self.s:
            if (step is 'H'):                               
                notes.append(validNotes[(index + 1) % 12])  # use mod 12 to loop back around list (12 possible notes)
                index += 1                                  # add 1 b/c it's a half-step
            elif (step is 'W'):
                notes.append(validNotes[(index + 2) % 12])  # use mod 12 to loop back around list (12 possible notes)
                index += 2                                  # add 2 b/c it's a whole-step
            else:
                print("Dictionary must be wrong...")
                return None   
        return notes                                        # return the populated scale

class Chord:
    validNotes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
    'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
    validQualities = [ 'maj', 'M','min', 'm', 'dim', 
    'aug', '7', 'maj7', 'min7', 'dim7', 'aug7']
    triads = ['maj', 'M', 'min', 'm', 'dim', 'aug']
    chordIntervals = {
        'maj'  : [4, 7], 
        'M'    : [4, 7],
        'min'  : [3, 7], 
        'm'    : [3, 7], 
        'dim'  : [3, 6], 
        'aug'  : [4, 8], 
        '7'    : [4, 7, 10], 
        'maj7' : [4, 7, 11], 
        'min7' : [3, 7, 10], 
        'dim7' : [3, 6, 9], 
        'aug7' : [4, 8, 11]
    }
    def __init__(self, r, q):
        if (r not in self.validNotes or q not in self.validQualities):    # check if input is valid
            print("I don't know that chord...")
            return None
        self.root = r                       # set root
        self.quality = q                    # set quality
        self.setChord()    

    def setChord(self):
        chordList = [self.root]
        idx = self.validNotes.index(self.root)              # index of root note in self.validNotes list         
        intervalList = self.chordIntervals[self.quality]    # get list of chord intervals
        for i in intervalList:                              # build the chord
            chordList.append(self.validNotes[(idx + i) % 12])
        self.chord = chordList

    def getChord(self):
        return self.chord

# chord = Chord('C', 'aug')
# print(chord.getChord())

# class MyChordProgression:
#     def __init__(self, note):


# myNote = Note('B')
# myMode = Mode('minor')
# myScale = MyScale(myNote, myMode)
# print(myScale.getScale())

#class Chord:
class GUI(tk.Frame):
    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 
             'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
    modes = ['Major', 'Dorian', 'Phrygian', 'Lydian', 
              'Mixolydian', 'Minor', 'Locrian']
    notesDashes = ['A', 'A#-Bb', 'B', 'C', 'C#-Db', 'D', 
             'D#-Eb', 'E', 'F', 'F#-Gb', 'G', 'G#-Ab']
    qualities = [ 'maj','min', 'dim', 'aug', 
    '7', 'maj7', 'min7', 'dim7', 'aug7']          
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        #self.cbframe = tk.Frame(self)

        # define dropdown tracker vars
        self.tkvarNote = tk.StringVar(self.master)
        self.tkvarMode = tk.StringVar(self.master)

        # set default options for dropdowns
        self.tkvarNote.set('A') 
        self.tkvarMode.set('Major')

        lab = tk.Label(self.master, text="Scale Calculator", background='gray', font='Helvetica 15 bold')
        lab.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nswe')

        # define root note dropdown menu widget
        popupMenuNote = tk.OptionMenu(self.master, self.tkvarNote, *(self.notes))
        tk.Label(self.master, text="Root:", background='gray').grid(row=2, column=0, sticky="ew")
        popupMenuNote.grid(row=3, column=0, sticky="ew")

        # define scale mode dropdown menu widget
        popupMenuMode = tk.OptionMenu(self.master, self.tkvarMode, *(self.modes))
        tk.Label(self.master, text="Mode:", background='gray').grid(row=2, column=1, sticky="ew")
        popupMenuMode.grid(row=3, column=1, sticky="ew")

        # set widget width
        popupMenuNote.config(width=10)
        popupMenuMode.config(width=10)

        # set scale label - class object
        n = Note('A')
        m = Mode('Major')
        scale = MyScale(n, m)
        self.scaleLabel = tk.Label(self.master, text=scale.getScaleString(), width=40, background='gray')
        self.scaleLabel.grid(row=7, columnspan=2, sticky="ew")

        # define clear and set buttons
        clearBtn = tk.Button(self.master, text="Clear Scale", fg="black", width=10, command=self.clear_scale)
        setBtn = tk.Button(self.master, text="Compute Scale", fg="black", width=10, command=self.set_scale)
        
        # define clear and set button attributes
        clearBtn.grid(row=5, column=0, sticky="ew")
        setBtn.grid(row=5, column=1, sticky="ew")

        # set return label
        retLabel = tk.Label(self.master, text="Scale Output:", width=40, background='gray')
        retLabel.grid(row=6, column=0, columnspan=2, sticky="w")

        # define dropdown tracker vars
        self.tkvarChordNote = tk.StringVar(self.master)
        self.tkvarChordQual = tk.StringVar(self.master)

        # set default values
        self.tkvarChordNote.set('A') 
        self.tkvarChordQual.set('maj')

        #tk.Label(self.master, text="", background='gray').grid(row=6)
        lb = tk.Label(self.master, text="Chord Library", background='gray', font='Helvetica 15 bold')
        lb.grid(row=8, column=0, rowspan=2, columnspan=2, sticky='nswe')

        # select chord
        popupMenuMode = tk.OptionMenu(self.master, self.tkvarChordNote, *(self.notesDashes))
        tk.Label(self.master, text="Chord Root:", background='gray').grid(row=11, column=0, sticky="ew")
        popupMenuMode.grid(row=12, column=0, sticky="ew")

        # select chord quality
        popupMenuMode = tk.OptionMenu(self.master, self.tkvarChordQual, *(self.qualities))
        tk.Label(self.master, text="Chord Quality:", background='gray').grid(row=11, column=1, sticky="ew")
        popupMenuMode.grid(row=12, column=1, sticky="ew")        

        # set chord image
        self.set_chord()
        
        # define set buttons
        setBtnChord = tk.Button(self.master, text="Show Chord", fg="black", width=10, command=self.set_chord)
        
        # define set button attributes
        setBtnChord.grid(row=13, column=0, columnspan=2, sticky="ew")

        #Displaying it
        #imglabel = tk.Label(self.master, image=img).grid(row=7, rowspan=7, column=0, columnspan=3, sticky='ew')

        # cb1 = tk.Checkbutton(self.master, text="Choice 1")
        # cb2 = tk.Checkbutton(self.master, text="Choice 2")
        # cb3 = tk.Checkbutton(self.master, text="Choice 3")

        # cb1.pack(side="left", fill=None, expand=False)
        # cb2.pack(side="left", fill=None, expand=False)
        # cb3.pack(side="left", fill=None, expand=False)

        # this entry is for illustrative purposes: it
        # will force column 2 to be widget than a checkbutton
        
        # e1 = tk.Entry(self, width=20)
        # e1.grid(row=1, column=1, sticky="ew")

        # place our frame of checkbuttons in the same column
        # as the entry widget. Because the checkbuttons are
        # packed in a frame, they will always be "stuck"
        # to the left side of the cell.
        #self.master.grid(row=2, column=1, sticky="ew")

        # let column 1 expand and contract with the 
        # window, so you can see that the column grows
        # with the window, but that the checkbuttons
        # stay stuck to the left
        self.grid_columnconfigure(1, weight=1)
   
    def set_scale(self, *args):
        note = Note(self.tkvarNote.get())    # construct note object
        mode = Mode(self.tkvarMode.get())    # construct mode object
        scale = MyScale(note, mode)          # construct scale object
        self.scaleLabel = tk.Label(self.master, text=scale.getScaleString(), width=40, background='gray').grid(row=7, columnspan=2, sticky="ew")
   
    def clear_scale(self, *args):
        self.scaleLabel = tk.Label(self.master, text="", width=40, background='gray').grid(row=7, columnspan=2, sticky="ew")

    def set_chord(self, *args):
        fl = 'C:/Users/tmjan/Documents/VSCode/My-Music-GUI/ChordDiagrams/'+ self.tkvarChordNote.get() + self.tkvarChordQual.get() +'.png'
        img = tk.PhotoImage(file=fl)
        img1 = img.subsample(2,2)
        label = tk.Label(image = img1, background='gray')
        label.grid(row = 14, column = 0, columnspan = 2, rowspan = 2, padx = 5, pady = 5, sticky='ew')
        label.image = img1

if __name__ == "__main__":
    root = tk.Tk()
    #root.grid()
    view = GUI(root)
    root.wm_title("MyMusicGUI")
    #view.pack(side="top", fill="both", expand=True)
    root.wm_geometry("300x650")
    root.configure(background='gray')
    root.mainloop()