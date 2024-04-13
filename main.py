import kivy
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
import random

Window.size = (720/2.5, 1600/2.5)
Window.clearcolor = (1, 1, 1, 1)

class RoundButton(Button):
    def buttonPressed(self):
        self.ids.round_button_texture.source = 'textures/buttons/roundbutton_redorange_down.png'
    
    def buttonReleased(self):
        self.ids.round_button_texture.source = 'textures/buttons/roundbutton_redorange_up.png'

class RoundRecButton(Button):
    pass

class RoundRecButtonSub(Button):
    def buttonPressed(self):
        self.ids.roundrec_button_texture.source = 'textures/buttons/roundrecbutton_redorange_up_ver.png'

    def buttonReleased(self):
        self.ids.roundrec_button_texture.source = 'textures/buttons/roundrecbutton_redorange_up_ver.png'

class OvalButtonRed(Button):
    def buttonPressed(self):
        self.ids.oval_button_red_texture.source = 'textures/buttons/ovalbutton_red_down.png'

    def buttonReleased(self):
        self.ids.oval_button_red_texture.source = 'textures/buttons/ovalbutton_red_up.png'

class OvalButtonBlue(Button):
    def buttonPressed(self):
        self.ids.oval_button_blue_texture.source = 'textures/buttons/ovalbutton_blue_down.png'
        
    def buttonReleased(self):
        self.ids.oval_button_blue_texture.source = 'textures/buttons/ovalbutton_blue_up.png'

class RoundButtonGuess(Button):
    def buttonPressed(self):
        self.ids.round_button_texture.source = 'textures/buttons/roundbutton_redorange_down.png'
    
    def buttonReleased(self):
        self.ids.round_button_texture.source = 'textures/buttons/roundbutton_redorange_up.png'

class RoundRecButtonGuess(Button):
    def buttonPressed(self):
        self.ids.roundrec_button_texture.source = 'textures/buttons/roundrecbutton_redorange_down_hor.png'

    def buttonReleased(self):
        self.ids.roundrec_button_texture.source = 'textures/buttons/roundrecbutton_redorange_up_hor.png'

class MainMenu(Screen):
    def start(self):
        kv.current = "setup"       

class SetUpScreen(Screen):
    currentTeamTurn = 1
    currentInputIndex = 0
    currentTotal = 0

    showWarning = False
    
    def enternumber(self, button):
        SetUp.inputNumber(button)
        self.updateWidget(button)
            
    def erase(self, button):
        SetUp.eraseNumber()
        self.updateWidget(button)

    def enterProceed(self):
        SetUp.enterProceed()

        if self.showWarning:
            self.ids.warning.text = "The combination must sum up to 20."
        else:
            self.ids.warning.text = " "
            self.ids.combinum_0.text = '0'
            self.ids.combinum_1.text = '0'
            self.ids.combinum_2.text = '0'
            self.ids.combinum_3.text = '0'
            self.ids.total.text = '= 0'

            GameData.combinationSum = 0

            if self.currentTeamTurn == 1:
                self.ids.teamturn.source = 'textures/letter_and_box/your_combination_p1.png'
            elif self.currentTeamTurn == 2:
                self.ids.teamturn.source = 'textures/letter_and_box/your_combination_p2.png'
            
    def updateWidget(self, button):
        if self.currentInputIndex == 0:
            self.ids.combinum_0.text = str(button)
        elif self.currentInputIndex == 1:
            self.ids.combinum_1.text = str(button)
        elif self.currentInputIndex == 2:
            self.ids.combinum_2.text = str(button)
        elif self.currentInputIndex == 3:
            self.ids.combinum_3.text = str(button)

        self.ids.warning.text = " "
        self.ids.total.text = "= " + str(self.currentTotal)

    def ProceedGame():
        kv.transition = FadeTransition()
        kv.current = "game"
        print("Proceed")
        print("Team 1 = " + str(GameData.combinationTeam1))
        print("Team 2 = " + str(GameData.combinationTeam2))

