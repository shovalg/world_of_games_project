from selenium import webdriver


class TestWebService:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.my_driver = webdriver.Chrome(executable_path="web_drivers/chromedriver.exe", options=chrome_options)

    def test_scores_service(self):
        app_url = "http://localhost:8777"
        self.my_driver.get(app_url)
        score = self.my_driver.find_element_by_id("score").text
        score = int(score)
        if 1 < score < 1000:
            return True
        else:
            return False

    def main(self):
        test_succeeded = self.test_scores_service()
        if test_succeeded:
            return exit(0)
        else:
            return exit(-1)


if __name__ == '__main__':
    unit_test = TestWebService()
    unit_test.main()



# from selenium import webdriver
#
# my_driver = webdriver.Chrome(executable_path="web_drivers/chromedriver.exe")
#
#
# def test_scores_service():
#     app_url = "http://localhost:5000"
#     my_driver.get(app_url)
#     score = my_driver.find_element_by_id("score").text
#     if 1 < score < 1000:
#         return True
#     else:
#         return False
#
#
# print(test_scores_service())
