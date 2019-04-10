from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent

import subprocess
import os

from .KeywordQueryEventListener import KeywordQueryEventListener
from .ItemEnterEventListener    import ItemEnterEventListener

class ShellExtension(Extension):

    ICON_FILE = 'images/icon.png'

    def __init__(self):
        super(ShellExtension, self).__init__()
        self.icon = self.ICON_FILE
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener(self.ICON_FILE))
        self.subscribe(ItemEnterEvent, ItemEnterEventListener(self.ICON_FILE))

    def get_executables(self, word=None):
        try:
            output = subprocess.check_output(['bash', '-c', 'compgen -c {}'.format(word or '')])
        except subprocess.CalledProcessError as processError:
            raise Exception('no bash or no compgen available')
        return output.decode().splitlines()

    def execute(self, command):
        devnull = open(os.devnull, "w")
        try:
            subprocess.Popen(command.split(), stdout=devnull, stderr=devnull, close_fds=True)
        except subprocess.CalledProcessError as processError:
            raise Exception('The proccess did an oopsie')

    def get_description(self, command):
        try:
            output = subprocess.check_output(['whatis', command], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as processError:
            if processError.returncode is 16:
                return ''
            raise Exception('Can\'t call whatis')
        return output.decode()