class GameScreen(Screen):    
    compare_element1 = ' '
    compare_element2 = ' '
    compare_indicator = ' '

    teamTurn = 1

    see_1 = False
    see_2 = False

    guessingTeam1 = False
    guessingTeam2 = False

    guessCombiTeam1_index = 0
    guessCombiTeam2_index = 0

    correctGuess_Team1 = False
    correctGuess_Team2 = False

    def clueAccess(self, team):
        if self.teamTurn == team:
            MainGame.searchRandomCompare(MainGame)
            MainGame.switchTurn(team)

            if self.compare_element1 == 'A':
                self.ids.element_team1.source = 'textures/letter_and_box/a_1.png'
            elif self.compare_element1 == 'B':
                self.ids.element_team1.source = 'textures/letter_and_box/b_1.png'
            elif self.compare_element1 == 'C':
                self.ids.element_team1.source = 'textures/letter_and_box/c_1.png'
            elif self.compare_element1 == 'D':
                self.ids.element_team1.source = 'textures/letter_and_box/d_1.png'

            if self.compare_element2 == 'A':
                self.ids.element_team2.source = 'textures/letter_and_box/a_2.png'
            elif self.compare_element2 == 'B':
                self.ids.element_team2.source = 'textures/letter_and_box/b_2.png'
            elif self.compare_element2 == 'C':
                self.ids.element_team2.source = 'textures/letter_and_box/c_2.png'
            elif self.compare_element2 == 'D':
                self.ids.element_team2.source = 'textures/letter_and_box/d_2.png'

            if self.compare_indicator == '>':
                self.ids.compare_indicator.source = 'textures/letter_and_box/greater_than.png'
            elif self.compare_indicator == '<':
                self.ids.compare_indicator.source = 'textures/letter_and_box/less_than.png'
            elif self.compare_indicator == '=':
                self.ids.compare_indicator.source = 'textures/letter_and_box/equal.png'

            self.ids.element_team1.opacity = 1   
            self.ids.element_team2.opacity = 1
            self.ids.compare_indicator.opacity = 1

            #timeFinished = False
            #start = 3000
            #clock = pygame.time.Clock()

            #while not timeFinished:
            #    start -= 1

            #    if start <= 0:
            #        timeFinished = True
            #        self.ids.clue.opacity = 0

            #    clock.tick(100)

            self.updateWidget("clue", None)

    def seeCombination(self, team):
        if team == 1:
            if not self.see_1:
                self.see_1 = True
                self.ids.view_combination_1.source = 'textures/labels_black/hide_combination.png'
                self.ids.mycombi_0_1.source = 'textures/letter_and_box/box_square_blue.png'
                self.ids.mycombi_1_1.source = 'textures/letter_and_box/box_square_blue.png'
                self.ids.mycombi_2_1.source = 'textures/letter_and_box/box_square_blue.png'
                self.ids.mycombi_3_1.source = 'textures/letter_and_box/box_square_blue.png'
                self.ids.combi_1.opacity = 1
            else:
                self.see_1 = False
                self.ids.view_combination_1.source = 'textures/labels_black/view_combination.png'
                self.ids.mycombi_0_1.source = 'textures/letter_and_box/a_1.png'
                self.ids.mycombi_1_1.source = 'textures/letter_and_box/b_1.png'
                self.ids.mycombi_2_1.source = 'textures/letter_and_box/c_1.png'
                self.ids.mycombi_3_1.source = 'textures/letter_and_box/d_1.png'
                self.ids.combi_1.opacity = 0
        elif team == 2:
            if not self.see_2:
                self.see_2 = True
                self.ids.view_combination_2.source = 'textures/labels_black/hide_combination.png'
                self.ids.mycombi_0_2.source = 'textures/letter_and_box/box_square_red.png'
                self.ids.mycombi_1_2.source = 'textures/letter_and_box/box_square_red.png'
                self.ids.mycombi_2_2.source = 'textures/letter_and_box/box_square_red.png'
                self.ids.mycombi_3_2.source = 'textures/letter_and_box/box_square_red.png'
                self.ids.combi_2.opacity = 1
            else:
                self.see_2 = False
                self.ids.view_combination_2.source = 'textures/labels_black/view_combination.png'
                self.ids.mycombi_0_2.source = 'textures/letter_and_box/a_2.png'
                self.ids.mycombi_1_2.source = 'textures/letter_and_box/b_2.png'
                self.ids.mycombi_2_2.source = 'textures/letter_and_box/c_2.png'
                self.ids.mycombi_3_2.source = 'textures/letter_and_box/d_2.png'
                self.ids.combi_2.opacity = 0

        self.updateWidget("combination", team)

    def guessTeam1(self, action_bool, isFinished):
        action_int = 1
        secondAction_int = 0
        secondAction_bool = True

        self.guessingTeam1 = action_bool

        secondAction_size1 = 0.1 * 1.2
        secondAction_size2 = 0.045 * 1.2
        secondAction_size1_2 = 0.1 * 3
        secondAction_size2_2 = 0.015 * 3

        if not isFinished:
            if action_bool == True:
                action_int = 0.5
                secondAction_int = 1
                secondAction_bool = False
                secondAction_size1 = 0.1 * 1.2
                secondAction_size2 = 0.045 * 1.2
                secondAction_size1_2 = 0.1 * 3
                secondAction_size2_2 = 0.015 * 3
            elif action_bool == False:
                action_int = 1
                secondAction_int = 0
                secondAction_bool = True
                secondAction_size1 = 0
                secondAction_size2 = 0
                secondAction_size1_2 = 0
                secondAction_size2_2 = 0
        else:
            action_int = 1
            action_bool = True
            secondAction_int = 0
            secondAction_bool = True

        self.ids.guess_1.opacity = action_int
        self.ids.guess_1.disabled = action_bool
        self.ids.see_combi_1.opacity = action_int
        self.ids.see_combi_1.disabled = action_bool

        if self.teamTurn == 1:
            self.ids.clue_button_1.opacity = action_int
            self.ids.clue_button_1.disabled = action_bool

        self.ids.guess_team1_box.opacity = secondAction_int

        self.ids.guess_team1_1.opacity = secondAction_int
        self.ids.guess_team1_1.disabled = secondAction_bool
        self.ids.guess_team1_1.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_2.opacity = secondAction_int
        self.ids.guess_team1_2.disabled = secondAction_bool
        self.ids.guess_team1_2.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_3.opacity = secondAction_int
        self.ids.guess_team1_3.disabled = secondAction_bool
        self.ids.guess_team1_3.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_4.opacity = secondAction_int
        self.ids.guess_team1_4.disabled = secondAction_bool
        self.ids.guess_team1_4.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_5.opacity = secondAction_int
        self.ids.guess_team1_5.disabled = secondAction_bool
        self.ids.guess_team1_5.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_6.opacity = secondAction_int
        self.ids.guess_team1_6.disabled = secondAction_bool
        self.ids.guess_team1_6.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_7.opacity = secondAction_int
        self.ids.guess_team1_7.disabled = secondAction_bool
        self.ids.guess_team1_7.size_hint = secondAction_size1, secondAction_size2\
        
        self.ids.guess_team1_8.opacity = secondAction_int
        self.ids.guess_team1_8.disabled = secondAction_bool
        self.ids.guess_team1_8.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_9.opacity = secondAction_int
        self.ids.guess_team1_9.disabled = secondAction_bool
        self.ids.guess_team1_9.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_0.opacity = secondAction_int
        self.ids.guess_team1_0.disabled = secondAction_bool
        self.ids.guess_team1_0.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_selectRight.opacity = secondAction_int
        self.ids.guess_team1_selectRight.disabled = secondAction_bool
        self.ids.guess_team1_selectRight.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_selectLeft.opacity = secondAction_int
        self.ids.guess_team1_selectLeft.disabled = secondAction_bool
        self.ids.guess_team1_selectLeft.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_back.opacity = secondAction_int
        self.ids.guess_team1_back.disabled = secondAction_bool
        self.ids.guess_team1_back.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team1_enter.opacity = secondAction_int
        self.ids.guess_team1_enter.disabled = secondAction_bool
        self.ids.guess_team1_enter.size_hint = secondAction_size1_2, secondAction_size2_2

        self.ids.guess_team1_select.opacity = secondAction_int
        self.ids.guess_team1_combination.opacity = secondAction_int
        self.ids.guess_team1_label.opacity = secondAction_int

        self.ids.guess_team1_combi_box_0.opacity = secondAction_int
        self.ids.guess_team1_combi_box_1.opacity = secondAction_int
        self.ids.guess_team1_combi_box_2.opacity = secondAction_int
        self.ids.guess_team1_combi_box_3.opacity = secondAction_int

        self.ids.wrongGuess_team1.opacity = 0

        self.updateWidget("guess", 1)

    def guessTeam2(self, action_bool, isFinished):
        action_int = 1
        secondAction_int = 0
        secondAction_bool = True

        secondAction_size1 = 0.1 * 1.2
        secondAction_size2 = 0.045 * 1.2

        secondAction_size1_2 = 0.1 * 3
        secondAction_size2_2 = 0.015 * 3

        self.guessingTeam2 = action_bool

        if not isFinished:
            if action_bool == True:
                action_int = 0.5
                secondAction_int = 1
                secondAction_bool = False
                secondAction_size1 = 0.1 * 1.2
                secondAction_size2 = 0.045 * 1.2
                secondAction_size1_2 = 0.1 * 3
                secondAction_size2_2 = 0.015 * 3
            elif action_bool == False:
                action_int = 1
                secondAction_int = 0
                secondAction_bool = True
                secondAction_size1 = 0
                secondAction_size2 = 0
                secondAction_size1_2 = 0
                secondAction_size2_2 = 0
        else:
            action_int = 1
            action_bool = True
            secondAction_int = 0
            secondAction_bool = True
            secondAction_size1 = 0
            secondAction_size2 = 0
            secondAction_size1_2 = 0
            secondAction_size2_2 = 0

        self.ids.guess_2.opacity = action_int
        self.ids.guess_2.disabled = action_bool
        self.ids.see_combi_2.opacity = action_int
        self.ids.see_combi_2.disabled = action_bool

        if self.teamTurn == 2:
            self.ids.clue_button_2.opacity = action_int
            self.ids.clue_button_2.disabled = action_bool

        self.ids.guess_team2_box.opacity = secondAction_int

        self.ids.guess_team2_1.opacity = secondAction_int
        self.ids.guess_team2_1.disabled = secondAction_bool
        self.ids.guess_team2_1.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_2.opacity = secondAction_int
        self.ids.guess_team2_2.disabled = secondAction_bool
        self.ids.guess_team2_2.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_3.opacity = secondAction_int
        self.ids.guess_team2_3.disabled = secondAction_bool
        self.ids.guess_team2_3.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_4.opacity = secondAction_int
        self.ids.guess_team2_4.disabled = secondAction_bool
        self.ids.guess_team2_4.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_5.opacity = secondAction_int
        self.ids.guess_team2_5.disabled = secondAction_bool
        self.ids.guess_team2_5.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_6.opacity = secondAction_int
        self.ids.guess_team2_6.disabled = secondAction_bool
        self.ids.guess_team2_6.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_7.opacity = secondAction_int
        self.ids.guess_team2_7.disabled = secondAction_bool
        self.ids.guess_team2_7.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_8.opacity = secondAction_int
        self.ids.guess_team2_8.disabled = secondAction_bool
        self.ids.guess_team2_8.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_9.opacity = secondAction_int
        self.ids.guess_team2_9.disabled = secondAction_bool
        self.ids.guess_team2_9.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_0.opacity = secondAction_int
        self.ids.guess_team2_0.disabled = secondAction_bool
        self.ids.guess_team2_0.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_selectRight.opacity = secondAction_int
        self.ids.guess_team2_selectRight.disabled = secondAction_bool
        self.ids.guess_team2_selectRight.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_selectLeft.opacity = secondAction_int
        self.ids.guess_team2_selectLeft.disabled = secondAction_bool
        self.ids.guess_team2_selectLeft.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_back.opacity = secondAction_int
        self.ids.guess_team2_back.disabled = secondAction_bool
        self.ids.guess_team2_back.size_hint = secondAction_size1, secondAction_size2

        self.ids.guess_team2_enter.opacity = secondAction_int
        self.ids.guess_team2_enter.disabled = secondAction_bool
        self.ids.guess_team2_enter.size_hint = secondAction_size1_2, secondAction_size2_2

        self.ids.guess_team2_select.opacity = secondAction_int
        self.ids.guess_team2_combination.opacity = secondAction_int
        self.ids.guess_team2_label.opacity = secondAction_int

        self.ids.guess_team2_combi_box_0.opacity = secondAction_int
        self.ids.guess_team2_combi_box_1.opacity = secondAction_int
        self.ids.guess_team2_combi_box_2.opacity = secondAction_int
        self.ids.guess_team2_combi_box_3.opacity = secondAction_int

        self.ids.wrongGuess_team2.opacity = 0

        self.updateWidget("guess", 2)

    def enternumber(self, team, button):
        if team == 1:
            MainGame.guessCombiTeam1[self.guessCombiTeam1_index] = button
            MainGame.guessCheck(MainGame, team)
            self.updateWidget("guess", team)
        elif team == 2:
            MainGame.guessCombiTeam2[self.guessCombiTeam2_index] = button
            MainGame.guessCheck(MainGame, team)
            self.updateWidget("guess", team)

    def guessMoveLeft(self, team):
        if team == 1:
            if self.guessCombiTeam1_index > 0:
                self.guessCombiTeam1_index -= 1
            self.updateWidget("guess", team)
        elif team == 2:
            if self.guessCombiTeam2_index > 0:
                self.guessCombiTeam2_index -= 1
            self.updateWidget("guess", team)

    def guessMoveRight(self, team):
        if team == 1:
            if self.guessCombiTeam1_index < 3:
                self.guessCombiTeam1_index += 1
            self.updateWidget("guess", team)
        elif team == 2:
            if self.guessCombiTeam2_index < 3:
                self.guessCombiTeam2_index += 1
            self.updateWidget("guess", team)

    def guessEnter(self, team):
        if team == 1:
            if self.correctGuess_Team1:
                GameData.winner = 1
                self.showWinner()
            else:
                self.ids.wrongGuess_team1.opacity = 1
            print("Team 1 Guess = " + str(MainGame.guessCombiTeam1))
        elif team == 2:
            if self.correctGuess_Team2:
                GameData.winner = 2
                self.showWinner()
            else:
                self.ids.wrongGuess_team2.opacity = 1
            print("Team 2 Guess = " + str(MainGame.guessCombiTeam2))
    
    def resetWidget(self):
        self.guessCombiTeam1_index = 0
        self.guessCombiTeam2_index = 0

        self.guessTeam1(False, False)
        self.guessTeam2(False, False)
        
        self.clueAccess(2)
        self.ids.element_team1.opacity = 0
        self.ids.element_team2.opacity = 0
        self.ids.compare_indicator.opacity = 0

        self.see_1 = True
        self.see_2 = True

        self.seeCombination(1)
        self.seeCombination(2)

        self.ids.winner_bg.opacity = 0
        self.ids.winner_icon.opacity = 0
        self.ids.winner_label.opacity = 0
        self.ids.play_again_button.opacity = 0
        self.ids.home_screen_button.opacity = 0

        self.ids.play_again_button.disabled = True
        self.ids.home_screen_button.disabled = True

    def updateWidget(self, action, team):
        if action == "clue":
            if self.teamTurn == 2:
                self.ids.clue_button_1.opacity = 0.6
                self.ids.clue_button_1.disabled = True

                if self.guessingTeam2 == True:
                    self.ids.clue_button_2.opacity = 0.5
                    self.ids.clue_button_2.disabled = True
                else:
                    self.ids.clue_button_2.opacity = 1
                    self.ids.clue_button_2.disabled = False

            elif self.teamTurn == 1:
                self.ids.clue_button_2.opacity = 0.6
                self.ids.clue_button_2.disabled = True

                if self.guessingTeam1 == True:
                    self.ids.clue_button_1.opacity = 0.5
                    self.ids.clue_button_1.disabled = True
                else:
                    self.ids.clue_button_1.opacity = 1
                    self.ids.clue_button_1.disabled = False

        if action == "combination":
            if team == 1:
                self.ids.combi_1.text = str(GameData.combinationTeam1[0]) + "   " + str(GameData.combinationTeam1[1]) + "   " + str(GameData.combinationTeam1[2]) + "   " + str(GameData.combinationTeam1[3])
            elif team == 2:
                self.ids.combi_2.text = str(GameData.combinationTeam2[0]) + "   " + str(GameData.combinationTeam2[1]) + "   " + str(GameData.combinationTeam2[2]) + "   " + str(GameData.combinationTeam2[3])
        
        if action == "guess":
            if team == 1:
                if self.guessCombiTeam1_index == 0:
                    self.ids.guess_team1_select.text = "_         "
                elif self.guessCombiTeam1_index == 1:     
                    self.ids.guess_team1_select.text = "   _      "
                elif self.guessCombiTeam1_index == 2:     
                    self.ids.guess_team1_select.text = "      _   "
                elif self.guessCombiTeam1_index == 3:     
                    self.ids.guess_team1_select.text = "         _"

                self.ids.guess_team1_combination.text = str(MainGame.guessCombiTeam1[0]) + "   " + str(MainGame.guessCombiTeam1[1]) + "   " + str(MainGame.guessCombiTeam1[2]) + "   " + str(MainGame.guessCombiTeam1[3])

            elif team == 2:
                if self.guessCombiTeam2_index == 0:
                    self.ids.guess_team2_select.text = "_         "
                elif self.guessCombiTeam2_index == 1:     
                    self.ids.guess_team2_select.text = "   _      "
                elif self.guessCombiTeam2_index == 2:     
                    self.ids.guess_team2_select.text = "      _   "
                elif self.guessCombiTeam2_index == 3:     
                    self.ids.guess_team2_select.text = "         _"

                self.ids.guess_team2_combination.text = str(MainGame.guessCombiTeam2[0]) + "   " + str(MainGame.guessCombiTeam2[1]) + "   " + str(MainGame.guessCombiTeam2[2]) + "   " + str(MainGame.guessCombiTeam2[3])

    def showWinner(self):
        self.guessTeam1(True, True)
        self.guessTeam2(True, True)

        self.ids.winner_bg.opacity = 0.5
        self.ids.winner_icon.opacity = 1
        self.ids.winner_label.opacity = 1
        self.ids.play_again_button.opacity = 1
        self.ids.home_screen_button.opacity = 1

        self.ids.play_again_button.size_hint = 0.035 * 4.2, 0.045 * 4.2
        self.ids.home_screen_button.size_hint = 0.035 * 4.2, 0.045 * 4.2

        self.ids.play_again_button.disabled = False
        self.ids.home_screen_button.disabled = False

        if GameData.winner == 1:
            self.ids.winner_label.source = 'textures/labels_black/winner_player_1.png'
        elif GameData.winner == 2:
            self.ids.winner_label.source = 'textures/labels_black/winner_player_2.png'

        randomIcon = random.randint(0, 1)

        if randomIcon == 0:
            self.ids.winner_icon.source = 'textures/other_icons/winner_stars.png'
            self.ids.winner_icon.size_hint = 0.55, 0.55
        elif randomIcon == 1:
            self.ids.winner_icon.source = 'textures/other_icons/winner_trophy.png'
            self.ids.winner_icon.size_hint = 0.35, 0.35

    def playAgain(self):
        self.resetWidget()
        PostGame.resetGame()
        kv.current = "setup"
    
    def homeScreen(self):
        self.resetWidget()
        PostGame.resetGame()
        kv.current = "menu"

