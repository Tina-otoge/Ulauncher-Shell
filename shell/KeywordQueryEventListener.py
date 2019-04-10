from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

class KeywordQueryEventListener(EventListener):
    def __init__(self, icon):
        self.icon = icon

    def on_event(self, event, extension):

        argument = event.get_argument()
        min_length = 2
        arg_length = len(argument) if argument else 0
        delta = min_length - arg_length

        if delta > 0:
            msg = 'Type {} more letter{} to enable auto-complete'.format(
                delta,
                's' if delta > 1 else ''
            )
            return RenderResultListAction([ExtensionResultItem(
                icon = 'images/icon.png',
                name = msg
            )])

        executables = extension.get_executables(argument)[:7]
        items = []
        for i in executables:
            data = {'item': i, 'argument': argument}
            items.append(
                ExtensionResultItem(
                    icon = self.icon,
                    name = i,
                    description = extension.get_description(i),
                    on_enter = ExtensionCustomAction(data)
                )
            )

        return RenderResultListAction(items)
