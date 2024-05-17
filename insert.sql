INSERT INTO point(name, positionx, positiony) VALUES 
("A", 0, 0),
("B", 0, 1),
("C", 0, 2),
("D", 1, 0),
("E", 1, 1),
("F", 1, 2),
("G", 2, 0),
("H", 2, 1),
("I", 2, 2);

INSERT INTO path(`length`, `left`, `right`, point_leftID, point_rightID) VALUES
(1, 1, 1, 1, 2),    #A -- B
(3, 1, 1, 2, 3),    #B -- C
(2, 1, 0, 4, 2),    #D <- B
(4, 1, 1, 5, 3),    #E -- C
(2, 1, 1, 5, 6),    #E -- F
(2, 1, 1, 7, 4),    #G -- D
(2, 1, 0, 7, 8),    #G <- H
(3, 1, 1, 8, 4),    #H -- D
(2, 0, 1, 8, 6),    #H -> F
(3, 1, 1, 9, 6);    #F -- I

#A 1
#B 2
#C 3
#D 4
#E 5
#F 6
#G 7
#H 8
#I 9