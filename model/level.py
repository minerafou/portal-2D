def GetLevel(num):
    if num == 1:
        return ['mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'ply', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'fin', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur']
    else:
        return ['mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'ply', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'fin', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur']


def CreateLevel(lvl_width, lvl_height):
        level_default = []
        for i in range(lvl_width):
            level_default.append("mur")
        for i in range(lvl_height -2):
            level_default.append("mur")
            for i in range(lvl_width - 2):
                level_default.append("air")
            level_default.append("mur")
        for i in range(lvl_width):
            level_default.append("mur")
        for i in range(310, 320):
            level_default[i] = ("mur")
        return level_default