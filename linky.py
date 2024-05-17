from peewee import *
db = MySQLDatabase(
    'metro',
    user='root',
    password='',
    host='localhost',
    port=3306
)

class point(Model):
    idpoint = AutoField()
    name = CharField(max_length=45)
    positionx = IntegerField()
    positiony = IntegerField()
    class Meta:
        database = db

class path(Model):
    idpath = AutoField()
    length = IntegerField()
    left = IntegerField()
    right = IntegerField()
    point_leftID = ForeignKeyField(point, backref='paths_left', column_name='point_leftID')
    point_rightID = ForeignKeyField(point, backref='paths_right', column_name='point_rightID')
    class Meta:
        database = db


def get_idpoint():
    idpoints = [point.idpoint for point in point.select()]
    return idpoints

def get_name():
    name = [point.name for point in point.select()]
    return name

def get_positionx():

    positionx_value = [point.positionx for point in point.select()]
    return positionx_value

def get_positiony():
    positiony_value = [point.positiony for point in point.select()]
    return positiony_value

# def m_map():
#     seleect = point.select()
#     store = {(point.positionx, point.positiony): point.name for point in seleect}
#     print(store)
#     width = 3
#     grid = 5
#     for x in range(grid):
#         for y in range(grid):
#             if (x, y) in store:
#                 print(store[(x, y)], end="-")
#             else:
#                 print(" " * width, end=" ")
#         print()

#pokus o vykreslení mapy dokáže pouze tohle
# {(0, 0): 'A', (0, 1): 'B', (0, 2): 'C', (1, 0): 'D', (1, 1): 'E', (1, 2): 'F', (2, 0): 'G', (2, 1): 'H', (2, 2): 'I'}
# A-B-C-
# D-E-F-
# G-H-I-


db.connect()
print("id =", get_idpoint())
print("name =",get_name())
print("position_x =",get_positionx())
print("position_y =",get_positiony())