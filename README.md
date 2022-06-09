# Тут что-то ввести надо хз


### Для создания понадобится

- Скачать исходник под названием **prefix_screens**
- Текстовый редактор [**Notepad++**](https://notepad-plus-plus.org/downloads/)
- Обязательное раздение **bg** и **cg** на разные папки.

### Начало
1. Заходим в наш текстовой редактор
2. Нажимаем **CTRL+F**
3. Заходим во вкладку **Замена**
4. В строке **Найти** вводим **PREFIX**. 
5. В строке **Заменить на** вводим, к примеру, сокращенное название вашего мод (в моем случае VSIG)
6. Нажимаем справа на кнопку **Заменить всё**
7. Так же изменяем **PREFIX** названии вашего файла.

### Работа с кодом
#### (Внутри файла есть комментарии для удобства)
* Внутри файла находим строку:
```sh
gallery_cg_PREFIX = [ 
        "ЗАПОЛНИТЬ СЛОВАРЬ ЦГ"
]
```
* Заполняем словарь названиями CG вашего мода
### Пример правильного заполнения
```sh
gallery_cg_PREFIX = [
        "d2_cards",
        "d2_elnaked",
        "d3_bandage",
        "d3_boat",
    ]
```
## Важно! 
#### Не нужно указывать формат изображения в словаре.
* Тоже самое делаем и со словарем BG
```sh
gallery_bg_PREFIX = [
    "d5_polyana_bonfire_night",
    "d6_domiki_night",
    "d6_scena_sunset",
    "d6_vsyascena_sunset",
    "int_semen_room_evening1"
    ]
```
* Дальше нам нужно заполнить словарь музыки, в формате **"Название": "путь"**
### Пример правильного заполнения
```sh
gallery_music_PREFIX = {
    "Sunlight In Emerald Pieces": "mods/VSIG/assets/sounds/music/sunlight_in_emerald_pieces.ogg"
    }
```
* Далее находим строки и вводим путь к вашим файлам.
```sh
for cg in gallery_cg_VSIG:
    g_VSIG.button(cg)
    g_VSIG.image(im.Crop("ПУТЬ К ЦГ"+cg+".jpg" , (0,0,1920,1080)))
    g_VSIG.unlock(""+cg)
    
for bg in gallery_bg_VSIG:
    g_VSIG.button(bg)
    g_VSIG.image(im.Crop("ПУТЬ К БГ"+bg+".jpg" , (0,0,1920,1080)))
    g_VSIG.unlock(""+bg)
```
### Пример правильного заполнения
```sh
for cg in gallery_cg_PREFIX:
    g_PREFIX.button(cg)
    g_PREFIX.image(im.Crop("mods/VSIG/assets/images/cg/"+cg+".jpg" , (0,0,1920,1080)))
    g_PREFIX.unlock(""+cg)
    
for bg in gallery_bg_PREFIX:
    g_PREFIX.button(bg)
    g_PREFIX.image(im.Crop("mods/VSIG/assets/images/bg/"+bg+".jpg" , (0,0,1920,1080)))
    g_PREFIX.unlock(""+bg)
```

## Важно! 
#### Если вы указываете bg, cg в формате _bg название_, то нужно изменить строки
```sh
g_PREFIX.unlock(""+bg)
g_PREFIX.unlock(""+cg)
```
#### На такие
```sh
g_PREFIX.unlock("bg "+bg)
g_PREFIX.unlock("cg "+cg)
```

* Далее находим строку
```sh
python:
    if gallery_mode_PREFIX == "cg":
        _t = im.Crop("Путь к ЦГ"+gallery_table_VSIG[n]+".jpg" , (0,0,1920,1080))
    elif gallery_mode_PREFIX == "bg":
        _t = im.Crop("Путь к БГ"+gallery_table_PREFIX[n]+".jpg" , (0,0,1920,1080))
```
* И заполняем пути к файлам.
* Данные строки кода отвечают за превью (маленькие карты внутри галереи) изображений.

#### Готово. Примеры готовой галереи:
![alt text](https://i.imgur.com/lOEmtOx.png)
![alt text](https://i.imgur.com/Yn2TYPO.png)
![alt text](https://i.imgur.com/0HlltDA.png)

#### Послесловие
За основу взят код [**Дмитрия Сладкова**](https://vk.com/sladkov2001) (за что ему большое спасибо) и оригинальный код игры **"Бесконечное Лето"**
По всем вопросам обращайтесь в [**VK**](https://vk.com/poslednyasmert)







