# Importing cef
from cef_wrapper import cef, Browser


# Example with the 'Browser' object:
# 'Browser' can be used for type hints
# https://github.com/cztomczak/cefpython/blob/master/api/Browser.md
def foo(browser: Browser):
    browser.CanGoBack()  # Syntax highlighting and a docstring ;)


# Example with the class 'WindowInfo':
# https://github.com/cztomczak/cefpython/blob/master/api/WindowInfo.md
def bar():
    window_info = cef.WindowInfo()  # Like with cefpython3, WindowInfo() needs to be initialized
    window_info.SetAsChild(parentWindowHandle=None, windowRect=None)


# Using the hello_world example from:
# https://github.com/cztomczak/cefpython/blob/master/examples/hello_world.py
#
# Hello world example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v57.0+.
# 
# ==== High DPI support on Windows ====
# To enable DPI awareness on Windows you have to either embed DPI aware manifest
# in your executable created with pyinstaller or change python.exe properties manually:
# Compatibility > High DPI scaling override > Application.
# Setting DPI awareness programmatically via a call to cef.DpiAware.EnableHighDpiSupport
# is problematic in Python, may not work and can cause display glitches.


import platform
import sys


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://www.google.com/",
                          window_title="Hello World!")
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


if __name__ == '__main__':
    main()