class Screen(ScreenManager):
    pass
    
class SetUp:
    currentTeam = 1
    combinationIndex = 0
    
    currentTeamLabel = str(currentTeam)

    def inputNumber(number):
        if SetUp.currentTeam == 1:
            GameData.combinationTeam1[SetUp.combinationIndex] = number
        elif SetUp.currentTeam == 2:
            GameData.combinationTeam2[SetUp.combinationIndex] = number

        SetUpScreen.currentInputIndex = SetUp.combinationIndex

        if SetUp.combinationIndex < 3:
            SetUp.combinationIndex+= 1

        GameData.sumCombination()

    def eraseNumber():
        if SetUp.currentTeam == 1:
            if SetUp.combinationIndex > 0 and GameData.combinationTeam1[SetUp.combinationIndex] == 0:
                SetUp.combinationIndex -= 1

            GameData.combinationTeam1[SetUp.combinationIndex] = 0      

        elif SetUp.currentTeam == 2:
            if SetUp.combinationIndex > 0 and GameData.combinationTeam2[SetUp.combinationIndex] == 0:
                SetUp.combinationIndex -= 1

            GameData.combinationTeam2[SetUp.combinationIndex] = 0

        SetUpScreen.currentInputIndex = SetUp.combinationIndex
        
        GameData.sumCombination()

    def enterProceed():
        if SetUp.currentTeam == 1:
            if GameData.combinationSum == 20:
                SetUpScreen.currentTeamTurn = 2
                SetUp.currentTeam = 2
                SetUp.combinationIndex = 0
                SetUpScreen.showWarning = False
            else:
                SetUpScreen.showWarning = True
        elif SetUp.currentTeam == 2:
            if GameData.combinationSum == 20:
                SetUpScreen.currentTeamTurn = 1
                SetUpScreen.showWarning = False                
                SetUpScreen.ProceedGame()
            else:
                SetUpScreen.showWarning = True

