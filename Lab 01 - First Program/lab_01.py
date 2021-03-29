import arcade

arcade.open_window(600, 600, "AMONGNUS US")

arcade.set_background_color((arcade.color.SKY_BLUE))

arcade.start_render()
#arcade.draw_circle_filled(300,300,30,30,arcade.color.DARK_BROWN)

arcade.draw_rectangle_filled(300,150,600,300, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(140,374,100,150, arcade.csscolor.SLATE_GRAY)
arcade.draw_rectangle_filled(80, 339, 60, 80, arcade.csscolor.SLATE_GRAY)
arcade.draw_polygon_filled(((280,300),
                            (320, 300),
                            (200, 0),
                            (400, 0),
                            ),
                            arcade.csscolor.SLATE_GREY)




arcade.finish_render()
arcade.run()


