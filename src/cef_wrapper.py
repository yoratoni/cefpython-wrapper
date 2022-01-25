# Copyright of cefpython3:
#   Copyright (c) 2022 CEF Python, see the Authors file.
#   All rights reserved. Licensed under BSD 3-clause license.
#   Project website: https://github.com/cztomczak/cefpython


# MADE BY YORATONI: https://github.com/yoratoni
# Licensed under MIT license.
#
# cef_wrapper.py allows autocompleting & methods highlighting
# for the cefpython3 library.
#
# Classes directly calls internal cefpython methods.
# Objects are only defined as separated classes.
# You can find all the classes / objects here:
# https://github.com/cztomczak/cefpython#classes-and-objects


from cefpython3 import cefpython
from typing import Any, Callable


class Frame:
    # https://github.com/cztomczak/cefpython/blob/master/api/Frame.md
    pass


class TextInputContext:
    # NOT YET PORTED
    pass


class Image:
    # https://github.com/cztomczak/cefpython/blob/master/api/Image.md

    class cef_color_type_t:
        '''cef_color_type_t constants in the cefpython module:
        - CEF_COLOR_TYPE_RGBA_8888
        - CEF_COLOR_TYPE_BGRA_8888
        '''
        
    class cef_alpha_type_t:
        '''enum cef_alpha_type_t constants in the cefpython module:
        - CEF_ALPHA_TYPE_OPAQUE
        - CEF_ALPHA_TYPE_PREMULTIPLIED
        - CEF_ALPHA_TYPE_POSTMULTIPLIED
        '''

    @staticmethod
    def GetAsBitmap(scale_factor: float, color_type: cef_color_type_t, alpha_type: cef_alpha_type_t) -> bytes:
        '''Returns the bitmap representation that most closely matches |scale_factor|.
        
        cef_color_type_t constants in the cefpython module:
        - CEF_COLOR_TYPE_RGBA_8888
        - CEF_COLOR_TYPE_BGRA_8888
        
        enum cef_alpha_type_t constants in the cefpython module:
        - CEF_ALPHA_TYPE_OPAQUE
        - CEF_ALPHA_TYPE_PREMULTIPLIED
        - CEF_ALPHA_TYPE_POSTMULTIPLIED
        '''
        
        
    @staticmethod
    def GetAsPng(scale_factor: float, with_transparency: bool) -> bytes:
        '''Returns image data as bytes.
        
        Description from upstream CEF:
        
        Returns the PNG representation that most closely matches |scale_factor|.
        
        If |with_transparency| is true any alpha transparency in the image will be represented
        in the resulting PNG data.
        
        |pixel_width| and |pixel_height| are the output representation size in pixel coordinates.
        
        Returns a CefBinaryValue containing the PNG image data on success or NULL on failure.
        '''
        
        
    @staticmethod
    def GetHeight() -> int:
        '''Returns the image height in density independent pixel (DIP) units.
        '''
        
        
    @staticmethod
    def GetWidth() -> int:
        '''Returns the image width in density independent pixel (DIP) units.
        '''


class DragData:
    # https://github.com/cztomczak/cefpython/blob/master/api/DragData.md

    @staticmethod
    def IsLink() -> bool:
        '''Returns true if the drag data is a link.
        '''


    @staticmethod
    def IsFragment() -> bool:
        '''Returns true if the drag data is a text or html fragment.
        '''


    @staticmethod
    def GetLinkUrl() -> str:
        '''Return the link URL that is being dragged.
        '''


    @staticmethod
    def GetLinkTitle() -> str:
        '''Return the title associated with the link being dragged.
        '''


    @staticmethod
    def GetFragmentText() -> str:
        '''Return the plain text fragment that is being dragged.
        '''


    @staticmethod
    def GetFragmentHtml() -> str:
        '''Return the text/html fragment that is being dragged.
        '''


    @staticmethod
    def GetImage() -> Image:
        '''Description from upstream CEF:
        
        Get the image representation of drag data. May return NULL
        if no image representation is available.
        
        Check with HasImage() first, otherwise if there is no image an exception is thrown.
        '''


    @staticmethod
    def GetImageHotspot() -> Image:
        '''Get the image hotspot (drag start location relative to image dimensions).
        '''


    @staticmethod
    def HasImage() -> bool:
        '''Returns true if an image representation of drag data is available.
        '''


