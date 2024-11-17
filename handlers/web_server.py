from aiohttp import web

async def handle_health_check(request):
    return web.Response(text="Bot is running!")

def create_web_server():
    app = web.Application()
    app.router.add_get("/", handle_health_check)  # Health check endpoint
    return app
