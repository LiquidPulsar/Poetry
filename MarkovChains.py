import gzip,json,random
all_lines = []
for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
    all_lines.append(json.loads(line.strip()))
print("Phase 1: Finished Importing Data")

#print(list(map(lambda x: x["s"],__import__("random").sample(all_lines,10))))

def filter_data(id=19, data = all_lines): return list(filter(lambda x: int(x["gid"])==id, data))

def getlines(book): return [line["s"] for line in book]

def get_ids():
    seen = []
    for line in all_lines:
        if int(line["gid"]) not in seen:
            seen.append(int(line["gid"]))
    return seen

#print(x:=get_ids())
x=[19, 20, 26, 58, 109, 136, 151, 163, 207, 213, 214, 228, 230, 232, 246, 257, 258, 259, 261, 262, 263, 264, 266, 301, 304, 309, 312, 313, 315, 317, 323, 328, 348, 353, 390, 391, 392, 397, 400, 409, 413, 424, 438, 441, 442, 454, 458, 487, 574, 579, 591, 592, 594, 595, 596, 602, 610, 615, 617, 618, 651, 658, 679, 680, 691, 692, 703, 715, 772, 785, 791, 795, 835, 841, 845, 937, 941, 962, 981, 982, 995, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1019, 1020, 1021, 1030, 1031, 1034, 1035, 1040, 1041, 1042, 1045, 1054, 1057, 1062, 1141, 1151, 1165, 1166, 1186, 1199, 1211, 1229, 1238, 1246, 1247, 1279, 1280, 1287, 1304, 1317, 1321, 1322, 1333, 1358, 1365, 1381, 1382, 1383, 1393, 1418, 1459, 1469, 1471, 1505, 1506, 1525, 1543, 1544, 1545, 1567, 1568, 1612, 1645, 1664, 1719, 1727, 1728, 1731, 1745, 1746, 1830, 1847, 1852, 1855, 1894, 1919, 1924, 1934, 1953, 1958, 1962, 1974, 1978, 1995, 1996, 1997, 2002, 2003, 2008, 2080, 2136, 2151, 2161, 
2199, 2294, 2303, 2304, 2334, 2378, 2381, 2383, 2388, 2428, 2487, 2490, 2491, 2507, 2558, 2615, 2619, 2620, 2621, 2622, 2665, 2666, 2670, 2678, 2679, 2732, 2817, 2819, 2824, 2863, 2888, 2997, 3021, 3023, 3026, 3039, 3059, 3160, 3167, 3168, 3170, 3228, 3232, 3238, 3255, 3257, 3295, 3305, 3468, 3473, 3477, 3525, 3545, 3628, 3636, 3650, 3665, 3692, 3697, 3698, 3753, 3757, 3759, 4006, 4007, 4009, 4010, 4027, 4072, 4096, 4099, 4207, 4253, 4272, 4295, 4331, 4332, 4369, 4399, 4513, 4530, 4549, 4556, 4560, 4654, 4678, 4679, 4696, 4697, 4730, 4756, 4758, 5098, 5101, 5184, 5185, 5186, 5198, 5408, 5428, 5625, 5720, 6076, 6081, 6130, 6150, 6268, 6269, 6270, 6271, 6272, 6273, 6274, 6375, 6438, 6519, 6520, 6522, 6574, 6619, 6652, 6670, 6686, 6763, 6794, 6795, 6796, 6797, 6859, 6956, 7122, 7164, 7321, 7391, 7394, 7409, 7846, 7848, 7889, 7928, 7971, 8187, 8197, 8426, 8433, 8565, 8672, 8779, 8780, 8781, 8782, 8783, 8784, 8785, 8786, 8787, 8788, 8789, 
8790, 8791, 8792, 8793, 8794, 8795, 8796, 8797, 8798, 8799, 8800, 8820, 8905, 8912, 8930, 9093, 9372, 9388, 9399, 9465, 9575, 9576, 9577, 9578, 9579, 9580, 9612, 9825, 9842, 9870, 9889, 9989, 10122, 10140, 10469, 10493, 10557, 10602, 10671, 11014, 11073, 11101, 11150, 11333, 11351, 11435, 11439, 11689, 11985, 12109, 12116, 12241, 12242, 12286, 12413, 12475, 12664, 13086, 13118, 13167, 13213, 13646, 13647, 13648, 13649, 13650, 13983, 14005, 14019, 14020, 14410, 14460, 14495, 14531, 14591, 14757, 14869, 14906, 14959, 14993, 15370, 15390, 15524, 15529, 15553, 15612, 15618, 15809, 15834, 15937, 16059, 16081, 16251, 16265, 16362, 16376, 16436, 16452, 16568, 16632, 16686, 16688, 16904, 17102, 17104, 17135, 17192, 17254, 17270, 17283, 17364, 17382, 17393, 17448, 17568, 17604, 17630, 17764, 17779, 17933, 18007, 18238, 18287, 18396, 18466, 18500, 18619, 18720, 18908, 18937, 19084, 19096, 19170, 19221, 19226, 19363, 19385, 19389, 19482, 19525, 
19529, 19722, 19871, 20072, 20113, 20179, 20181, 20378, 20586, 20652, 20956, 21025, 21029, 21210, 21566, 21700, 21765, 21769, 21784, 21874, 22032, 22142, 22229, 22374, 22382, 22403, 22421, 22535, 22803, 22848, 22888, 23037, 23111, 23196, 23245, 23281, 23305, 23314, 23316, 23318, 23336, 23338, 23348, 23350, 23353, 23404, 23431, 23433, 23436, 23454, 23455, 23456, 23457, 23459, 23460, 23467, 23480, 23482, 23545, 23665, 23684, 23819, 23972, 24011, 24018, 24019, 24083, 24108, 24117, 24125, 24167, 24191, 24199, 24216, 24258, 24262, 24269, 24280, 24298, 24308, 24312, 24331, 24334, 24336, 24363, 24364, 24405, 24449, 24465, 24485, 24530, 24560, 24605, 24611, 24623, 24644, 24662, 24673, 24679, 24694, 24734, 24736, 24760, 24778, 24795, 24815, 24819, 24825, 24834, 24840, 24849, 24856, 24869, 24894, 25008, 25055, 25153, 25281, 25340, 25426, 25442, 25455, 25458, 25546, 25553, 25592, 25599, 25608, 25609, 25610, 25611, 25617, 25621, 25631, 25634, 25639, 25643, 25657, 25681, 25698, 25733, 25794, 25880, 25942, 25953, 25961, 25965, 25979, 26036, 26060, 26073, 26199, 26275, 26333, 26383, 26388, 26398, 26431, 26437, 26445, 26505, 26611, 26626, 26650, 26675, 26715, 26736, 26785, 26787, 26788, 26790, 26791, 26792, 26793, 26796, 26802, 26803, 26805, 26831, 26832, 26833, 26834, 26861, 26864, 26874, 26916, 26918, 26937, 27024, 27069, 27126, 27129, 27130, 27139, 27175, 27176, 27179, 27182, 27195, 27199, 27221, 27275, 27297, 27333, 27336, 27370, 27391, 27396, 27401, 27405, 27406, 27407, 27408, 27409, 27424, 27441, 27473, 27474, 27494, 27530, 27534, 27663, 27677, 27700, 27727, 27731, 27735, 27739, 27770, 27776, 27781, 27849, 27851, 27864, 27870, 27885, 27912, 27971, 28032, 28043, 28184, 28218, 28260, 28287, 28352, 28375, 28434, 28591, 28621, 28660, 28665, 28666, 28722, 28744, 28796, 28816, 28824, 28830, 28847, 28903, 29210, 29324, 29345, 29357, 29358, 29378, 29515, 29521, 29531, 29552, 29574, 29606, 29700, 29722, 29732, 29795, 29840, 29879, 29993, 30023, 30038, 30184, 30185, 30198, 30225, 30235, 30272, 30276, 30279, 30282, 30327, 30332, 30357, 30391, 30420, 30426, 30481, 30488, 30494, 30501, 30568, 30599, 30652, 30659, 30669, 30672, 30687, 30690, 30720, 30730, 30795, 30842, 31015, 31027, 31036, 31172, 
31184, 31272, 31283, 31303, 31304, 31305, 31314, 31342, 31466, 31467, 31486, 31591, 31594, 31706, 31712, 31726, 31764, 31874, 31877, 31878, 31890, 31896, 31913, 31919, 31926, 31928, 31959, 31967, 31968, 32030, 32091, 32099, 32110, 32145, 32146, 32153, 32167, 32184, 32190, 32210, 32233, 32262, 32275, 32276, 32277, 32335, 32373, 32445, 32452, 32456, 32458, 32459, 32477, 32491, 32493, 32499, 32503, 32523, 32528, 32532, 32553, 32767, 32772, 32778, 32944, 32986, 32990, 33023, 33073, 33089, 33112, 33149, 33150, 33156, 33171, 33193, 33363, 33417, 33441, 33456, 33457, 33486, 33533, 33552, 33553, 33555, 33629, 33658, 33674, 33681, 33686, 33691, 33730, 33732, 33758, 33768, 33770, 33774, 33786, 33792, 33855, 33902, 33940, 34001, 34015, 34027, 34050, 34113, 34117, 34159, 34163, 34215, 34227, 34234, 34235, 34237, 34269, 34298, 34331, 34409, 34438, 34665, 34741, 34752, 34762, 34780, 34790, 34821, 34870, 34936, 34966, 34982, 35033, 35051, 35059, 35098, 35115, 35174, 35188, 35190, 35193, 35227, 35243, 35260, 35279, 35287, 35357, 35394, 35402, 35411, 35452, 35475, 35479, 35497, 35515, 35524, 35536, 35546, 35553, 35612, 35667, 35714, 35777, 35779, 35780, 35848, 35903, 35907, 35922, 35991, 35996, 36005, 36038, 36051, 36068, 36091, 36094, 36098, 36135, 36137, 36149, 36150, 36153, 36168, 36214, 36287, 36305, 36321, 36337, 36441, 36501, 36508, 36543, 36617, 36618, 36620, 36637, 36661, 36664, 36702, 36737, 36770, 36773, 36782, 36803, 36831, 36841, 36865, 36913, 36915, 36916, 36925, 36935, 36954, 36980, 37074, 37085, 37086, 37087, 37091, 37132, 37154, 37155, 37188, 37213, 37214, 37323, 37365, 37366, 37367, 37371, 37375, 37414, 37452, 37469, 37510, 37518, 37529, 37542, 37543, 37556, 37557, 37648, 37649, 37655, 37690, 37718, 37751, 37752, 37804, 37810, 37845, 37852, 37859, 37860, 37861, 37867, 37938, 37980, 37999, 38011, 38052, 38071, 38135, 38174, 38230, 38275, 38407, 38410, 38438, 38463, 38468, 38475, 38503, 38511, 38520, 38529, 38549, 38550, 38562, 38565, 38566, 38572, 38594, 38599, 38741, 38766, 38839, 38856, 38857, 38877, 38880, 38898, 38902, 38927, 39028, 39032, 39037, 39128, 39131, 39132, 39198, 39236, 39475, 39494, 39496, 39499, 39614, 39626, 39638, 39656, 39741, 39750, 39783, 39784, 39796, 
39797, 39798, 39804, 39821, 39844, 39909, 40124, 40134, 40152, 40188, 40200, 40237, 40344, 40345, 40379, 40425, 40442, 40444, 40462, 40490, 40560, 40562, 40598, 40622, 40717, 40786, 40852, 40895, 40906, 41016, 41026, 41059, 41076, 41077, 41162, 41215, 41216, 41230, 41397, 41466, 41467, 41468, 41537, 41615, 41691, 41693, 41760, 41808, 41810, 41865, 41944, 41945, 41955, 41985, 42034, 42041, 42051, 42052, 42058, 42076, 42134, 42162, 42166, 42171, 42181, 42265, 42290, 42299, 42301, 42306, 42330, 42392, 42407, 42422, 42439, 42543, 42553, 42667, 42668, 43271, 43406, 44201, 45066, 45082, 45199, 45292, 45470, 47383, 48323]
lines = getlines(filter_data(random.choice(x)))
#print(len(lines),lines[:10])


