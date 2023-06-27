# """
# this is an example how to implement the callback feature in winotify
# """
# import os.path
# import random
# import string
# import time
# import sys

# import winotify

# # instantiate Notifier and Registry class
# app_id = "winotify test"
# app_path = os.path.abspath(__file__)

# r = winotify.Registry(app_id, winotify.PY_EXE, app_path, force_override=True)
# notifier = winotify.Notifier(r)


# @notifier.register_callback
# def do_somethin():
#     print('yo hey')
#     for x in range(3, 0, -1):
#         print(f"toast in {x} secs")
#         time.sleep(1)

#     toast = notifier.create_notification("a new notification", "this is called from another thread",
#                                          launch=quit_)
#     toast.add_actions("Clear all")
#     toast.show()


# @notifier.register_callback(run_in_main_thread=True)  # register quit func
# def quit_():
#     # this wont work if called from another thread
#     print('YESSSSSS')
#     sys.exit()


# @notifier.register_callback
# def spam():
#     for i in range(3):
#         rand = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # random toast body
#         t = notifier.create_notification(f"spam motification {i}", rand)
#         t.add_actions("clear all", clear)
#         # t.add_actions("sys.exit", notifier.callback_to_url(sys.exit))
#         t.show()
#         time.sleep(1)

# def main():
#     # no need to specify app_id every time
#     toast = notifier.create_notification("a notification", 'a notification test with callback',
#                                          launch=do_somethin)
#     # generic url still works
#     toast.add_actions("Open Github", "https://github.com/versa-syahptr/winotify")
#     toast.add_actions("Quit app", quit_)
#     toast.add_actions("spam", spam)
#     toast.show()

#     print(toast.script)


# @notifier.register_callback
# def clear(): notifier.clear()


# if __name__ == '__main__':
#     notifier.start()
#     main()

#     while True:
#         notifier.update()
#         time.sleep(1)
#         print("i'm running")

import win32clipboard as cb
CLIPBOARD_CONTENT = None
couldBeScreenshot = False

cb.OpenClipboard()
CLIPBOARD_HAS_FILE_HANDLER = cb.IsClipboardFormatAvailable(cb.CF_HDROP)
if cb.IsClipboardFormatAvailable(cb.CF_HDROP):
    CLIPBOARD_CONTENT = cb.GetClipboardData(cb.CF_HDROP)
    CLIPBOARD_HAS_FILE_HANDLER = True
else:
    # tuple to allow for multiple items
    try:
        CLIPBOARD_CONTENT = (cb.GetClipboardData(), )
    except TypeError:
        CLIPBOARD_CONTENT = None
        couldBeScreenshot = True
cb.CloseClipboard()

if couldBeScreenshot:
    # screenshots copied to clipboard cause this exception
    # grab the screenshow with Pillow, save to file and return the file handler
    from PIL import ImageGrab
    tempSc = r"C:\Users\omnic\local\temp\screenshot.png"
    img = ImageGrab.grabclipboard()
    print(img)
    img.save(tempSc)
    CLIPBOARD_CONTENT = (tempSc, )

print(CLIPBOARD_CONTENT)