from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.OpenAction import OpenAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

class ItemEnterEventListener(EventListener):
    def __init__(self, icon):
        self.icon = icon

    def on_event(self, event, extension):
        data = event.get_data()
        extension.execute(data['item'])
        return HideWindowAction()
