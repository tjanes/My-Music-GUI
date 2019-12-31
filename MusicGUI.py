try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk

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
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.cbframe = tk.Frame(self)

        # define dropdown tracker vars
        self.tkvarNote = tk.StringVar(self.cbframe)
        self.tkvarMode = tk.StringVar(self.cbframe)

        # set default options for dropdowns
        self.tkvarNote.set('A') 
        self.tkvarMode.set('Major')

        # define root note dropdown menu widget
        popupMenuNote = tk.OptionMenu(self.cbframe, self.tkvarNote, *(self.notes))
        tk.Label(self.cbframe, text="Root:").grid(row=0, column=0, sticky="w")
        popupMenuNote.grid(row=1, column=0, sticky="ew")

        # define scale mode dropdown menu widget
        popupMenuMode = tk.OptionMenu(self.cbframe, self.tkvarMode, *(self.modes))
        tk.Label(self.cbframe, text="Mode:").grid(row=0, column=1, sticky="w")
        popupMenuMode.grid(row=1, column=1, sticky="ew")

        # set widget width
        popupMenuNote.config(width=10)
        popupMenuMode.config(width=10)

        # set scale label - class object
        n = Note('A')
        m = Mode('Major')
        scale = MyScale(n, m)
        self.scaleLabel = tk.Label(self.cbframe, text=scale.getScaleString(), width=40).grid(row=5, columnspan=2, sticky="ew")

        # define clear and set buttons
        clearBtn = tk.Button(self.cbframe, text="Clear Scale", fg="black", width=10, command=self.clear_scale)
        setBtn = tk.Button(self.cbframe, text="Compute Scale", fg="black", width=10, command=self.set_scale)
        
        # define clear and set button attributes
        clearBtn.grid(row=3, column=0, sticky="ew")        
        setBtn.grid(row=3, column=1, sticky="ew")

        # set return label
        retLabel = tk.Label(self.cbframe, text="Scale Output:", width=40)
        retLabel.grid(row=4, column=0, columnspan=2, sticky="w")

        # cb1 = tk.Checkbutton(self.cbframe, text="Choice 1")
        # cb2 = tk.Checkbutton(self.cbframe, text="Choice 2")
        # cb3 = tk.Checkbutton(self.cbframe, text="Choice 3")

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
        self.cbframe.grid(row=2, column=1, sticky="w")

        # let column 1 expand and contract with the 
        # window, so you can see that the column grows
        # with the window, but that the checkbuttons
        # stay stuck to the left
        self.grid_columnconfigure(1, weight=1)
   
    def set_scale(self, *args):
        note = Note(self.tkvarNote.get())    # construct note object
        mode = Mode(self.tkvarMode.get())    # construct mode object
        scale = MyScale(note, mode)          # construct scale object
        self.scaleLabel = tk.Label(self.cbframe, text=scale.getScaleString(), width=40).grid(row=5, columnspan=2, sticky="ew")
   
    def clear_scale(self, *args):
        self.scaleLabel = tk.Label(self.cbframe, text="", width=40).grid(row=5, columnspan=2, sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    view = GUI(root)
    view.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x200")
    root.mainloop()