def chain_repl(string,items,target):  
    if type(string) == str:
        if type(target) == list:
            if len(target) == len(items):
                action = lambda index: string.replace(items[index], target[index])
            else:
                raise IndexError("List of items and targets not the same length")
        elif type(target) == str:
            action = lambda index: string.replace(items[index], target)
        else:
            raise ValueError("Invalid target type")
        for index in range(len(items)):
            string = action(index)
        return string
    elif type(string) == list:
        return [chain_repl(elem,items,target) for elem in string]


fixed = lambda string: chain_repl(string,[elem for elem in '!?,.`;:"\'[]()'],"")
def rando():
    
    from collections import defaultdict
    map_ = defaultdict(lambda:[])

    #for index,word in enumerate(words:=fixed(" ".join(lines).split(" "))):
    for index,word in enumerate(words:=" ".join(lines).split(" ")):
        if index < len(words)-1:
            map_[word].append(words[index+1])
        else:
            map_[word].append("the")


    def randwalk(n=100, map_=map_, curr = random.choice(list(map_.keys()))):
        out = []
        for _ in range(n):
            try:
                curr = random.choice(map_[curr])
            except:
                print("yikes")
                curr = "the"
            out.append(curr)
        return " ".join(out)

        #return " ".join([curr:=random.choice(map_[curr]) for _ in range(n)])


    #print(list(filter(lambda x:map_[x]==[] ,list(map_.keys()))))
    vals = []
    for bit in list(map_.values()):
        for bop in bit:
            vals.append(bop)
    print(v:=[elem for elem in vals if elem not in list(map_.keys())])
    print(randwalk())

