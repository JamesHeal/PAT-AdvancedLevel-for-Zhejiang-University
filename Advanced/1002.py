#coding:utf-8
if __name__ == '__main__':
	#map()的用法，对每一个输入进行格式转换
    A = list(map(float, input().strip().split()))
    B = list(map(float, input().strip().split()))
    C = []

    tmp_length = int(max(A[1], B[1]) + 1)
    A_tmp = []
    B_tmp = []
    C_tmp = []
    for index in range(tmp_length):
        A_tmp.append(0)
        B_tmp.append(0)
        C_tmp.append(0)
    for A_index in range(int((len(A)-1)/2)):
        A_tmp[int(tmp_length-A[A_index*2+1]-1)] = A[(A_index+1)*2]

    for B_index in range(int((len(B) - 1)/2)):
        B_tmp[int(tmp_length-B[B_index*2+1]-1)] = B[(B_index+1)*2]

    for index in range(tmp_length):
        C_tmp[index] = A_tmp[index] + B_tmp[index]

    C.append(0)
    for C_index in range(len(C_tmp)):
        if C_tmp[C_index] != 0:
            C.append(int(tmp_length-C_index-1))
            C.append(C_tmp[C_index])

    C[0] = int((len(C)-1)/2)

    for index in range(len(C)):
        if index == 0:
            if int(C[index]) != 0:
                print(int(C[index]), end=' ')
            else:
                print((int(C[index])))
        elif index % 2 == 0:
            if index != len(C)-1:
                print('{:.1f}'.format(C[index]), end=' ')
            else:
                print('{:.1f}'.format(C[index]))
                print("end")
        else:
            print(int(C[index]), end=' ')

