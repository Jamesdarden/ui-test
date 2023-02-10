import pyautogui
import os
import pywinauto
import time
import shutil
import numpy as np
import cv2
from PIL import Image


### scailing would make the image find not work //DPI setting is on %100 ###

### checkscheduler*data* might be userfull
### scan*data*  scheduled scan
### pcmatic*date  ui or manual scans

### error dictionary to hold errors and will dictate if email is sent
### click all areas one by one
### compare with static image
### if not a match take screen
### save to email folder 
### grab corresponding logfile
### place it in email folder
### place in email folder


### figure out function for email
### figure out function for get log

def copy_file (file_name, todays_date):
    original_dest = f'C:\ProgramData\PCPitstop\{file_name}'
    destination = os.path.join(os.cur, 'screenshots_to_send')
    try:
        if os.path.exists(original_dest):
            shutil.copy(f'{original_dest}', destination)   
    except Exception as e:
        print(e)
        
def mean_calc (img1, img2, stage):
    obj ={}
    obj['min'] = f'{img1.min()} min {img2.min()} '
    obj['max'] = f'{img1.max()} max  {img2.max()}'
    obj['mean']= f'{img1.mean()} mean {img2.mean()}'
    obj['close'] = f'{np.allclose(img1.mean(), img2.mean())}'
 
    print(obj, stage)
    

    
#Function to compare two images
def do_images_match(image1,image2):
    #Read the two images 
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    
    mean_calc(img1 , img2, 'image read')
    
    #Resize the images to same size
    img1 = cv2.resize(img1, (100,100))
    img2 = cv2.resize(img2, (100,100))
    
    mean_calc(img1 , img2, 'image resize')
    
    #Convert both images to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    mean_calc(img1_gray , img2_gray, 'convert gray scale')
    
    print(img1_gray.astype('float'))
    print(img2_gray.astype('float'))
    
    mean_calc(img1_gray , img2_gray, 'after cast 8bit')
    #Calculate the mean square error between the two images
    # err = np.sum((img1_gray.astype('float') - img2_gray.astype('float')) ** 2)
    err = abs(img1_gray.mean() - img2_gray.mean())
    print(type(err))
    if err >= 1:
        print( False, err)
    else:
        print(True, err)
    print(err)
        
        

errorObj = {
    
}



app = pywinauto.application.Application(backend='uia').start('C:\Program Files (x86)\PCMatic\pc matic\pcmatic.exe').connect(title="PC Matic", timeout=5)


time.sleep(5)
# box = app.PCMatic.rectangle()
# print(type(box))
# print(box ,'box')



image_dir = f"{os.getcwd()}\\images\\"
screenshot_to_send_dir = f"{os.getcwd()}\\screenshots_to_send"


# coordinates = get_active_window_coordinates(app)
# print(coordinates)
what_image_should_be = './images/supershield_header.PNG'
image_to_test_for_error = 'supershield_header.png'


    # test = test
    # errorObj['error'] = 'dashboard'
    # image =pyautogui.screenshot()
    # image.save('./screenshots_to_send/dashboard.png')
try:

    # test = pyautogui.locateOnScreen('./images/dashboard.PNG')
  # Locate the image on the screen
    location = pyautogui.locateOnScreen(what_image_should_be,confidence=.9)
    image_size = Image.open(what_image_should_be).size
    # box_loc = Image.open('./images/supershield header.PNG').getbbox()
    print(location, 'location')
    # print(pyautogui.center(location))
    
# Take a screenshot of the image location
    if location is None:
        location =(290,94, image_size[0],image_size[1] -5)
    else:
        location[3] - 5 
    screenshot = pyautogui.screenshot(region=location)
    screenshot.save(image_to_test_for_error)
    # im = Image.open('SS_test.png')
    # im.crop(box=box_loc)
    # im.save('ss_cropeed.png')
 

# # Convert the screenshot to a numpy array for comparison
#     screenshot_np = np.array(screenshot)

# # Read in the reference image as a numpy array
#     reference_image = np.array(cv2.imread('./images/dashboard.PNG'))

# Compare the reference image and the screenshot
    # if np.array_equal(screenshot_np, reference_image):
	#     print(True)
    # else:
    #     print(False)
    do_images_match(image_to_test_for_error, what_image_should_be)
    
  
except Exception as e:
    print(e)
    
# print('done')

# theBody = app.PCMatic.child_window(title="PC Matic", auto_id="thebody", control_type="Pane")

# # theBody.print_control_identifiers()

# ss_button = app.PCMatic.child_window(title="\r\nSuperShield", control_type="Button").wrapper_object()

# ss_button.click_input()

# time.sleep(3)

# theBody.print_control_identifiers()







# def startTest(args):
#     os.system('cmd /c start pcmatic')