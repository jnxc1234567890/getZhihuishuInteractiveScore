# getZhihuishuInteractiveScore
A Python script for automatically participating in Interactive Zone in Zhihuishu

## Requirement
The script requires:

```PIL```,```pyautogui```,```bs4```,```pyperclip```

## General description

The script simulates human behavior by copying others' comments and pasting it, after that, it likes the comment done just now.

The script has many restrictions, be sure to recapture your image of dividers and submission button. And most importantly, the script only works for Windows with Chromium-based browsers. Besides, make sure that your DevTools is set at 'Console' tab.

Another strange thing is that Zhihuishu seems to have a protection system, preventing the users to download their webpage in a high speed, which is why I set a window to wait for the download procedure.