import microbit

key_delay = 10
acc = microbit.accelerometer
a = microbit.button_a
b = microbit.button_b
img = microbit.display.image

while True:
    message = ''
    microbit.display.clear()
    x = acc.get_x()
    y = acc.get_y()
    if x > 300:
        message += 'r'
        img.set_pixel_value(4, 2, 1)
    elif x < -300:
        message += 'l'
        img.set_pixel_value(0, 2, 1)

    if y > 300:
        message += 'd'
        img.set_pixel_value(2, 4, 1)
    elif y < -300:
        message += 'u'
        img.set_pixel_value(2, 0, 1)

    if a.is_pressed():
        message += 'a'
        img.set_pixel_value(1, 2, 1)

    if b.is_pressed():
        message += 'b'
        img.set_pixel_value(3, 2, 1)

    print(message)
    
    microbit.sleep(key_delay)
