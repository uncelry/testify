from datetime import datetime
import json
import psutil
import web

# Адрес главной страницы
urls = (
  '/', 'index'
)


def get_memory_stat():
    """Get local machine memory statistics"""
    # Get percentage of used RAM
    used_ram_percent = psutil.virtual_memory().percent
    # Get percentage of free RAM
    free_ram_percent = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

    return used_ram_percent, free_ram_percent


# All checks list
checks = []


# View for index page
class index:
    def GET(self):
        web.header('Content-Type', 'application/json')
        used, free = get_memory_stat()
        checks.append({'used_memory_percent': used, 'free_memory_percent': free, 'timestamp': str(datetime.now())})
        return json.dumps(checks, indent=4)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
