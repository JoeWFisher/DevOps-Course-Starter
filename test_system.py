import os
import pytest
import app
from mongo import create_trello_board, delete_trello_board
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import dotenv
import requests
import pymongo
 
@pytest.fixture(scope='module')
def test_app():

    file_path = dotenv.find_dotenv('.env') 
    dotenv.load_dotenv(file_path, override=True) 

    test_db = "todo_test_db"
    os.environ['Mongo_db'] = test_db
    
    # construct the new application   
    application = app.create_app()   

    # start the app in its own thread.  
    thread = Thread(target=lambda: application.run(use_reloader=False))  
    thread.daemon = True  
    thread.start()   
    yield app   

    # Tear Down     
    thread.join(1)  



@pytest.fixture(scope="module")
def driver():  
    opts = webdriver.ChromeOptions() 
    opts.add_argument('--headless')   
    opts.add_argument('--no-sandbox') 
    opts.add_argument('--disable-dev-shm-usage')   
    with webdriver.Chrome('./chromedriver', options=opts) as driver:   
        yield driver 

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')  

    assert driver.title == 'To-Do App' 

    input_field = driver.find_element_by_id('new_item_input')
    input_field.send_keys("Selenium test")
    add_item = driver.find_element_by_id('create_new_item')
    add_item.click()

    to_do_items = driver.find_element_by_xpath("/html/body/div/div[2]/div/ul/li[1]")
    
    assert 'Selenium test' in to_do_items.text

    doing_button = driver.find_elements_by_id('make_doing_item')[0]
    doing_button.click()

    doing_items = driver.find_element_by_xpath("/html/body/div/div[2]/div/ul[2]")

    assert 'Selenium test' in doing_items.text

    done_button = driver.find_elements_by_id('make_done_item')[0]
    done_button.click()

    done_items = driver.find_element_by_xpath("/html/body/div/div[2]/div/ul[3]")

    assert 'Selenium test' in done_items.text
    
