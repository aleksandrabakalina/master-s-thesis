import os.path
from functions_for_audio import read_sbl_file
from collections import defaultdict
import struct
from seg_functions import create_new_seg
from seg_functions import create_new_seg_header
from seg_functions import read_seg
from diplom_functions import bad_phoneme
from diplom_functions import vowels_4_2
from diplom_functions import vowels_1
from diplom_functions import vowels_0
from diplom_functions import normal_cons

seg = r'C:\Users\Пользователь\Desktop\careva_100_files\cta0091-0100\cta0098.seg_B1'
seg1 = r'C:\Users\Пользователь\Desktop\careva_100_files\cta0091-0100\cta0098.seg_G1'
seg_2 = r'C:\Users\Пользователь\Desktop\careva_100_files\cta0091-0100\cta0098.seg_G2'
file = r'C:\Users\Пользователь\Desktop\careva_100_files\cta0091-0100\cta0098.sbl'

byte_rate = 2
sample_rate = 22050
n_channels = 1

signal, frames = read_sbl_file(file)

seg2 = read_seg(seg)  # читаем слой
seg3 = read_seg(seg1)  # читаем слой
seg4 = read_seg(seg_2)

clunk_phoneme_dic = ['s', "s'", 'p', "p'", 'k', "k'", 'sh', 't', "t'", 'f', "f'", 'ch', 'sc', 'h', 'h', 'c']
bad_phoneme_dic = ['z', "z'", 'g', "g'", 'd', "d'", 'zh', 'b', "b'"]

voc = defaultdict(lambda: defaultdict(float))

dic_seg2 = []
dic_seg3 = []
dic_seg4 = []
start_seg3 = 7
stop_seg3 = 0
number_seg3 = -1
start_seg4 = 7
stop_seg4 = 0
number_seg4 = -1

# блок 1
for i in range(7, len(seg2) - 1):
    mark1 = int(seg2[i].split(',')[0])
    mark2 = int(seg2[i + 1].split(',')[0])
    stringer = seg2[i].split(',')[2].strip('\n')

    phoneme = 1
    for j in clunk_phoneme_dic:
        if stringer == j:
            phoneme = -1
            break
    if stringer == '':
        phoneme = -2

    for j in bad_phoneme_dic:
        if stringer == j:
            phoneme = -3
            break

    interv_tuple = ()

    if phoneme == 1:
        mark_dic = []
        for k in range(start_seg3, len(seg3)):
            mark = int(seg3[k].split(',')[0])
            if mark1 <= mark <= mark2:
                mark_dic.append(mark)
                stop_seg3 = k
        dic_seg3.append(mark_dic)
        start_seg3 = stop_seg3 + 1
        number_seg3 = number_seg3 + 1

        interv_tuple += (mark1,)
        interv_tuple += (mark2,)
        interv_tuple += (stringer,)
        interv_tuple += (number_seg3,)
        interv_tuple += ('seg3',)

    elif phoneme == -1:
        mark_dic = []
        for m in range(start_seg4, len(seg4)):
            mark = int(seg4[m].split(',')[0])
            phone_3 = seg4[m].split(',')[2].strip('\n')
            if mark1 <= mark <= mark2:
                if phone_3 == '-' or phone_3 == 'x':
                    mark_dic.append(mark)
                    stop_seg4 = m
                elif phone_3 == '' and stop_seg4 == m - 1:
                    mark_dic.append(mark)
                    stop_seg4 = m

        dic_seg4.append(mark_dic)
        start_seg4 = stop_seg4 + 1
        number_seg4 = number_seg4 + 1

        interv_tuple += (mark1,)
        interv_tuple += (mark2,)
        interv_tuple += (stringer,)
        interv_tuple += (number_seg4,)
        interv_tuple += ('seg4',)

    elif phoneme == -3:
        variable = 0
        mark_dic = []
        for m in range(start_seg4, len(seg4)):
            mark = int(seg4[m].split(',')[0])
            phone_3 = seg4[m].split(',')[2].strip('\n')
            if mark1 <= mark <= mark2:
                if phone_3 == '-':
                    mark_dic.append(mark)
                    stop_seg4 = m
                    variable = 41
                elif variable == 41:
                    if phone_3 == '' and stop_seg4 == m - 1:
                        mark_dic.append(mark)
                        stop_seg4 = m
                        variable = 42
        if variable == 0:
            for k in range(start_seg3, len(seg3)):
                mark = int(seg3[k].split(',')[0])
                if mark1 <= mark <= mark2:
                    mark_dic.append(mark)
                    stop_seg3 = k
                    variable = 3
        if variable == 3:
            dic_seg3.append(mark_dic)
            start_seg3 = stop_seg3 + 1
            number_seg3 = number_seg3 + 1

            interv_tuple += (mark1,)
            interv_tuple += (mark2,)
            interv_tuple += (stringer,)
            interv_tuple += (number_seg3,)
            interv_tuple += ('seg3',)

        elif variable == 42:
            dic_seg4.append(mark_dic)
            start_seg4 = stop_seg4 + 1
            number_seg4 = number_seg4 + 1

            interv_tuple += (mark1,)
            interv_tuple += (mark2,)
            interv_tuple += (stringer,)
            interv_tuple += (number_seg4,)
            interv_tuple += ('seg4',)
        else:
            print('error')
    else:
        interv_tuple += (mark1,)
        interv_tuple += (mark2,)
        interv_tuple += (stringer,)
        interv_tuple += (-2,)
        interv_tuple += ('seg0',)

    dic_seg2.append(interv_tuple)

