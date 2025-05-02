import asyncio
import random
from pathlib import Path
from playwright.async_api import async_playwright
import concurrent
import json
import time
import concurrent.futures
import threading
import itertools
from utils import logger

USE_PROXY = False
MAX_THREADS = 2




EMAIL_FILE = "emails.txt"
PROXY_FILE = "proxies.txt"
result_filename = f"results_{str(int(time.time()))}.txt"
error_filename = f"errors_{str(int(time.time()))}.txt"

TARGET_URL = "https://www.cambrian.org/"

RESOLUTIONS = [
    (1280, 720),
    (1440, 900),
    (1600, 900),
    (1920, 1080)
]



def get_chrome_user_agent():
    version = random.randint(132, 136)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version}.0.0.0 Safari/537.36"

async def run(email, proxy=None):
    success_results = []
    error_results = []

    user_agent = get_chrome_user_agent()
    width, height = random.choice(RESOLUTIONS)
    launch_args = {
        "headless": False,
        "channel": "chrome",
    }

    if proxy is not None:
        launch_args["proxy"] = {"server": proxy}

    async with async_playwright() as p:
        browser = await p.chromium.launch(**launch_args)
        context = await browser.new_context(
            user_agent=user_agent,
            viewport={"width": width, "height": height},
            screen={"width": width, "height": height}
        )
        page = await context.new_page()

        await page.goto(TARGET_URL, timeout=60000)
        await asyncio.sleep(random.randint(2,5))
        try:
            await page.wait_for_selector('//div[contains(@data-framer-name, "WAITLIST")]', timeout=10000)
            await page.locator('//div[contains(@data-framer-name, "WAITLIST")]').focus()
            await page.locator('//div[contains(@data-framer-name, "WAITLIST")]').click()
            await asyncio.sleep(random.randint(2, 5))

            email_input = await page.wait_for_selector("(//form//input[@type='email'])[last()]", timeout=10000)
            await email_input.focus()
            await email_input.click()
            await asyncio.sleep(random.randint(2, 5))
            await email_input.fill(email)

            submit_button = await page.wait_for_selector("(//button[@type='submit' and @data-framer-name='Default'])[last()]", timeout=10000)
            await submit_button.focus()
            await asyncio.sleep(random.randint(2, 5))
            await submit_button.click()

            try:
                await page.wait_for_selector("(//button[@type='submit' and @data-framer-name='Success'])[last()]", timeout=10000)
                logger.warning(f"✅ {email} - Регистрация успешна")
                success_results.append(f"{email}:{proxy}")
            except:
                logger.error("❌ Регистрация не подтвердилась (Success не найден)")
                error_results.append(f"{email}:{proxy}")

        except Exception as e:
            logger.error(f"❌ Ошибка в процессе: {e}")
            error_results.append(f"{email}:{proxy}")

        await page.wait_for_timeout(5000)
        await browser.close()

        with open(result_filename, "a", encoding="utf-8") as r_file:
            for line in success_results:
                r_file.write(f"{line}\n")

        if error_results:
            with open(error_filename, "a", encoding="utf-8") as e_file:
                for email in error_results:
                    e_file.write(f"{email}\n")


def thread_wrapper(email, proxy):
    try:
        asyncio.run(run(email, proxy))
    except Exception as e:
        logger.error(f"❌ Ошибка run: {e}")

def main():
    print("======== CAMBRIAN.ORG WL REGISTRATION ========")
    print(f"Наши ресурсы:\n"
          f"Telegram-канал: @quantumlab_official\n"
          f"Продукты: @quantum_lab_bot\n\n")


    with open(EMAIL_FILE, encoding="utf-8") as f:
        emails = [line.strip() for line in f if line.strip()]

    if not emails:
        logger.error("❌ Нет email-адресов в файле!")
        return

    proxies = []
    if USE_PROXY:
        with open(PROXY_FILE, encoding="utf-8") as f:
            proxies = [line.strip() for line in f if line.strip()]
        proxy_cycle = itertools.cycle(proxies) if proxies else itertools.cycle([None])
    else:
        proxy_cycle = itertools.cycle([None])

    logger.warning(f"Запуск активности в {MAX_THREADS} потоков")
    logger.warning(f"В работу отправлено: {len(emails)} Email'ов")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for email in emails:
            logger.error(f"Автоматизация и разработка by QUANTUM LAB | Telegram-канал: @quantumlab_official | Продукты: @quantum_lab_bot")
            proxy = next(proxy_cycle)
            futures.append(executor.submit(thread_wrapper, email, proxy))
            time.sleep(random.randint(3,10))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f"❌ Ошибка потока: {e}")


    print(f"Наши ресурсы:\n"
          f"Telegram-канал: @quantumlab_official\n"
          f"Продукты: @quantum_lab_bot\n\n")
    print("======== CAMBRIAN.ORG WL REGISTRATION ========")


if __name__ == "__main__":
    main()