#character#
#background#
image bg_trainUB = im.Scale("bg/train urban.png", 1920, 1080)
image bg_trainCT = im.Scale("bg/train city.png", 1920, 1080)
image bg_classroomDAY = im.Scale("bg/classroom day.png", 1920, 1080)
image bg_classroonEL = im.Scale("bg/classroom early.png", 1920, 1080)
image bg_classroomRAIN = im.Scale("bg/classroom rain.png", 1920, 1080)

#character#
image dad = im.Scale("char/dad.png", 693.3, 980.8) 
image tiwa = im.Scale("char/tiwa.png", 630.3, 891.66)
image lily = im.Scale("char/lily.png", 573, 810.6)

#cutscene asset#
image movie = Movie(size=(1920,1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

#define#
define m = "[player_name]"
define q = "???"
define mo ="แม่"
define d = "พ่อ"
define l = "แครล์ ลิลลี่"

#start here#
label start:
    $ player_name = renpy.input("โปรดใส่ชื่อ")


label tenyrs:
    play music "audio/bgm/bgm01.mp3" fadein 1.0 volume 0.5

    #cut-scene mom1#
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #mom01#
    show movie with dissolve
    pause(2.0)

    m "ดูนี่สิครับแม่" with wiperight
    mo "สวยแบบนี้ วาดแม่สินะ" with wiperight
    mo "ลูกบอกแม่ได้ไหม ว่าลูกรักในการวาดรูปหรือเปล่า" with wiperight
    m "แน่นอนครับ ไม่ว่าจะเกิดอะไรขึ้น ผมก็จะสนุกกับการวาดรูปตลอดไปครับ !" with wiperight

    hide movie with dissolve
    stop movie

    #cut-scene mom2#
    scene black with dissolve
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #mom02#
    show movie with dissolve
    pause(4.5)

    mo "ถ้าวันหนึ่งแม่ไม่อยู่เป็นแบบให้ลูกวาดแล้ว สัญญากับแม่นะ ว่าจะไม่เลิกวาดรูปและสนุกกับมันเหมือนตอนนี้นะ" with wiperight
    m "แน่นอนครับ แต่แม่คงไม่หนีไปอยู่แล้วล่ะ จะแกล้งกันใช่มั้ยเล่า" with wiperight
    mo "แม่จะไม่หนีลูกไปไหนหรอกจ้ะ" with wiperight
    "แต่คำพูดของแม่ที่พูดออกมา เด็กหนุ่มไม่เคยคิดว่าจะเป็นคำพูดสุดท้ายที่เขาได้ยินจากปากแม่..." with dissolve
    hide movie with dissolve
    stop movie
    stop music fadeout 2.0
    pause(3.0)

label nineyrs:
    play music "audio/bgm/bgm02.mp3" fadein 1.0 volume 0.5
    "9 ปีถัดมา.." with dissolve
    pause(2.0)
    scene bg_trainUB with dissolve
    m "ผมไปเรียนแล้วนะครับพ่อ ไว้ถ้ามีโอกาสจะมาเยี่ยมบ่อย ๆ นะครับ" with wiperight
    show dad at right
    with moveinright
    d "อืม ตั้งใจเรียนด้วยล่ะ พ่อรู้อยู่แล้วล่ะ ว่าลูกต้องทำได้" with wiperight
    m "แค่โชคช่วยนั่นแหล่ะครับ" with wiperight
    show dad at center
    with move
    d "แม่ของแกพูดไว้เสมอว่าแกน่ะทำได้ ถึงตอนนี้แม่แกจะไม่อยู่แล้วก็เถอะนะ" with wiperight
    m "แม่ไม่ได้ไปไหนหรอกครับ แม่จะอยู่กับคุณพ่อและผมเสมอครับ" with wiperight
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #dad01#
    show movie with dissolve
    pause(5.0)  
    hide movie with dissolve
    stop movie
    scene bg_trainUB 
    show dad at center
    d "ไปดีมาดีนะ แล้วก็ขอบคุณสำหรับรูปนะ" with wiperight
    pause(3.0)

label meet_lily:
    scene bg_trainCT with dissolve
    m "ในที่สุดก็ถึงซักที ! จากบ้านนอกเข้าตัวเมืองนี่นานชะมัด" with wiperight
    m "นั่งวาดรูปตั้ง 4 ชม. ดินสอก็ใช้จะหมดแท่งแล้วสิเนี่ย.." with wiperight
    m "เห้อ.. หวังว่าที่โรงเรียนจะมีดินสอให้ใช้ฟรีนะ เอาล่ะ มาพยายามกันต่อดีกว่า !" with wiperight
    m "ว่าแต่ โรงเรียนมันไปทางไหนกันนะ.." with wiperight
    q "โหวกเหวก โวยวาย ไม่สมกับเป็นนักเรียนจากโรงเรียนเดียวกันเลยนะคะ เป็นไปได้ช่วยมีมารยาทหน่อยค่ะ" with wiperight
    show lily at right
    with moveinright
    m "เอ่อ. . ไม่ทราบว่าคุณอยู่โรงเรียนเดียวกับผมหรอครับ" with wiperight
    q "เกรงว่าจะใช่ค่ะ" with wiperight
    m "\'เหมือนจะเป็นเด็กประถมแฮะ..\'" with wiperight
    m ".​.​.อย่างนี้นี่เอง เอ่อ.. คุณ.." with wiperight
    l "แครล์... แครล์ ลิลลี่ ค่ะ" with wiperight
    pause(99)