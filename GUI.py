from tkinter import *
import Blackjack as blj
from PIL import ImageTk, Image


class Test(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces with new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainPage(Frame):
    def __init__(self, master):
        # Initialization for Main Menu
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')
        frame = Frame(master)

        # Configuration of Labels/Buttons for Main Menu
        Label(self, text="BLACKJACK", font='Helvetica 50 bold underline', bg='green').pack(side=TOP, ipady=100)
        Button(self, text="Start Game", font='Helvetica 15', width=25, command=lambda: master.switch_frame(Start)).pack(
            pady=5)
        Button(self, text="Rules", font='Helvetica 15', width=25, command=lambda: master.switch_frame(Rules)).pack(
            pady=5)
        Button(self, text="Change Language", font='Helvetica 15', width=25,
               command=lambda: master.switch_frame(LangChange)).pack(pady=5)
        Button(self, text="Exit", font='Helvetica 15', width=25, command=frame.quit).pack(pady=5)


class Start(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')
        self.master.title("BLACKJACK GAME")
        dealer_frame = Frame(master, bg='green', width=1500, height=300)
        dealer_frame.pack(side=TOP)
        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options:", menu=subMenu)
        subMenu.add_command(label="Main Menu", command=lambda:  self.mainmenu(dealer_frame, player_frame, control_frame, menu))
        subMenu.add_command(label="Exit Game", command=master.quit)

        player_frame = Frame(master, bg='green', width=1500, height=300)
        player_frame.pack()
        control_frame = Frame(master, bg='green', width=1500, height=300)
        Button(control_frame, text="Hit", font='Helvetica 15', width=15, command=lambda: blj.hit(player_frame)).place(
            x=550, y=120)
        Button(control_frame, text="Stay", font='Helvetica 15', width=15, command=lambda: blj.stay(dealer_frame)).place(
            x=850, y=120)
        control_frame.pack(side=BOTTOM)

        blj.deal()
        print(blj.dealer.get_value())
        blj.dealer.show_hand(dealer_frame, blj.dealer)
        print(blj.hand.get_value())
        blj.hand.show_hand(player_frame, blj.hand)

    def mainmenu(self, f1, f2, f3, m):
        f1.destroy()
        f2.destroy()
        f3.destroy()
        m.destroy()
        self.master.switch_frame(MainPage)


class Rules(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')

        # Configuring Rules Page with correct labels to display rules to the player
        Label(self, text="Rules of Blackjack", font='Helvetica 50 bold italic', bg='green').pack(side=TOP, ipady=80)
        Label(self, text="Basic Rules:", font='Helvetica 30 underline', bg='green').pack(anchor=W, pady=10)
        Label(self, text="Rules of blackjack are ... figure out how to get this to display from my webscraper. I also "
                         "need to see if this will wrap around the screen or be annoying and just keep going off the  "
                         "screen because computers hate me.", font='Helvetica 15', bg='green', wraplength=600).pack(
            pady=10)
        Button(self, text="Back to Main Menu", font='Helvetica 15', width=25,
               command=lambda: master.switch_frame(MainPage)).pack(side=BOTTOM, pady=5)


class LangChange(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.configure(bg='green')
        v = IntVar()
        Label(self, text="Choose your language", font='Helvetica 50 bold italic', bg='green', justify=LEFT).pack(
            side=TOP, ipady=80)
        Radiobutton(self, text="Language 1", padx=20, variable=v, value=1, font='Helvetica 15', bg='green').pack(
            anchor=W, pady=10)
        Radiobutton(self, text="Language 2", padx=20, variable=v, value=2, font='Helvetica 15', bg='green').pack(
            anchor=W, pady=10)
        Radiobutton(self, text="Language 3", padx=20, variable=v, value=3, font='Helvetica 15', bg='green').pack(
            anchor=W, pady=10)
        Radiobutton(self, text="Language 4", padx=20, variable=v, value=4, font='Helvetica 15', bg='green').pack(
            anchor=W, pady=10)

        Button(self, text="Confirm", font='Helvetica 15', width=25,
               command=lambda: master.switch_frame(MainPage)).pack(side=LEFT, anchor=SW, padx=5, pady=10)
        Button(self, text="Back to Main Menu", font='Helvetica 15', width=25,
               command=lambda: master.switch_frame(MainPage)).pack(side=LEFT, anchor=SE, padx=5, pady=10)


if __name__ == "__main__":
    root = Test()
    root.geometry('1500x800')
    root.configure(bg='green')
    root.mainloop()