class Browser:
    # https://github.com/cztomczak/cefpython/blob/master/api/Browser.md
    
    
    # ONLY FOR TYPING
    # Because cef.JavascriptBindings can't be referenced here
    class JavascriptBindings:
        pass
    
    
    @staticmethod
    def AddWordToDictionary(word: str):
        '''Add the specified |word| to the spelling dictionary.
        '''

    
    @staticmethod
    def CanGoBack() -> bool:
        '''Returns true if the browser can navigate backwards.
        '''
    
    
    @staticmethod
    def CanGoForward() -> bool:
        '''Returns true if the browser can navigate forwards.
        '''
    
    
    @staticmethod
    def CloseBrowser(forceClose: bool):
        '''Closes the browser.
        
        If the window was created explicitily by you (not a popup)
        you still need to post WM_DESTROY message to the window.

        Request that the browser close.
        
        The Javascript 'onbeforeunload' event will be fired.
        
        If |force_close| is false the event handler, if any,
        will be allowed to prompt the user and the user can optionally cancel the close.
        
        If |force_close| is true the prompt will not be displayed and the close will proceed.
        
        Results in a call to LifespanHandler::DoClose() if the event handler allows the close
        or if |force_close| is true.
        
        See LifespanHandler::DoClose() documentation for additional usage information.
        '''


    @staticmethod
    def CloseDevTools() -> bool:
        '''Explicitly close the associated DevTools browser, if any.
        '''
    
    
    @staticmethod
    def DragTargetDragEnter(drag_data: DragData, x: int, y: int, allowed_ops:int):
        '''Description from upstream CEF:
        
        Call this method when the user drags the mouse into the web view
        (before calling DragTargetDragOver/DragTargetLeave/DragTargetDrop).
        
        |drag_data| should not contain file contents
        as this type of data is not allowed to be dragged into the web view.
        
        File contents can be removed using CefDragData::ResetFileContents
        (for example, if |drag_data| comes from CefRenderHandler::StartDragging).
        
        This method is only used when window rendering is disabled.
        '''
    
    
    @staticmethod
    def DragTargetDragOver(x: int, y: int, allowed_ops:int):
        '''Description from upstream CEF:
        
        Call this method each time the mouse is moved across the web view during a drag operation
        (after calling DragTargetDragEnter and before calling DragTargetDragLeave/DragTargetDrop).
        
        This method is only used when window rendering is disabled.
        '''
    
    
    @staticmethod
    def DragTargetDragLeave():
        '''Description from upstream CEF:
        
        Call this method when the user drags the mouse out of the web view
        (after calling DragTargetDragEnter).
        
        This method is only used when window rendering is disabled.
        '''
        
    
    @staticmethod
    def DragTargetDrop(x: int, y: int):
        '''Description from upstream CEF:
        
        Call this method when the user completes the drag operation by
        dropping the object onto the web view (after calling DragTargetDragEnter).
        
        The object being dropped is |drag_data|, given as an argument
        to the previous DragTargetDragEnter call.
        
        This method is only used when window rendering is disabled.
        '''
    
    
    @staticmethod
    def DragSourceEndedAt(x: int, y: int, operation: int):
        '''Description from upstream CEF:

        Call this method when the drag operation started by a CefRenderHandler::StartDragging
        call has ended either in a drop or by being cancelled.
        
        |x| and |y| are mouse coordinates relative to the upper-left corner of the view.
        
        If the web view is both the drag source and the drag target
        then all DragTarget* methods should be called before DragSource* methods.
        
        This method is only used when window rendering is disabled.
        
        Operation enum from upstream CEF - these constants are declared in the cefpython module:
        - DRAG_OPERATION_NONE = 0,
        - DRAG_OPERATION_COPY = 1,
        - DRAG_OPERATION_LINK = 2,
        - DRAG_OPERATION_GENERIC = 4,
        - DRAG_OPERATION_PRIVATE = 8,
        - DRAG_OPERATION_MOVE = 16,
        - DRAG_OPERATION_DELETE = 32,
        - DRAG_OPERATION_EVERY = UINT_MAX
        '''
    
    
    @staticmethod
    def DragSourceSystemDragEnded():
        '''Description from upstream CEF:
        
        Call this method when the drag operation started by
        a CefRenderHandler::StartDragging call has completed.
        
        This method may be called immediately without first calling DragSourceEndedAt
        to cancel a drag operation.
        
        If the web view is both the drag source and the drag
        target then all DragTarget* methods should be called before DragSource* methods.
        
        This method is only used when window rendering is disabled.
        '''
        
    
    @staticmethod
    def ExecuteFunction(funcName: str, params: list[Any]):
        '''Call javascript function asynchronously.
        
        This can also call object's methods, just pass "object.method" as funcName.
        
        Any valid javascript syntax is allowed as funcName,
        you could even pass an anonymous function here.

        For a list of allowed types for mixed see JavascriptBindings.IsValueAllowed()
        (except function, method and instance).

        Passing a python function here is not allowed,
        it is only possible through JavascriptCallback object.
        '''
        
        
    @staticmethod
    def ExecuteJavascript(jsCode: str, scriptUrl: str, startLine: int):
        '''Execute a string of JavaScript code in this frame.
        
        The scriptURL parameter
        is the URL where the script in question can be found, if any.
        
        The renderer may request this URL to show the developer the source of the error.
        
        The startLine parameter is the base line number to use for error reporting.

        This function executes asynchronously so there is no way to get the returned value.

        Calling javascript from native code synchronously is not possible in CEF 3.
        
        It is also not possible doing it synchronously the other way around ie. js->native.
        '''
    
    
    @staticmethod
    def Find(searchId: int, searchText: str, forward: bool, matchCase: bool, findNext: bool):
        '''Description from upstream CEF:
        
        Search for |searchText|.
        
        |identifier| must be a unique ID and these IDs must strictly increase
        so that newer requests always have greater IDs than older requests.
        
        If |identifier| is zero or less than the previous ID value
        then it will be automatically assigned a new valid ID.
        
        |forward| indicates whether to search forward or backward within the page.
        
        |matchCase| indicates whether the search should be case-sensitive.
        
        |findNext| indicates whether this is the first request or a follow-up.
        
        The CefFindHandler instance, if any, returned via CefClient::GetFindHandler
        will be called to report find results.
        '''
    
    
    @staticmethod
    def GetClientCallback(name: str):
        '''Get client callback by name.
        '''
    
    
    @staticmethod
    def GetClientCallbacksDict() -> dict:
        '''Get client callbacks as a dictionary.
        '''
    
    
    @staticmethod
    def GetFocusedFrame() -> Frame:
        '''Returns the focused Frame for the browser window.
        '''
    
    
    @staticmethod
    def GetFrame(name: str) -> Frame:
        '''Returns the Frame with the specified name, or NULL if not found.
        '''
    
    
    @staticmethod
    def GetFrameByIdentifier(identifier: int) -> Frame:
        '''Available only in CEF 3.
        
        Returns the Frame with the specified identifier, or None if not found.
        '''
    
    
    @staticmethod
    def GetFrames() -> list[Frame]:
        '''Get all frames.
        
        This is an internal CEF Python implementation that uses
        GetFrameNames() and GetFrame() methods to list through all frames.
        
        The main frame is not included in that list.
        '''
    
    
    # @staticmethod
    # def GetFrameCount() -> int:
    #     '''Available only in CEF 3. Not yet implemented.

    #     Returns the number of frames that currently exist.
    #     '''
    
    
    # @staticmethod
    # def GetFrameIdentifiers() -> list[int]:
    #     '''Available only in CEF 3. Not yet implemented.

    #     Returns the identifiers of all existing frames.
    #     '''
    
    
    @staticmethod
    def GetFrameNames() -> list[str]:
        '''Returns the names of all existing frames.
        
        This list does not include the main frame.
        '''
    
    
    @staticmethod
    def GetImage() -> tuple[bytes, int, int]:
        '''Currently available only on Linux (Issue #427).

        Get browser contents as image.
        
        Only screen visible contents are returned.

        Returns an RGB buffer which can be converted to an image using PIL library.
        '''
    

    @staticmethod
    def GetJavascriptBindings() -> JavascriptBindings:
        '''Returns the JavascriptBindings object
        that was passed to cefpython.CreateBrowserSync().
        '''
    
    
    @staticmethod
    def GetMainFrame() -> Frame:
        '''Returns the main (top-level) Frame for the browser window.
        '''
    
    
    # @staticmethod
    # def GetNSTextInputContext() -> TextInputContext:
    #     '''Not yet ported. Available only in CEF 3.

    #     Get the NSTextInputContext implementation for enabling IME on Mac
    #     when window rendering is disabled.
    #     '''
    
    
    @staticmethod
    def GetOpenerWindowHandle() -> int:
        '''Retrieve the CEF-internal (inner or outer) window handle
        of the browser that opened this browser.
        
        Will return None for non-popup windows.
        
        See GetWindowHandle() for an explanation of inner/outer window handles.
        '''
        
    
    @staticmethod
    def GetOuterWindowHandle() -> int:
        '''Get the most outer window handle.
        '''
    
    
    @staticmethod
    def GetSetting(key: str) -> Any:
        '''Get a browser setting.
        
        You can set browser settings by passing settings parameter to cef.CreateBrowserSync().
        '''
    
    
    @staticmethod
    def GetUrl() -> str:
        '''Get url of the main frame.
        '''
    
    
    @staticmethod
    def GetUserData(key: Any) -> Any:
        '''Get user data. See also SetUserData().
        '''
    
    
    @staticmethod
    def GetWindowHandle() -> int:
        '''Returns an inner or outer window handle for the browser.
        
        If the browser was created using CreateBrowserSync() then this will
        return an inner CEF-internal window handle.
        
        If this is a popup browser created from javascript using window.open()
        and its WindowInfo has not been set in LifespanHandler.OnAfterCreated(),
        then it returns CEF-internal window handle
        which is the most outer window handle in this case.'''
    
    
    @staticmethod
    def GetIdentifier() -> int:
        '''Returns the globally unique identifier for this browser.
        
        This value is also used as the tabId for extension APIs.
        '''
        
    
    @staticmethod
    def GetZoomLevel() -> float:
        '''Get the current zoom level.
        
        The default zoom level is 0.0.
        '''
    
    
    @staticmethod
    def GoBack():
        '''Navigate backwards.
        '''
    
    
    @staticmethod
    def GoForward():
        '''Navigate forwards.
        '''
    
    
    # @staticmethod
    # def HandleKeyEventAfterTextInputClient(keyEvent: int):
    #     '''Available only in CEF 3. Not yet implemented.

    #     Performs any additional actions after NSTextInputClient handles the event.
    #     '''
    
    
    # @staticmethod
    # def HandleKeyEventBeforeTextInputClient():
    #     '''Available only in CEF 3. Not yet implemented.

    #     Handles a keyDown event prior to passing it through the NSTextInputClient machinery.
    #     '''
    
    
    @staticmethod
    def HasDevTools() -> bool:
        '''Description from upstream CEF:
        
        Returns true if this browser currently has an associated DevTools browser.
        
        Must be called on the browser process UI thread.
        '''
    
    
    @staticmethod
    def HasDocument() -> bool:
        '''Returns true if a document has been loaded in the browser.
        '''

    
    class PaintElementType:
        '''PaintElementType enum values defined in cefpython module:
            - PET_VIEW
            - PET_POPUP
        '''
    
    
    @staticmethod
    def Invalidate(element_type: PaintElementType):
        '''Description from upstream CEF:
        
        Invalidate the view.
        
        The browser will call CefRenderHandler::OnPaint asynchronously.
        
        This method is only used when window rendering is disabled.
        
        PaintElementType enum values defined in cefpython module:
        - PET_VIEW
        - PET_POPUP
        '''
    
    
    @staticmethod
    def IsFullscreen():
        '''Whether in fullscreen mode, see ToggleFullscreen().
        
        This function is Windows-only.
        '''
    
    
    # @staticmethod
    # def IsLoading() -> bool:
    #     '''Available only in CEF 3. Not yet implemented.

    #     Returns true if the browser is currently loading.
    #     '''
    
    
    @staticmethod
    def IsMouseCursorChangeDisabled() -> bool:
        '''Available only in CEF 3.

        Returns true if mouse cursor change is disabled.
        '''
    
    
    @staticmethod
    def IsPopup() -> bool:
        '''Returns true if the window is a popup window.
        '''
    
    
    @staticmethod
    def IsWindowRenderingDisabled() -> bool:
        '''Returns true if window rendering is disabled.
        '''
    
    
    @staticmethod
    def LoadUrl(url: str):
        '''Load url in the main frame.

        If the url is a local path it needs to start with the file:// prefix.
        
        If the url contains special characters it may need proper handling.
        
        Starting with v66.1+ it is required for the app code to encode the url properly.
        
        You can use the pathlib.PurePath.as_uri in Python 3 or urllib.pathname2url in Python 2
        (urllib.request.pathname2url in Python 3) depending on your case.
        '''
    
    
    @staticmethod
    def Navigate(url: str):
        '''This is an alias for the LoadUrl method.
        '''
    
    
    @staticmethod
    def NotifyMoveOrResizeStarted():
        '''Notify the browser of move or resize events so that popup widgets (e.g. <select>)
        are displayed in the correct location and dismissed when the window moves.
        
        Also so that drag&drop areas are updated accordingly.
        
        In upstream cefclient this method is being called only on Linux and Windows.
        '''
    
    
    @staticmethod
    def NotifyScreenInfoChanged():
        '''Send a notification to the browser that the screen info has changed.
        
        The browser will then call RenderHandler.GetScreenInfo() to update
        the screen information with the new values.
        
        This simulates moving the webview window from one display to another,
        or changing the properties of the current display.
        
        This method is only used when window rendering is disabled.
        '''
    
    
    @staticmethod
    def ParentWindowWillClose():
        '''This method does nothing. Kept for BC.
        '''
    
    
    @staticmethod
    def Print():
        '''Print the current browser contents.
        '''
    
    
    @staticmethod
    def Reload():
        '''Reload the current page.
        '''
    
    
    @staticmethod
    def ReloadIgnoreCache():
        '''Reload the current page ignoring any cached data.
        '''
    
    
    @staticmethod
    def ReplaceMisspelling(word: str):
        '''If a misspelled word is currently selected in an editable node calling
        this method will replace it with the specified |word|.
        '''
    
    
    @staticmethod
    def SetAutoResizeEnabled(enabled: bool, min_size: list[int, int], max_size: list[int, int]):
        '''Description from upstream CEF:
        
        Enable notifications of auto resize via CefDisplayHandler::OnAutoResize.
        
        Notifications are disabled by default.
        
        |min_size| and |max_size| define the range of allowed sizes.
        '''
    
    
    @staticmethod
    def SetBounds(x: int, y: int, width: int, height: int):
        '''Linux-only.
        
        Set window bounds.
        '''
    
    
    @staticmethod
    def SendKeyEvent(event: dict):
        '''KeyEvent is a dictionary,
        see KeyboardHandler.OnPreKeyEvent() for a description of the available keys.
        
        https://github.com/cztomczak/cefpython/blob/master/api/KeyboardHandler.md
        '''
    
    
    @staticmethod
    def SendMouseClickEvent(x: int, y: int, mouseButtonType: int, mouseUp: bool, clickCount: int, modifiers: int):
        '''Send a mouse click event to the browser.
        
        The |x| and |y| coordinates are relative to the upper-left corner of the view.

        mouseButtonType may be one of:
        - cefpython.MOUSEBUTTON_LEFT
        - cefpython.MOUSEBUTTON_MIDDLE
        - cefpython.MOUSEBUTTON_RIGHT

        Modifiers flags:
        - EVENTFLAG_NONE
        - EVENTFLAG_CAPS_LOCK_ON
        - EVENTFLAG_SHIFT_DOWN
        - EVENTFLAG_CONTROL_DOWN
        - EVENTFLAG_ALT_DOWN
        - EVENTFLAG_LEFT_MOUSE_BUTTON
        - EVENTFLAG_MIDDLE_MOUSE_BUTTON
        - EVENTFLAG_RIGHT_MOUSE_BUTTON
        - EVENTFLAG_COMMAND_DOWN (Mac)
        - EVENTFLAG_NUM_LOCK_ON (Mac)
        - EVENTFLAG_IS_KEY_PAD (Mac)
        - EVENTFLAG_IS_LEFT (Mac)
        - EVENTFLAG_IS_RIGHT (Mac)
        '''
    
    
    @staticmethod
    def SendMouseMoveEvent(x: int, y: int, mouseLeave: bool, modifiers: int):
        '''Send a mouse move event to the browser.
        
        The |x| and |y| coordinates are relative to the upper-left corner of the view.
        
        Modifiers flags:
        - EVENTFLAG_NONE
        - EVENTFLAG_CAPS_LOCK_ON
        - EVENTFLAG_SHIFT_DOWN
        - EVENTFLAG_CONTROL_DOWN
        - EVENTFLAG_ALT_DOWN
        - EVENTFLAG_LEFT_MOUSE_BUTTON
        - EVENTFLAG_MIDDLE_MOUSE_BUTTON
        - EVENTFLAG_RIGHT_MOUSE_BUTTON
        - EVENTFLAG_COMMAND_DOWN (Mac)
        - EVENTFLAG_NUM_LOCK_ON (Mac)
        - EVENTFLAG_IS_KEY_PAD (Mac)
        - EVENTFLAG_IS_LEFT (Mac)
        - EVENTFLAG_IS_RIGHT (Mac)
        '''
    
    
    @staticmethod
    def SendMouseWheelEvent(x: int, y: int, deltaX: int, deltaY: int, modifiers: int):
        '''Send a mouse wheel event to the browser.
        
        The |x| and |y| coordinates are relative to the upper-left corner of the view.
        
        The |deltaX| and |deltaY| values represent the movement delta
        in the X and Y directions respectively.
        
        In order to scroll inside select popups with window rendering disabled
        RenderHandler.GetScreenPoint() should be implemented properly.
        
        Modifiers flags:
        - EVENTFLAG_NONE
        - EVENTFLAG_CAPS_LOCK_ON
        - EVENTFLAG_SHIFT_DOWN
        - EVENTFLAG_CONTROL_DOWN
        - EVENTFLAG_ALT_DOWN
        - EVENTFLAG_LEFT_MOUSE_BUTTON
        - EVENTFLAG_MIDDLE_MOUSE_BUTTON
        - EVENTFLAG_RIGHT_MOUSE_BUTTON
        - EVENTFLAG_COMMAND_DOWN (Mac)
        - EVENTFLAG_NUM_LOCK_ON (Mac)
        - EVENTFLAG_IS_KEY_PAD (Mac)
        - EVENTFLAG_IS_LEFT (Mac)
        - EVENTFLAG_IS_RIGHT (Mac)
        '''
    
    
    @staticmethod
    def SendFocusEvent(setFocus: bool):
        '''Send a focus event to the browser.
        '''
    
    
    @staticmethod
    def SendCaptureLostEvent():
        '''Send a capture lost event to the browser.
        '''
    
    
    class cef_state_t:
        '''cef_state_t enum values defined in cefpython module:
        - STATE_DEFAULT
        - STATE_ENABLED
        - STATE_DISABLED
        '''
    
    
    @staticmethod
    def SetAccessibilityState(state: cef_state_t):
        '''Description from upstream CEF:
        
        Set accessibility state for all frames.
        
        |accessibility_state| may be default, enabled or disabled.
        
        If |accessibility_state| is STATE_DEFAULT then accessibility will be disabled
        by default and the state may be further controlled
        with the "force-renderer-accessibility"
        and "disable-renderer-accessibility" command-line switches.
        
        If |accessibility_state| is STATE_ENABLED then accessibility will be enabled.
        
        If |accessibility_state| is STATE_DISABLED then accessibility will be completely disabled.

        For windowed browsers accessibility will be enabled in Complete mode
        (which corresponds to kAccessibilityModeComplete in Chromium).
        
        In this mode all platform accessibility objects will be created
        and managed by Chromium's internal implementation.
        
        The client needs only to detect the screen reader and call this method appropriately.
        
        For example, on macOS the client can handle the @"AXEnhancedUserInterface" accessibility
        attribute to detect VoiceOver state changes and on Windows
        the client can handle WM_GETOBJECT with OBJID_CLIENT to detect accessibility readers.

        For windowless browsers accessibility will be enabled in TreeOnly mode
        (which corresponds to kAccessibilityModeWebContentsOnly in Chromium).
        
        In this mode renderer accessibility is enabled, the full tree is computed,
        and events are passed to CefAccessibiltyHandler,
        but platform accessibility objects are not created.
        
        The client may implement platform accessibility objects
        using CefAccessibiltyHandler callbacks if desired.
        
        cef_state_t enum values defined in cefpython module:
        - STATE_DEFAULT
        - STATE_ENABLED
        - STATE_DISABLED
        '''
    
    
    @staticmethod
    def SetClientCallback(name: str, callback: Callable):
        '''Set client callback.
        '''
    
    
    @staticmethod
    def SetClientHandler(clientHandler: Any):
        '''Set client handler object (class instance), its members will be inspected.
        
        Private methods that are not meant to be callbacks
        should have their names prepended with an underscore.

        You can call this method multiple times with to set many handlers.
        
        For example you can create in your code several objects named LoadHandler,
        LifespanHandler etc.
        '''
    
    
    @staticmethod
    def SetFocus(focus: bool):
        '''Set whether the browser is focused.
        '''
    
    
    @staticmethod
    def SetMouseCursorChangeDisabled(disabled: bool):
        '''Set whether mouse cursor change is disabled.
        '''
    
    
    @staticmethod
    def SetJavascriptBindings(bindings: JavascriptBindings):
        '''Set javascript bindings.
        '''
    
    
    @staticmethod
    def SetUserData(key: Any, value: Any):
        '''Set user data.
        
        Use this function to keep data associated with this browser.
        
        See also GetUserData().
        '''
    
    
    @staticmethod
    def SetZoomLevel():
        '''Change the zoom level to the specified value.
        
        Specify 0.0 to reset the zoom level.
        
        If called on the UI thread the change will be applied immediately.
        
        Otherwise, the change will be applied asynchronously on the UI thread.
        '''
    
    
    @staticmethod
    def ShowDevTools():
        '''Open developer tools (DevTools) in its own browser.
        
        The DevTools browser will remain associated with this browser.
        
        If the DevTools browser is already open then it will be focused,
        in which case the |windowInfo|, |client| and |settings| parameters will be ignored.
        
        If |inspect_element_at| is non-empty then the element
        at the specified (x,y) location will be inspected.
        
        The |windowInfo| parameter will be ignored if this browser is wrapped in a CefBrowserView.
        '''
    
    
    @staticmethod
    def StartDownload(url: str):
        '''Download the file at |url| using DownloadHandler.
        
        https://github.com/cztomczak/cefpython/blob/master/api/DownloadHandler.md
        '''
    
    
    @staticmethod
    def StopLoad():
        '''Stop loading the page.
        '''
    
    
    @staticmethod
    def StopFinding(clearSelection: bool):
        '''Cancel all searches that are currently going on.
        '''
    
    
    @staticmethod
    def ToggleFullscreen():
        '''Switch between fullscreen mode / windowed mode.
        
        To check whether in fullscreen mode call IsFullscreen().

        This function is Windows-only.
        '''
    
    
    @staticmethod
    def TryCloseBrowser() -> bool:
        '''Helper for closing a browser.
        
        Call this method from the top-level window close handler.
        
        Internally this calls CloseBrowser(false) if the close has not yet been initiated.
        
        This method returns false while the close is pending
        and true after the close has completed.
        
        See CloseBrowser() and CefLifeSpanHandler::DoClose() documentation
        for additional usage information.
        
        This method must be called on the browser process UI thread.
        '''
    
    
    @staticmethod
    def WasResized():
        '''Notify the browser that the widget has been resized.
        
        The browser will first call RenderHandler::GetViewRect
        to get the new size and then call RenderHandler::OnPaint asynchronously
        with the updated regions.
        
        This method is only used when window rendering is disabled.
        '''
    
    
    @staticmethod
    def WasHidden(hidden: bool):
        '''Notify the browser that it has been hidden or shown.
        
        Layouting and RenderHandler::OnPaint notification will stop when the browser is hidden.
        
        This method is only used when window rendering is disabled.
        '''


