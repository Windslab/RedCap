from os import system
from os import getcwd
from time import sleep
from codecs import open
from random import randint
from datetime import datetime
from datetime import timedelta
from selenium import webdriver
from configparser import RawConfigParser
from selenium.common.exceptions import NoSuchElementException


class Settings:
    Parser = RawConfigParser()
    Parser.read(getcwd() + '\config.ini', 'utf8')
    Options = webdriver.ChromeOptions()
    Options.add_argument("user-data-dir=Cookies")
    Options.add_argument("load-extension=" + getcwd() + '\Adblock')
    Options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=getcwd() + '\chromedriver.exe', options=Options)
    driver.get(Parser.get('BASE', 'START'))

    CVS_Send_Url = Parser.get('CVS', 'URL')
    CVS_Name = Parser.get('CVS', 'NAME')
    CVS_Letter = Parser.get('CVS', 'LETTER')
    CVS_Send_24hours = randint(3600, 3960) * 24

    CVU_Update_Url = Parser.get('CVU', 'URL')

    def CVS_VacancyTitle(self):
        me = Settings()
        try:
            d = me.driver.find_element_by_xpath('//*[@class="bloko-modal-header bloko-modal-header_outlined"]/div')
            return d
        except NoSuchElementException:
            return False

    def CVS_ReplayBtn(self, i):
        me = Settings()
        try:
            d = me.driver.find_elements_by_xpath('//*[@data-qa="vacancy-serp__vacancy_response"]')[i]
            return d
        except NoSuchElementException:
            return False

    def CVS_СVListName(self):
        me = Settings()
        try:
            d = me.driver.find_element_by_xpath(
                '//*[@data-qa="resume-title" and text()="%s"]' % me.CVS_Name)
            if d.is_displayed():
                return d
        except NoSuchElementException:
            return False

    def CVS_LetterRequiredLink(self):
        me = Settings()
        try:
            d = me.driver.find_element_by_xpath('//*[@data-qa="vacancy-response-letter-toggle"]')
            if d.is_displayed():
                return d
            else:
                return False
        except NoSuchElementException:
            return False

    def CVS_LetterRequiredText(self, d):
        me = Settings()
        try:
            Text = me.driver.find_element_by_xpath('//*[@name="letter"]')
            if Text.is_enabled():
                Text.send_keys(d)
            else:
                return False
        except NoSuchElementException:
            return False

    def CVS_CVFormButton(self):
        me = Settings()
        try:
            d = me.driver.find_element_by_xpath('//*[@data-qa="vacancy-response-submit-popup"]')
            if d.is_displayed():
                return d
            else:
                return False
        except NoSuchElementException:
            return False

    def CVS_Limit200(self):
        me = Settings()
        try:
            d = me.driver.find_element_by_xpath('//*[@data-qa="negotiations-limit-exceeded"]')
            print(d.text)
            print(d)
            if d.is_displayed():
                return d
            else:
                return False
        except NoSuchElementException as e:
            print(e)
            return False

    def CVU_UpdateButtonRounded(self, i):
        me = Settings()
        try:
            d = me.driver.find_elements_by_xpath(
                '//*[@class="bloko-button bloko-button_primary-dimmed bloko-button_small bloko-button_stretched bloko-button_rounded"][@data-qa="resume-update-button"]')[i]
            if d.is_displayed():
                return d
        except NoSuchElementException:
            return False

    def CVU_UpdateButtonDimmed(self, i):
        me = Settings()
        try:
            d = me.driver.find_elements_by_xpath('//*[@class="applicant-resumes-update-button"]')[i]
            if d.is_displayed():
                return d
        except NoSuchElementException:
            return False

    def CVU_NewPage(self):
        me = Settings()
        try:
            d = int(me.Parser.get('CVS', 'PAGE')) + 1
            me.Parser.set('CVS', 'PAGE', d)
            me.WriteConfig()
        except Exception:
            return False

    def WriteConfig(self):
        me = Settings()
        try:
            with open('config.ini', 'w', 'utf-8') as ini:
                me.Parser.write(ini)
        except Exception:
            return False

    def Next(self, d):
        me = Settings()
        try:
            td = datetime.now() + timedelta(seconds=d)
            print('Next try at> ' + td.strftime('%H:%M:%S %d.%m.%Y') + ' P: ' + str(me.Parser.get('CVS', 'PAGE')))
            return d
        except Exception:
            return False

    def Border(self):
        bdr = '-'
        bdr = bdr * 64
        return bdr

    def Sleep(self):
        sleep(randint(1, 3))


