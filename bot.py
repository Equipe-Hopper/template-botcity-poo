from botcity.web import WebBot, Browser, By
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False
from webdriver_manager.chrome import ChromeDriverManager

class Bot(WebBot):

    def action(self,execution = None):
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")
    
    
        self.headless = False        
        self.browser = Browser.CHROME
        self.driver_path = ChromeDriverManager().install()

        self.browse("https://www.botcity.dev")
        
        
        try:
            pass
        except Exception as ex:
            print("Erro: ", ex)
            self.save_screenshot('erro.png')
        finally:
            self.wait(3000)        
            self.stop_browser()

        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )


    def not_found(self,label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
