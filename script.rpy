#background#
image bg_trainUB = im.Scale("bg/train urban.png", 1920, 1080)
image bg_trainCT = im.Scale("bg/train city.png", 1920, 1080)
image bg_classroomDAY = im.Scale("bg/classroom day.png", 1920, 1080)
image bg_classroonEL = im.Scale("bg/classroom early.png", 1920, 1080)
image bg_classroomRAIN = im.Scale("bg/classroom rain.png", 1920, 1080)
image bg_schoolFR = im.Scale("bg/school front.png", 1920, 1080)
image bg_schoolMT = im.Scale("bg/classroom day.png", 1920, 1080) ##เปลี่ยนพื้นหลัง## #meeting point school#
image bg_hallway = im.Scale("bg/classroom day.png", 1920, 1080)  ##เปลี่ยนพื้นหลัง## #hallway#
image bg_artclub = im.Scale("bg/classroom rain.png",1920, 1080) ##เปลี่ยนพื้นหลัง## #art club school#

#character#
image dad = im.Scale("char/dad.png", 693.3, 980.8) 
image tiwa = im.Scale("char/tiwa.png", 611.9, 865.6)
image lily = im.Scale("char/lily.png", 573, 810.6)
image beta = im.Scale("char/beta.png", 611.9, 865.6)
image grace = im.Scale("char/grace.png", 630.3, 891.66)

