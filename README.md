# praktikum_new_diplom



## Запускаем загрузчик json
python manage.py import_ingredients_json --path 'recepies/data/ingredients.json'

## Шаблон загрузки рецепта
{
    "ingredients": [{
            "id": 1,
            "amount": 2
        },
        {
            "id": 2,
            "amount": 3
        }
        ],
   "name": "топленое молоко три",
    "text": "на плиту и варить",
    "cooking_time": "60",
    "tags": [ 1 ],
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAJ2BLADASIAAhEBAxEB/8QAHQABAAEFAQEBAAAAAA"
}