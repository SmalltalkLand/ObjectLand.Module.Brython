from browser import webcomponent, html, bind
import tkinter
class Py(object):
    def __init__(self):
        self.shadow = self.attachShadow({'mode': 'open'})
        self.locals = {}
        self.globals = {}
        ta = html.TEXTAREA()
        self.shadow <= ta
        bind(ta,'change')(self.onChange(ta))
        button = html.BUTTON('Evaluate')
        self.shadow <= button
        bind(button,'click')(self.eval)
    def onChange(self,ta):
        def output():
            self.value = ta.value
        return output
    def eval(self):
        exec(self.value,self.globals,self.locals)

webcomponent.define('ol-python-py',Py)