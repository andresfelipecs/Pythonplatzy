class coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, othercoordinate):
        x_diff = (self.x - othercoordinate.x)**2
        y_diff = (self.y - othercoordinate.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = coordinate(3, 30)
    coord_2 = coordinate(4, 8)

    print(coord_1.distance(coord_2))
    print(isinstance(3, coordinate))