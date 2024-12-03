from aiohttp import web

async def proizvodi_handler(request):
    proizvodi = [
        {"naziv": "Proizvod A", "cijena": 10.99, "količina": 5},
        {"naziv": "Proizvod B", "cijena": 15.49, "količina": 8},
        {"naziv": "Proizvod C", "cijena": 7.99, "količina": 12},
    ]
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', proizvodi_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)
