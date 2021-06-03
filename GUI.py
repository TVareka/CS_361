from tkinter import *
import Blackjack as blj
import urllib.request
import json

lang = 'en'
lang_dict = {
    'en': ['Rules of Blackjack', 'Basic Rules:', 'Exit', 'Start Game', 'Rules', 'Change Language', 'Exit Game',
           'Options:', 'Main Menu', 'Hit', 'Stay', 'Continue to End Game Screen', 'Game Finished!',
           'Current Session Totals:', 'Wins: ', 'Losses: ', 'Play Again?', 'Choose your language', 'Confirm'],
    'pt': ['Regras do Blackjack', 'Regras Básicas:', 'Saída', 'Começar o Jogo', 'Regras', 'Mudar Idioma',
           'Sair do Jogo', 'Opções:', 'Menu Principal', 'Acertar', 'Fique', 'Continuar para a Tela Final do Jogo',
           'Jogo Terminado!', 'Totais da Sessão Atual:', 'Vitórias: ', 'Perdas: ', 'Jogar de Novo?',
           'Escolha seu idioma', 'Confirme'],
    'fr': ['Règles du Blackjack', 'Règles de Base:', 'Sortir', 'Démarrer Jeu', 'Des Règles', 'Changer de Langue',
           'Quitter le Jeu', 'Options:', 'Menu Principal', 'Frappé', 'Rester', 'Continuer à Terminer l\'écran de Jeu',
           'Jeu Terminé', 'Totaux de la Session en Cours', 'Gagne: ', 'Pertes: ', 'Rejouer?', 'Choisissez Votre Langue',
           'Confirmer']
}

# Must be VPN'd into OSU in order to user the web scraper/web transformer.  Avoid this window if you cannot VPN
# in.
def RulesWindow():
    newWindow = Toplevel(root)
    newWindow.title("Rules")
    newWindow.geometry('1600x900+200+0')
    newWindow.configure(bg='green')
    url = 'http://flip3.engr.oregonstate.edu:11285/?url=https://en.wikipedia.org/wiki/Blackjack&header=Rules'
    contents = urllib.request.urlopen(url).read()
    # contents = urllib2.urlopen(url).read()
    a = json.loads(contents)
    output = "".join(a['Rules'])
    rules_lang = lang_dict[lang][0]
    basic_lang = lang_dict[lang][1]
    exit_lang = lang_dict[lang][2]

    if lang == 'pt':
        output = output.replace(' ', '%20')
        output = output.replace('\n', '%0A')
        j_url = 'http://flip3.engr.oregonstate.edu:60639/?sourceLanguage=en&destinationLanguage=pt&text=' + output
        contents2 = urllib.request.urlopen(j_url).read()
        # contents2 = urllib2.urlopen(j_url).read()
        b = json.loads(contents2)
        output = "".join(b['translation'])

    elif lang == 'fr':
        output = output.replace(' ', '%20')
        output = output.replace('\n', '%0A')
        j_url = 'http://flip3.engr.oregonstate.edu:60639/?sourceLanguage=en&destinationLanguage=fr&text=' + output
        contents2 = urllib.request.urlopen(j_url).read()
        # contents2 = urllib2.urlopen(j_url).read()
        b = json.loads(contents2)
        output = "".join(b['translation'])

    # Configuring Rules Page with correct labels to display rules to the player
    Label(newWindow, text=rules_lang, font='Stencil 50 bold italic underline', bg='green').place(
        x=425, y=10)
    Label(newWindow, text=basic_lang, font='Perpetua 30 underline bold', bg='green').place(x=20, y=130)
    Label(newWindow, text=output, font='Perpetua 18', bg='green', wraplength=1400, justify=LEFT).place(
        x=50, y=180)
    Button(newWindow, text=exit_lang, font='Perpetua 20 bold', width=25,
           command=newWindow.destroy).pack(side=BOTTOM, pady=5)


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
        start_lang = lang_dict[lang][3]
        rules_lang = lang_dict[lang][4]
        lang_lang = lang_dict[lang][5]
        exit_lang = lang_dict[lang][6]

        # Configuration of Labels/Buttons for Main Menu
        Label(self, text="BLACKJACK", font='Stencil 50 bold underline', bg='green').pack(side=TOP, ipady=100)
        Button(self, text=start_lang, font='Perpetua 25 bold', width=15,
               command=lambda: master.switch_frame(Start)).pack(
            pady=5)
        Button(self, text=rules_lang, font='Perpetua 25 bold', width=15, command=lambda: RulesWindow()).pack(
            pady=5)
        Button(self, text=lang_lang, font='Perpetua 25 bold', width=15,
               command=lambda: master.switch_frame(LangChange)).pack(pady=5)
        Button(self, text=exit_lang, font='Perpetua 25 bold', width=15, command=master.quit).pack(pady=5)


