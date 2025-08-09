from settings import TILE_SIZE, SCREEN_WIDTH

# FOREST
FP_Tile_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Forest/FP_Tile.png', "YBounce": 0.1, "XBounce": 1, "Friction": 0.3}

# OUTPOST
OP_Tile_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Outpost/OP_Tile.png', "YBounce": 0.2, "XBounce": 1, "Friction": 0.4}
OP_Background_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Outpost/OP_Background.png'}
D_Crystal_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Outpost/Dash_Crystal.png'}

# SEWER
SP_Tile_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Sewer/SP_Tile.png', "YBounce": 0.3, "XBounce": 1, "Friction": 0.5}
SP_Background_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Sewer/SP_Background.png'}
B_Data = {"Graphic": './GolfTower/Graphics/Finished/Sewer/B-1.png', "YBounce": 1, "XBounce": 1, "Friction": 1}

# ICE CAVE
IP_Tile_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Ice_Cave/IP_Tile.png', "YBounce": 0.4, "XBounce": 1, "Friction": 0.6}
Ice_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Ice_Cave/Ice.png', "YBounce": 0.2, "XBounce": 1, "Friction": 1}
IP_Background_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Ice_Cave/IP_Background.png'}

# Peak
PP_Tile_Data = {"Graphic": './GolfTower/Graphics/Placeholder/Peak/PP_Tile.png', "YBounce": 0.6, "XBounce": 1, "Friction": 0.8}

# SLOPES
SL_Data = {"Graphic": './GolfTower/Graphics/Placeholder/SL.png', "Facing": "Left"}
SR_Data = {"Graphic": './GolfTower/Graphics/Placeholder/SR.png', "Facing": "Right"}

HeightTracker = {"Graphic": './GolfTower/Graphics/Placeholder/Outpost/OP_Tile.png', "YBounce": 0.1, "XBounce": 1, "Friction": 0.3}


class Main:
    def __init__(self):
        self.tileData = {
            # Forest
            "0": FP_Tile_Data,
            "1": SL_Data,
            "2": SR_Data,

            # Outpost
            "5": D_Crystal_Data,
            "6" : OP_Tile_Data,
            "10": OP_Background_Data,

            # Sewer
            "7": B_Data,
            "9": SP_Tile_Data,
            "8": SP_Background_Data,

            # Ice Area
            "11": Ice_Data,
            "12": IP_Background_Data,
            "13": IP_Tile_Data,

            "141": PP_Tile_Data,

            # Decoration For Forest
            "37": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-00.png'},
            "38": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-01.png'},
            "50": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-02.png'},
            "51": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-03.png'},
            "39": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-04.png'},
            "40": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-05.png'},
            "41": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-06.png'},
            "42": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-07.png'},
            "43": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-08.png'},
            "44": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-09.png'},
            "45": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-10.png'},
            "46": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-11.png'},
            "47": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-12.png'},
            "48": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-13.png'},
            "49": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-14.png'},
            "34": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-15.png'},
            "35": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-16.png'},
            "36": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-17.png'},
            "31": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-18.png'},
            "32": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-19.png'},
            "33": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-20.png'},
            "52": {"Graphic": './GolfTower/Graphics/Finished/Forest/FP_Tile-21.png'},

            # Decoration For Outpost
            "53": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-00.png'},
            "54": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-01.png'},
            "55": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-02.png'},
            "56": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-03.png'},
            "57": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-04.png'},
            "58": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-05.png'},
            "59": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-06.png'},
            "60": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-07.png'},
            "61": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-08.png'},
            "62": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-09.png'},
            "63": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-10.png'},
            "64": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-11.png'},
            "65": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-12.png'},
            "66": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-13.png'},
            "67": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-14.png'},
            "68": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-15.png'},
            "69": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-16.png'},
            "70": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-17.png'},
            "71": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-18.png'},
            "72": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-19.png'},
            "73": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-20.png'},
            "96": {"Graphic": './GolfTower/Graphics/Finished/Outpost/OP_Tile-21.png'},

            # Decoration For Sewer
            "74": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-00.png'},
            "75": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-01.png'},
            "76": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-02.png'},
            "77": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-03.png'},
            "78": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-04.png'},
            "79": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-05.png'},
            "80": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-06.png'},
            "81": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-07.png'},
            "82": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-08.png'},
            "83": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-09.png'},
            "84": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-10.png'},
            "85": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-11.png'},
            "86": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-12.png'},
            "87": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-13.png'},
            "88": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-14.png'},
            "89": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-15.png'},
            "90": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-16.png'},
            "91": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-17.png'},
            "92": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-18.png'},
            "93": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-19.png'},
            "94": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-20.png'},
            "95": {"Graphic": './GolfTower/Graphics/Finished/Sewer/SP_Tile-21.png'},

            # Decoration For Ice Cave
            "97": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-00.png'},
            "98": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-01.png'},
            "99": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-02.png'},
            "100": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-03.png'},
            "101": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-04.png'},
            "102": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-05.png'},
            "103": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-06.png'},
            "104": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-07.png'},
            "105": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-08.png'},
            "106": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-09.png'},
            "107": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-10.png'},
            "108": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-11.png'},
            "109": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-12.png'},
            "110": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-13.png'},
            "111": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-14.png'},
            "112": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-15.png'},
            "113": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-16.png'},
            "114": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-17.png'},
            "115": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-18.png'},
            "116": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-19.png'},
            "117": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-20.png'},
            "118": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-21.png'},
            "142": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-22.png'},
            "143": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-23.png'},
            "144": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-24.png'},
            "145": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-25.png'},
            "146": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-26.png'},
            "147": {"Graphic": './GolfTower/Graphics/Finished/Ice_Cave/IP_Tile-27.png'},

            # Decoration For Peak
            "119": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-00.png'},
            "120": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-01.png'},
            "121": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-02.png'},
            "122": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-03.png'},
            "123": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-04.png'},
            "124": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-05.png'},
            "125": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-06.png'},
            "126": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-07.png'},
            "127": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-08.png'},
            "128": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-09.png'},
            "129": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-10.png'},
            "130": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-11.png'},
            "131": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-12.png'},
            "132": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-13.png'},
            "133": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-14.png'},
            "134": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-15.png'},
            "135": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-16.png'},
            "136": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-17.png'},
            "137": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-18.png'},
            "138": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-19.png'},
            "139": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-20.png'},
            "140": {"Graphic": './GolfTower/Graphics/Finished/Peak/PP_Tile-21.png'},

        }

        self.layers = { 
            'Layout' : './GolfTower/Levels/Main_Level/CSV/Main_Level_Layout.csv',
            'Slopes' : './GolfTower/Levels/Main_Level/CSV/Main_Level_Slopes.csv',
            'D_Crystal' :  './GolfTower/Levels/Main_Level/CSV/Main_Level_D_Crystal.csv',
            'Slime' :  './GolfTower/Levels/Main_Level/CSV/Main_Level_Slime.csv',
            'Decoration': './GolfTower/Levels/Main_Level/CSV/Main_Level_Decoration.csv',
            'Decoration2': './GolfTower/Levels/Main_Level/CSV/Main_Level_Decoration2.csv',
            'Decoration3': './GolfTower/Levels/Main_Level/CSV/Main_Level_Decoration3.csv'
        }

        self.levelHeight = 1000
        self.playerSpawn = (SCREEN_WIDTH*0.5 - 16, 990 * TILE_SIZE)


level = Main()

drawOrder = []
for i in level.layers:
    drawOrder.append(i)
drawOrder.append("Player")



