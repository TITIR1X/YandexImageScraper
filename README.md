## Ideal for downloading over 10 million specific images for use in testing and training 😅
___________________________________________________________
## YandexBot_keyword_search.py
This tool allows you to perform a search on Yandex.com using a keyword provided by the user and then downloads a specified number of images resulting from the search. The downloaded images are stored in an HTML file in a folder specified by the user.
___________________________________________________________
## YandexBot_image_recognition.py
This tool allows searching Yandex.com using a list of images provided by the user in the URL_.py file. By default, it downloads 1400 images resulting from each search and stores them in an HTML file in a user-specified folder.
___________________________________________________________
## link_extractor.py
This code allows you to extract image links from HTML files and save them to a text file. First, it goes through a user-specified folder and identifies all HTML files in it. Then, it extracts the image links from each HTML file and saves them to an individual text file with the same name as the original HTML file, but with a ".txt" file extension instead of ".html".
___________________________________________________________
## file_organizer.py
This code is used to group by 50 files from the "YandexBot_image_recognition" or "YandexBot_keyword_search" folder generated by YandexBot into files named "./1/50_src_files.html", "./2/50_src_files.html", "./3/50_src_files.html", and so on. Once the files are created, you can open them one by one and save the page to download the images to your local disk.

**file_organizer.py** can be configured to group 100 files or more (in the variable 'LIMIT=50'), by default it is set to 50.
___________________________________________________________
### To download the images, follow these steps:

1- Open the .html file

2- Right click on the file

3- Select "save page".

4- This will start the automatic download of the page and the images contained in it.
___________________________________________________________

## **Installation: tested in python 3.10.0 | Windows 10**

- pip install beautifulsoup4==4.11.1

- pip install requests==2.28.1

- pip install selenium==4.7.2

**For the robot to work, you must add ChromeDriver from selenium, the version corresponding to your Chrome Browser.**

**(If your Chrome version is 108.0.5359.98, you must download ChromeDriver version 108).**
**To see which version of Chrome is installed on your computer, follow these steps:**
- Open Chrome on your computer.

- Click on the Chrome menu in the upper right corner of the browser window.

- Select "Help" and then click on "Google Chrome Information or About Google Chrome".

-  A window will open with information about the version of Chrome that is installed on your computer.

- To install the same version of ChromeDriver from Selenium, follow these steps:

**Make sure you have the updated version of Chrome on your computer.**
- Download the correct version of ChromeDriver at: https://chromedriver.chromium.org/downloads

- Extract the downloaded file to a folder on your computer.

- Copy the ChromeDriver file to the webdriver folder.

- The robot is now ready to run.

___________________________________________________________

This program was created for a project called PsicoRecogn. The purpose of this project is to capture and analyze the morphopsychology of any user in order to create a detailed profile of their characteristics and provide ultra-personalization in the readings that the user makes. The project will be released gradually and the first mission is to obtain enough data to validate the usefulness of morphopsychology, as there is currently not enough data to prove it.

The programs I created for the project were designed to analyze on a massive scale.
___________________________________________________________
**file_organizer.py**
![stack50_1](https://user-images.githubusercontent.com/115203597/206514765-c06b72ed-29ab-4eb0-9f21-f0e41ec5494e.png)

![stack50_2](https://user-images.githubusercontent.com/115203597/206514834-d331cce0-0960-4cb6-be97-bd168553ae58.png)

![stack50_3](https://user-images.githubusercontent.com/115203597/206516990-51b6af85-efb8-4ccc-a61d-515a09468819.png)