class MainGame:
    guessCombiTeam1 = [0, 0, 0, 0]
    guessCombiTeam2 = [0, 0, 0, 0]

    def searchRandomCompare(self):
        randomIndexTeam1 = random.randint(0, 3)
        randomIndexTeam2 = random.randint(0, 3)     
            
        self.setElementsLetter(None, randomIndexTeam1, randomIndexTeam2)

        if GameData.combinationTeam1[randomIndexTeam1] < GameData.combinationTeam2[randomIndexTeam2]:
            GameScreen.compare_indicator = '<'
        elif GameData.combinationTeam1[randomIndexTeam1] > GameData.combinationTeam2[randomIndexTeam2]:
            GameScreen.compare_indicator = '>'
        elif GameData.combinationTeam1[randomIndexTeam1] == GameData.combinationTeam2[randomIndexTeam2]:
            GameScreen.compare_indicator = '='
        
    def setElementsLetter(self, team1_index, team2_index):
        if team1_index == 0:
            GameScreen.compare_element1 = 'A'
        elif team1_index == 1:
            GameScreen.compare_element1 = 'B'
        elif team1_index == 2:
            GameScreen.compare_element1 = 'C'
        elif team1_index == 3:
            GameScreen.compare_element1 = 'D'

        if team2_index == 0:
            GameScreen.compare_element2 = 'A'
        elif team2_index == 1:
            GameScreen.compare_element2 = 'B'
        elif team2_index == 2:
            GameScreen.compare_element2 = 'C'
        elif team2_index == 3:
            GameScreen.compare_element2 = 'D'

    def switchTurn(current_team):
        if current_team == 1:
            GameScreen.teamTurn = 2
        elif current_team == 2:
            GameScreen.teamTurn = 1

    def guessCheck(self, team):
        if team == 1:
            if self.guessCombiTeam1[0] == GameData.combinationTeam2[0] and self.guessCombiTeam1[1] == GameData.combinationTeam2[1] and self.guessCombiTeam1[2] == GameData.combinationTeam2[2] and self.guessCombiTeam1[3] == GameData.combinationTeam2[3]:
                GameScreen.correctGuess_Team1 = True
            else:
                GameScreen.correctGuess_Team1 = False
        elif team == 2:
            if self.guessCombiTeam2[0] == GameData.combinationTeam1[0] and self.guessCombiTeam2[1] == GameData.combinationTeam1[1] and self.guessCombiTeam2[2] == GameData.combinationTeam1[2] and self.guessCombiTeam2[3] == GameData.combinationTeam1[3]:
                GameScreen.correctGuess_Team2 = True
            else:
                GameScreen.correctGuess_Team2 = False

