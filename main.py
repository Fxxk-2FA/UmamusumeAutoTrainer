import sys
import threading

from bot.base.manifest import register_app
from bot.engine.scheduler import scheduler
from module.umamusume.manifest import UmamusumeManifest
from uvicorn import run
from config import loadConfig

if __name__ == '__main__':
    if sys.version_info.minor != 10 or sys.version_info.micro != 9:
        print("\033[33m{}\033[0m".format("注意：python 版本号不正确，可能无法正常运行"))
        print("建议python版本：3.10.9 当前：" + sys.version)
    
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = "config.yaml"
    
    CONFIG = loadConfig(config_file)
    UmamusumeManifest.extra_config = CONFIG
    port = int(CONFIG["port"])
    
    register_app(UmamusumeManifest)
    scheduler_thread = threading.Thread(target=scheduler.init, args=())
    scheduler_thread.start()
    print(f"Using config file: {config_file}, UAT running on http://127.0.0.1:{port}")
    run("bot.server.handler:server", host="127.0.0.1", port=port, log_level="error")

