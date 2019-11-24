from browser import webcomponent, html, bind
class Tk(object):
    def __init__(self,screenName,baseName,className,useTk,render,windowProvider,ui):
        self.render = render
        self.windowProvider = windowProvider
        self.ui = ui
def _getRoot(theUIElement):
    e = theUIElement
    while e.parent is not None:
        e = e.parent
    return e
class Widget(object):
    def __init__(self,parent = None):
        self.parent = parent
        self.packed = False
        self.parent.addChild(self)
    def render(self,r):
        return None
    def pack(self):
        self.rendered = self.render(_getRoot(self).render)
        self.packed = True
class WithChildren(object):
    def __init__(self):
        self.children = []
    def addChild(self,c):
        self.children.append(c)
class Text(Widget):
    def insert(self,pos,text):
        self.text = self.text[:pos] + text + self.text[pos:]
    def delete(self,start,end = None):
        self.text = self.text[:start] + self.text[end:]
    def get(start, end=None):
        return self.text[start:end]
    def render(self,r):
        def getText():
            return self.text
        def setText(v):
            self.text = v
        return r(_getRoot(self).ui.TextArea,{'getText': getText,'setText': setText})
class Frame(Widget,WithChildren):
    def __init__(self,parent = None):
        Widget.__init__(self,parent)
        WithChildren.__init__(self)
        self._window = None
    def pack():
        super().pack()
        root = _getRoot(self)
        if self._window is not None:
            self._window.destroy()
        self._window = root.windowProvider.addWindow({'children': list(map(self.children,lambda c: c.rendered))})
