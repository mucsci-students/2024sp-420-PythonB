from Views.gui_view import GUI_View

class GUI_Controller:

    def __init__(self):
       self._gui_view = GUI_View()

    def update (self):
        while len(self._gui_view._commands) > 0:
            cmd = self.request_update()
            cmd[0](*cmd[1:])

    def request_update(self):
        while len(self._gui_view._commands) == 0:
            pass
        return self._gui_view._commands.pop(0)