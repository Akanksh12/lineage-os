from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
driver.get("https://download.lineageos.org/")
brands_list = []
element = driver.find_element_by_xpath('//*[@id="slide-out"]')
children = element.find_elements_by_xpath(".//*")
print(element.text.split("\n"))
no_of_brands = 27
for i in range(no_of_brands):
    element = driver.find_element_by_xpath(f'//*[@id="slide-out"]/li[{i+2}]/ul/li/a')
    print(i + 1,element.get_attribute("innerText"))
    brands_list.append(element)

print("\n")

brand = int(input("Enter your option number\n"))
brand_element = element.find_element_by_xpath(f'//*[@id="slide-out"]/li[{brand + 1}]/ul/li/div/ul/li')
brand_children = brand_element.find_elements_by_xpath(".//*")
for i in range(len(brand_children)):
    print(brand_children[i].text)
    print(brand_children.get_attribute("innerText"))
phones_list = []
for i in range():
    phones = brand_element.find_element_by_xpath(f'//li[{i + 2}]/a/div')
    phones = phones.get_attribute('innerText')
    phones_list.append(phones)

print(phones_list)