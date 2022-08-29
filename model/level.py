def GetLevel(num):
    if num == 1:
        return ['mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'mlu', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur',
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mlu', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'owd', 'owd', 'owd', 'air', 'air', 'air', 'air', 'mld', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'owu', 'owu', 'owu', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'ply', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'lav', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'res', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owl', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owl', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owl', 'air', 'air', 'air', 'air', 'air', 'air', 'fin', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owr', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owr', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
                'mur', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'lav', 'air', 'air', 'air', 'air', 'owr', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'air', 'mur', 
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
        return level_default