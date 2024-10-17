from botcity.web import WebBot, Browser, By
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False
from webdriver_manager.chrome import ChromeDriverManager


class Bot(WebBot):

    def configuration_browser(self):
        self.headless = False
        self.browser = Browser.CHROME
        self.driver_path = ChromeDriverManager().install()

    def start_browser_bot(self, url="https://www.botcity.dev"):
        try:
            self.browse(url)
        except Exception as ex:
            print(f"Error starting browser : {ex}")
        finally:
            print("Finished initialization browser")

    def action(self, execution=None):
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        try:
            self.configuration_browser()
            self.start_browser_bot()

        except Exception as ex:
            print("Error: ", ex)
            self.save_screenshot("erro.png")
        finally:
            self.wait(3000)
            self.stop_browser()

        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == "__main__":
    Bot.main()