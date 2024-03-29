import matplotlib.pyplot as plt

clauses = [
    [-50, -19, -95],
    [-71, 67, 194],
    [-16, -50, -110],
    [-182, 151, -230],
    [3, 113, 207],
    [-142, -173, -225],
    [-181, 235, 84],
    [-248, -197, -244],
    [191, 79, 132],
    [-114, -227, 67],
    [101, -109, 114],
    [-124, -142, -209],
    [-30, 215, -47],
    [-111, -66, 41],
    [-184, 176, -52],
    [143, 46, 36],
    [205, -246, 150],
    [-192, -52, 207],
    [104, 105, 166],
    [63, 215, -52],
    [-248, -27, 26],
    [65, 69, 207],
    [-177, 216, -244],
    [-18, -123, -154],
    [52, 140, 150],
    [-221, 69, -91],
    [1, -155, -136],
    [-232, 231, 228],
    [-190, -158, -189],
    [136, -172, 152],
    [-88, 174, -15],
    [-115, -157, -217],
    [95, 160, -201],
    [29, -5, 185],
    [-219, 163, 229],
    [22, 92, -104],
    [-239, 93, 224],
    [82, -34, 100],
    [132, -60, 10],
    [50, -73, 22],
    [7, 107, -99],
    [-110, -53, 101],
    [-50, -11, 151],
    [163, 83, -151],
    [220, 62, -231],
    [106, 168, 89],
    [205, -111, 141],
    [20, -48, 235],
    [-139, 184, -224],
    [5, -129, 238],
    [27, -162, 172],
    [147, 40, -212],
    [-103, -181, -149],
    [51, 206, -20],
    [34, -213, -38],
    [108, 65, 19],
    [-8, -55, -183],
    [-238, -241, -132],
    [131, 12, 83],
    [34, 250, -190],
    [67, -61, 41],
    [122, 166, -39],
    [-124, 191, -234],
    [183, -204, 212],
    [51, -184, -29],
    [195, -185, -52],
    [1, -196, 91],
    [-236, 13, -6],
    [87, 147, -218],
    [-247, 209, 184],
    [191, 127, 106],
    [58, -6, -101],
    [-146, -102, 126],
    [155, -6, -206],
    [157, -8, -188],
    [-163, 219, -54],
    [53, 41, -135],
    [237, 248, -201],
    [-168, -24, -114],
    [-224, -7, 193],
    [71, -6, 15],
    [-191, -9, 84],
    [140, -79, -18],
    [-21, 5, 134],
    [-249, 135, -222],
    [-60, -110, -77],
    [3, 229, -122],
    [-187, -185, 86],
    [171, 228, -35],
    [-10, 75, 43],
    [-188, -104, -229],
    [213, -190, 206],
    [-63, 158, -85],
    [91, 240, -220],
    [-104, 100, -174],
    [231, 4, 186],
    [129, 117, -136],
    [35, -193, 231],
    [189, 171, 25],
    [-176, -233, 15],
    [-222, 120, -190],
    [-161, -120, 222],
    [-209, -213, -141],
    [218, 36, 174],
    [-205, 6, -209],
    [-26, 199, 240],
    [191, 13, 152],
    [-68, 175, 59],
    [-120, -124, 32],
    [238, -230, 174],
    [160, -125, 21],
    [-168, 130, 184],
    [-246, -18, 221],
    [181, -58, -63],
    [163, -68, 210],
    [-120, 109, -160],
    [158, 98, 6],
    [-69, 28, 54],
    [43, 41, -138],
    [-190, 210, 171],
    [-128, 66, -92],
    [177, 75, 232],
    [217, 57, 4],
    [-31, -45, 193],
    [-7, 17, -21],
    [-118, -59, 192],
    [-117, 152, -209],
    [22, 35, 91],
    [-174, -17, 93],
    [-150, 125, 62],
    [79, -166, -148],
    [25, 191, 146],
    [-46, -93, 187],
    [47, -144, 174],
    [-187, -194, -191],
    [57, 129, 141],
    [-36, 163, -67],
    [72, 228, -105],
    [-236, -195, 229],
    [51, 199, -44],
    [-40, -233, 49],
    [216, 89, 157],
    [188, -95, 54],
    [-218, -77, -133],
    [-23, 69, 230],
    [15, -22, 61],
    [185, 15, 172],
    [124, -80, 219],
    [-43, -7, 136],
    [-245, 62, -191],
    [-141, -34, 151],
    [-151, 166, -62],
    [162, -42, 239],
    [-192, -144, -84],
    [227, 203, -106],
    [66, -35, 19],
    [-178, -165, -82],
    [-69, 18, -148],
    [-228, 221, -186],
    [-30, 184, 64],
    [196, 168, -12],
    [116, 101, -43],
    [-218, 171, 247],
    [161, -140, 231],
    [16, -213, -131],
    [97, 172, -211],
    [168, 114, 71],
    [-128, -22, -151],
    [84, -126, 174],
    [27, -86, -172],
    [103, -224, 158],
    [155, -13, 23],
    [-150, -87, -165],
    [62, 8, 33],
    [-193, -92, 11],
    [110, 159, 5],
    [-238, 177, -86],
    [-152, -125, 191],
    [-177, -73, -101],
    [-128, 56, -227],
    [230, 174, -183],
    [98, 40, 13],
    [177, -113, 142],
    [126, 109, -146],
    [242, 190, 147],
    [197, -5, -207],
    [-88, -210, 150],
    [104, 174, 176],
    [-166, -151, 229],
    [-75, -55, -6],
    [-28, 32, 83],
    [125, -31, -186],
    [-208, 51, -116],
    [-83, -141, 216],
    [-49, 109, 113],
    [99, -187, 67],
    [73, -111, -98],
    [197, -26, 169],
    [-161, 47, 248],
    [124, -2, 213],
    [37, 25, -26],
    [-197, -178, 91],
    [-15, 159, -34],
    [47, -199, 156],
    [-124, -173, 63],
    [190, -79, -244],
    [245, -10, -78],
    [158, -175, 89],
    [-152, 94, -47],
    [49, -148, -166],
    [-10, -131, 114],
    [-238, 107, -213],
    [222, -212, -46],
    [-171, -227, -83],
    [101, 85, -87],
    [-248, -154, 97],
    [-162, 134, -51],
    [-208, -10, -133],
    [38, 74, -4],
    [152, -3, 235],
    [148, -211, 202],
    [-60, -229, 146],
    [44, -99, 104],
    [24, 72, 157],
    [-105, 69, 186],
    [97, 185, 50],
    [-67, 236, -109],
    [156, -240, -74],
    [91, 15, 54],
    [-222, 164, -234],
    [-108, -64, -143],
    [225, 64, 141],
    [-133, 42, -161],
    [76, -79, 147],
    [62, 43, 219],
    [213, 20, 184],
    [-196, 129, 86],
    [-166, -78, 248],
    [170, -118, -208],
    [-191, 229, 225],
    [126, -176, 95],
    [-201, -49, -234],
    [240, -243, 117],
    [68, 67, 94],
    [168, -26, 223],
    [-25, -245, 128],
    [-235, -27, -39],
    [-200, -202, 247],
    [-77, 48, -137],
    [-39, 17, -161],
    [194, -76, -19],
    [95, 209, 163],
    [-136, 188, 154],
    [223, 241, -109],
    [-116, 125, -48],
    [-101, -110, -8],
    [35, -3, -44],
    [-126, -233, -69],
    [43, 62, -11],
    [181, 207, -8],
    [247, -13, 176],
    [143, -94, -83],
    [-83, 64, -133],
    [-233, -141, -33],
    [-60, -183, 191],
    [-106, -236, 122],
    [115, -90, 218],
    [-21, 136, -146],
    [15, 106, 154],
    [-61, -163, 142],
    [-204, 123, -79],
    [-125, 95, 219],
    [235, -59, 186],
    [-183, 220, -63],
    [174, -66, -172],
    [10, 78, 111],
    [-20, 180, -170],
    [214, -33, 112],
    [142, -31, 87],
    [-206, 194, -142],
    [144, 217, -76],
    [-152, -42, -172],
    [102, 159, 16],
    [-151, 243, -216],
    [-78, -104, -157],
    [135, 58, -63],
    [81, -233, -4],
    [112, -103, -81],
    [103, 38, 98],
    [-1, -157, -175],
    [-228, 233, -149],
    [162, 185, -17],
    [200, -73, -126],
    [-221, 38, 233],
    [-187, -180, -229],
    [-220, -91, 128],
    [203, 118, 149],
    [203, -109, -17],
    [-12, -227, -210],
    [25, -22, 249],
    [78, 171, -221],
    [-236, -162, 239],
    [247, 144, -75],
    [153, -189, 230],
    [-111, -106, -193],
    [-246, -151, -24],
    [-58, 35, 151],
    [-132, -75, 21],
    [212, 55, -144],
    [-156, 225, 62],
    [-21, 250, 191],
    [-101, 118, 105],
    [249, 122, -76],
    [126, -20, -131],
    [-243, -111, 195],
    [99, 203, 129],
    [-149, 112, 248],
    [64, 100, -188],
    [-15, 20, -116],
    [168, 211, 191],
    [236, -183, 164],
    [-199, -22, 203],
    [33, -104, 119],
    [244, -60, 245],
    [144, 139, 88],
    [-168, 6, 154],
    [44, -48, 93],
    [112, -37, 97],
    [160, -74, -110],
    [184, -143, 32],
    [100, -237, 227],
    [-187, 15, 25],
    [-196, -22, -70],
    [-169, -131, -150],
    [-15, 66, 176],
    [3, -248, -31],
    [244, -75, -7],
    [-209, 134, -226],
    [221, -68, -247],
    [160, 31, -163],
    [-131, -183, 8],
    [-77, 71, -227],
    [140, -28, -150],
    [106, -108, 91],
    [-226, 12, 65],
    [226, 18, 217],
    [-128, -164, 227],
    [176, -243, -164],
    [172, 212, 228],
    [-239, 86, 69],
    [-146, -36, 239],
    [-124, 69, 195],
    [-105, 33, 224],
    [176, 51, -144],
    [188, 222, 213],
    [-175, 7, -183],
    [23, 54, -230],
    [189, 178, -53],
    [195, 226, 67],
    [11, 201, -223],
    [192, 188, 232],
    [108, -46, -33],
    [-103, 212, -74],
    [123, 37, -230],
    [-89, 236, 2],
    [-201, -142, 145],
    [-104, -238, 78],
    [-141, 106, -13],
    [154, -79, -27],
    [210, 222, -64],
    [183, 236, 210],
    [-157, 165, -213],
    [-24, -2, -235],
    [-152, -224, 118],
    [-141, -34, -99],
    [79, 197, -172],
    [-200, -145, 17],
    [25, 186, -230],
    [-35, -166, -46],
    [163, 35, 243],
    [-219, 166, 155],
    [-101, 179, -55],
    [146, -194, 224],
    [-63, -14, -226],
    [-246, -182, -130],
    [-203, -200, -1],
    [-228, -56, -192],
    [-173, -231, 130],
    [191, 196, -99],
    [176, 106, -160],
    [175, 121, -99],
    [168, 226, -6],
    [-62, -177, -161],
    [168, -192, 5],
    [-208, -25, -161],
    [242, -232, -105],
    [229, -126, 95],
    [-204, -46, 24],
    [-149, -117, -144],
    [-70, -27, 246],
    [162, 171, -65],
    [-153, -28, 143],
    [-157, 185, 245],
    [49, -215, 149],
    [19, 94, 108],
    [-176, -43, -227],
    [-6, 229, 74],
    [-242, -240, 71],
    [-138, 196, -169],
    [132, 100, 10],
    [-122, 13, 34],
    [-36, 28, 177],
    [-16, -196, 178],
    [-113, -112, 177],
    [202, 150, 140],
    [117, 249, -162],
    [201, -54, -219],
    [242, -101, 54],
    [-69, -232, 98],
    [62, -109, -222],
    [-25, 89, 64],
    [-23, 223, -11],
    [-142, 192, -173],
    [-54, 212, 178],
    [-169, -37, -159],
    [70, 226, 34],
    [48, -183, 181],
    [-174, -32, -139],
    [136, -134, 108],
    [114, 208, 129],
    [48, -89, -171],
    [-136, -71, -137],
    [-152, -208, 90],
    [-65, 117, -223],
    [-63, -10, -178],
    [-64, -85, -94],
    [20, 183, 234],
    [-165, -100, -207],
    [20, 16, -228],
    [190, 191, 79],
    [-2, 213, -111],
    [171, -237, -32],
    [-106, 177, 92],
    [125, 105, 148],
    [-12, -153, 95],
    [233, 230, -232],
    [59, -123, -27],
    [168, -100, 82],
    [-80, 40, -235],
    [-40, -246, -62],
    [-237, 25, 220],
    [-60, 215, -219],
    [-225, 98, 65],
    [-62, -31, -128],
    [-9, -14, 8],
    [128, 38, -155],
    [-124, 133, -160],
    [-116, 195, 192],
    [-65, -247, 64],
    [-41, -131, 217],
    [175, 246, -242],
    [130, -191, 114],
    [-58, -60, -34],
    [69, 55, -116],
    [197, 20, 118],
    [-92, 183, -42],
    [35, 96, -213],
    [-124, 129, 171],
    [-168, 216, -115],
    [131, -164, 77],
    [54, 33, 44],
    [87, -139, -179],
    [-39, 85, 10],
    [70, -239, -27],
    [188, -178, -193],
    [178, 39, 2],
    [-89, 64, 233],
    [-192, -13, -5],
    [-45, 20, 55],
    [-236, 161, -171],
    [-30, -94, -92],
    [97, -57, 163],
    [119, -89, 24],
    [-58, 238, 214],
    [107, -126, -189],
    [-98, 12, 145],
    [-134, 82, 35],
    [-122, -147, -224],
    [9, -106, -134],
    [-172, -151, 67],
    [246, -220, -84],
    [84, 19, 128],
    [116, -125, 186],
    [-228, 58, 99],
    [-220, 121, -169],
    [-179, -143, -112],
    [93, 49, -54],
    [162, -122, 116],
    [9, -48, -142],
    [-239, 223, -64],
    [-68, 118, -136],
    [-203, 47, -78],
    [-130, 218, -128],
    [79, -217, -152],
    [249, -203, 187],
    [-203, 136, 139],
    [250, 148, 89],
    [-61, -179, 209],
    [158, -83, -119],
    [-133, -34, 184],
    [235, 186, -44],
    [38, 137, 151],
    [248, -169, 66],
    [-12, 50, 19],
    [-132, 45, -128],
    [249, -99, -192],
    [-79, 46, 201],
    [-16, -53, 135],
    [103, -224, 240],
    [128, -107, -230],
    [-127, 104, 155],
    [177, -106, -214],
    [222, 64, 18],
    [144, 111, 186],
    [-99, 102, -190],
    [-37, -174, -93],
    [78, -64, 8],
    [-6, 5, 216],
    [-165, 22, -85],
    [-209, -115, -193],
    [216, 91, 120],
    [-36, 180, -11],
    [73, 210, 133],
    [247, 191, -195],
    [196, -137, 71],
    [-119, 231, 182],
    [190, -80, -134],
    [86, -228, -67],
    [155, 228, -195],
    [-110, 24, 117],
    [162, -247, 74],
    [-18, 31, 177],
    [223, -14, 155],
    [-206, 168, 162],
    [-7, -206, 225],
    [144, -15, 98],
    [233, -212, 81],
    [-12, -201, -11],
    [-187, 150, 82],
    [-134, 66, -185],
    [-149, -81, 233],
    [-239, 24, 31],
    [217, 227, -117],
    [-200, 30, 103],
    [176, -157, -41],
    [74, 237, 32],
    [124, -92, 184],
    [134, -40, -246],
    [152, 97, -93],
    [215, 194, -69],
    [156, 179, 17],
    [28, 152, -211],
    [-18, -70, -1],
    [201, -29, 17],
    [239, -202, -111],
    [57, 156, -24],
    [173, 1, -35],
    [-104, 216, 9],
    [112, 236, 128],
    [56, 76, -155],
    [-176, -42, 83],
    [-129, -204, -162],
    [-205, 101, 175],
    [-105, -33, -104],
    [-157, 207, 200],
    [222, 175, -79],
    [-163, 115, 226],
    [-151, 134, -97],
    [-178, 220, -65],
    [-47, 194, 214],
    [129, 171, 53],
    [-7, -3, -10],
    [78, -136, -120],
    [-6, 143, 204],
    [23, 87, 137],
    [115, 35, -64],
    [-211, 178, 23],
    [-119, 149, -50],
    [-192, -47, -174],
    [81, 104, -33],
    [52, -19, 79],
    [-209, 236, -196],
    [-121, -185, 182],
    [199, -150, -125],
    [-70, 231, 121],
    [-187, -64, -158],
    [-55, 115, 216],
    [226, -222, -221],
    [215, 231, 243],
    [-32, -3, -153],
    [-167, -241, -85],
    [218, -191, 200],
    [-70, 173, -204],
    [-136, -169, -219],
    [-75, 201, -160],
    [89, -159, -230],
    [-15, -14, 187],
    [181, 137, -170],
    [20, 109, -18],
    [137, 218, 11],
    [-234, 147, 159],
    [-144, 246, -42],
    [147, 174, -17],
    [-186, -206, -229],
    [-72, 35, -24],
    [210, -28, 172],
    [-185, -15, 50],
    [12, -243, 109],
    [184, 182, 99],
    [-180, -39, 199],
    [-210, -230, -152],
    [67, -12, -217],
    [143, 173, -205],
    [202, -106, -163],
    [75, 32, -239],
    [87, 231, 119],
    [-148, 63, -107],
    [-29, 77, 158],
    [150, -211, -186],
    [79, 22, 208],
    [40, 169, 29],
    [-80, -87, 60],
    [205, -195, -154],
    [6, -16, -53],
    [-232, 24, 50],
    [118, -131, 223],
    [-115, -137, -244],
    [-58, -209, -151],
    [-6, 53, 88],
    [-175, 227, 220],
    [78, 120, 190],
    [30, -65, -96],
    [-205, -152, -23],
    [-181, -37, 97],
    [100, 48, 245],
    [-3, 159, -27],
    [186, 126, -76],
    [196, 45, -171],
    [181, -67, 220],
    [-200, 56, -104],
    [11, 226, -184],
    [57, -172, 61],
    [-27, 179, 43],
    [-119, 232, 133],
    [-56, 162, -87],
    [-11, 186, 46],
    [-213, 244, 127],
    [231, 117, -105],
    [83, 141, 94],
    [-195, -37, 53],
    [-223, 225, -242],
    [-187, -48, -37],
    [-198, -75, -210],
    [89, 141, -235],
    [3, 167, -187],
    [208, 94, -219],
    [-12, 91, -69],
    [221, -63, 155],
    [49, -101, -99],
    [129, 19, -90],
    [155, -94, -198],
    [42, -119, -219],
    [45, -132, 28],
    [-166, -213, 156],
    [-233, -82, 37],
    [-108, 237, -166],
    [77, 215, -6],
    [-197, -232, -112],
    [-60, -188, 44],
    [196, -151, 167],
    [137, -229, 127],
    [-74, -197, -228],
    [-65, -150, -8],
    [-176, 57, 37],
    [57, -219, -22],
    [-50, 80, -133],
    [-97, 219, 137],
    [87, -222, 227],
    [-202, -220, -185],
    [-85, 205, 34],
    [33, -49, -58],
    [118, -38, -20],
    [50, -102, 242],
    [32, -35, 74],
    [142, 26, -57],
    [-132, -120, -87],
    [213, 142, -182],
    [-100, 212, 144],
    [-224, 32, -68],
    [-137, 21, -207],
    [223, 155, 200],
    [-197, -146, 222],
    [-184, 242, -155],
    [168, 193, -207],
    [161, -35, 187],
    [234, -154, 156],
    [12, 119, -248],
    [141, 22, -189],
    [-65, -123, -193],
    [215, -9, -18],
    [-160, 156, 179],
    [148, -5, -23],
    [245, 120, 153],
    [204, 208, 134],
    [46, 142, -73],
    [-241, -246, 249],
    [-149, -197, 194],
    [-212, -203, 188],
    [188, 47, 66],
    [103, -200, -65],
    [-122, 141, 227],
    [-116, -161, -152],
    [230, -205, 183],
    [-7, 41, 181],
    [-74, -248, 137],
    [128, -135, 40],
    [-134, 68, 159],
    [-70, -33, -192],
    [133, -154, 103],
    [-124, -232, -133],
    [-20, -69, 14],
    [145, 152, -155],
    [-130, 110, 141],
    [217, 189, -196],
    [-44, 154, 7],
    [206, -118, -68],
    [57, 91, 131],
    [-56, 128, -46],
    [-139, -65, -38],
    [-158, -195, -115],
    [-6, -152, 169],
    [-186, -43, -25],
    [-93, -106, 20],
    [120, -153, -167],
    [179, -181, -135],
    [185, -82, -151],
    [111, -32, 139],
    [224, -175, -2],
    [157, -89, 177],
    [146, 213, -15],
    [-241, -96, -156],
    [-147, -157, 206],
    [-161, -48, -191],
    [-23, -113, 159],
    [99, 193, 233],
    [-94, 4, 118],
    [128, -24, 79],
    [71, 52, 188],
    [209, -171, -111],
    [-27, 39, 41],
    [164, 176, -242],
    [138, 232, -67],
    [51, -18, 247],
    [-44, -81, 2],
    [182, -243, -98],
    [-20, -236, -53],
    [-26, 19, 220],
    [237, 194, -148],
    [89, -142, 248],
    [-120, 234, 238],
    [33, 199, -143],
    [-83, 41, -149],
    [-146, 231, -29],
    [-189, 152, -186],
    [133, 101, 116],
    [-11, -123, -101],
    [-71, -199, 29],
    [-36, -160, -77],
    [156, -131, -15],
    [215, 144, 232],
    [53, 2, 177],
    [-28, 190, -135],
    [-246, 11, 209],
    [82, 191, 101],
    [156, 133, 88],
    [226, -195, -72],
    [-41, 119, 31],
    [140, -92, -233],
    [131, -235, 6],
    [47, 241, 133],
    [197, 98, 101],
    [-185, 117, 168],
    [-37, 195, 57],
    [167, 39, -244],
    [153, 194, -224],
    [-13, -143, -8],
    [68, -103, -33],
    [93, -214, 232],
    [244, 69, 156],
    [57, 173, -144],
    [-88, 175, 136],
    [67, -90, 91],
    [146, 14, 192],
    [154, 207, -213],
    [38, -10, -106],
    [84, -7, 196],
    [224, -12, 141],
    [158, 74, 179],
    [-130, -157, -98],
    [-100, 246, -118],
    [210, 59, -66],
    [245, -160, 93],
    [-27, -90, 75],
    [183, 194, -119],
    [-185, -183, 237],
    [-26, -139, -134],
    [-77, -134, 22],
    [142, -160, 243],
    [47, 160, 73],
    [-248, 91, -177],
    [150, 188, -158],
    [-117, -81, 17],
    [-27, 143, -242],
    [51, 94, 123],
    [13, 212, 221],
    [-175, 56, -124],
    [174, 88, -228],
    [195, 237, 54],
    [166, -4, 168],
    [15, 11, -26],
    [170, 94, -26],
    [-65, 27, -167],
    [209, -188, 121],
    [23, -185, 177],
    [-171, -168, -15],
    [196, -27, 203],
    [-157, -173, 4],
    [222, -237, 112],
    [175, -21, -139],
    [161, -150, 171],
    [246, 7, -187],
    [-110, 50, 131],
    [71, -111, 132],
    [128, -192, 56],
    [206, 180, 28],
    [38, -102, -94],
    [-26, -236, 196],
    [150, 211, 129],
    [-151, -132, 82],
    [-164, 140, -143],
    [-178, -229, -143],
    [196, 138, -248],
    [-101, 221, 128],
    [-118, -107, 233],
    [-32, 209, 224],
    [30, -81, -96],
    [-208, 37, -1],
    [-12, -193, 38],
    [26, -55, 214],
    [134, -229, 63],
    [-84, 226, 68],
    [234, -28, -2],
    [-239, -184, 135],
    [-176, 110, -198],
    [138, 169, -223],
    [-101, 55, -162],
    [-198, 108, -138],
    [119, -15, 193],
    [-31, -35, -166],
    [224, -102, -80],
    [65, 95, -2],
    [-76, 116, 160],
    [104, 250, 53],
    [-142, -221, -219],
    [-34, 72, -161],
    [-169, 80, 102],
    [8, 69, -52],
    [-198, 91, 88],
    [214, 231, 27],
    [-222, 157, -189],
    [137, 105, 138],
    [-208, -187, 60],
    [-152, -74, 52],
    [7, -125, -202],
    [8, -85, 194],
    [-113, -121, 15],
    [-155, -198, -124],
    [24, 126, 220],
    [6, -198, 76],
    [93, 2, 111],
    [245, -73, 172],
    [247, 50, -63],
    [114, 1, 10],
    [-135, -24, -8],
    [111, 107, -69],
    [-124, 173, 121],
    [-115, -242, -214],
    [-59, 116, -250],
    [-64, -56, -30],
    [181, 35, 221],
    [-120, -227, -184],
    [114, -81, -15],
    [152, -7, -81],
    [157, -235, 248],
    [-142, -227, -123],
    [93, 219, -177],
    [-83, -175, 141],
    [238, -212, 79],
    [-104, 43, -172],
    [66, 77, -149],
    [-106, -70, 60],
    [-141, 172, 246],
    [19, 141, 48],
    [7, -139, -36],
    [128, 30, 121],
    [-235, 146, 118],
    [103, -105, 188],
    [-158, -200, -6],
    [-1, -8, 123],
    [146, 29, -237],
    [-27, 135, -12],
    [-209, -1, -101],
    [-149, 93, 222],
    [-245, 17, -141],
    [-61, 9, 131],
    [-123, -195, -128],
    [-96, -21, 36],
    [-208, 24, 122],
    [-130, 92, -184],
    [56, 27, 240],
    [-29, -226, -212],
    [99, 82, -88],
    [15, 47, -218],
    [245, -118, -183],
    [-93, -99, -147],
    [182, -96, 87],
    [53, -54, 57],
    [-64, -56, 73],
    [-163, -190, -157],
    [175, -222, 45],
    [140, 50, 37],
    [90, 222, -74],
    [219, 60, -196],
    [-169, 40, -220],
    [-127, -163, 41],
    [-59, 86, 180],
    [-39, 34, 200],
    [20, -14, -71],
    [-75, -235, 96],
    [-129, -241, -95],
    [-248, 206, 159],
    [-193, 215, -203],
    [227, -177, -59],
    [56, 118, 210],
    [230, 96, -185],
    [31, 105, -52],
    [-191, 172, -241],
    [106, -2, -141],
    [183, 170, -51],
    [222, 127, -159],
    [194, 74, 191],
    [45, 101, 118],
    [235, 111, 187],
    [230, 33, -226],
    [-114, 2, -120],
    [136, 186, 195],
    [54, 73, 221],
    [-208, 14, 243],
    [127, -73, 185],
    [-88, 11, 28],
    [216, -135, -232],
    [-93, 197, 25],
    [-104, 66, -45],
    [-163, -140, 131],
    [189, 141, -137],
    [115, -247, 231],
    [-3, 47, -89],
    [-136, 216, 61],
    [221, 126, 211],
    [-222, 168, -113],
    [-222, -241, 219],
    [-73, 36, 61],
    [-5, -229, -128],
    [-7, -3, -148],
    [158, -234, 224],
    [39, 33, 184],
    [-160, -159, 216],
    [-67, -66, -102],
    [-145, 58, 93],
    [239, 7, -176],
    [51, -74, 14],
    [202, 133, -240],
    [-46, 172, -41],
    [156, 21, -245],
    [-14, -239, 194],
    [176, -73, 3],
    [-135, -81, 240],
    [15, -149, -141],
    [37, -5, -47],
    [-202, -28, -145],
]

