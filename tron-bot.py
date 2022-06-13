
from colorama import Fore, init
import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc

os.environ['WDM_LOG_LEVEL'] = '0'
init(autoreset=True)

REF_CODE_BASE_URL = "https://tronseed.com/ref/"


def GET_VPN():
    print(
        Fore.MAGENTA + "[!] Setting the VPN...")

    EXTENSION_ICON = pyautogui.locateOnScreen(
        'assets/extensions.png', confidence=0.8)
    pyautogui.click(pyautogui.center(EXTENSION_ICON)[
                    0], pyautogui.center(EXTENSION_ICON)[1])
    time.sleep(1)

    VPN_ICON = pyautogui.locateOnScreen(
        "assets/vpn_icon.png", confidence=0.8)
    pyautogui.click(pyautogui.center(VPN_ICON)[
                    0], pyautogui.center(VPN_ICON)[1])
    time.sleep(1)

    SWITCH_VPN = pyautogui.locateOnScreen(
        "assets/vpn-off.png", confidence=0.8)

    TURN_ON = pyautogui.click(pyautogui.center(SWITCH_VPN)[
        0], pyautogui.center(SWITCH_VPN)[1])

    time.sleep(2)
    CHANGE_BUTTON = pyautogui.locateOnScreen(
        "assets/change_location.png", confidence=0.8)
    pyautogui.click(pyautogui.center(CHANGE_BUTTON)[
                    0], pyautogui.center(CHANGE_BUTTON)[1])
    time.sleep(1)
    CHANGE_TO_US_SERVER = pyautogui.locateOnScreen(
        "assets/us-server.png", confidence=0.8)
    pyautogui.click(pyautogui.center(CHANGE_TO_US_SERVER)[
                    0], pyautogui.center(CHANGE_TO_US_SERVER)[1])


if __name__ == "__main__":

    print(f"{Fore.MAGENTA}[-] Tron Bot by @edermxf")
    print(f"{Fore.GREEN}[-] Starting...")

    ADDRESS_FILENAME = input(
        F"{Fore.BLUE}[?] Enter the address filename .txt: {Fore.RESET}") or "list.txt"
    REF_CODE = input(
        F"{Fore.BLUE}[?] Enter the Referral code: {Fore.RESET}") or "AaOXMyRZ"
    print(f"{Fore.GREEN}[Ref]: {REF_CODE}")

    REFERRAL_COUNTER = 0
    INVALID_WALLETS = 0

    with open(ADDRESS_FILENAME, 'r') as f:
        ADDRESS_LIST = f.readlines()

        for LINE in ADDRESS_LIST:
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument(
                '--user-data-dir=C://Users//ederm//AppData//Local//Google//Chrome//User Data//Default')
            driver = uc.Chrome(options=options)

            GET_VPN()

            ADDR = LINE.strip()

            print(Fore.GREEN + "[+] Starting the bot for: " + ADDR)

            driver.get(f"{REF_CODE_BASE_URL}{REF_CODE}")

            time.sleep(7)

            WALLET_INPUT = driver.find_element(
                By.XPATH, "//input[@placeholder='Your valid TRX address']")
            WALLET_INPUT.send_keys(ADDR)

            SUBMIT_BUTTON = driver.find_element(
                By.XPATH, "//input[@value='Get Started']")
            SUBMIT_BUTTON.click()

            time.sleep(3)

            try:
                READY = driver.find_element(
                    By.XPATH, "//a[@class='btn btn-success']")
                REFERRAL_COUNTER += 1
                print(Fore.GREEN + f"[{REFERRAL_COUNTER}] Referral countered!")
                driver.quit()
                continue

            except:
                INVALID_WALLETS += 1
                print(
                    Fore.RED + f"[{INVALID_WALLETS}] Wallets address not supported")
                driver.quit()
