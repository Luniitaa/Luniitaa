from turtle import *
color('red','pink')
begin_fill()
while True:
	forward(600)
	left(570)
	if abs(pos()) < 1:
		break
end_fill()
done()