values = {50: False, 19: True, 95: False, 71: True, 67: True, 194: True, 16: False, 110: False, 182: False, 151: False, 230: True, 3: False, 113: False, 207: False, 142: False, 173: False, 225: True, 181: False, 235: False, 84: False, 248: True, 197: False, 244: True, 191: False, 79: True, 132: False, 114: False, 227: True, 101: True, 109: True, 124: False, 209: True, 30: True, 215: True, 47: True, 111: False, 66: False, 41: False, 184: True, 176: True, 52: False, 143: False, 46: False, 36: True, 205: False, 246: True, 150: True, 192: False, 104: False, 105: False, 166: True, 63: False, 27: False, 26: False, 65: True, 69: False, 177: True, 216: True, 18: True, 123: False, 154: True, 140: True, 221: True, 91: True, 1: False, 155: True, 136: False, 232: True, 231: True, 228: False, 190: True, 158: True, 189: False, 172: False, 152: True, 88: False, 174: False, 15: False, 115: False, 157: False, 217: True, 160: True, 201: True, 29: True, 5: True, 185: True, 219: False, 163: False, 229: False, 22: False, 92: False, 239: False, 93: True, 224: True, 82: False, 34: False, 100: True, 60: True, 10: True, 73: False, 7: False, 107: False, 99: False, 53: False, 11: False, 83: False, 220: True, 62: True, 106: False, 168: True, 89: True, 141: False, 20: True, 48: True, 139: False, 129: True, 238: True, 162: False, 147: True, 40: False, 212: True, 103: False, 149: False, 51: True, 206: True, 213: False, 38: True, 108: False, 8: False, 55: True, 183: False, 241: True, 131: False, 12: True, 250: True, 61: False, 122: False, 39: False, 234: False, 204: False, 195: False, 196: True, 236: True, 13: False, 6: False, 87: False, 218: True, 247: False, 127: True, 58: False, 146: False, 102: True, 126: False, 188: True, 54: False, 135: False, 237: True, 24: True, 193: False, 9: False, 21: True, 134: False, 249: True, 222: False, 77: False, 187: False, 86: True, 171: True, 35: False, 75: True, 43: False, 85: False, 240: True, 4: False, 186: True, 117: True, 25: True, 233: True, 120: False, 161: False, 199: True, 68: False, 175: True, 59: False, 32: False, 125: False, 130: False, 210: False, 98: True, 28: False, 138: False, 128: True, 57: True, 31: False, 45: True, 17: False, 118: True, 148: True, 144: True, 72: False, 44: True, 49: True, 133: True, 23: True, 80: False, 245: True, 42: False, 203: False, 178: True, 165: False, 64: False, 116: False, 97: True, 211: False, 33: False, 159: False, 56: True, 242: True, 208: False, 169: False, 2: False, 37: True, 156: True, 78: False, 94: True, 74: False, 202: False, 164: False, 76: False, 170: True, 243: True, 223: False, 200: False, 137: True, 90: True, 180: True, 214: True, 112: True, 81: False, 153: False, 119: False, 70: True, 226: False, 145: False, 179: True, 14: True, 121: False, 96: False, 167: True, 198: False}

import sys

import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx

G = nx.DiGraph()
G.add_node("Root", level=1)

color_map = ["white"]

for index, clause in enumerate(clauses):
    name = "Clause #{}".format(index)
    G.add_node(name,level=2)
    G.add_edge("Root", name)

    result = False
    literal_colors = []

    for literal in clause:
        literal = int(literal)
        literal_absolute = abs(literal)
        literal_name = "Clause #{}, Literal #{}".format(index, literal)

        G.add_node(literal_name, level=3)
        G.add_edge(name, literal_name)

        if literal < 0:
            result |= not values[literal_absolute]
            literal_colors += ["green" if not values[literal_absolute] else "red"]
        else:
            result |= values[literal_absolute]
            literal_colors += ["green" if values[literal_absolute] else "red"]

    color_map.append("green" if result else "red")
    color_map.extend(literal_colors)


nx.draw(G, pos=graphviz_layout(G), node_size=25, #cmap=plt.cm.Blues,
    node_color=color_map,
    prog='dot')

#plt.draw()
#plt.show()

fig = plt.gcf()
fig.set_size_inches((12, 5))

plt.savefig("{}.png".format("figure"), format='png', dpi=280)