class Start(Frame):
    # Configures the 'Start Game' page and separates it into 3 frames
    def __init__(self, master):
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')
        self.master.title("BLACKJACK")
        dealer_frame = Frame(self, bg='green', width=1500, height=300)
        dealer_frame.pack(side=TOP)
        menu = Menu(master)
        master.config(menu=menu)
        # Displaying correct language
        options_lang = lang_dict[lang][7]
        menu_lang = lang_dict[lang][8]
        rules_lang = lang_dict[lang][4]
        exit_lang = lang_dict[lang][6]
        hit_lang = lang_dict[lang][9]
        stay_lang = lang_dict[lang][10]
        continue_lang = lang_dict[lang][11]

        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label=options_lang, menu=subMenu)
        subMenu.add_command(label=menu_lang, command=lambda: self.mainmenu(menu, MainPage))
        subMenu.add_command(label=rules_lang, command=lambda: RulesWindow())
        subMenu.add_command(label=exit_lang, command=master.quit)

        player_frame = Frame(self, bg='green', width=1500, height=300)
        player_frame.pack()
        control_frame = Frame(self, bg='green', width=1500, height=300)
        Next = Button(control_frame, text=continue_lang, font='Perpetua 20 bold', width=35,
                      command=lambda: self.mainmenu(menu, EndGame))
        Next.place_forget()
        Button(control_frame, text=hit_lang, font='Perpetua 20 bold', width=15,
               command=lambda: blj.hit(player_frame, dealer_frame, Next, lang)).place(
            x=525, y=10)
        Button(control_frame, text=stay_lang, font='Perpetua 20 bold', width=15,
               command=lambda: blj.stay(dealer_frame, Next, lang)).place(
            x=825, y=10)
        control_frame.pack(side=BOTTOM)

        # Start game by dealing and showing player their hand
        blj.deal()
        blj.dealer.show_hand(dealer_frame, blj.dealer)
        blj.hand.show_hand(player_frame, blj.hand)
        master.update()
        if blj.hand.get_value() == 21:
            Label(player_frame, bg='green', font='Perpetua 20 bold', text='Blackjack!').place(x=750, y=240)
            blj.stay(dealer_frame, Next, lang)

    # Needed to destroy all frames, destroy dropdown menu, and switch pages
    def mainmenu(self, m, page):
        m.destroy()
        self.master.switch_frame(page)


class EndGame(Frame):
    # Configuring the 'End Game' page
    def __init__(self, master):
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')
        # Selecting correct language to display
        finished_lang = lang_dict[lang][12]
        totals_lang = lang_dict[lang][13]
        wins_lang = lang_dict[lang][14]
        losses_lang = lang_dict[lang][15]
        again_lang = lang_dict[lang][16]
        main_lang = lang_dict[lang][8]
        exit_lang = lang_dict[lang][6]

        Label(self, text=finished_lang, font='Stencil 50 bold italic underline', bg='green').place(
            x=500, y=10)
        Label(self, text=totals_lang, font='Perpetua 35 bold italic', bg='green').place(x=20, y=130)
        Label(self, text=wins_lang + str(blj.total_wins), font='Perpetua 30', bg='green').place(x=650, y=200)
        Label(self, text=losses_lang + str(blj.total_losses), font='Perpetua 30', bg='green').place(x=650, y=280)
        Button(self, text=again_lang, font='Perpetua 20 bold', width=20, command=lambda: master.switch_frame(Start)
               ).place(x=625, y=400)
        Button(self, text=main_lang, font='Perpetua 20 bold', width=20, command=lambda: master.switch_frame(MainPage)
               ).place(x=625, y=470)
        Button(self, text=exit_lang, font='Perpetua 20 bold', width=20, command=master.quit).place(x=625, y=540)


class LangChange(Frame):
    # Configuring the 'Change Language' page
    def __init__(self, master):
        Frame.__init__(self, master, width=1500, height=800)
        self.configure(bg='green')
        v = IntVar()
        choose_lang = lang_dict[lang][17]
        confirm_lang = lang_dict[lang][18]

        Label(self, text=choose_lang, font='Perpetua 50 bold italic', bg='green', justify=LEFT).pack(
            side=TOP, ipady=80)
        Radiobutton(self, text="English", padx=20, variable=v, value=1, font='Helvetica 15', bg='green',
                    command=lambda: self.En_lang()).pack(
            anchor=W, pady=10)
        Radiobutton(self, text="Portuguese", padx=20, variable=v, value=2, font='Helvetica 15', bg='green',
                    command=lambda: self.Pt_lang()).pack(
            anchor=W, pady=10)
        Radiobutton(self, text="French", padx=20, variable=v, value=3, font='Helvetica 15', bg='green',
                    command=lambda: self.Fr_lang()).pack(
            anchor=W, pady=10)

        Button(self, text=confirm_lang, font='Perpetua 20 bold', width=25,
               command=lambda: master.switch_frame(MainPage)).pack(side=LEFT, anchor=SW, padx=140, pady=10)

    # Needed to allow the player to change the language on this page
    def En_lang(self):
        global lang
        lang = 'en'

    def Pt_lang(self):
        global lang
        lang = 'pt'

    def Fr_lang(self):
        global lang
        lang = 'fr'


if __name__ == "__main__":
    root = Test()
    root.geometry('1500x800+150+100')
    root.configure(bg='green')
    root.mainloop()
