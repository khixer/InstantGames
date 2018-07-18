from selenium import webdriver
from threading import Thread
import time


def parse_games(html):
    all_games = html.find_elements_by_class_name("ellipsis")
    names = []
    for i in all_games:
        names.append(i.text)

    game_name = []
    makers = []
    number_of_users = []

    for i, val in enumerate(names):
        if i % 2 == 0:
            game_name.append(names[i])
        else:
            makers.append(names[i])

    return game_name, makers


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/instantgames/')

print driver.title
# html = driver.find_element_by_xpath(".//html")

# doing infifnte scrolling
count = 0

all_pages = ''
while True:
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    html_source = driver.find_element_by_xpath(".//html")
    count += 1
    print(count)
    if html_source:
        # TODO: function to parse the page
        # TODO: check if result of previous data = new scraped data break the
        # loop.
        all_pages = html_source
    else:
        break


# game, maker = parse_games(all_pages)


# print "\n\n\n\n"
# print("--------game_name------------")
# print game
# print("--------makers------------")
# print maker

driver.quit()
