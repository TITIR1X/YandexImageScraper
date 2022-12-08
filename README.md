# YandexImageScraper
The script allows you to perform a search on Yandex.com using a keyword provided by the user, and then downloads a specified number of images resulting from the search. The downloaded images are stored in an HTML file in a folder specified by the user.

___________________________________________________________

**Installation: tested in python 3.10.0 | Windows 10**

- pip install beautifulsoup4==4.11.1

- pip install requests==2.28.1

- pip install selenium==4.7.2

**For the robot to work, you must add ChromeDriver from selenium, the version corresponding to your Chrome Browser.

**(If your Chrome version is 108.0.5359.98, you must download ChromeDriver version 108).
**To see which version of Chrome is installed on your computer, follow these steps:
- Open Chrome on your computer.

- Click on the Chrome menu in the upper right corner of the browser window.

- Select "Help" and then click on "Google Chrome Information or About Google Chrome".

-  A window will open with information about the version of Chrome that is installed on your computer.

- To install the same version of ChromeDriver from Selenium, follow these steps:

**Make sure you have the updated version of Chrome on your computer.
- Download the correct version of ChromeDriver at: https://chromedriver.chromium.org/downloads

- Extract the downloaded file to a folder on your computer.

- Copy the ChromeDriver file to the webdriver folder.

- The robot is now ready to run.

___________________________________________________________

The program **direct_links_generator.py** is used to isolate the links generated by **YandexBot_keyword_search.py.** To use it:
- Insert the path created by *YandexBot_keyword_search.py* into the *direct_links_generator.py* program.

**For the operation of YandexBot_image_recognition.py:**
- Please upload your personal list of URLs into the **URLS.py** file. I personally use the free imgbb.com server to generate image links, which must then be inserted into URLS.py.

To download the images, follow these steps:

1- Open the .html file

2- Right click on the file

3- Select "save page".

4- This will start the automatic download of the page and the images contained in it.

**separador_stacks_50.py**
The file separator_stacks_50.py is used to group by 50 files from the "recognition_images_src" folder generated by YandexBot_recognition_image.py into a file named "./1/all_src.html", "./2/all_src.html", "./3/all_src.html", etc. Once the files have been created, you can open it one by one and follow the steps mentioned above to download the images contained in it.

**separador_stacks_50.py** can be configured to group 100 files or more, by default it is set to 50.


This program was created for a project called PsicoRecogn. The purpose of this project is to capture and analyze the morphopsychology of any user in order to create a detailed profile of their characteristics and provide ultra-personalization in the readings that the user makes. The project will be released gradually and the first mission is to obtain enough data to validate the usefulness of morphopsychology, as there is currently not enough data to prove it.

The programs I created for the project were designed to analyze on a massive scale.