#cutscene asset#
image movie = Movie(size=(1920,1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

#define#
define m = "[player_name]"
define q = "???"
define mo ="แม่"
define d = "พ่อ"
define l = "แครล์ ลิลลี่"
define b = "เบต้า"
define g = "เกรซ"
define t = "ครูทิวา"

#variable#
default mompics = False
default r_lily = False

################################################

#################start here#####################
label start:
    #pause
    $ player_name = renpy.input("โปรดใส่ชื่อ")

label tenyrs:
    play music "audio/bgm/origin.mp3" fadein 1.0 volume 0.5
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
    play music "audio/bgm/urban.mp3" fadein 1.0 volume 0.5
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
    pause(5.0)
    hide movie with dissolve
    stop movie
    scene bg_trainCT with dissolve
    show lily at center with dissolve
    menu:
        "ขอโทษละกัน จะไม่โหวกเหวกโวยวายแล้วครับ":
            m "ขอโทษละกัน จะไม่โหวกเหวกโวยวายแล้วครับ"
            q "ถ้างั้นก็ดีเลยค่ะ"
            m "ช่วยนำทางผมไปโรงเรียนได้ไหม เอ่อ.."
            l "\"แครล์\".. \"แครล์ ลิลลี่\" ค่ะ ยังไงดิฉันจะเดินไปโรงเรียนอยู่แล้ว"
            l "ดิฉันไม่รังเกียจหรอกค่ะถ้าจะเดินตามมา"
            l "ก่อนอื่นเลยช่วยแต่งตัวให้เป็นระเบียบก่อนค่ะ"
            l "ถ้าจะเดินตามมาก็ช่วยเว้นระยะห่าง และก็อย่ามาสนทนากับดิฉันอีกนะคะ"
            hide lily with dissolve
            m "เอ่อ.. ขอบคุณ คิดว่านะ"
            m "\'..คนในเมืองเป็นแบบนี้หมดเลยหรอ\'" with wiperight
            m "\'แค่เสื้อผ้าหลุดลุ่ยนิดหน่อยเอง..\'" with wiperight
            $ r_lily = True
            scene black with dissolve
            stop music fadeout 2.0
            pause(3.0)
            jump meet_beta

        "ผมไม่ต้องให้เด็กมัธยมต้นมาเตือนหรอกนะ":
            m "เด็ก ม.ปลาย แบบผมไม่ต้องให้รุ่นน้องแบบคุณมาเตือนหรอกนะ"
            q "ถ้างั้นช่วยมีมารยาทให้สมกับเป็นเด็กมัธยมปลายด้วยค่ะ"
            l "นี่ถือว่าเป็นคำสั่งสอนจากเด็กมัธยมปลายด้วยกันนะคะ"
            m ".​.​.อย่างนี้นี่เอง เอ่อ.. คุณ.." with wiperight
            q "ช่วยรบกวนแต่งตัวให้เป็นระเบียบ แล้วอย่ามาสนทนากับดิฉันอีกนะคะ ขอตัวก่อนค่ะ" with wiperight
            hide lily with dissolve
            m "\'..คนในเมืองเป็นแบบนี้หมดเลยหรอ\'" with wiperight
            m "\'แค่เสื้อผ้าหลุดลุ่ยนิดหน่อยเอง..\'" with wiperight
            m "\'เอ๊ะ งั้นเราก็แอบตามเธอไปดีกว่า คิดว่าเธอคงเดินไปโรงเรียนนั่นแหล่ะ\'" with wiperight
            m "\'ฉลาดจริง ๆ ตัวฉัน!\'" with wiperight
            $ r_lily = False
            scene black with dissolve
            stop music fadeout 2.0
            pause(3.0)
            jump meet_beta


label meet_beta:
    play music "audio/bgm/beta version.mp3" fadein 1.0 volume 0.5
    scene bg_schoolFR with dissolve
    m "อย่างน้อยก็มาถึงโรงเรียนแล้วแฮะ ต้องขอบคุณคุณหนูนั่น ชื่ออะไรซักอย่างนี่แหละ" with wiperight
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
    scene black with dissolve
    pause(3.0)

label begeining:
    "หลังจากปฐมนิเทศเสร็จเป็นเวลา 30 นาที.​.." with wiperight
    scene bg_schoolMT with dissolve
    m "น่าเบื่อเป็นบ้า ต้องนั่งฟังผู้อำนวยการกว่าครึ่งชั่วโมง อยากวาดรูปจะตายอยู่แล้ว !" with wiperight
    show beta at center with dissolve
    b "ฉันก็คิดว่ามันน่าเบื่อน่ะน้า ~" with wiperight
    b "นี่ นายทำอะไรอยู่หรอ ?" with wiperight
    m "วาดรูปน่ะ" with wiperight
    b "เห.. ฉันก็ชอบวาดรูปเหมือนกัน ขอดูรูปของนายหน่อยได้ไหม" with wiperight
    menu:
        m "\'ให้ดูดีไหมนะ..\'" with wiperight
        "ให้ดู": 
            m "ได้สิ" with wiperight
            "\'คุณได้ยื่นรูปให้เธอ\'" with wiperight
            b "นี่นาย.. วาดรูปได้เก่งขนาดนี้เลยหรอ" with wiperight
            b "นายช่วยมากับฉันครู่นึงได้มั้ย" with wiperight
            m "เอ่อ.. ก็ได้อยู่หรอกนะ" with wiperight
            "เบต้ารีบคว้ามือ และวิ่งตรงไปยังห้องห้องหนึ่ง.." with wiperight
            b "\'ทำไมเธอต้องอึ้งขนาดนั้นด้วยนะ..\'" with wiperight
            scene black
            stop music fadeout 2.0
            jump artclub_beta
            
        "ไม่ให้ดู":
            m "ทำไมฉันต้องให้ดูด้วย" with wiperight
            b "นี่นายจะขี้หวงตั้งแต่เจอกันเลยหรอ" with wiperight
            b "ชิ" with wiperight
            m "เอ่อ เบต้า คุณครูเข้าคาบแล้วนะ" with wiperight
            show beta at right
            with move 
            b "!!!" with wiperight
            b "งั้นคงต้องขอตัวก่อนละกัน แล้วก็.." with wiperight
            b "คำว่าจังหายอีกแล้วนะ!" with wiperight
            hide beta with moveoutright
            m "\'จริงๆเลยนะ ผู้หญิงคนนี้..\'" with wiperight
            scene black
            stop music fadeout 2.0
            if r_lily == True:
                stop music fadeout 2.0
                jump artclub_lily
            elif r_lily == False:
                stop music fadeout 2.0
                jump artclub_grace

label artclub_beta:
    play music "audio/bgm/art of plight.mp3" fadein 1.0 volume 0.5
    scene bg_artclub with dissolve
    show beta at center with dissolve
    m "ที่นี่.. ห้องอะไรหรอ" with wiperight
    b "ห้องของชมรมศิลปะยังไงล่ะ!" with wiperight
    m "เบต้าไม่เหนื่อยเลยหรือไงนะ.." with wiperight
    b "ไม่นะ แล้วก็คำว่าจังหายอีกแล้วนะ" with wiperight
    m "จ้า เบต้าจังจ้า" with wiperight
    b "ต้องอย่างนี้สิ งั้นเข้าเรื่องเลยนะ" with wiperight
    b "นายช่วยเข้าชมรมศิลปะหน่อยสิ" with wiperight
    b "ฉันจะตอบแทนให้ด้วยการให้นายสอนวาดรูปกับเบต้าจังคนนี้" with wiperight
    m "ตรงไหนคือกำไรของฉันหรอ.." with wiperight
    b "เอาน่า ถ้านายเข้าชมรมศิลปะ นายจะได้สอนฉันวาดรูปด้วยไง" with wiperight
    m "\'เธอจะพูดวกไปวนมาทำไมนะ..\'" with wiperight
    m "ขอปฎิเสธ" with wiperight ######################################################
    b "ฉันก็คิดไว้อยู่แล้ว เพราะความจริงนายอยากจะอยู่กับเบต้าจัง.." with wiperight
    b "เดี๋ยว นายปฎิเสธหรอ" with wiperight
    m "ใช่" with wiperight
    b ". . ." with wiperight
    b "แล้วเธอจะเอาเวลาไหนมาสอนฉันหล่ะ ~"
    m "แล้วฉันบอกตอนไหนว่าจะสอนเธอ.. อ้าว เธอคือ เอ่อ.. คุณหนูแบร์ใช่มั้ย" with wiperight
    show beta at right with move
    show lily at left with dissolve
    m "ก่อนหน้านี้ฉันยังไม่ได้ขอบคุณที่นำทางมาโรงเรียนเลย" with wiperight
    l "ไม่ทราบว่าพูดกับใคร เรื่องอะไรหรอคะ? ดิฉันชื่อแครล์ค่ะ" with wiperight
    b "แหม นาน ๆ ทีจะเห็นคนกล้าแซวเจ้าหญิงลิลลี่ได้นะเนี่ย" with wiperight
    l "กรุณาเรียกว่าแครล์ด้วยค่ะ" with wiperight
    b "ว่าแต่วันนี้ลี่เดินมาโรงเรียนหรอ ปกติจะมีรถรับส่งไม่ใช่หรอ" with wiperight
    l "..วันนี้แค่อยากเดินน่ะค่ะ" with wiperight
    b "เห~ ไม่ใช่เพราะว่าสงสารเลยอยากเดินนำทางเด็กหนุ่มคนนี้มาโรงเรียนหรอกหรอคะคุณหญิงลิลลี่" with wiperight
    l "ชะ ชายคนนี้เขาเดินตามมาเองค่ะ" with wiperight
    b "แหม~ ลิลลี่ก็เป็นซะอย่างนี้ ปากไม่ตรงกับใจตลอดเลยนะ" with wiperight
    q "พอเลย ทั้งสองคน" with wiperight
    l "รบกวนรุ่นพี่เกรซช่วยอบรมเบต้ามากกว่านี้หน่อยนะคะ" with wiperight
    show beta at center with move
    show grace at right with dissolve
    b "วันนี้พร้อมหน้าพร้อมตาเลยนะเนี่ย" with wiperight
    l "หายากที่พี่เกรซจะเข้าชมรม" with wiperight
    b "ไหน ๆ ก็ไหน ๆ แล้ว ขอแนะนำสมาชิกคนที่ 4 ของเราเลยค่า!" with wiperight
    m "เดี๋ยว ๆ ผมไปตกลงตอนไหนเนี่ย" with wiperight
    g "เธอคือคนที่ได้โควต้าเข้าเรียนมาใช่มั้ย" with wiperight
    m "เอ่อ ใช่ครับ" with wiperight
    g "งั้นเธอก็คงเลี่ยงที่จะเข้าชมรมไม่ได้แล้วล่ะ" with wiperight
    g "ฉันชื่อ \'เกรซ\' อยู่ปีสองห้อง A ยินดีที่ได้รู้จัก" with wiperight
    m "ยินดีที่ได้รู้จักครับ.. เดี๋ยวก่อนนะ" with wiperight
    m "..ทำไมผมต้องเข้าชมรมด้วยล่ะ?" with wiperight
    q "เงื่อนไขของนักเรียนโควต้าน่ะ" with wiperight
    hide lily with dissolve
    show beta at left with move
    show grace at center with move
    show tiwa at right with dissolve
    b "สวัสดีค่า ~ ครูทิวา" with wiperight
    t "มากันครบแล้ว งั้นเรามาประชุมหารือกิจกรรมชมรมกันเลยดีกว่า" with wiperight

label artclub_lily:
    play music "audio/bgm/art of plight.mp3" fadein 1.0 volume 0.5
    scene bg_hallway with dissolve
    m "ในที่สุดก็คาบชมรมซักที !"  with wiperight
    m "ถ้าจำไม่ผิด เหมือนในจดหมายโควต้าของเรา เขาจะบังคับให้เราไปที่\'ชมรมศิลปะ\'ก่อนสินะ"  with wiperight
    m "ลืมไปเลยแฮะ ตอนนี้น่าจะยังทันแหล่ะ"  with wiperight
    m "มั้ง"  with wiperight
    m "อ้าว คุณหนู.. แบร์ ที่เจอเมื่อเช้านี่ !"  with wiperight
    show lily at center with dissolve
    l "แคร์ค่ะ ดิฉันชื่อ \'แครล์ ลิลลี่\' ค่ะ"  with wiperight
    m "เอ่อ คุณแครล์พอรู้มั้ย ว่าชมรมศิลปะอยู่ที่ไหน" with wiperight
    l "ไม่ทราบว่าคุณรู้อะไรบ้างคะ ?"  with wiperight
    m "\'ก็เป็นนักเรียนใหม่นี่หว่า\'"  with wiperight
    l "เอาเถอะค่ะ ดิฉันอยู่ชมรมศิลปะ"  with wiperight
    l "จะเป็นผลดีกับชมรมถ้ามีสมาชิกชายเพิ่มขึ้น อยู่ทางนี้ค่ะ"  with wiperight
    scene black with dissolve
    "คุณเดินตามแครล์ไป"  with wiperight
    scene bg_artclub with dissolve
    show lily at center with dissolve
    m "ก่อนหน้านี้ฉันยังไม่ได้ขอบคุณที่นำทางมาโรงเรียนเลย" with wiperight
    l "ไม่จำเป็นหรอกค่ะ" with wiperight
    b "แหม นาน ๆ ทีจะเห็นผู้ชายคุยกับเจ้าหญิงลิลลี่ได้นะเนี่ย" with wiperight
    show lily at right with move
    show beta at left with dissolve
    l "กรุณาเรียกว่าแครล์ด้วยค่ะ" with wiperight
    m "อ้าว เบต้านี่" with wiperight
    m "เธออยู่ชมรมนี้ด้วยหรอ" with wiperight
    b "ใช้แล้วล่ะ ฉันน่ะ รักการวาดรูปที่สุด !" with wiperight
    l "ถึงเธอจะวาดไม่ได้เลยก็ตาม" with wiperight
    b "ว่าแต่วันนี้ลี่เดินมาโรงเรียนหรอ ปกติจะมีรถรับส่งไม่ใช่หรอ" with wiperight
    l "..วันนี้แค่อยากเดินน่ะค่ะ" with wiperight
    b "เห~ ไม่ใช่เพราะว่าสงสารเลยอยากเดินนำทางเด็กหนุ่มคนนี้มาโรงเรียนหรอกหรอคะคุณหญิงลิลลี่" with wiperight
    l "ชะ ชายคนนี้เขาเดินตามมาเองค่ะ" with wiperight
    b "แหม~ ลิลลี่ก็เป็นซะอย่างนี้ ปากไม่ตรงกับใจตลอดเลยนะ" with wiperight
    q "พอเลย ทั้งสองคน" with wiperight
    l "รบกวนรุ่นพี่เกรซช่วยอบรมเบต้ามากกว่านี้หน่อยนะคะ" with wiperight
    show lily at center with move
    show grace at right with dissolve
    b "วันนี้พร้อมหน้าพร้อมตาเลยนะเนี่ย" with wiperight
    l "หายากที่พี่เกรซจะเข้าชมรม" with wiperight
    b "ไหน ๆ ก็ไหน ๆ แล้ว ขอแนะนำสมาชิกคนที่ 4 ของเราเลยค่า!" with wiperight
    m "เดี๋ยว ๆ ผมไปตกลงตอนไหนเนี่ย" with wiperight
    g "เธอคือคนที่ได้โควต้าเข้าเรียนมาใช่มั้ย" with wiperight
    m "เอ่อ ใช่ครับ" with wiperight
    g "งั้นเธอก็คงเลี่ยงที่จะเข้าชมรมไม่ได้แล้วล่ะ" with wiperight
    g "ฉันชื่อ \'เกรซ\' อยู่ปีสองห้อง A ยินดีที่ได้รู้จัก" with wiperight
    m "ยินดีที่ได้รู้จักครับ.. เดี๋ยวก่อนนะ" with wiperight
    m "..ทำไมผมต้องเข้าชมรมด้วยล่ะ?" with wiperight
    q "เงื่อนไขของนักเรียนโควต้าน่ะ" with wiperight
    hide lily with dissolve
    show beta at left with move
    show grace at center with move
    show tiwa at right with dissolve
    b "สวัสดีค่า ~ ครูทิวา" with wiperight
    t "มากันครบแล้ว งั้นเรามาประชุมหารือกิจกรรมชมรมกันเลยดีกว่า" with wiperight

label artclub_grace:
    "artclub_grace"
    pause(99.0)