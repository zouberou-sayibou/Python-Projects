from cs1graphics import*
#paper = Canvas(800,600, 'white', "HANGMAN")
def ground():
    return Path(Point(400,500),Point(50,500))
#paper.add(ground())
def standing_pole():
    return Path(Point(80,500),Point(80,50))
#paper.add(standing_pole())
def up_pole():
    return Path(Point(300,50), Point(78,50))
#paper.add(up_pole())
def rope():
    return Path(Point(280,50), Point(280,100))
#paper.add(rope())
def head():
    return Circle(30, Point(280, 130))
#paper.add(head())
def body():
    return Path(Point(280,160), Point(280, 350))
#paper.add(body())
def left_hand():
    return Path(Point(280,175), Point(240,235))
#paper.add(left_hand())
def right_hand():
    return Path(Point(320,235), Point(280,175))
#paper.add(right_hand())
def left_leg():
    return Path(Point(280,350), Point(240,405))
#paper.add(left_leg())
def right_leg():
    return Path(Point(320,405), Point(280,350))
#paper.add(right_leg())

