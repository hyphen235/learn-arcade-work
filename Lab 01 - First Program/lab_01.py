import arcade

arcade.open_window(600, 600, "AMONGNUS US")

arcade.set_background_color((arcade.color.SKY_BLUE))

arcade.start_render()
#arcade.draw_circle_filled(300,300,30,30,arcade.color.DARK_BROWN)

arcade.draw_rectangle_filled(300,150,600,300, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(100,300,20,60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100,350,30, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200,370,60,80, arcade.csscolor.DARK_GREEN)





arcade.finish_render()
arcade.run()