class PostGame:
    def resetGame():
        SetUpScreen.currentTeamTurn = 1
        SetUpScreen.currentInputIndex = 0
        SetUpScreen.currentTotal = 0
        SetUpScreen.showWarning = False

        SetUp.currentTeam = 1
        SetUp.combinationIndex = 0

        GameScreen.teamTurn = 1
        GameScreen.correctGuess_Team1 = False
        GameScreen.correctGuess_Team2 = False

        MainGame.guessCombiTeam1 = [0, 0, 0, 0]
        MainGame.guessCombiTeam2 = [0, 0, 0, 0]

        GameData.combinationTeam1 = [0, 0, 0, 0]
        GameData.combinationTeam2 = [0, 0, 0, 0]
        GameData.combinationSum = 0
        GameData.winner = 0

        print("Game Reset")

class GameData:
    combinationTeam1 = [0, 0, 0, 0]
    combinationTeam2 = [0, 0, 0, 0]

    combinationSum = 0

    winner = 0

    def sumCombination():
        if SetUp.currentTeam == 1:
            GameData.combinationSum = sum(GameData.combinationTeam1)
        elif SetUp.currentTeam == 2:
            GameData.combinationSum = sum(GameData.combinationTeam2)

        SetUpScreen.currentTotal = GameData.combinationSum

kv = Builder.load_file("appmain.kv")

class AppMain(App):
    def build(self):
        return kv

if __name__ == '__main__':
    AppMain().run()