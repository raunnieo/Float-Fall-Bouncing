        elif event.type == pygame.VIDEORESIZE:
            print(event.h, event.w)
            bg_surface = pygame.transform.scale_by(bg_surface, event.h/window_height)
            bg_grd = pygame.transform.scale_by(bg_grd, event.h/window_height)
            bg_water = pygame.transform.scale_by(bg_water, event.h/window_height)
            bg_moon = pygame.transform.scale_by(bg_moon, event.h/window_height)
            bg_moongrd = pygame.transform.scale_by(bg_moongrd, event.h/window_height)
            midscene = pygame.transform.scale_by(midscene, event.h/window_height)
            window_height = event.h
            window_width = event.w
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)