#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences


#print(lines)
#tokenizer = Tokenizer(num_words = 1000, oov_token = "<OOV>") #keeps a max number of words
#tokenizer.fit_on_texts(lines)
#sequences = tokenizer.texts_to_sequences(lines)
#print(sequences)
#print(pad_sequences(sequences))

import markovify
txtmodel = markovify.NewlineText("\n".join(lines),well_formed=False)

from wordtools import rhymes

from TIMER import trace_time
@trace_time
def f(word):
    return rhymes(word)

def make_v():
    global txtmodel
    s2 = False
    while not s2:
        s2 = txtmodel.make_sentence()
    return s2


biglist = " ".join(lines)
unique,nonunique = 0,0
def copycheck(sentence):
    global unique, nonunique
    #s = sentence.split()

    if sentence in biglist:
        nonunique+=1
        return None
    unique+=1
    #for index,word in enumerate(s[:-4]):
    #    if f"{word} {s[index+1]} {s[index+2]} {s[index+3]} {s[index+4]}" in biglist:
    #        #print(f"Copycat!! This line exists...")
    #        nonunique += 1
    #        return None
    ##print("UNIQUE!")
    #unique+=1


while True:
    lastword = lambda line : line.split(" ")[-1]
    #thing = [txtmodel.make_sentence() for _ in range(2)]
    print(s1:=make_v())
    #f(fixed(lastword(s1)))
    targetrhymes = set(rhymes(fixed(lastword(s1))))
    count = 0
    while True:
        s2 = make_v()
        copycheck(s2)

        count+=1
        if count > 1000 or fixed(lastword(s2)) in targetrhymes:
            print(s2)
            break
    if nonunique > 100:
        print(f"{nonunique} seen, {unique} unique")
x="""
The world needs men to battle for the gentle father who's with him there.
That art passed out with the shiny stair;
And oh, the hurt and the smile,
A visitor devoid of pomp or gaudy style,
But I hold to the youngster, cannot compare
Now the epicures may snicker and the baby! Oh, I know no lovelier pair,

When all of these are pleasant joys to set the eyes aglow;
And we have faith in Him although
That life has given from a grate fire's merry throng;
It is laughter and good-fellowship and song.
When the long day's mile;
Yet I must try for it bore the style
Though all of us agree.
Kings, to the tree.

And from her strength and skill for every test,
Speech seems so vain when sorrow's at my worst, but my very best;
There's nothing constant in the hazards which abound.
Is always to stop for the curious key kept high upon the ground.
Then came a day when they were pleased to write
Why never more shall Marjorie come to a sorry sight,
But once I stood.

The whole field of noon.
The tones of the moon,
And the woods of fruit,
I hear the passing flute?
"""
