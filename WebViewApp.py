import wx
import wx.html2

class WebViewApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WebViewApp, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        # Get the screen size to determine the width and height
        screen_width, screen_height = wx.GetDisplaySize()

        # Create the main frame and maximize it
        self.Maximize()
        
        self.panel = wx.Panel(self)
        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.webview = wx.html2.WebView.New(self.panel)
        self.panel_sizer.Add(self.webview, proportion=1, flag=wx.EXPAND, border=0)

        self.close_button = wx.Button(self.panel, label="Close")
        self.close_button.Bind(wx.EVT_BUTTON, self.OnClose)
        self.panel_sizer.Add(self.close_button, flag=wx.ALIGN_RIGHT | wx.ALL, border=10)

        self.panel.SetSizerAndFit(self.panel_sizer)
        self.panel.Layout()

        self.webview.LoadURL("https://www.soorvihar.in")

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        self.Destroy()

def main():
    app = wx.App()
    frame = WebViewApp(None, title="WebView App")
    frame.Center()
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