print(dic_seg2)
print(dic_seg3)
print(dic_seg4)

#  блок 2
for i in dic_seg2:
    allophone = i[2]
    n_seg = i[4]

    mark_tuple = ()

    if allophone == 's' or allophone == "s'" or allophone == 'k' or allophone == "k'" \
            or allophone == 'p' or allophone == "p'" or allophone == 'f' or allophone == "f'" \
            or allophone == 't' or allophone == "t'" or allophone == 'h' or allophone == "h'" \
            or allophone == 'sh' or allophone == 'ch' or allophone == 'sc' or allophone == 'c' \
            or (allophone == 'b' and n_seg == 'seg4') or (allophone == "b'" and n_seg == 'seg4') \
            or (allophone == 'g' and n_seg == 'seg4') or (allophone == "g'" and n_seg == 'seg4') \
            or (allophone == 'd' and n_seg == 'seg4') or (allophone == "d'" and n_seg == 'seg4') \
            or (allophone == 'zh' and n_seg == 'seg4') \
            or (allophone == 'z' and n_seg == 'seg4') or (allophone == "z'" and n_seg == 'seg4'):
        bad_phoneme(i, dic_seg4, mark_tuple, voc, signal, allophone)

    elif allophone == 'a4' or allophone == 'y4' or allophone == 'i4' or allophone == 'e4' \
            or allophone == 'o4' or allophone == 'u4' or allophone == 'a2' or allophone == 'y2' \
            or allophone == 'i2' or allophone == 'e2' or allophone == 'o2' or allophone == 'u2':
        vowels_4_2(i, dic_seg3, mark_tuple, voc, signal, allophone)

    elif allophone == 'a1' or allophone == 'y1' or allophone == 'i1' or allophone == 'e1' \
            or allophone == 'o1' or allophone == 'u1':
        vowels_1(i, dic_seg3, mark_tuple, voc, signal, allophone)

    elif allophone == 'a0' or allophone == 'y0' or allophone == 'i0' or allophone == 'e0' \
            or allophone == 'o0' or allophone == 'u0':
        vowels_0(i, dic_seg3, mark_tuple, voc, signal, allophone)

    elif allophone == 'l' or allophone == "l'" or allophone == 'm' or allophone == "m'" \
            or allophone == 'n' or allophone == "n'" or allophone == 'v' or allophone == "v'" \
            or allophone == 'j' \
            or (allophone == 'b' and n_seg == 'seg3') or (allophone == "b'" and n_seg == 'seg3') \
            or (allophone == 'g' and n_seg == 'seg3') or (allophone == "g'" and n_seg == 'seg3') \
            or (allophone == 'd' and n_seg == 'seg3') or (allophone == "d'" and n_seg == 'seg3') \
            or (allophone == 'zh' and n_seg == 'seg3') \
            or (allophone == 'z' and n_seg == 'seg3') or (allophone == "z'" and n_seg == 'seg3'):
        normal_cons(i, dic_seg3, mark_tuple, voc, signal, allophone)

    elif allophone == '':
        continue

    else:
        mark1 = i[0] // 2
        mark2 = i[1] // 2
        for e in range(mark1, mark2):
            mark_tuple += (signal[e],)
        voc[mark_tuple] = allophone

#  блок 3
out_signal = []
for i in voc:
    out_signal.append(i)

out_signal = sum(out_signal, ())

new_audio_sbl = r'C:\Users\Пользователь\Desktop\new_data\cta0098_11.05_0.sbl'

new_f = open(new_audio_sbl, 'wb')
n_channels = 1
byte_rate = 2
sample_rate = 22050
frames = len(out_signal)

fmt = str(frames) + 'h'
new_data = struct.pack(fmt, *out_signal)
new_f.write(new_data) and new_f.close()

filename, ext = os.path.splitext(new_audio_sbl)
new_seg = os.path.join(filename + '.seg_B1')
number_of_layer = 2  # номер слоя В1

create_new_seg_header(new_seg, len(voc))  # записываем шапку нового слоя
create_new_seg(voc, number_of_layer, new_seg)  # записываем новый слой
