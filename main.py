from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ObjectProperty,NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.video import Video
from kivy.uix.widget import Widget
import pandas as pd
from question import quiz
from kivy.uix.stacklayout import StackLayout

#class for the invalid information popup window

class InvalidInfo(Widget):
    def btn(self):
        Invalid_infor()

#function for the invalid information popup window
def Invalid_infor():
    show = InvalidInfo()
    window = Popup(content= show, title= 'Warning!', size_hint=(None,None), size= (250,250))
    window.open()

class Screen1(Screen):
    def Object(self):
        nam = ObjectProperty(None)
        age = ObjectProperty(None)
        grade = ObjectProperty(None)
        hobby = ObjectProperty(None)
    def on_validate(self):
        # creating a DataFrame of the info
        user = pd.DataFrame([[self.nam.text, self.age.text, self.grade.text,self.hobby.text]],
                            columns=['Name', 'Age', 'Grade','Hobby'])
        # if self.nam.text == self.number:
        #     Invalid_infor()
        if self.nam.text == "":
            Invalid_infor()
        # elif self.age.text != int:
        #     Invalid_infor()
        elif self.age.text == "":
            Invalid_infor()
        # elif self.grade.text != int:
        #     Invalid_infor()
        elif self.grade.text == "":
            Invalid_infor()
        # elif self.hobby.text == int:
        #     Invalid_infor()
        elif self.hobby.text == "":
            Invalid_infor()
        else:
            user.to_csv('userdetails.csv', mode='w', header=False, index=False)
            sm.current = 'two'
            self.nam.text = ""
            self.age.text = ""
            self.grade.text = ""
            self.hobby.text = ""





class Screen2(Screen):
    pass


class Screen3(Screen):
    pass


class Screen4(Screen):
    pass


class Screen5(Screen):
    pass


class Screen6(Screen):
    pass


class Screen7(Screen):
    pass


class Screen8(Screen):
    # def Object(self):
    #     song = ObjectProperty(None)
    # def Play_video(self):
    #     song = Video(source = 'videos/finger.mp4')
    #     song.state = 'play'
    #     song.options = {'eos': 'loop'}
    #     song.allow_stretch = True
    #     return song
    pass
#changes


class Screen9(Screen):
    def Object(self):
        add = ObjectProperty(None)
    def Addition(self):
        try:
            score = 0
            for question in quiz:
                attempts = 3
                while attempts > 0:
                    print(quiz[question]['question'])
                    answer = input("Enter Answer: ")
                    def check_ans(question, ans,attempts,score):
                        if quiz[question]['answer'].lower() == ans.lower():
                            print(f"Correct Answer! \nYour score is {score + 1}!")
                            return True
                        else:
                            print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
                            return False
                    attempts -= 1

                    check = check_ans(question, answer, attempts, score)
                    if check:
                        score += 1
                        break
        except:
            print('Error')


class Screen10(Screen,StackLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     for i in range(0, 10):
    #         b1 = Button(text=str(i+1), size_hint=(.2, .3))
    #         self.add_widget(b1)
    pass
class Screen11(Screen):
    pass
class Screen12(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')
sm = WindowManager()

# reading all the data stored
users = pd.read_csv('childdetails.csv')

# adding screens
sm.add_widget(Screen1(name='one'))
sm.add_widget(Screen2(name='two'))
sm.add_widget(Screen3(name='three'))
sm.add_widget(Screen4(name='four'))
sm.add_widget(Screen5(name='five'))
sm.add_widget(Screen6(name='six'))
sm.add_widget(Screen7(name='seven'))
sm.add_widget(Screen8(name='eight'))
sm.add_widget(Screen9(name='nine'))
sm.add_widget(Screen10(name='ten'))
sm.add_widget(Screen11(name='eleven'))
sm.add_widget(Screen12(name='twelve'))


class ChildApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    ChildApp().run()


