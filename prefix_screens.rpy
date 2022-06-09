init python:

    g_PREFIX = Gallery()
    page_PREFIX = 0
    gallery_mode_page_PREFIX = "cg"
    g_PREFIX.locked_button = get_image("gui/gallery/not_opened_idle.png")
    g_PREFIX.navigation = False
    rows_PREFIX = 4
    cols_PREFIX = 3
    cells_PREFIX  = rows_PREFIX * cols_PREFIX
    gallery_cg_PREFIX = [ 
        "ЗАПОЛНИТЬ СЛОВАРЬ ЦГ", # Название изображение без обозначения формата изображения.
                                # Пример правильного обозначения: "d6_scena"
                                # Пример неправильного обозначения "d6_scena.jpg"
    ]
    gallery_bg_PREFIX = [
        "ЗАПОЛНИТЬ СЛОВАРЬ БГ", # То же правило, что и с ЦГ
    ]

    gallery_music_PREFIX = {
        "Название в галереи": "Путь",
    }
    
    
    PREFIX_mr = MusicRoom(fadeout=1.0)
    
    for name in gallery_music_PREFIX.values():
        PREFIX_mr.add(name)

init 101 python:

    for cg in gallery_cg_PREFIX:
        g_PREFIX.button(cg)
        g_PREFIX.image(im.Crop("Путь к папке с ЦГ"+cg+".jpg" , (0,0,1920,1080)))
        g_PREFIX.unlock(""+cg)  # Если ваши цг обозначаются в формате: "cg название", то измените строку на g_PREFIX.unlock("cg "+cg)
    
    for bg in gallery_bg_PREFIX:
        g_PREFIX.button(bg)
        g_PREFIX.image(im.Crop("Путь к папке с БГ"+bg+".jpg" , (0,0,1920,1080)))
        g_PREFIX.unlock(""+bg) # Если ваши бг обозначаются в формате: "bg название", то измените строку на g_PREFIX.unlock("bg "+bg)
    
    g_PREFIX.transition = fade

 