class cef:
    # https://github.com/cztomczak/cefpython/blob/master/api/cefpython.md#cefpython
    
    
    __all__ = ["cefpython"]
    __version__ = cefpython.__version__
    __author__ = "The CEF Python authors"
    
    
    class WindowInfo:
        # https://github.com/cztomczak/cefpython/blob/master/api/WindowInfo.md
        
        
        __window_info__ = None
        
        
        @staticmethod
        def __init__():
            # From the cefpython doc:
            #   To instantiate this class call cefpython.WindowInfo().
            cef.WindowInfo.__window_info__ = cefpython.WindowInfo()
        
        
        @staticmethod
        def SetAsChild(parentWindowHandle: int, windowRect: list = None):
            '''Create the browser as a child window/view.
            
            - windowRect example value (int32..): [left, top, right, bottom].

            Args:
                parentWindowHandle (int): Parent window handle.
                windowRect (list, optional): [description].
            '''
            
            cef.WindowInfo.__window_info__.SetAsChild(parentWindowHandle, windowRect)


        @staticmethod
        def SetAsPopup(parentWindowHandle: int, windowName: str):
            '''[Available only on Windows] Create the browser as a popup window.

            Args:
                parentWindowHandle (int): Parent window handle.
                windowName (str): Name of the window.
            '''
            
            cef.WindowInfo.__window_info__.SetAsPopup(parentWindowHandle, windowName)


        @staticmethod
        def SetAsOffscreen(parentWindowHandle: int):
            '''Description from upstream CEF:
            
            Create the browser using windowless (off-screen) rendering.
            
            No window will be created for the browser and all rendering
            will occur via the CefRenderHandler interface.
            
            The |parent| value will be used to identify monitor info and to act
            as the parent window for dialogs, context menus, etc.
            
            If |parent| is not provided then the main screen monitor
            will be used and some functionality that requires
            a parent window may not function correctly.
            
            In order to create windowless browsers the CefSettings.windowless_rendering_enabled
            valuemust be set to true.
            
            Transparent painting is enabled by default but can be disabled by setting
            CefBrowserSettings.background_color to an opaque value.
            
            Call this method to disable windowed rendering and to use RenderHandler.
            See the pysdl2, screenshot, panda3d and kivy examples.

            In order to create windowless browsers the ApplicationSettings.windowless_rendering_enabled
            value must be set to true.

            You can pass 0 as parentWindowHandle, but then some things
            like context menus and plugins may not display correctly.
            
            Args:
                parentWindowHandle (int): Parent window handle.
            '''
            
            cef.WindowInfo.__window_info__.SetAsOffscreen(parentWindowHandle)


    class JavascriptBindings:
        # https://github.com/cztomczak/cefpython/blob/master/api/JavascriptBindings.md
        
        
        __javascript_bindings__ = None
        
        
        @staticmethod
        def __init__(bindToFrames: bool = False, bindToPopups: bool = False):
            '''By default we bind only to top frame.

            bindToFrames option - whether bindings are accessible inside iframes and frameset.

            bindToPopups option - whether bindings are accessible from popups.
            '''
            
            cef.JavascriptBindings.__javascript_bindings__ = cefpython.JavascriptBindings(bindToFrames, bindToPopups)


        @staticmethod
        def IsValueAllowed(value: Any):
            '''Whether you are allowed to bind this value to javascript, value may be one of:
            - list
            - bool
            - float
            - int
            - long
            - None (null in js)
            - dict (object in js)
            - string
            - unicode
            - tuple
            - function
            - instancemethod (an object's method)
            
            If long value is outside of int32 limits (-2147483647..2147483647)
            then it will be converted to string in javascript
            (it should really be -2147483648, but then Cython complains about it).
            '''
            
            cef.JavascriptBindings.__javascript_bindings__.IsValueAllowed(value)


        @staticmethod
        def Rebind():
            '''Call this to rebind javascript bindings.
            
            This is useful when using reload() on python's module,
            you can make changes to application and see it instantly
            without having to re-launch application.
            
            After you reload() module set all the bindings again using
            SetFunction/SetObject/SetProperty methods, then call Rebind() to rebind it to javascript.
            
            See Issue #12 (reload_example.zip) for an example.

            There is an another way of doing rebinding, you can call Frame.SetProperty(),
            but this is not best performant way as it creates a C++ class V8FunctionHandler
            for each function, when doing Rebind() there is only one such class created.
            
            Frame.SetProperty() is also more limited, you cannot bind objects using it,
            though it could be supported, I'm wondering whether there is a need for that,
            it would allow to pass objects as arguments to javascript callbacks so maybe
            it will be implemented in the future. Also Rebind() does bindings to frames
            and popups automatically according to bindToFrames and bindToPopups constructor options,
            while using Frame.SetProperty() you would need to take care of that by yourself.

            Rebind does not solve all scenarios, take for example: what happens if you pass
            a python callback to javascript and then do rebindings?
            You still get old function referenced in javascript.
            '''
            
            cef.JavascriptBindings.__javascript_bindings__.Rebind()


        @staticmethod
        def SetFunction(name: str, func: Callable):
            '''This function will be binded to window object in html, you can call it in two ways:
            
                ```
                window.myfunc()
                    myfunc() # window properties are global
                ```
                
                You can use SetFunction() to overwrite native javascript function,
                for example if you would like to implement your own version of "window.alert" do this:
                
                ```
                def PyAlert(msg):
                    win32gui.MessageBox(__browser.GetWindowID(), msg, "PyAlert()", win32con.MB_ICONQUESTION)
                    bindings = cefpython.JavascriptBindings(bindToFrames=True, bindToPopups=True)
                    bindings.SetFunction("alert", PyAlert)
                ```
                
                This function is dummy, it really calls SetProperty(),
                you might use it as well to bind functions.
            '''
            
            cef.JavascriptBindings.__javascript_bindings__.SetFunction(name, func)
            

        @staticmethod
        def SetObject(name: str, obj):
            '''Currently this function binds only methods of an object. Example:
            
            ### In python:
                - bindings.SetObject("myobject", myobject)
                
            ### In javasript:
                - window.myobject.someMethod();
                - myobject.someMethod();
            
            Currently when binding object only methods are binded,
            I decided not to bind properties of the object,
            as they would be binded by copying value and this might be confusing,
            as accessing object's property from javascript might give a different value during runtime
            then the real value when getting the property from python runtime. Only object's methods
            and functions can be binded by reference.
            
            Still you can bind object's properties if you like,
            you can find useful method IsValueAllowed() to check which properties can be binded,
            of course doing it this way will not allow you to access properties
            through "window.myobject.property", you can only bind to the "window" object
            so you should imitate some kind of namespace, so that accessing property would be through
            "window.myobject_property" or "myobject_property" as window prefix is always optional.
            
            Use dir() function to list object's properties.
            
            https://github.com/cztomczak/cefpython/blob/master/api/JavascriptBindings.md#setobject
            '''
            
            cef.JavascriptBindings.__javascript_bindings__.SetObject(name, obj)
            
            
        @staticmethod
        def SetProperty(name: str, value: Any):
            '''Set some value to property of the window object in html.
            
            This propertiy for example can hold configuration options
            or some other data required at startup of your application.

            Mixed type is one that can be converted to javascript types,
            see IsValueAllowed() for a full list.

            To get the value during runtime (as it might been changed via javascript)
            call Frame.GetProperty().

            This function copies the values and converts them to V8 Javascript values
            (the only exception are functions and methods), if you pass a Dictionary don't expect
            that if you change it later and then call Frame.GetProperty
            that you will get the modified value.
            '''
            
            cef.JavascriptBindings.__javascript_bindings__.SetProperty(name, value)

    
    @staticmethod
    def CreateBrowser(
        window_info: WindowInfo = None,
        browser_settings: dict = {},
        url: str = None,
        window_title: str = None
    ) -> Browser:
        '''Not yet implemented - currently this method just calls CreateBrowserSync.
        
        In upstream CEF this method creates browser asynchronously.
        
        Currently CEF Python depends on browser being created synchronously in a few parts of code.

        Create a new browser window using the window parameters specified by |windowInfo|.
        
        All values will be copied internally and the actual window
        will be created on the UI thread.
        
        If |request_context| is empty the global request context will be used.
        
        This method can be called on any browser process thread and will not block.

        Args:
            window_info (WindowInfo, optional): Info of the window (WindowInfo class).
            browser_settings (dict, optional): BrowserSettings dict.
            url (str, optional): File / Website url.
            window_title (str, optional): Title of the window (if parent window window_info = 0).
            
        Return:
            Browser: Browser object.
        '''
        
        return cef.CreateBrowserSync(window_info, browser_settings, url, window_title)
    
    
    @staticmethod
    def CreateBrowserSync(
        window_info: WindowInfo = None,
        browser_settings: dict = {},
        url: str = None,
        window_title: str = None
    ) -> Browser:
        '''Create a new browser window using the window parameters specified by |windowInfo|.
        
        If |request_context| is empty the global request context will be used.
        
        This method can only be called on the browser process UI thread.

        Args:
            window_info (WindowInfo, optional): Info of the window (WindowInfo class).
            browser_settings (dict, optional): BrowserSettings dict.
            url (str, optional): File / Website url.
            window_title (str, optional): Title of the window (if parent window window_info = 0).
            
        Return:
            Browser: Browser object.
        '''
        
        return cefpython.CreateBrowserSync(window_info, browser_settings, url, window_title)


    @staticmethod
    def ExceptHook(exc_type: Any = None, exc_value: Any = None, exc_trace: Any = None):
        '''Global except hook to exit app cleanly on error.
        
        This hook does the following: in case of exception write it to
        the "error.log" file, display it to the console, shutdown CEF
        and exit application immediately by ignoring "finally" (_exit()).
        
        Args:
            (exc_type, exc_value, exc_trace): (Any, optional) Using traceback.format_exception().
        '''
        
        cefpython.ExceptHook(exc_type, exc_value, exc_trace)
    
    
    @staticmethod
    def GetAppSetting(key: str) -> Any:
        '''Returns ApplicationSettings option that was passed to Initialize().
        
        Returns None if key is not found.

        Args:
            key (str): Key inside ApplicationSettings.
        
        Return:
            Any
        '''
        
        return cefpython.GetAppSetting(key)
    
    
    @staticmethod
    def GetAppPath(file: str = None) -> str:
        '''Get path to where application resides.

        Args:
            file (str): Path of the file.

        Returns:
            str: Path of the application.
        '''
        
        return cefpython.GetAppPath(file)
    
    
    @staticmethod
    def GetBrowserByIdentifier(identifier: int):
        '''Get browser by identifier.
        
        Browser identifier can be obtained by calling Browser.GetIdentifier

        Args:
            identifier (int): Identifier of the browser.
        '''
        
        cefpython.GetBrowserByIdentifier(identifier)
    
    
    @staticmethod
    def GetBrowserByWindowHandle(windowHandle: int):
        '''Get browser by outer or inner window handle.
        
        An outer window handle is the one that was passed to CreateBrowserSync().
        
        An inner window handle is a CEF internal window handle.

        Args:
            windowHandle (int): Windowhandle data (int or long type).
        '''
        
        cefpython.GetBrowserByWindowHandle(windowHandle)
    
    
    @staticmethod
    def GetCommandLineSwitch(key: str) -> Any:
        '''Returns the CommandLineSwitches switch that was passed to Initialize().

        Args:
            key (str): Key inside GetCommandLineSwitch.
        
        Return:
            Any
        '''
        
        return cefpython.GetCommandLineSwitch(key)
    
    
    @staticmethod
    def GetDataUrl(data: str, mediatype: str = 'html') -> dict:
        '''Convert data to a Data URL.

        See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs

        Args:
            data (str): Data that needs to be converted.
            mediatype (str, optional): Only 'html' media type is currently supported.

        Returns:
            dict: Data URL.
        '''
        
        return cefpython.GetDataUrl(data, mediatype)
    
    
    @staticmethod
    def GetGlobalClientCallback(name: str) -> Any:
        '''Returns a global client callback that was set using SetGlobalClientCallback()
        or SetGlobalClientHandler.
        
        Returns None if callback was not set.

        Args:
            name (str): Name of the callback.

        Returns:
            Any
        '''
        
        return cefpython.GetGlobalClientCallback(name)
    
    
    @staticmethod
    def GetModuleDirectory() -> str:
        '''Get the cefpython module directory.
        
        This method is useful to get full path to CEF binaries.
        
        This is required when setting ApplicationSettings options like: 'browser_subprocess_path',
        'resources_dir_pat' and 'locales_dir_path'.

        Returns:
            str: Cefpython module directory.
        '''
        
        return cefpython.GetModuleDirectory()
    
    
    @staticmethod
    def GetVersion() -> dict:
        '''Return CEF Python and CEF versions dictionary with keys:
        - version
        - chrome_version
        - cef_version
        - cef_api_hash_platform
        - cef_api_hash_universal
        - cef_commit_hash
        - cef_commit_number
        
        Returns:
            dict: CEF Python / CEF versions.
        '''
        
        return cefpython.GetVersion()
    
    
    @staticmethod
    def Initialize(settings: dict = {}, switches: dict = {}) -> bool:
        '''This function should be called on the main application thread (UI thread)
        to initialize CEF when the application is started.
        
        A call to Initialize() must have a corresponding call to Shutdown()
        so that CEF exits cleanly.
        
        Otherwise when application closes data (eg. storage, cookies)
        might not be saved to disk or the process might freeze (experienced on Windows XP).

        Args:
            settings (dict, optional): ApplicationSettings.
            switches (dict, optional): CommandLineSwitches.

        Returns:
            bool: Initalized correctly.
        '''
    
        return cefpython.Initialize(settings, switches)
    
    
    @staticmethod
    def IsThread(threadID: int) -> bool:
        '''CEF maintains multiple internal threads that are used
        for handling different types of tasks.
        
        The UI thread creates the browser window and is used for all interaction
        with the webkit rendering engine and V8 Javascript engine.
        
        The UI thread will be the same as the main application thread
        if CefInitialize() is called with an ApplicationSettings
        'multi_threaded_message_loop' option set to false.
        
        The IO thread is used for handling schema and network requests.
        
        The FILE thread is used for the application cache and other miscellaneous activities.
        
        See PostTask() for a list of threads.

        Args:
            threadID (int): ID of the thread.

        Returns:
            bool: Returns true if called on the specified thread.
        '''
        
        return cefpython.IsThread(threadID)
    
    
    @staticmethod
    def LoadCrlSetsFile(path: bytes) -> bool:
        '''Description from upstream CEF:
        
        Loads the existing "Certificate Revocation Lists" file that is managed by Google Chrome.
        
        This file can generally be found in Chrome's User Data directory
        (e.g. "C:/Users[User]/AppData/Local/Google/Chrome/User Data" on Windows)
        and is updated periodically by Chrome's component updater service.
        
        Must be called in the browser process after the context has been initialized.
        
        See https://dev.chromium.org/Home/chromium-security/crlsets for background.

        Args:
            path (bytes): "Certificate Revocation Lists" file path.

        Returns:
            bool: File found and loaded correctly.
        '''
        
        return cefpython.LoadCrlSetsFile(path)
    
    
    @staticmethod
    def MessageLoop():
        '''Run the CEF message loop.
        Use this function instead of an application- provided message loop to get the best balance
        between performance and CPU usage.
        
        This function should only be called on the main application thread (UI thread)
        and only if cefpython.Initialize() is called
        with a ApplicationSettings.multi_threaded_message_loop value of false.
        
        This function will block until a quit message is received by the system.

        See also MessageLoopWork().
        '''
        
        cefpython.MessageLoop()
    
    
    @staticmethod
    def MessageLoopWork():
        '''Call this function in a periodic timer (eg. 10ms).
        
        Description from upstream CEF:
        
        Perform a single iteration of CEF message loop processing.
        
        This function is provided for cases where the CEF message loop must be integrated
        into an existing application message loop.
        
        Use of this function is not recommended
        for most users; use either the CefRunMessageLoop() function
        or CefSettings.multi_threaded_message_loop if possible.
        
        When using this function care must be taken to balance performance
        against excessive CPU usage.
        
        It is recommended to enable the CefSettings.external_message_pump option
        when using this function so that CefBrowserProcessHandler::OnScheduleMessagePumpWork()
        callbacks can facilitate the scheduling process.
        
        This function should only be called on the main application thread
        and only if CefInitialize() is called
        with a CefSettings.multi_threaded_message_loop value of false.
        
        This function will not block.
        '''
        
        cefpython.MessageLoopWork()
        
    
    
    @staticmethod
    def PostTask(thread: int, func: Callable, args: list[Any]):
        '''Post a task for execution on the thread associated with this task runner.
        
        Execution will occur asynchronously.
        
        Only Browser process threads are allowed.

        List of threads in the Browser process:

        - cef.TID_UI: The main thread in the browser. This will be the same as the main application
            thread if cefpython.Initialize() is called
            with a ApplicationSettings.multi_threaded_message_loop value of false.
            Do not perform blocking tasks on this thread.
            All tasks posted after CefBrowserProcessHandler::OnContextInitialized()
            and before CefShutdown() are guaranteed to run.
            This thread will outlive all other CEF threads.
            
        - cef.TID_FILE (alias cef.TID_FILE_BACKGROUND): Used for blocking tasks
            (e.g. file system access) where the user won't notice if the task takes
            an arbitrarily long time to complete. All tasks posted after
            CefBrowserProcessHandler::OnContextInitialized()
            and before CefShutdown() are guaranteed to run.
            
        - cef.TID_FILE_USER_VISIBLE: Used for blocking tasks (e.g. file system access)
            that affect UI or responsiveness of future user interactions.
            Do not use if an immediate response to a user interaction is expected.
            All tasks posted after CefBrowserProcessHandler::OnContextInitialized()
            and before CefShutdown() are guaranteed to run. Examples:
                - Updating the UI to reflect progress on a long task.
                - Loading data that might be shown in the UI after a future user interaction.
                
        - cef.TID_FILE_USER_BLOCKING: Used for blocking tasks (e.g. file system access)
            that affect UI immediately after a user interaction.
            All tasks posted after CefBrowserProcessHandler::OnContextInitialized()
            and before CefShutdown() are guaranteed to run.
            Example: Generating data shown in the UI immediately after a click.
            
        - cef.TID_IO: Used to process IPC and network messages.
            Do not perform blocking tasks on this thread.
            All tasks posted after CefBrowserProcessHandler::OnContextInitialized()
            and before CefShutdown() are guaranteed to run.
        
        List of threads in the Renderer process:

        - cef.TID_RENDERER: Tasks may be posted to this thread after
            CefRenderProcessHandler::OnRenderThreadCreated but are not guaranteed to run before
            sub-process termination (sub-processes may be killed at any time without warning).

        Args:
            thread (int): Thread where the task is posted for execution (Use cef.TID_UI etc..).
            func (Callable): Function of the task.
            args (list[Any]): Function args.
        '''
        
        cefpython.PostTask(thread, func, args)
    
    
    @staticmethod
    def PostDelayedTask(thread: int, delay_ms: int, func: Callable, args: list[Any]):
        '''Post a task for delayed execution on the specified thread.
        
        This function behaves similarly to PostTask above,
        but with an additional |delay_ms| argument.
        
        Check PostTask() docstring for more details.

        Args:
            thread (int): Thread where the task is posted for execution (Use cef.TID_UI etc..).
            delay_ms (int): Delay in ms before task execution.
            func (Callable): Function of the task.
            args (list[Any]): Function args.
        '''
        
        cefpython.PostDelayedTask(thread, delay_ms, func, args)
    
    
    @staticmethod
    def QuitMessageLoop():
        '''Quit the CEF message loop that was started by calling cefpython.MessageLoop().
        
        This function should only be called on the main application thread (UI thread)
        and only if cefpython.MessageLoop() was used.
        '''
        
        cefpython.QuitMessageLoop()
        
    
    @staticmethod
    def SetGlobalClientCallback(name: str, callback: Callable):
        '''Current CEF Python implementation is limited in handling callbacks
        that occur during browser creation, in such cases a callback set
        with Browser.SetClientCallback() or Browser.SetClientHandler() won't work,
        as this methods can be called only after browser was created.
        
        An example of such callback is LifespanHandler.OnAfterCreated().

        Some client callbacks are not associated with any browser.
        
        In such case use this function instead of the SetClientCallback()
        and SetClientHandler() Browser methods.
        
        An example of such callback is OnCertificateError() in RequestHandler.

        Example of using SetGlobalClientCallback() is provided in the wxpython.py example.

        Args:
            name (str): Name of the callback.
            callback (Callable): Callback function reference.
        '''
        
        cefpython.SetGlobalClientCallback(name, callback)
    
    
    @staticmethod
    def SetGlobalClientHandler(handler: Any):
        '''Set client handler object (class instance).
        
        Its members will be inspected.
        
        Private methods that are not meant to be callbacks should have their names prepended
        with two underscores.
        
        Methods with single underscore
        or no underscore are treated the same as client callbacks.

        You can call this method multiple times to set many handlers.
        
        For example you can create in your code several objects
        named AccessibilityHandler, RequestHandler etc.
        
        Args:
            handler (Any): Client handler object.
        '''
        
        cefpython.SetGlobalClientHandler(handler)
        
    
    @staticmethod
    def SetOsModalLoop(modalLoop: bool):
        '''Set to true before calling Windows APIs like 'TrackPopupMenu'
        that enter a modal message loop.
        
        Set to false after exiting the modal message loop.
        
        Args:
            modalLoop (bool): Modal message loop state.
        '''
    
        cefpython.SetOsModalLoop(modalLoop)
        
    
    @staticmethod
    def Shutdown():
        '''This function should be called on the main application thread (UI thread)
        to shut down CEF before the application exits.
        You must call this function so that CEF shuts down cleanly.
        
        Remember also to delete all CEF browsers references for the browsers to shut down cleanly.
        
        For an example see the wxpython.py example MainFrame.OnClose().
        '''

        cefpython.Shutdown()
