#background#
image bg_trainUB = im.Scale("bg/train urban.png", 1920, 1080)
image bg_trainCT = im.Scale("bg/train city.png", 1920, 1080)
image bg_classroomDAY = im.Scale("bg/classroom day.png", 1920, 1080)
image bg_classroonEL = im.Scale("bg/classroom early.png", 1920, 1080)
image bg_classroomRAIN = im.Scale("bg/classroom rain.png", 1920, 1080)
image bg_schoolFR = im.Scale("bg/classroom early.png", 1920, 1080) ##เปลี่ยนพื้นหลัง## #fornt school#
image bg_schoolMT = im.Scale("bg/classroom day.png", 1920, 1080) ##เปลี่ยนพื้นหลัง## #meeting point school#

#character#
image dad = im.Scale("char/dad.png", 693.3, 980.8) 
image tiwa = im.Scale("char/tiwa.png", 630.3, 891.66)
image lily = im.Scale("char/lily.png", 573, 810.6)
image beta = im.Scale("char/beta.png", 611.9, 865.6)

#cutscene asset#
image movie = Movie(size=(1920,1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

#prop#
image saved:
    size (150, 150)
    "prop/save1.png"
    align(0.1,0.1)
    pause(0.5)
    "prop/save2.png"
    pause(0.5)
    "prop/save3.png"
    pause(0.5)

#define#
define m = "[player_name]"
define q = "???"
define mo ="แม่"
define d = "พ่อ"
define l = "แครล์ ลิลลี่"
define b = "เบต้า"

#variable#
default mompics = False

################################################

screen save_icon():
    add "saved"

#################start here#####################
label start:
    #pause
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
    menu:
        mo "ลูกบอกแม่ได้ไหม ว่าลูกรักในการวาดรูปหรือเปล่า" 
        "แน่นอนครับ ไม่ว่าจะเกิดอะไรขึ้น ผมก็จะสนุกกับการวาดรูปตลอดไปครับ !":
            jump tenyrs_a
        "ผมเองก็ตอบแม่ได้ครับว่าวันนึงผมจะยังสนุกกับการวาดรูปอยู่ไหม..":
            jump tenyrs_b

label tenyrs_a:
    hide movie with dissolve
    stop movie
    scene black with dissolve
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #mom02#
    show movie with dissolve
    pause(4.5)
    mo "ถ้างั้นวันหนึ่งแม่ไม่อยู่เป็นแบบให้ลูกวาดแล้ว สัญญากับแม่นะ ว่าจะไม่เลิกวาดรูปและสนุกกับมันเหมือนตอนนี้นะ" with wiperight
    menu:
        mo "ถ้างั้นวันหนึ่งแม่ไม่อยู่เป็นแบบให้ลูกวาดแล้ว สัญญากับแม่นะ ว่าจะไม่เลิกวาดรูปและสนุกกับมันเหมือนตอนนี้นะ"
        "แน่นอนครับ":
            jump tenyrs_a1
        "ผมคงวาดไม่ได้ถ้าไม่มีแม่อยู่..":
            jump tenyrs_a2

label tenyrs_a1:
    m "แน่นอนครับ แต่แม่คงไม่หนีไปอยู่แล้วล่ะ จะแกล้งกันใช่มั้ยเล่า" with wiperight
    mo "แม่จะไม่หนีลูกไปไหนหรอกจ้ะ" with wiperight
    jump tenyrs_c

label tenyrs_a2:
    m "ผมวาดรูปก็เพื่อแม่ ถ้าแม่หนีผมไป.." with wiperight
    mo "แม่จะไม่หนีลูกไปไหนหรอกจ้ะ" with wiperight
    mo "เพราะอย่างนั้น ไม่ว่ายังไง ลูกต้องพยายามและสนุกกับมันเพื่อแม่นะ" with wiperight
    jump tenyrs_c

label tenyrs_b:
    hide movie with dissolve
    stop movie
    scene black with dissolve
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #mom02#
    show movie with dissolve
    pause(4.5)
    m "ผมคงวาดไม่ได้ถ้าไม่มีแม่อยู่.." with wiperight
    mo "มันเป็นสิ่งที่ลูกรักและสนุกกับมันใช่มั้ย" with wiperight
    m "ผม.." with wiperight
    mo "ถึงตอนนี้ ลูกต้องตอบคำถามนี้ด้วยตัวเองแล้วนะ" with wiperight
    mo "ถ้างั้นสัญญากับแม่นะ ว่าจะไม่เลิกวาดรูปและสนุกกับมัน ถ้าแม่ยังอยู่เคียงข้างลูก" with wiperight
    menu:
        mo "ถ้างั้นสัญญากับแม่นะ ว่าจะไม่เลิกวาดรูปและสนุกกับมัน ถ้าแม่ยังอยู่เคียงข้างลูก"
        "แน่นอนครับ":
            jump tenyrs_a1
        "ผมคงวาดไม่ได้ถ้าไม่มีแม่อยู่..":
            jump tenyrs_a2

label tenyrs_c:
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
    menu:
        m "\'เอาภาพวาดของแม่ให้พ่อดีไหมนะ?\'" with wiperight
        "ให้":
            m "แม่ไม่ได้ไปไหนหรอกครับ แม่จะอยู่กับคุณพ่อและผมเสมอครับ" with wiperight
            play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #dad01#
            show movie with dissolve
            pause(5.0)  
            hide movie with dissolve
            stop movie
            scene bg_trainUB 
            show dad at center
            d "ไปดีมาดีนะ แล้วก็ขอบคุณสำหรับรูปนะ" with wiperight
            scene black with dissolve
            pause(3.0)
            $ mompics = False
            jump meet_lily         

        "ไม่ให้":
            m "แม่ไม่ได้ไปไหนหรอกครับ แม่จะอยู่กับคุณพ่อและผมเสมอครับ" with wiperight
            m "ผมขอตัวก่อนนะครับ"
            show dad at center
            d "ไปดีมาดีนะ" with wiperight
            scene black with dissolve
            pause(3.0)
            $ mompics = True       
            jump meet_lily

label meet_lily:
    "4 ชั่วโมงต่อมา.."
    scene bg_trainCT with dissolve
    m "ในที่สุดก็ถึงซักที ! จากบ้านนอกเข้าตัวเมืองนี่นานชะมัด" with wiperight
    m "นั่งวาดรูปตั้ง 4 ชม. ดินสอก็ใช้จะหมดแท่งแล้วสิเนี่ย.." with wiperight
    m "เห้อ.. หวังว่าที่โรงเรียนจะมีดินสอให้ใช้ฟรีนะ เอาล่ะ มาพยายามกันต่อดีกว่า !" with wiperight
    m "ว่าแต่ โรงเรียนมันไปทางไหนกันนะ.." with wiperight
    q "โหวกเหวก โวยวาย ไม่สมกับเป็นนักเรียนจากโรงเรียนเดียวกันเลยนะคะ เป็นไปได้ช่วยมีมารยาทหน่อยค่ะ" with wiperight
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #lily01#
    show movie with dissolve
    pause(3.0)  
    m "เอ่อ. . ไม่ทราบว่าคุณอยู่โรงเรียนเดียวกับผมหรอครับ" with wiperight
    q "เกรงว่าจะใช่ค่ะ" with wiperight
    m "\'เหมือนจะเป็นเด็กประถมแฮะ..\'" with wiperight
    hide movie with dissolve
    stop movie
    scene bg_trainCT with dissolve
    show lily at right
    with moveinright
    m ".​.​.อย่างนี้นี่เอง เอ่อ.. คุณ.." with wiperight
    l "แครล์... แครล์ ลิลลี่ ค่ะ" with wiperight
    m "เอ่อ แครล์สินะ" with wiperight
    show lily at center
    with move
    l "คุณแครล์ค่ะ" with wiperight
    l "ช่วยรบกวนแต่งตัวให้เป็นระเบียบ แล้วอย่ามาสนทนากับดิฉันอีกนะคะ ขอตัวก่อนค่ะ" with wiperight
    hide lily with dissolve
    m "..คนในเมืองเป็นแบบนี้หมดเลยหรอ" with wiperight
    m "แค่เสื้อผ้าหลุดลุ่ยนิดหน่อยเอง.." with wiperight
    m "เอ๊ะ งั้นเราก็แอบตามเธอไปดีกว่า คิดว่าเธอคงเดินไปโรงเรียนนั่นแหล่ะ" with wiperight
    m "ฉลาดจริง ๆ ตัวฉัน" with wiperight
    scene black with dissolve
    stop music fadeout 2.0
    pause(3.0)

label meet_beta:
    play music "audio/bgm/bgm03.mp3" fadein 1.0 volume 0.5
    scene bg_schoolFR with dissolve
    m "อย่างน้อยก็มาถึงโรงเรียนแล้วแฮะ ต้องขอบคุณคุณหนู.​. แบร์ อะไรซักอย่างนี่แหละ" with wiperight
    m "ว่าแต่เธอหายไปไหนแล้วนะ.. ชั่งมันแล้วกัน ไว้ค่อยขอบคุณทีหลัง" with wiperight
    m "ถ้าได้เจอกันน่ะนะ" with wiperight
    m "ต่อไปก็ พิธีปฐมนิเทศสินะ เอาล่ะ ต้องไปทางไหนนะ.." with wiperight
    scene black with dissolve
    "15 นาทีถัดมา.." with wiperight
    scene bg_schoolMT with dissolve
    m "ที่นี่มันที่ไหนเนี่ย.." with wiperight
    q "เธอคงเป็นนักเรียนใหม่สินะ!" with wiperight
    m "เอ่อ.." with wiperight
    play movie "cs/mom1.ogv" loop ###เปลี่ยนคัทซีน### #beta01#
    show movie with dissolve
    pause(3.0) 
    b "ฉันชื่อ \"เบต้าจัง\" ว่าแต่นายชื่ออะไร อยู่ห้องอะไรหรอ?" with wiperight
    m "เอ่อ ฉันชื่อ \"[player_name]\" เหมือนว่าจะอยู่ห้อง B นะ" with wiperight
    m " \'ตอนแรกคิดว่าคนในเมืองจะเหมือนยัยคุณหนูนั่นทุกคนซะอีก\'" with wiperight
    hide movie with dissolve
    stop movie
    scene bg_schoolMT with dissolve
    show beta at center
    with dissolve
    b "อ้าว งั้นเราก็อยู่ห้องเดียวกันน่ะสิ เธอเรียกฉันว่า ‘เบต้าจัง’ ได้เลยนะ" with wiperight
    b "เดาว่านายคงไปประฐมนิเทศไม่ถูกใช่มั้ยล่ะ งั้นเดี๋ยวเบต้าจะพานายไปเอง!" with wiperight
    "เบต้าคว้ามือและรีบจูงไปยังสถานที่จัดพิธีปฐมนิเทศ" with wiperight
    m "เอ่อ ขอบคุณ เบต้า.." with wiperight
    b "เบต้าจังต่างหาก เบต้าจัง" with wiperight
    m "เบต้าจังสินะ.." with wiperight
    m "\'เป็นคนแปลกชะมัด\'" with wiperight