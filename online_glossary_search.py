from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from csv_handler import *
def use_online_glossary(website):
    '''
    Function to search through a online glossary, and find term - definition pairs
    to use as flashcards
    
    '''
    # Use raw string to avoid escape sequence warning
    driver_path = r".\drivers\chromedriver\chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Use Service to specify the driver path
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website)

    # Get the page content
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    p_tags = soup.find_all('p')
    glossary = [p.get_text() for p in p_tags]
    terms = []

    try:
        for i in range(0, len(glossary), 2):  # Increment by 2 to get term-definition pairs
            term = glossary[i]
            definition = glossary[i + 1]
            # remove colon from term if needed
            term = term.replace(":", "")
            terms.append([term, definition])
    except IndexError:
        print('Found all definitions!')

    for term in terms:
        print(f"Term: {term[0]}\nDefinition: {term[1]}\n")

    driver.quit()

