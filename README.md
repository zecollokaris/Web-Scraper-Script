# WEBSCRAPER SCRIPT

## DESCRIPTION.

This is a **python webscraping script** used to scrap for Cars and their Details from a car website and arrange the **list of attributes** in an organized way that can be referenced.  

**Web Scraping** - refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user. Be it a spreadsheet or an API.

## FEATURES.

- This Application allows users to **search for cars** based on **countries** and get a full break down list about **specific cars depending on attributes parsed**. 

- The **output of the web scrapper** is fed into an **Excel Workbook** (.xlsx file) where each
of these attributes are written in **separate columns.**

- For **Contact** user is **redirected to another website** which contains this **listing**.


## PREREQUISITES.


**Nano Text Editor.**

If you don't have it installed, you can quicky do that by typing:


```
 sudo apt-get install nano
```

* You need to have (python3.6) installed in your machine.

* To check if you already have python3.6 before installing type:



```
python3.6 -V
```


**Python3.6**

To install python3.6 you can quicky do that by typing:



```
sudo apt-get install python3.6
```

## TECHNOLOGIES USED.

1. **[Python](https://www.python.org/)**

**Python** is an interpreted **high-level general-purpose programming language**. Its design philosophy emphasizes code readability with its use of significant indentation.

2. **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**

**Beautiful Soup** is a library that makes it easy to **scrape information by to pulling the data out of HTML and XML files & Web Pages**. It sits atop an HTML or XML parser, providing **Pythonic idioms for iterating, searching, and modifying the parse tree**.

3. **[Pandas DataFrame](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**

**Pandas DataFrame** is **two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes** (rows and columns).


## **SETUP/INSTALLATION!**


1. You will need **Internet connection**.

2. You need to get into the **Webscraper Script Repository**.

3. From there you can access the **Webscraper**.

4. **Clone** the project.

5. **get into project folder** (cd into project).

6. If you have all the **Pre-requisites**

7. Open your **Code Editor and run the Application**.


# **HOW TO RUN.**

**To work With this WebScrapper**

1. **Make sure your inside folder containing script.**

2. Initialize the Python Script 

    ```
    python3 scraper.py germany
    ```

3. **Note** to **Initialize the Script there has to always be Country args parsed**. Not every Country is Included so the **Custom List** is added below.

    ```
    
    python3 scraper.py austria
    python3 scraper.py belgium
    python3 scraper.py bulgaria
    python3 scraper.py czech+republic
    python3 scraper.py denmark
    python3 scraper.py finland
    python3 scraper.py france
    python3 scraper.py germany
    python3 scraper.py greece
    python3 scraper.py hungary
    python3 scraper.py italy
    python3 scraper.py latvia
    python3 scraper.py netherlands
    python3 scraper.py poland
    python3 scraper.py portugal
    python3 scraper.py romania
    python3 scraper.py russia

    ```

4. From there the it will **prompt output of a an Excel Workbook (.xlsx file) where each of these attributes are written in separate columns.**

5. You are now ready **THANK YOU :-)**