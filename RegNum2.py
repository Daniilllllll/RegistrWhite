from flet import *
import flet



Baza = Container(
    Container(
        Stack([
            Container(
                border_radius = 15,
                width=350,
                height=500,
                bgcolor="#dbd2c9",
            ),
            Container(
                ElevatedButton(
                    content=Text(
                        "SIGN IN",
                        color="White",
                        weight="w500",
                    ), width=280, bgcolor="black"
                ), padding=padding.only(35, 400),
            ),
            Container(
                TextButton(
                    content = Text(
                        "I forgot my password!",
                         color= "black",
                        weight= "w700",
                    ),                            
                ), padding=padding.only(95,450),
            ),
            Container(
                Column([
                    TextField(
                        width=280,
                        height=50,
                        border_radius= 20,
                        bgcolor="#dad1c4",
                        color="#635f5c",
                    ),
                ]), padding=padding.only(30, 240),
            ),
            Container(
                Stack([
                    Row([
                        Container(
                            Icon(
                                icons.LOCK_ROUNDED,
                                size = 30,
                                color="#95908c",
                            ),
                        ),
                    ]),
                ]), padding=padding.only(38,248),
            ),
            Container(
                Column([
                    TextField(
                        width=280,
                        height=50,
                        border_radius= 20,
                        bgcolor="#dad1c4",
                        color="#635f5c",
                    ),
                ]), padding=padding.only(30, 180),
            ),
            Container(
                Stack([
                    Row([
                        Container(
                            Icon(
                                icons.EMAIL,
                                size = 30,
                                color="#95908c",
                            ),
                        ),
                    ]),
                ]), padding=padding.only(38,188),
            ),
            Container(
                Stack([
                    Container(),
                    Text(
                        "Log in",
                        width=350,
                        size= 40,
                        color= "black",
                        weight="w700",
                    ),
                ]), padding=padding.only(30,100),
            ),
            Container(
                Stack([
                    Container(),
                    Text(
                        "Cannabis Lab",
                        width=350,
                        size= 20,
                        color= "#a19893",
                    ),
                ]), padding=padding.only(30,20),
            ),
            Container(
                Row([
                    TextButton(
                        content=Text(
                            "Sign up",
                            color="black",
                            width=350,
                            size=15,
                            weight="w500",
                        ),
                    ),
                ]), padding=padding.only(250, 20),
                
            ),
            Container(
                Stack([
                    Container(
                        border_radius = 15,
                        width=350,
                        height=180,
                        bgcolor="#1e1e1e",
                    ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "Discover",
                                    width=350,
                                    size= 25,
                                    # weight = "w700",
                                    color= "#c6c0be",
                                ),
                            ),
                        ]), padding=padding.only(230,120),
                    ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "C.A.B Joints",
                                    width=350,
                                    size= 30,
                                    # weight = "w700",
                                    color= "#c6c0be",                                 
                                ),
                            ),
                        ]), padding=padding.only(30,50),
                    ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "New in",
                                    width=350,
                                    size= 40,
                                    # weight = "w700",
                                    color= "white",                                 
                                ),
                            ),
                        ]), padding=padding.only(30,10),
                    ),
                ]), padding=padding.only(0, 520),
            ),
            Container(
                Stack([
                    Container(
                        border_radius = 15,
                        width=350,
                        height=700,
                        bgcolor="#ffffff",
                    ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "Join in",
                                    width=350,
                                    size= 20,
                                    weight = "w700",
                                    color= "Black",                                 
                                ),
                            ),
                        ]), padding=padding.only(230, 625),
                    ),
                    Container(
                        Stack([
                            Row([
                                Container(
                                        Icon(
                                            icons.ARROW_FORWARD_IOS,
                                            size = 30,
                                            color="black",
                                        ),
                                    ),
                                ]),
                            ]), padding=padding.only(300,627),
                        ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "New Store",
                                    width=350,
                                    size= 15,
                                    color= "#b6b6b6",
                                ),
                            ),
                        ]), padding= padding.only(266, 50),
                    ),
                    Container(
                        Stack([
                            Container(
                                Text(
                                    "Grand opening",
                                    width=350,
                                    size= 15,
                                    color= "#b6b6b6",
                                ),
                            ),
                        ]), padding= padding.only(235, 30),
                    ),
                    Container(
                        Stack([
                            Container(
                                border_radius = 150,
                                width=250,
                                height=250,
                                gradient=LinearGradient(["#fea056", "#fb7b0e"]),
                            ),
                            Container(
                                Stack([
                                    Container(
                                        border_radius = 15,
                                        width=175,
                                        height=680,
                                        bgcolor="transparent",
                                        blur=Blur(60,60,BlurTileMode.MIRROR),
                                    ),
                                    Container(
                                        Stack([
                                            Row([
                                                Container(
                                                    Text(
                                                        "C.A.B",
                                                        size = 15,
                                                        color="#b3b2ae",
                                                    ),
                                                ),
                                            ]),
                                        ]), padding=padding.only(73,640),
                                    ),
                                    Container(
                                        Stack([
                                            Row([
                                                Container(
                                                    Icon(
                                                        icons.SUNNY,
                                                        size = 30,
                                                        color="#b3b2ae",
                                                    ),
                                                ),
                                            ]),
                                        ]), padding=padding.only(75,600),
                                    ),
                                    Text(
                                        "Sun",
                                        width=175,
                                        size=60,
                                        # weight="w900",
                                        text_align="center",
                                        color="#242120",
                                    ),
                                    Container(
                                        Stack([
                                            Container(
                                                Text(
                                                    "Perm, Russia",
                                                    width=175,
                                                    size=15,
                                                    color="#242120",
                                                ),
                                            ),
                                        ]), padding=padding.only(32, 350),
                                    ),
                                    Container(
                                        Stack([
                                            Container(
                                                Text(
                                                    "Moldavskaya 8",
                                                    width=175,
                                                    size=15,
                                                    color="#242120",
                                                ),
                                            ),
                                        ]), padding=padding.only(32, 330),
                                    ),
                                    Container(
                                        Stack([
                                            Container(
                                                Text(
                                                    "18PM",
                                                    width=175,
                                                    size=15,
                                                    color="#242120",
                                                ),
                                            ),
                                        ]), padding=padding.only(30, 310),
                                    ),
                                    Container(
                                        Stack([
                                            Container(
                                                Text(
                                                    "10th",
                                                    width=175,
                                                    size=65,                                                   
                                                    # text_align="center",
                                                    color="#c6c0be",
                                                ), 
                                            ),
                                        ]), padding=padding.only(15, 60),
                                    ),
                                    
                                ]),padding=padding.only(-35, -210),
                            ),
                        ]),padding=padding.only(50, 220),
                    ),
                ]),padding=padding.only(450),
            ),
        ]),padding=padding.only(100, 100),
        
    ),
    
    width=1024,
    height=1024,
    gradient=LinearGradient(["#d8cac1", "#bcaca5"])
    
)


def main(page:Page):
    page.window_max_width = 1024
    page.window_max_height = 1024
    page.padding = 0
    page.add(Baza)
    


app(target=main)
