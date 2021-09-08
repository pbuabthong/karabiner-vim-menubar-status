import rumps

class StatusBarApp(rumps.App):
    def __init__(self):
        super(StatusBarApp, self).__init__("I", icon="insert.ico")
        self.mode = 0

    def set_title(self, mode):
        if mode == 0:
            self.icon = "normal.ico"
        elif mode == 1:
            self.icon = "insert.ico"
        elif mode == 2:
            self.icon = "visual.ico"
        else:
            self.icon = "disabled.ico"

    @rumps.timer(0.5)
    def a(self, sender):
        with open('/Users/pbuabthong/mode') as f:
            mode = int(f.readlines()[0])
            if mode != self.mode:
                self.set_title(mode)
                self.mode = mode


if __name__ == "__main__":
    StatusBarApp().run()

