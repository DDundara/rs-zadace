from aiohttp import web

proizvodi = [
    {"naziv": "Proizvod A", "cijena": 10.99, "količina": 5},
    {"naziv": "Proizvod B", "cijena": 15.49, "količina": 8},
    {"naziv": "Proizvod C", "cijena": 7.99, "količina": 12},
]

async def proizvodi_handler(request):
    if request.method == 'GET':
        return web.json_response(proizvodi)
    elif request.method == 'POST':
        novi_proizvod = await request.json()
        print("Primljeni podaci:", novi_proizvod)
        proizvodi.append(novi_proizvod)
        return web.json_response(proizvodi)

app = web.Application()
app.router.add_route('*', '/proizvodi', proizvodi_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)