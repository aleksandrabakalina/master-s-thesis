import os.path


def main():
    pass


def create_new_seg_header(seg_file_name, number_of_labels):
    with open(seg_file_name, 'w') as seg:
        seg.write('п»ї[PARAMETERS]\n')
        seg.write('SAMPLING_FREQ=22050\n')
        seg.write('BYTE_PER_SAMPLE=2\n')
        seg.write('CODE=0\n')
        seg.write('N_CHANNEL=1\n')
        seg.write('N_LABEL=' + str(number_of_labels) + '\n')
        seg.write('[LABELS]\n')


def create_new_seg(data, number_of_layer, seg_file_name):
    with open(seg_file_name, 'a') as seg:
        mark = 0
        mark2 = 0
        stringer = ''
        for j in data:
            mark2 = mark + (len(j))*2
            stringer = str(mark) + ',' + str(number_of_layer) + ',' + str(data[j]) + '\n'
            seg.write(stringer)
            mark = mark2
        stringer = str(mark) + str(number_of_layer) + '\n'
        seg.write(stringer)


def create_new_seg_from_seg(data, number_of_layer, seg_file_name):
    with open(seg_file_name, 'a') as seg:
        mark = 0
        mark2 = 0
        stringer = ''
        for j in data:
            mark = j
            stringer = str(mark) + ',' + str(number_of_layer) + ',' + str(data[j]) + '\n'
            seg.write(stringer)
        stringer = str(mark) + str(number_of_layer) + '\n'
        seg.write(stringer)


def read_seg(seg_file_name):
    with open(seg_file_name, 'r') as fl:
        seg = fl.readlines()

    return seg


def layer_boundaries_offset():

    main()