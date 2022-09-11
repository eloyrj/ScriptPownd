
import scrapy

class ScriptSelenium(scrapy.Spider):
    name = 'ScriptSelenium'
    start_urls = ['https://monitor.firefox.com/']

    def parse(self, response):
        return [scrapy.FormRequest(
            'https://monitor.firefox.com/',
            formdata = {'email':'cortecerito@gmail.com'},
            callback = self.after_login
            )] 
    
    def after_login(self, response):
        print(self)
        return "hola"