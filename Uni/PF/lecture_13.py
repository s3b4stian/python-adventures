## ESERCIZI

# Scrivere i seguenti metodi.

# 1. Contrasto dei colori dell'intera immagine, come da lezione precedente, usando le operazioni aritmetiche
# sui colori. Introdurre un metodo per correggere i colori fuori scala.

# 2. Generare mosaici, come da lezione precedente, introducendo un metodo per calcolare la media dei
# colori in un quadratino dell'immagine.

# 3. Introdurre la copia di parte di un'immagine su un'altra, come da lezione precedente.

from lec_12_files_img import image as im

class Color:

    def __init__(self, r, g, b):
            self.set_color(r, g, b)
    
    def set_color(self, r, g, b):
        def bound(componente):
            return min(255, max(0, round(componente)))
        self.r, self.g, self.b = bound(r), bound(g), bound(b)

    def inverse(self):
        return Color(255 - self.r, 255 - self.g, 255 - self.b)

    def __repr__(self):
        return 'Color({self.r}, {self.g}, {self.b})'

    def __add__(self, other):
        return Color(self.r+other.r,self.g+other.g,self.b+other.b)

    def __mul__(self, f):
        return Color(self.r * f, self.g * f, self.b * f)

    def to_tuple(self):
        return self.r, self.g, self.b

class Image:

    def __init__(self, w = 0, h = 0):
        self._pixels = [[Color(0,0,0)] * w for _ in range(h)]

    def width(self):
        return len(self._pixels[0])

    def height(self):
        return len(self._pixels)

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width() and 0 <= y < self.height():
            self._pixels[y][x].set_color(color.r, color.g, color.b)

    def get_pixel(self, x, y):
        if 0 <= x < self.width() and 0 <= y < self.height():
            return self._pixels[y][x]
        else: 
            return None

    def to_img(self):
        return [[ c.to_tuple() for c in line ] for line in self._pixels]

    def load(self, filename):
        img = im.load(filename)
        self._pixels = [[Color(*c) for c in riga ] for riga in img]

    def save(self, filename):
        im.save(filename, self.to_img())

    def visd(self, msg=None):
        im.visd(self.to_img(), msg)

    def __str__(self):
        return f"Image@{self.width()}x{self.height()}"

    def contrast(self, c):
        for y in range(self.height()):
            for x in range(self.width()):
                r, g, b = self._pixels[y][x].to_tuple()
                #print(c, r, g, b)
                r, g, b = self._contrast_pixel(r, g, b, c)
                self._pixels[y][x].set_color(r, g, b)

    def _contrast_pixel(self, r, g, b, c):
        r = ((r - 128) * c) + 128
        g = ((g - 128) * c) + 128
        b = ((b - 128) * c) + 128
        r = round(min(255, max(0, r)))
        g = round(min(255, max(0, g)))
        b = round(min(255, max(0, b)))
        return (r, g, b)

    def draw_quad(self, x, y, w, h, c):
        for xx in range(x, x + w):
            for yy in range(y, y + h):
                self.set_pixel(xx, yy, c)

    def draw_gradienth(self, c0, c1):
        for x in range(self.width()):
            u = x / self.width()
            c = c0 * (1 - u) + c1 * u
            for y in range(self.height()):
                self.set_pixel(x, y, c)

    def draw_gradientv(self, c0, c1):
        for y in range(self.height()):
            v = y / self.height()
            c = c0 * (1 - v) + c1 * v
            for x in range(self.width()):
                self.set_pixel(x, y, c)

    def draw_gradientq(self, c00, c01, c10, c11):
        for y in range(self.height()):
            for x in range(self.width()):
                u = x / self.width()
                v = y / self.height()
                c = c00 * (1 - u) * (1 - v) + c01 * (1 - u) * v + c10 * u * (1 - v) + c11 * u * v
                self.set_pixel(x, y, c)


# doesn't work in python 3.9
# tested succesfuly using Spyder 4.2.5 and Python 3.8 on windows 10
if __name__ == '__main__':

    # img = Image(256,256)
    # img.draw_quad(32,32,64,64,Color(255,128,0))
    # img.draw_quad(160,160,64,64,Color(255,128,0))
    # img.visd()

    # img = Image(256,256)
    # img.draw_gradienth(Color(255,0,0),Color(0,255,0))
    # img.visd()

    # img = Image(256,256)
    # img.draw_gradientv(Color(255,0,0),Color(0,255,0))
    # img.visd()

    # img = Image(256,256)
    # img.draw_gradientq(Color(255,0,0), Color(0,255,0), Color(0,0,255), Color(0,0,0))
    # img.visd()
    c_test = [ i/10 for i in range(0,21)]
    for c in c_test:
        img = Image()
        img.load('lec_12_files_img/img_in_01.png')
        img.contrast(c)
        img.visd()
