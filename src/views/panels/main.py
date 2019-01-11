#######################
# Authors:            #
#                     #
# Olivier Dion - 2019 #
#######################

from urwid import Filler

from src.views.base.buffer import Controller, Signal
from src.views.base.hydra import Hydra, HydraWidget

from src.views.base.tui import TUI

@Signal("on_swap")
class MainPanel(HydraWidget, Controller):

    def __init__(self):

        hydra = Hydra("MainView", [],
                      info="Welcome to INF1900 interactive grading tool!",
                      color=Hydra.blue)

        super().__init__(hydra=hydra, align="center")

        self.root = Filler(self, valign="bottom")

    def add_views(self, views):


        heads = []

        for letter, view, hint,  in views:
            heads.append((letter, self.swap_view, hint, None, {"view":view,
                                                               "hint":hint}))

        self.add_heads(heads)

    def add_actions(self, actions):

        if not isinstance(actions, list):
            actions = [actions]

        heads = []

        for action in actions:
            heads.append((action[0], action[1], action[2]))

        self.add_heads(heads)

    def swap_view(self, view, hint):
        self.emit("on_swap", view, hint)

    def restore(self, *kargs):
        self.emit("on_swap", self, "")
