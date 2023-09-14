from turtle import *

#위치 조정
shape("classic")
penup()
setpos(-50,-250)
pendown()

#9각형
fillcolor("lightgreen")
begin_fill()
fd(75)
fd(75)
left(360/9)

for i in range(8):
    fd(75)
    stamp()
    fd(75)
    left(360/9)

end_fill()
#9각형 끝

#위치 조정
penup()
setpos(-45,-250)
pendown()

#8각형 시작
fillcolor("lightpink")
begin_fill()
fd(70)
fd(70)
left(360/8)

for i in range(7):
    fd(70)
    stamp()
    fd(70)
    left(360/8)
end_fill()
# 8각형 끝

#위치조정
penup()
setpos(-40,-250)
pendown()

#7각형 시작
fillcolor("darkorange")
begin_fill()
fd(65)
fd(65)
left(360/7)

for i in range(6):
    fd(65)
    stamp()
    fd(65)
    left(360/7)
end_fill()
#7각형 끝

#위치조정
penup()
setpos(-35,-250)
pendown()

# 6각형 시작
fillcolor("yellow")
begin_fill()
fd(60)
fd(60)
left(360/6)

for i in range(5):
    fd(60)
    stamp()
    fd(60)
    left(360/6)
end_fill()
#6각형 끝

#위치조정
penup()
setpos(-30,-250)
pendown()

# 5각형
fillcolor("blue")
begin_fill()
fd(55)
fd(55)
left(360/5)

for i in range(4):
    fd(55)
    stamp()
    fd(55)
    left(360/5)
end_fill()
#5각형 끝

#위치 조정
penup()
setpos(-25,-250)
pendown()

#4각형
fillcolor("lawngreen")
begin_fill()

for i in range(4):
    fd(50)
    stamp()
    fd(50)
    left(90)

#시작 지점 잔상
fd(5)
stamp()

end_fill()
#4각형 끝

#이름 남기기
hideturtle()
penup()
setpos(-20,100)
write("김선국", move=False, align ="left", font=("Arial", 25, "bold"))

done()