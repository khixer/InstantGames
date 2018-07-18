from selenium import webdriver
from threading import Thread
import time


def parse_games(html):
    names = []
    for i in html:
        names.append(i.text)

    game_name, makers, number_of_users = [], [], []

    # TODO: need to extract the count of users
    for i, val in enumerate(names):
        if i % 2 == 0:
            game_name.append(names[i])
        else:
            makers.append(names[i])

    return game_name, makers


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/instantgames/')
time.sleep(10)

# doing infifnte scrolling
scroll_count = 0

prev_game, prev_maker = [], []
while True:
    html_source = driver.find_elements_by_class_name('ellipsis')
    scroll_count += 1
    print(scroll_count)
    if html_source:
        # function to parse the page
        game, maker = parse_games(html_source)
        # TODO: Wrtie to csv here
        print "\n\n\n\n"
        print("--------game_name------------")
        print game
        print("--------makers------------")
        print maker
        # TODO: if result of previous data = new scraped data break the loop
        if game != prev_game and maker != prev_maker:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
        else:
            break


driver.quit()
