from kivy.app import App 
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_line()
    
    def on_parent(self, widget, parent):
        # print("ON PARENT W:" + str(self.width) + " H:" + str(self.height))
        pass
    
    def on_size(self, *args):
        # print("ON SIZE W:" + str(self.width) + " H:" + str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        pass
    
    def on_perspective_point_x(self, widget, value):
        # print("PX: " + str(value))
        pass
    
    def on_perspective_point_y(self, widget, value):
        # print("PY: " + str(value))
        pass
    
    def init_vertical_line(self):
        with self.canvas:
            Color(1, 1, 1)
            Line(points=[100, 0, 100, 100])
    
    
class GalaxyApp(App):
    pass

if __name__ == "__main__":
    GalaxyApp().run()