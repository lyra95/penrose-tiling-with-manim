.PHONY: copy execute

copy: execute
	cp ./media/images/scene/*.png ./

execute: scene.py
	manim -pql scene.py PenroseOne \

set: scene.py
	sed -i -E "s/DEPTH=[0-9]*/DEPTH=$(depth)/" scene.py