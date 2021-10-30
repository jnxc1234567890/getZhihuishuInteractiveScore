from PIL.Image import Image
import pyautogui as pag
from PIL import ImageChops
from bs4 import BeautifulSoup
import pyperclip

__sizex__, __sizey__ = pag.size()
DeltaY1 = 80
DeltaY2 = 120

def findLink(divider_filename):
    pos = list(pag.locateAllOnScreen(divider_filename))
    center = pag.center(pos[1])
    pag.moveTo(center.x,center.y,duration=0.2)
    pag.sleep(0.3)
    im1 = pag.screenshot()
    pag.moveTo(center.x,center.y-DeltaY1,duration=0.2)
    pag.sleep(0.3)
    im2 = pag.screenshot()
    if Image.getbbox(ImageChops.difference(im1,im2)) == None:
        pag.moveTo(center.x,center.y-DeltaY2)
    pag.click()

def savePage():
    with pag.hold('ctrl'):
        pag.press('s')
    pag.sleep(1)
    pag.press('enter')
    pag.sleep(0.1)
    pag.press('left')
    pag.sleep(0.1)
    pag.press('enter')

def getAnswer():
    soup=BeautifulSoup(open("课程问答_智慧树.html",encoding = "utf-8"),features='lxml')
    div_ans = soup.find('div', class_='answer-content')
    return list(div_ans.p.span.stripped_strings)[0]

def submitAnswer(answer):
    center = pag.locateCenterOnScreen("Submit.png",confidence=0.9)
    if center == None:
        return
    pag.moveTo(*center, duration=0.1)
    pag.click()
    pag.press('tab')
    pag.sleep(0.1)
    pag.press('F12')
    pag.sleep(0.2)
    for chr in answer[::-1]:
        pyperclip.copy("document.querySelector(\"textarea\").setRangeText('"+chr+"')")
        with pag.hold('ctrl'):
            pag.press('v')
        pag.sleep(0.1)
        pag.press('enter')
        pag.sleep(0.1)
    pag.press('F12')
    pag.press('space')
    pag.press('backspace')
    center = pag.locateCenterOnScreen("FinalSubmit.png",confidence=0.9)
    pag.moveTo(*center, duration=0.1)
    pag.click()
    center = pag.locateCenterOnScreen("Like.png",confidence=0.9)
    pag.moveTo(*center, duration=0.1)
    pag.sleep(1)
    pag.click()
    pag.sleep(1)
    with pag.hold('ctrl'):
        pag.press('w')

if __name__ == '__main__':
    pag.confirm(text="",title="Test Title",buttons=['Begin']);
    N=1;
    try:
        for i in range(N):
            pag.scroll(-300)
            pag.sleep(2)
            findLink("divider.png")
            pag.sleep(2)
            savePage()
            #pag.sleep(30)
            pag.confirm(text="Please wait until download is completed.",title="Downloading",buttons=['Completed']);
            answer = getAnswer()
            print(answer)
            pag.sleep(1)
            submitAnswer(answer)
    except Exception as e:
        print(".{}".format(e))