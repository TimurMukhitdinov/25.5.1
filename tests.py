from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_my_pets_info(driver_friends_chrome):
    # Проверка редиректа "Мои питомцы"
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    WebDriverWait(driver_friends_chrome, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    assert driver_friends_chrome.find_element_by_xpath('//body/div[1]/div/div[1]/h2').text == "TimurMukhitdinov"


def test_my_pets_stat(driver_friends_chrome):

    # Проверка количества питомцев соответствующих указанной статистике.
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    WebDriverWait(driver_friends_chrome, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    pets = 'Питомцев: 6'
    pets_text = driver_friends_chrome.find_element_by_xpath('//body/div[1]/div[1]/div[1]')
    assert pets in pets_text.text


def test_my_pets_name_age_animal_type(driver_friends_chrome):

    # Проверка на наличие имени, возраста и породы.
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    WebDriverWait(driver_friends_chrome, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    string = driver_friends_chrome.find_elements_by_xpath('//table[@class ="table table-hover"]/tbody/tr')
    images = driver_friends_chrome.find_elements_by_css_selector('div#all_my_pets>table>tbody>tr>th>img')
    names = driver_friends_chrome.find_elements_by_xpath("//tr/td[1]")
    animal_type = driver_friends_chrome.find_elements_by_xpath('//tr/td[2]')
    age = driver_friends_chrome.find_elements_by_xpath('//tr/td[3]')
    table_pet = driver_friends_chrome.find_elements_by_xpath('//*[@id="all_my_pets"]/table')
    for i in range(len(string)):
        assert names[i].text and animal_type[i].text and age[i].text != ''
        count_nam = len(names)
        count_type = len(animal_type)
        count_age = len(age)
        assert count_type == count_nam
        assert count_nam == count_age


def test_different_names(driver_friends_chrome):

    # Проверка на разные имена.
    pet_data = driver_friends_chrome.find_elements_by_css_selector('.table.table-hover tbody tr')
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
        assert r == 0


def test_one_pet(driver_friends_chrome):

    # Проверка неповторяющихся питомцев
    pet_data = driver_friends_chrome.find_elements_by_css_selector('.table.table-hover tbody tr')
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '
    list_line = line.split(' ')
    set_list_line = set(list_line)
    a = len(list_line)
    b = len(set_list_line)
    result = a - b
    assert result == 0


def test_photo_more_then_half(driver_friends_chrome):

    # Проверка фото есть больше, чем у половины питомцев.
    driver_friends_chrome.implicitly_wait(10)
    driver_friends_chrome.find_element_by_xpath('//body/nav/div[1]/ul/li[1]/a').click()
    statistic = driver_friends_chrome.find_elements_by_css_selector(".\\.col-sm-4.left")
    images = driver_friends_chrome.find_elements_by_css_selector('.table.table-hover img')
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    half = number // 2
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1
    assert number_photos >= half