screen gallery_PREFIX:
    # Пути указывают к стандартным ассетам Бесконечного Лета. Не изменяя ничего, галерея будет выглядеть так же, как и в оригинальной игре.

    tag menu
    modal True
    $ gallery_table_PREFIX = []
    if gallery_mode_PREFIX == "cg":
        $ gallery_table_PREFIX = gallery_cg_PREFIX
    else:
        $ gallery_table_PREFIX = gallery_bg_PREFIX
    $ len_table_PREFIX = len(gallery_table_PREFIX)
    frame background get_image("gui/settings/history_bg.jpg"): # Фон
        if gallery_mode_PREFIX == "cg":
            textbutton "МУЗЫКА" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('page', 0), ShowMenu("music_gallery_PREFIX"))
            textbutton "ФОНЫ" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('gallery_mode_PREFIX', "bg"), SetVariable('page_PREFIX', 0), ShowMenu("gallery_PREFIX"))
            hbox xalign 0.5 yalign 0.08:
                add get_image("gui/settings/star.png") yalign 0.65
                text " " +"ИЛЛЮСТРАЦИИ"+ " " style "settings_link" yalign 0.5 color "#ffffff"
                add get_image("gui/settings/star.png") yalign 0.65
        elif gallery_mode_PREFIX == "bg":
            textbutton "МУЗЫКА" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('page', 0), ShowMenu("music_gallery_PREFIX"))
            textbutton "ИЛЛЮСТРАЦИИ" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('gallery_mode_PREFIX', "cg"), SetVariable('page_VPREFIX', 0), ShowMenu("gallery_PREFIX"))
            hbox xalign 0.5 yalign 0.08:
                add get_image("gui/settings/star.png") yalign 0.65
                text " "+"ФОНЫ"+" " style "settings_link" yalign 0.5 color "#ffffff"
                add get_image("gui/settings/star.png") yalign 0.65
        textbutton "Назад" style "log_button" text_style "settings_link" xalign 0.985 yalign 0.92 action Return()
        grid rows_PREFIX cols_PREFIX xpos 0.09 ypos 0.18:
            $ cg_displayed = 0
            $ next_page_PREFIX = page_PREFIX + 1           
            if next_page_PREFIX > int(len_table_PREFIX/cells_PREFIX ):
                $ next_page_PREFIX = 0
            for n in range(0, len_table_PREFIX):
                if n < (page_PREFIX+1)*cells_PREFIX  and n>=page_PREFIX*cells_PREFIX :
                    python:
                        if gallery_mode_PREFIX == "cg":
                            _t = im.Crop("Путь к ЦГ"+gallery_table_PREFIX[n]+".jpg" , (0,0,1920,1080)) # Тут указываем пути к изображениям в формате "mods/VSIG/assets/cg/"
                        elif gallery_mode_PREFIX == "bg":
                            _t = im.Crop("Путь к БГ"+gallery_table_PREFIX[n]+".jpg" , (0,0,1920,1080)) # Точно так же, как и с ЦГ
                        th = im.Scale(_t, 320, 180)
                        img_PREFIX = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image("gui/gallery/thumbnail_idle.png"))
                        imgh_PREFIX = im.Composite((336,196),(8,8),th,(0,0),im.Image("gui/gallery/thumbnail_hover.png"))
                    add g_PREFIX.make_button(gallery_table_PREFIX[n], get_image("gui/gallery/blank.png"), None, imgh_PREFIX , img_PREFIX , style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1
                    if n+1 == len_table_PREFIX:
                        $ next_page_PREFIX = 0
            for j in range(0, cells_PREFIX -cg_displayed):
                null
        if page_PREFIX != 0:
            imagebutton auto ("gui/dialogue_box/day/backward_%s.png") yalign 0.5 xalign 0.01 action (SetVariable('page_PREFIX', page_PREFIX-1), ShowMenu("gallery_PREFIX"))
            key "a" action (SetVariable('page_PREFIX', page_PREFIX-1), ShowMenu("gallery_PREFIX"))
            key "A" action (SetVariable('page_PREFIX', page_PREFIX-1), ShowMenu("gallery_PREFIX"))
            key "ф" action (SetVariable('page_PREFIX', page_PREFIX-1), ShowMenu("gallery_PREFIX"))
            key "Ф" action (SetVariable('page_PREFIX', page_PREFIX-1), ShowMenu("gallery_PREFIX"))
        imagebutton auto ("gui/dialogue_box/day/forward_%s.png") yalign 0.5 xalign 0.99 action (SetVariable('page_PREFIX', next_page_PREFIX), ShowMenu("gallery_PREFIX"))
        key "d" action (SetVariable('page_PREFIX', next_page_PREFIX), ShowMenu("gallery_PREFIX"))
        key "D" action (SetVariable('page_PREFIX', next_page_PREFIX), ShowMenu("gallery_PREFIX"))
        key "В" action (SetVariable('page_PREFIX', next_page_PREFIX), ShowMenu("gallery_PREFIX"))
        key "в" action (SetVariable('page_PREFIX', next_page_PREFIX), ShowMenu("gallery_PREFIX"))
        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l-int(l) > 0:
                    return int(l)+1
                else:
                    return l
            page_PREFIXs = str(page_PREFIX+1)+"/"+str(int(abc(len_table_PREFIX,cells_PREFIX )))
        text page_PREFIXs style "settings_link" xalign 0.015 yalign 0.92


screen music_gallery_PREFIX:
    # Пути указывают к стандартным ассетам Бесконечного Лета. Не изменяя ничего, галерея будет выглядеть так же, как и в оригинальной игре.

    tag menu
    modal True

    frame background get_image("gui/settings/history_bg.jpg"): # Фон
        textbutton "ФОНЫ" style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action (SetVariable('gallery_mode_PREFIX', "bg"), ShowMenu("gallery_PREFIX"), SetVariable('page_PREFIX', 0))
        textbutton "ИЛЛЮСТРАЦИИ" style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action (SetVariable('gallery_mode_PREFIX', "cg"), ShowMenu("gallery_PREFIX"), SetVariable('page_PREFIX', 0))
        hbox xalign 0.5 yalign 0.08:
            add get_image("gui/settings/star.png") yalign 0.65
            text " "+translation_new["MUSIC"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("gui/settings/star.png") yalign 0.65

        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.23, 0.15, 0.61, 0.75)
            viewport id "gallery_music_PREFIX":
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 len(gallery_music_PREFIX)
                for name, track in sorted(gallery_music_PREFIX.iteritems()):
                    textbutton name style "log_button" text_style "music_link" action PREFIX_mr.Play(track)

            $ vbar_null = Frame(get_image("gui/settings/vbar_null.png"),0,0)

            bar value XScrollValue("gallery_music_PREFIX") left_bar "images/misc/none.png" right_bar "images/misc/none.png" thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
            vbar value YScrollValue("gallery_music_PREFIX") bottom_bar vbar_null top_bar vbar_null thumb "images/gui/settings/vthumb.png" thumb_offset -12