class CVSend:
    def Pages(self):
        me = Settings()
        for i in range(int(me.Parser.get('CVS', 'PAGE')), 39):
            me.driver.get(me.CVS_Send_Url + str(i))
            self.Main()
            me.CVU_NewPage()
            if i >= 39:
                me.Parser.set('CVS', 'PAGE', 0)
                me.WriteConfig()
                self.Pages()

    def Main(self):
        me = Settings()
        system('cls')
        i = 1
        while i < 50:
            try:
                if not type(me.CVS_ReplayBtn(i)) is bool:
                    me.CVS_ReplayBtn(i).click()
                    me.Sleep()
                    if not type(me.CVS_VacancyTitle()) is bool:
                        print('N:' + str(i) + ' P:' + str(me.Parser.get('CVS', 'PAGE')) + ' ' + me.CVS_VacancyTitle().text)
                    if not type(me.CVS_СVListName()) is bool:
                        me.CVS_СVListName().click()
                        me.Sleep()
                    if not type(me.CVS_LetterRequiredLink()) is bool:
                        me.CVS_LetterRequiredLink().click()
                        me.Sleep()
                    if not type(me.CVS_LetterRequiredText(me.CVS_Letter)) is bool:
                        if not type(me.CVS_CVFormButton()) is bool:
                            me.CVS_CVFormButton().click()
                            me.Sleep()
                            if not type(me.CVS_Limit200()) is bool:
                                system('cls')
                                sleep(me.Next(me.CVS_Send_24hours))
                                me.CVS_CVFormButton().click()
                        else:
                            me.driver.get(me.CVS_Send_Url + str(me.Parser.get('CVS', 'PAGE')))
                if i >= 50:
                    self.Pages()
                    break
                i += 1
            except Exception:
                if i >= 50:
                    self.Pages()
                    break
                i += 1
                continue


class CVUpdate:
    def Main(self):
        me = Settings()
        system('cls')
        print(me.Border())
        print('The loop has been launched. Leave is as now for update it 24/7')
        print(me.Border())
        me.driver.get(me.CVU_Update_Url)
        i = 1
        while True:
            try:
                if not type(me.CVU_UpdateButtonRounded(i)) is bool:
                    me.Sleep()
                    print(me.CVU_UpdateButtonRounded(i).text)
                    me.CVU_UpdateButtonRounded(i).click()
                if not type(me.CVU_UpdateButtonDimmed(i)) is bool:
                    me.Sleep()
                    print(me.CVU_UpdateButtonDimmed(i).text)
                    me.CVU_UpdateButtonDimmed(i).click()
                i += 1
            except Exception as e:
                print(e)
                i += 1
                me.Sleep()
                if not me.driver.current_url == me.CVU_Update_Url:
                    me.driver.get(me.CVU_Update_Url)
                continue


me = Settings()
print(me.Border())
print('-> 1. for UPDATE your Curriculum Vitae')
print('-> 2. for SEND your Curriculum Vitae')
print(me.Border())


def choice():
    d = int(input("-> "))
    return d


Answer = choice()

if Answer == 1:
    me = CVUpdate()
    me.Main()
elif Answer == 2:
    me = CVSend()
    me.Pages()
else:
    choice()
