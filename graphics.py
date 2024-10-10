from tkinter import Tk, BOTH, Canvas


class Window: 
    def init(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill-BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self):
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def init(self, x, y):
        self.x = x 
        self.y = y


class Line:
    def init(self, p1, p2):
        self.p1 = p1
        self.p2 = p2        
        

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x1, self.p1.y1, self.p2.x2, self.p2.y2, fill=fill_color, width=2
        )