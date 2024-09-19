import wx
import wx.html2 as webview

class MyWebViewApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyWebViewApp, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.webview = webview.WebView.New(self.panel)

        # Load the Google website
        self.webview.LoadURL("https://www.google.com")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.webview, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyWebViewApp(None, wx.ID_ANY, "WebView Google")
    frame.Show()
    app.MainLoop()
