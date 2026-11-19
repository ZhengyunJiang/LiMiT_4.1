#cell 1

def neighbour_1(list0):
    i = 0
    while i < len(list0)-1:
        #print(i)
        if list0[i] == 1 and list0[i+1] == 1:
            return False
        i += 1
    while i == len(list0)-1:
        return True
#A = [1,1,3,4,5,1,2]
#neighbour_1(A)

def linker_cut(linker_l):    #linker长度切割，生成长度组合，生成长度数量组合
    #print('连接体长度为L为：',linker_l,'。')
    ll1 = linker_l + 1
    list0 = []
    set0 = set()
    list1 = []
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    i9 = 0
    i10 = 0
    i11 = 0
    i12 = 0
    i13 = 0
    i14 = 0
    i15 = 0
    i16 = 0
    i17 = 0
    i18 = 0
    i19 = 0
    i20 = 0
    if linker_l > 20:
        print('长度超过程序设计！！！')

    while i1 < ll1:
        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
        if ll2 > linker_l:
            i1 += 1
            i2 = 1
            if i1 == 1:
                AASDASD = 1
                #print('片段长度组合计算即将结束')
        else:
            while i2 < ll1:
                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                if ll2 > linker_l:
                    i2 += 1
                    i3 = 1
                    #if i2 == 1 and i1 ==0:
                        #print('i2开始计算') 
                else:
                    while i3 < ll1:
                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                        if ll2 > linker_l:
                            i3 += 1
                            i4 = 1
                            #if i3 == 1 and i1 ==0 and i2 ==0:
                                #print('i3开始计算')
                        else:
                            while i4 < ll1:
                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                if ll2 > linker_l:
                                    i4 += 1
                                    i5 = 1
                                    #if i4 == 1 and i1 ==0 and i2 ==0 and i3 == 0:
                                        #print('i4开始计算')
                                else:
                                    while i5 < ll1:
                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                        if ll2 > linker_l:
                                            i5 += 1
                                            i6 = 1
                                            #if i5 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0:
                                                #print('i5开始计算') 
                                        else:
                                            while i6 < ll1:
                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                if ll2 > linker_l:
                                                    i6 += 1
                                                    i7 = 1
                                                    #if i6 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0:
                                                        #print('i6开始计算') 
                                                else:
                                                    while i7 < ll1:
                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                        if ll2 > linker_l:
                                                            i7 += 1
                                                            i8 = 1
                                                            #if i7 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0:
                                                                #print('i7开始计算')
                                                        else:
                                                            while i8 < ll1:
                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                if ll2 > linker_l:
                                                                    i8 += 1
                                                                    i9 = 1
                                                                    #if i8 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0:
                                                                        #print('i8开始计算')
                                                                else: 
                                                                    while i9 < ll1:
                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                        if ll2 > linker_l:
                                                                            i9 += 1
                                                                            i10 = 1
                                                                            #if i9 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0 and i8 == 0:
                                                                                #print('i9开始计算')
                                                                        else:
                                                                            while i10 < ll1:
                                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                if ll2 > linker_l:
                                                                                    i10 += 1
                                                                                    i11 = 1
                                                                                    #if i10 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0 and i8 == 0 and i9 == 0:
                                                                                        #print('i10开始计算')                                                                                
                                                                                else:
                                                                                    while i11 < ll1:
                                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                        if ll2 > linker_l:
                                                                                            i11 += 1
                                                                                            i12 = 1
                                                                                            #if i11 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0 and i8 == 0 and i9 == 0 and i10 == 0:
                                                                                                ##print('i11开始计算') 
                                                                                        else:
                                                                                            while i12 < ll1:
                                                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                if ll2 > linker_l:
                                                                                                    i12 += 1
                                                                                                    i13 = 1
                                                                                                    #if i12 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0 and i8 == 0 and i9 == 0 and i10 == 0 and i11 == 0:
                                                                                                        #print('i12开始计算')                                                                                               
                                                                                                else:
                                                                                                    while i13 < ll1:
                                                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                        if ll2 > linker_l:
                                                                                                            i13 += 1
                                                                                                            i14 = 1  
                                                                                                            if i13 == 1 and i1 ==0 and i2 ==0 and i3 == 0 and i4 == 0 and i5 == 0 and i6 == 0 and i7 == 0 and i8 == 0 and i9 == 0 and i10 == 0 and i11 == 0 and i12 == 0:
                                                                                                                #print('片段长度组合计算中......') 
                                                                                                                asda = 1
                                                                                                        else:
                                                                                                            while i14 < ll1:
                                                                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                if ll2 > linker_l:
                                                                                                                    i14 += 1
                                                                                                                    i15 = 1
                                                                                                                else:
                                                                                                                    while i15 < ll1:
                                                                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                        if ll2 > linker_l:
                                                                                                                            i15 += 1
                                                                                                                            i16 = 1
                                                                                                                        else:
                                                                                                                            while i16 < ll1:
                                                                                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                                if ll2 > linker_l:
                                                                                                                                    i16 += 1
                                                                                                                                    i17 = 1
                                                                                                                                else: 
                                                                                                                                    while i17 < ll1:
                                                                                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                                        if ll2 > linker_l:
                                                                                                                                            i17 += 1
                                                                                                                                            i18 = 0
                                                                                                                                        else: 
                                                                                                                                            while i18 < ll1:
                                                                                                                                                ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                                                if ll2 > linker_l:
                                                                                                                                                    i18 += 1
                                                                                                                                                    i19 = 0
                                                                                                                                                else:
                                                                                                                                                    while i19 < ll1:
                                                                                                                                                        ll2 = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
                                                                                                                                                        if ll2 > linker_l:
                                                                                                                                                            i19 += 1
                                                                                                                                                            i20 = 0
                                                                                                                                                        elif  ll2 < linker_l:
                                                                                                                                                            i20 += 1
                                                                                                                                                        elif ll2 == linker_l:
                                                                                                                                                            if i1 != 0:
                                                                                                                                                                list0.append(i1)
                                                                                                                                                            if i2 != 0:
                                                                                                                                                                list0.append(i2)
                                                                                                                                                            if i3 != 0:
                                                                                                                                                                list0.append(i3)
                                                                                                                                                            if i4 != 0:
                                                                                                                                                                list0.append(i4)
                                                                                                                                                            if i5 != 0:
                                                                                                                                                                list0.append(i5)
                                                                                                                                                            if i6 != 0:
                                                                                                                                                                list0.append(i6)
                                                                                                                                                            if i7 != 0:
                                                                                                                                                                list0.append(i7)
                                                                                                                                                            if i8 != 0:
                                                                                                                                                                list0.append(i8)
                                                                                                                                                            if i9 != 0:
                                                                                                                                                                list0.append(i9)
                                                                                                                                                            if i10 != 0:
                                                                                                                                                                list0.append(i10)
                                                                                                                                                            if i11 != 0:
                                                                                                                                                                list0.append(i11)
                                                                                                                                                            if i12 != 0:
                                                                                                                                                                list0.append(i12)
                                                                                                                                                            if i13 != 0:
                                                                                                                                                                list0.append(i13)
                                                                                                                                                            if i14 != 0:
                                                                                                                                                                list0.append(i14)
                                                                                                                                                            if i15 != 0:
                                                                                                                                                                list0.append(i15)
                                                                                                                                                            if i16 != 0:
                                                                                                                                                                list0.append(i16)
                                                                                                                                                            if i17 != 0:
                                                                                                                                                                list0.append(i17)
                                                                                                                                                            if i18 != 0:
                                                                                                                                                                list0.append(i18)
                                                                                                                                                            if i19 != 0:
                                                                                                                                                                list0.append(i19)
                                                                                                                                                            if i20 != 0:
                                                                                                                                                                list0.append(i20)
                                                                                                                                                            a = tuple(list0)
                                                                                                                                                          #  #print(list0)
                                                                                                                                                            set0.add(a)
                                                                                                                                                            list0 = []
                                                                                                                                                            ll2 = 0
                                                                                                                                                            i19 += 1
    list1 = list(set0)
    print('linker长度为',linker_l,'的长度组合有：',len(list1),'种。  前30项为：',list1[:10])    #中英文翻译-中
    #print('Combinations of linker length',linker_l,'have',len(list1),'The top 10 items are',list1[:10])    #中英文翻译-英

    list4 = []
    for i in range(len(list1)):
        num1 = 1
        a = list(list1[i])
    #    if a.count(num1)<2 and neighbour_1(a):
        if neighbour_1(a):
            b = tuple(a)
            list4.append(b)
    print('去除包含连续两个或以上 1 的组合，长度为',linker_l,'的片段组合有：',len(list4),'种。',list4[:10])    #去除包含连续两个或以上 1 的组合    #中英文翻译-中
    #print('小单元长度的组合List0元素个数：',len(list4),'。')    
    #print('小单元长度的组合List0为：',list4,'。')    
    
    #print('Random combinations of linker length',linker_l,'have',len(list4),'The top 10 items are',list4[:10])    #去除包含连续两个或以上 1 的组合    #中英文翻译-英
    ##print('小单元长度的组合List0元素个数：',len(list4),'。')
    #print('All random combinations of linker length are',list4)    #中英文翻译-英
    c = []  #临时
    list5 = []   #转换碎片数
    for a in list4:
        b = list(a)
        for i in b:                       #新版Linker碎片参数
            if i == 1:
                c.append(7)
            elif i == 2:
                c.append(44)
            elif i == 3:
                c.append(88)
            elif i == 4:
                c.append(81)
            elif i == 5:
                c.append(45)
            elif i == 6:
                c.append(31)
            elif i == 7:
                c.append(4)
            elif i == 8:
                c.append(0)
            elif i == 9:
                c.append(0)
            elif i == 10:
                c.append(0)
            elif i == 11:
                c.append(0)
            elif i == 12:
                c.append(0)
            elif i == 13:
                c.append(0)
            elif i == 14:
                c.append(0)
            elif i == 15:
                c.append(0)            
            elif i == 16:
                c.append(0)
            elif i == 17:
                c.append(0)
            elif i == 18:
                c.append(0)
            elif i == 19:
                c.append(0)            
            if i == 20:
                c.append(0)
        d = tuple(c)
        c.clear()
        list5.append(d)
        
    #print('',len(list5),list5[:30])     
    print('全部组合数列表List1元素个数：',len(list5),'。')    #中英文翻译-中
    
    import numpy
    list6 = []
    for i in list5:
       # a = list(i)
        result1 = numpy.prod(i,dtype='int64')
        #print(i,result1)             #碎片单组合，该组合的总组合数
        list6.append(result1)         #各个组合的数量
    # 判断全部为正数
    arr6 = numpy.array(list6)
    all_positive = numpy.all(arr6 >= 0)

    '''if all_positive:
        print("✅list6所有数字都是正数或0")
    else:
        print("❌list6存在负数")
    print('每个碎片长度组合的组合数(前100)：',list6[:100])'''
    #all_count = numpy.sum(list6)      #总的组合数。大数报错
    all_count = sum(int(x) for x in list6)

    print('连接体长度为L为：',linker_l,'的各组合的组合数为：',len(list6),'。前30项数量分别为',list6[:30])
    print('组合总数为',all_count,', B_random随机抽取范围：[1,',all_count,']','。')
    
    return list4, list5, list6, all_count



#cell 2

def frag_combination(x, all_count, list6, list4, list5):    #产生随机数的个数；定位随机数位于第几个长度组合，第几个片段组合；片段代码组合
    import random    
    list7 = []
    lac = int(all_count)
    for i in range(x):
        b = random.randint(1,lac)
        list7.append(b)
    ##print(len(list7))


    i=0
    j=0
    a=[]
    list8=[]
    while i<int(len(list7)):
        x = list7[i]
        y = list6[j]
        if x<y:
            a.append(j)
            a.append(x)
            list8.append(a)
        #    #print(j,x)
            j=0
            a=[]    
        while x>y:
            x = x-y
            j=j+1
            y = list6[j]
            if x<=y:
                a.append(j)
                a.append(x)
                list8.append(a)
                j=0
                a=[]
                break
        i=i+1
    #print('随机数位于第几个长度组合，第几个片段组合',len(list8))    #随机数位于第几个长度组合，第几个片段组合
    
    
    frag = []
    list9 = []
    for x in list8:
        a=x[0]
        b=x[1]
        i=0
        if b<list5[a][0]:
            zfc = str(int(list4[a][0])) + '_' + str(int(b))
            frag.append(zfc)            
            list9.append(frag)
            frag = []
            while i < len(list5[a])-1:
                zfc = str(int(list4[a][i+1])) + '_1'
                frag.append(zfc)
                i = i + 1
              
        else:
            i=0
            c = b // list5[a][i]   #shang
            b = b % list5[a][i]  #yushu
            zfc = str(int(list4[a][i])) + '_' + str(int(b))
            frag.append(zfc)
            i=i+1
            #print('c',c,'a',a,'i',i,'list5',list5)     #?????????? Debug
            while i < len(list5[a]) and c > list5[a][i]:
                c = c//list5[a][i]   #shang
                b = c % list5[a][i]  #yushu
                zfc = str(int(list4[a][i])) + '_' + str(int(b))
                frag.append(zfc)
                i=i+1
              
            while i < len(list5[a]) and c == list5[a][i]:
      #          #print(b,c,x,list5[a][i])
                zfc = str(int(list4[a][i])) + '_0'
                frag.append(zfc)
      #          #print(zfc)
                while i < len(list5[a])-1:
                        zfc = str(int(list4[a][i+1])) + '_1'
                        frag.append(zfc)
                        i = i + 1
                list9.append(frag)
                frag = []
                i=0
                c=-2
                break
            
            while i < len(list5[a]) and -1 < c < list5[a][i]:
                zfc = str(int(list4[a][i])) + '_' + str(int(c))
                frag.append(zfc)
                while i < len(list5[a])-1:
                    zfc = str(int(list4[a][i+1])) + '_1'
                    frag.append(zfc)
                    i = i + 1
                list9.append(frag)
                frag = []
                i=0
                break

    #print('片段组合数list9，in cell 2：',len(list9),'list9前100：',list9[1:100])    #片段组合计算
    #print('随机数list7',list7,'随机数位于第几个长度组合，第几个片段组合list8', list8,'片段组合数list9', list9)

    return list7, list8, list9     #list7：随机数列表，list8：随机数对应linker长度组合编号和位置代码，list9片段组合列表


#cell 3

from glob import glob
from rdkit import Chem
from rdkit.Chem import AllChem
#from rdkit.Chem.Draw import IPythonConsole           #打包时注释掉
from rdkit.Chem.Draw import MolDrawing, DrawingOptions
import os

def combine2frag(asmi,Fr,bsmi,Cs):       #任意两个片段进行对接，允许两个片段同时存在两种接口
    Amol = Chem.MolFromSmiles(asmi)
    Bmol = Chem.MolFromSmiles(bsmi)
    combo = Chem.CombineMols(Amol,Bmol)
    Fr_NEI_ID=get_neiid_bysymbol2(combo,Fr)[0]
    Cs_NEI_ID=get_neiid_bysymbol2(combo,Cs)[-1]
    edcombo = Chem.EditableMol(combo)
    edcombo.AddBond(Fr_NEI_ID,Cs_NEI_ID,order=Chem.rdchem.BondType.SINGLE)
    Fr_id=[]
    Fr_id=get_id_bysymbol2(combo,Fr)
    Fr_ID=Fr_id[0]
    edcombo.RemoveAtom(Fr_ID)
    back = edcombo.GetMol()
    Cs_id=[]
    Cs_id=get_id_bysymbol2(back,Cs)
    edcombo=Chem.EditableMol(back)
    Cs_ID=Cs_id[-1]
    edcombo.RemoveAtom(Cs_ID)
    back = edcombo.GetMol()
    smi= Chem.MolToSmiles(back)
    return smi
    
def get_neiid_bysymbol2(combo,symbol):
    at_n=[]
    for at in combo.GetAtoms():
        if at.GetSymbol()==symbol:
            at_nei=at.GetNeighbors()[0]
            at_n.append(at_nei.GetIdx())
    return at_n

def get_id_bysymbol2(combo,symbol):
    at_Idx=[]
    for at in combo.GetAtoms():
        if at.GetSymbol()==symbol:
            at_Idx.append(at.GetIdx())
    return at_Idx

Fr='Fr'
Cs='Cs'
if os.path.exists('config.ini'):
    fh=open('config.ini')
    line=fh.readlines()[0].strip()
    Fr,Cs =line.split()



#cell 4

def frag_restriction_combination(E3,Target,list9,df_frag,zip_restriction):    #片段限制条件筛选，拼接，产物smiles不合理结构剔除
    '''zip_restriction = [['MolWt_restriction', [100,500]], ['HeavyAtomCount_restriction',[5,10]] .....]'''

    import pandas as pd
    import os

    #df_frag=pd.read_excel("linker-f-smiles.xlsx")   #############
    #print('zip_restriction',zip_restriction)
    rtt_dict_list = []
    list10=[]
    list_10=[]
    i_frag = 0
    fragdict=dict(zip(df_frag['Fragment_Num'],df_frag['smiles_[Fr][Cs]']))
    for rtt0 in zip_restriction:
        rtt0dict = dict(zip(df_frag['Fragment_Num'],df_frag[rtt0[0]]))
        #print('rtt0[0]',rtt0[0])#,'list9',list9)
        rtt_dict_list.append(rtt0dict)
    #print('Top 100 in linst9 cell 4:',list9[:100])
    for x in list9:
        for xi in x:
            list_10.append(fragdict[xi])
        #print('list_10',list_10)
           # x == ['3_74', '1_0', '2_42']
            
        for xii in range(len(rtt_dict_list)):
            rtt0_count = []
            for xi in x:
                rtt0_count.append(rtt_dict_list[xii][xi])
            if int(zip_restriction[xii][1][0]) <= int(sum(rtt0_count)) <= int(zip_restriction[xii][1][1]):
                i_frag += 1
                #print(x,rtt0_count,'满足要求','i_frag',i_frag,'zip_restriction[xii][1][0]',zip_restriction[xii][1][0],'zip_restriction[xii][1][1]',zip_restriction[xii][1][1])
            #else:
                #print(x,rtt0_count,'不满足要求','i_frag',i_frag,'zip_restriction[xii][1][0]',rtt0[1][0],'zip_restriction[xii][1][1]',zip_restriction[xii][1][1])
        #print('限制条件数 len(rtt_dict_list)',len(rtt_dict_list),'i_frag',i_frag)
        if i_frag == len(rtt_dict_list):
            list10.append(list_10)
            #print(x,'满足要求，纳入list10')
            list_10=[]
        else:
            list_10=[]
        i_frag = 0
    
#    print(len(list10))
    #print('满足Linker限制条件的碎片组合',list10[:30])
#len(list9) 500 [['3_74', '1_0', '2_42'], ['1_0', '2_42', '3_42'], ['2_23', '2_10', '2_10']

#    E3 = 'O=C1CCN(C(N1)=O)c2ccc([Fr])cc2'                    #拼接
#    Target = 'Cc1c([C@H](NC(c2nc(C(C)(C)C)on2)=O)C)ccc(c(n[nH]3)c4c3ncc(c5ccc([Cs])cc5)c4)c1'
    list11 = []
    a=0
    #print('len(list10)',len(list10),list10)
    ##print('len(list10[0])',len(list10[0]),list10[0][0:10])
    #print('len(list9)',len(list9),list9)
    while a < len(list10):
        list10[a].append(Target)
        #print('list10[a]',list10[a])
        midsmi = E3
        i = 0
        while i < len(list10[a]):
            #print(list10[a][i])
            midsmi = combine2frag(midsmi,Fr,list10[a][i],Cs)

            i += 1
        list11.append(midsmi)
        a += 1    
    #print('剔除错误结构前Linker SMILES',list11[:30])
    from rdkit import Chem    #Smiles中无效结构剔除   #产物smiles不合理结构剔除
    list_wrong = ['ON','OO','NN','OC(=O)O','OC(=O)N','nnO','nnN','onO','onN','noO','noN','C(=O)OC(=O)O','OC(=O)S','ClCO','FCO','BrCO','COCO']
    product_wrong = []
    product_correct = []
    for mol_smi in list11:
        mol_remain = Chem.MolFromSmiles(mol_smi)
        for wrong_smi in list_wrong:
            wrong_mol = Chem.MolFromSmarts(wrong_smi)
            if mol_remain.HasSubstructMatch(wrong_mol):
                product_wrong.append(mol_smi)
                break
    for mol_smi in list11:
        if mol_smi not in product_wrong:
            product_correct.append(mol_smi)
    #print('剔除错误结构后Linker SMILES',product_correct[:30])
    return product_correct



#cell 5

def smiles_descriptor(list_test):              #产物描述符计算模块
    import pandas as pd
    from rdkit import Chem, rdBase
    from rdkit.Chem import AllChem, MACCSkeys, QED,Descriptors, rdMolDescriptors, Lipinski
    from rdkit.ML.Descriptors import MoleculeDescriptors

    #list_test=['Cc1cc(-c2n[nH]c3ncc(-c4ccc(C5CC(CC(F)(F)c6ccc(N7CCC(=O)NC7=O)cc6)CN5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(OC5CC5n5ncnc5-c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(C)C(=O)C(C)C(=O)Oc5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(CNC(C(=O)C(=O)c5ccc(N6CCC(=O)NC6=O)cc5)C(C)(C)C)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(=O)C(C)OS(=O)(=O)C(F)(F)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(CCC(N)=O)C(=O)CC5CCCN5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(CNCC(C(F)(F)F)C(C)(C)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(CC(C)(C)CCc5ccc(N6CCC(=O)NC6=O)cc5)C(N)=O)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(F)(F)CC(C)C(CCC(N)=O)C(=O)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N(C)CC(=O)C(C)Cc5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N(C)CC(=O)N5CCCCC5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N(C)CC(=O)C5CCN(C)CC5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N(C)CC(=O)C(C(=O)c5ccc(N6CCC(=O)NC6=O)cc5)C(C)(C)C)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N5CCCCC5C(=O)C5CN(C)CCC5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(C)(C)NC(=O)C(Cc5ccc(N6CCC(=O)NC6=O)cc5)C(F)(F)F)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(-c5ncccc5C5CC(c6ccc(N7CCC(=O)NC7=O)cc6)CN5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(-c5ncccc5CC5CCCCN5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(C)C5CC5NC(=O)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(OCc5ccnc(-c6ccc(N7CCC(=O)NC7=O)cc6)c5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(C)C(=O)C(=O)C(=O)C(CCC(N)=O)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(CCC(N)=O)C(=O)N5CCOC(c6ccc(N7CCC(=O)NC7=O)cc6)C5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(N(C)CC(=O)N5CCCCC5c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(CCC(N)=O)C(=O)CC(=O)C(C)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(=O)COC(=O)Cc5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C5CCCN5C5CCCN5C(C)(C)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C5CCCCN5C(C)CC(C)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(C)(C)NC(=O)c5ccccc5-c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(=O)COC(CCC(N)=O)C(=O)c5ccc(N6CCC(=O)NC6=O)cc5)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1', 'Cc1cc(-c2n[nH]c3ncc(-c4ccc(C(=O)C(CC5CC(O)CN5c5ccc(N6CCC(=O)NC6=O)cc5)C(C)(C)C)cc4)cc23)ccc1[C@@H](C)NC(=O)c1noc(C(C)(C)C)n1']

    smiles = [x for x in list_test]
    mol_list = []    #smiles to mol
    for x in smiles:
        mol_list.append(Chem.MolFromSmiles(x))
    #print('描述符计算，输入分子数，SMILES：', len(mol_list), list_test)

    Descriptors.descList   #分子描述符列表
    descs = [desc_name[0] for desc_name in Descriptors.descList]
    desc_calc = MoleculeDescriptors.MolecularDescriptorCalculator(descs)
    result = []
    for i, mol in enumerate(mol_list):
        result.append(desc_calc.CalcDescriptors(mol))

    desc_df = pd.DataFrame(result)
    desc_df.columns = descs
    #desc_df.head(5)

    return desc_df

    '''产物限制条件列表：['MaxEStateIndex', 'MinEStateIndex', 'MaxAbsEStateIndex', 'MinAbsEStateIndex', 'qed', 
    'MolWt', 'HeavyAtomMolWt', 'ExactMolWt', 'NumValenceElectrons', 'NumRadicalElectrons', 'MaxPartialCharge', 
    'MinPartialCharge', 'MaxAbsPartialCharge', 'MinAbsPartialCharge', 'FpDensityMorgan1', 'FpDensityMorgan2', 
    'FpDensityMorgan3', 'BCUT2D_MWHI', 'BCUT2D_MWLOW', 'BCUT2D_CHGHI', 'BCUT2D_CHGLO', 'BCUT2D_LOGPHI', 
    'BCUT2D_LOGPLOW', 'BCUT2D_MRHI', 'BCUT2D_MRLOW', 'BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1', 
    'Chi1n', 'Chi1v', 'Chi2n', 'Chi2v', 'Chi3n', 'Chi3v', 'Chi4n', 'Chi4v', 'HallKierAlpha', 'Ipc', 'Kappa1', 
    'Kappa2', 'Kappa3', 'LabuteASA', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'PEOE_VSA12', 'PEOE_VSA13', 
    'PEOE_VSA14', 'PEOE_VSA2', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6', 'PEOE_VSA7', 'PEOE_VSA8', 
    'PEOE_VSA9', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4', 'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 
    'SMR_VSA8', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11', 'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 
    'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7', 'SlogP_VSA8', 'SlogP_VSA9', 'TPSA', 'EState_VSA1', 
    'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 
    'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'VSA_EState1', 'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 
    'VSA_EState4', 'VSA_EState5', 'VSA_EState6', 'VSA_EState7', 'VSA_EState8', 'VSA_EState9', 'FractionCSP3', 
    'HeavyAtomCount', 'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles', 'NumAliphaticRings', 
    'NumAromaticCarbocycles', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 
    'NumHeteroatoms', 'NumRotatableBonds', 'NumSaturatedCarbocycles', 'NumSaturatedHeterocycles', 'NumSaturatedRings', 
    'RingCount', 'MolLogP', 'MolMR', 'fr_Al_COO', 'fr_Al_OH', 'fr_Al_OH_noTert', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 
    'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0', 
    'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde', 
    'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 
    'fr_azide', 'fr_azo', 'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo', 'fr_dihydropyridine', 
    'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan', 'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole', 
    'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss', 'fr_lactam', 'fr_lactone', 'fr_methoxy', 
    'fr_morpholine', 'fr_nitrile', 'fr_nitro', 'fr_nitro_arom', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole', 
    'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 
    'fr_piperzine', 'fr_priamide', 'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 
    'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan', 'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea']'''





#cell 6

import math
import pickle
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
import os
import os.path as op
_fscores = None

def readFragmentScores(name='fpscores'):
    import gzip
    import os
    global _fscores
    
    #打包版
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # generate the full path filename:
    if name == "fpscores":
        file_name = "fpscores.pkl.gz"
        file_path = os.path.join(current_dir, file_name)
        #name = op.join(os.getcwd(), name)
        # name = op.join(op.dirname(__file__), name)
    data = pickle.load(gzip.open(file_path))
    '''

    #代码版
     #generate the full path filename:
    if name == "fpscores":
        name = op.join(os.getcwd(), name)
      #  # name = op.join(op.dirname(__file__), name)
    data = pickle.load(gzip.open('%s.pkl.gz' % name))
    '''
    
    #这个包在这里可以找到，复制到工作文件夹 
    #D:\ProgramData\Anaconda3\envs\my-rdkit-env-2\Library\share\RDKit\Contrib\SA_Score
    outDict = {}
    for i in data:
        for j in range(1, len(i)):
            outDict[i[j]] = float(i[0])
    _fscores = outDict


def numBridgeheadsAndSpiro(mol, ri=None):
    nSpiro = rdMolDescriptors.CalcNumSpiroAtoms(mol)
    nBridgehead = rdMolDescriptors.CalcNumBridgeheadAtoms(mol)
    return nBridgehead, nSpiro


def calculateScore(m):                                #计算SAscore
    if _fscores is None:
        readFragmentScores()
 
    # fragment score
    fp = rdMolDescriptors.GetMorganFingerprint(m,
                                            2)  # <- 2 is the *radius* of the circular fingerprint
    fps = fp.GetNonzeroElements()
    score1 = 0.
    nf = 0
    for bitId, v in fps.items():
        nf += v
        sfp = bitId
        score1 += _fscores.get(sfp, -4) * v
    score1 /= nf
 
    # features score
    nAtoms = m.GetNumAtoms()
    nChiralCenters = len(Chem.FindMolChiralCenters(m, includeUnassigned=True))
    ri = m.GetRingInfo()
    nBridgeheads, nSpiro = numBridgeheadsAndSpiro(m, ri)
    nMacrocycles = 0
    for x in ri.AtomRings():
        if len(x) > 8:
            nMacrocycles += 1
 
    sizePenalty = nAtoms**1.005 - nAtoms
    stereoPenalty = math.log10(nChiralCenters + 1)
    spiroPenalty = math.log10(nSpiro + 1)
    bridgePenalty = math.log10(nBridgeheads + 1)
    macrocyclePenalty = 0.
    # ---------------------------------------
    # This differs from the paper, which defines:
    # macrocyclePenalty = math.log10(nMacrocycles+1)
    # This form generates better results when 2 or more macrocycles are present
    if nMacrocycles > 0:
        macrocyclePenalty = math.log10(2)
 
    score2 = 0. - sizePenalty - stereoPenalty - spiroPenalty - bridgePenalty - macrocyclePenalty
 
    # correction for the fingerprint density
    # not in the original publication, added in version 1.1
    # to make highly symmetrical molecules easier to synthetise
    score3 = 0.
    if nAtoms > len(fps):
        score3 = math.log(float(nAtoms) / len(fps)) * .5
 
    sascore = score1 + score2 + score3
 
    # need to transform "raw" value into scale between 1 and 10
    min = -4.0
    max = 2.5
    sascore = 11. - (sascore - min + 1) / (max - min) * 9.
    # smooth the 10-end
    if sascore > 8.:
        sascore = 8. + math.log(sascore + 1. - 9.)
    if sascore > 10.:
        sascore = 10.0
    elif sascore < 1.:
        sascore = 1.0
 
    return sascore





#cell 7

def smiles_restriction(smiles_descriptor_result,zip_restriction_fn):
    #smiles_descriptor_result  DataFrame
    #zip_restriction_fn   List   ((rtt1,[0,3]),(rtt1,[0,5]),(...),(...),(...)....)
    import pandas as pd
    from rdkit import Chem  
    list_wrong = ['ON','OO','NN','OC(=O)O','OC(=O)N','nnO','nnN','onO','onN','noO','noN','C(=O)OC(=O)O','OC(=O)S','ClCO','FCO','BrCO','COCO']
    title_row = smiles_descriptor_result.columns
    smiles_screen = pd.DataFrame(columns=title_row)
    for i in range(len(smiles_descriptor_result)):
        ix = 0
        for rtt0 in zip_restriction_fn:
            if smiles_descriptor_result[rtt0[0]][i] < rtt0[1][0]  or rtt0[1][1] < smiles_descriptor_result[rtt0[0]][i]:
                ix += 1
        mol_smi = smiles_descriptor_result['Smiles'][i]
        mol_remain = Chem.MolFromSmiles(mol_smi)
        for wrong_smi in list_wrong:
            wrong_mol = Chem.MolFromSmarts(wrong_smi)
            if mol_remain.HasSubstructMatch(wrong_mol):
                ix += 1
                break
        if ix == 0:
            row_to_add = pd.DataFrame(smiles_descriptor_result.iloc[i]).T
            smiles_screen = pd.concat([smiles_screen, row_to_add], ignore_index=True)
            #smiles_screen.append(smiles_descriptor_result[i])
    #print('产物剔除错误前的smiles_screen', smiles_descriptor_result)
    #print('产物剔除错误后oo的smiles_screen', smiles_screen)
    return smiles_screen
    #smiles_screen   DataFrame




#cell 8


'''算法参数汇总循环计算，达到足够数量的符合要求的化合物'''

def Linker_Design(E3,
                  Target,
                  linker_lengh,
                  final_smiles_num,
                  zip_restriction,
                 zip_restriction_fn,
                 frag_onetime=50, 
                  Frag_All = 200000,
                  log_callback=None,        # [新增] 日志回调参数
                  smi_callback=None         # [新增] SMILES输出回调参数                 
                 ):

    frag_all=0          #合计计算组合数

    product_correct_smi_count=0         #合计符合linker要求的smiles

    from datetime import datetime
    import time
    import pandas as pd
    from rdkit import Chem
    smiles_screened_count=0         #合计符合产物限制条件的smiles
    smiles_final=[]        #符合产物限制条件的smiles存放

    list4=[]  #长度为linker_l的片段组合有
    list5=[]  #长度组合转换碎片数组合
    linker_frag_cut=[]
    list4, list5, linker_frag_cut, lac = linker_cut(linker_lengh)   # lac = linker_all_count    #linker_cut()输入linker的设计长度
  #  #print('设计长度的linker组合数前10个为：',linker_frag_cut[:10])
  #  #print('设计长度为：',linker_lengh,'的所有linker组合数为：',lac)
    #message = '设计长度的linker组合数前10个为：',linker_frag_cut[:10]    #中英文翻译-中
   # message = 'Top 10 fo the combinations of linker length are',linker_frag_cut[:10]    #中英文翻译-英
    #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
    #window.text_run.repaint()
    message = 'Top 10 fo the combinations of linker length are',linker_frag_cut[:10]
    if log_callback:                        # [新增]
        log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()

    message = 'Random combinations of linker length',linker_lengh,'have',lac
    if log_callback:                        # [新增]
        log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
        
    #message = '设计长度为：',linker_lengh,'的所有linker组合数为：',lac    #中英文翻译-中
   # message = 'Random combinations of linker length',linker_lengh,'have',lac    #中英文翻译-英
   # window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
   # window.text_run.repaint()
    
    import psutil
    import os
    import threading
    import time

    class ResourceMonitor:
        def __init__(self, interval=0.2):
            self.pid = os.getpid()
            self.proc = psutil.Process(self.pid)
            self.interval = interval
            self.max_cpu = 0.0
            self.max_mem_mb = 0.0
            self.running = False

        def _monitor_loop(self):
            while self.running:
                try:
                # CPU百分比（单核100%，8核最高800%）
                    cpu = self.proc.cpu_percent(interval=None)
                # RSS 物理内存，MB
                    mem = self.proc.memory_info().rss / 1024 / 1024

                    if cpu > self.max_cpu:
                        self.max_cpu = cpu
                    if mem > self.max_mem_mb:
                        self.max_mem_mb = mem
                except Exception:
                    pass
                time.sleep(self.interval)

        def start(self):
            self.running = True
            self.th = threading.Thread(target=self._monitor_loop, daemon=True)
            self.th.start()

        def stop(self):
            self.running = False
            self.th.join()
            return self.max_cpu, self.max_mem_mb
#资源监控
    monitor = ResourceMonitor(interval=0.2)
    monitor.start()
    t_start = time.time()


    import pandas as pd
    import os
    #打包版
    current_dir = os.path.dirname(os.path.abspath(__file__))
    aa_file_path = os.path.join(current_dir, "linker-f-smiles_new_202609.xlsx")
    df_frag=pd.read_excel(aa_file_path)   #构建片段字典

    '''
    #代码版
    df_frag=pd.read_excel("linker-f-smiles_new_202609.xlsx") #fragment imformation
    '''
    
    loca0=time.strftime('%Y-%m-%d %H-%M-%S')
    locatime0 = datetime.strptime(loca0, '%Y-%m-%d %H-%M-%S')
    print(f'开始时间：{loca0}\n'
          f'E3：{E3}\n'
          f'Target：{Target}\n'
          f'linker_lengh：{linker_lengh}\n'
          f'final_smiles_num：{final_smiles_num}\n'
          f'Linker限制条件zip_restriction：{zip_restriction}\n'
          f'产物限制条件zip_restriction_fn：{zip_restriction_fn}\n'
          f'frag_onetime：{frag_onetime}\n'
          f'Frag_All：{Frag_All}')
    if log_callback:                        # [新增]
        log_callback(f'开始时间：{loca0}\n'  # [修改] 原: print(...) 之后没有GUI输出，现在同步发日志
              f'E3：{E3}\n'
              f'Target：{Target}\n'
              f'linker_lengh：{linker_lengh}\n'
              f'final_smiles_num：{final_smiles_num}\n'
              f'Conditions of Linker：{zip_restriction}\n'
              f'Conditions of Product：{zip_restriction_fn}\n'
              f'frag_onetime：{frag_onetime}\n'
              f'Frag_All：{Frag_All}')


    
    #此处开始循环：
    j_turn = 0
    smiles_fn = pd.DataFrame()
    while final_smiles_num > smiles_screened_count:
        #print('final_smiles_num', final_smiles_num, 'smiles_screened_count', smiles_screened_count)
        random_list=[]
        ll_list=[]
        frag_com=[]
        random_list, ll_list, frag_com = frag_combination(frag_onetime, lac, linker_frag_cut, list4, list5)   #输入要产生的组合数量，ll组合总数，ll组合列表
        #print('片段组合数为：',len(frag_com))
        #message = '片段组合数为：',len(frag_com)    #中英文翻译-中
        message = 'Number of fragment combination',len(frag_com)    #中英文翻译-英
        #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
        #window.text_run.repaint()
        if log_callback:                        # [新增]
            log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()

        frag_all=frag_all+frag_onetime

        product_correct_smi = []
        product_correct_smi = frag_restriction_combination(E3,Target,frag_com,df_frag,zip_restriction)
        #frag_restriction_combination(E3,Target,list9,df_frag,zip_restriction)
        #print('符合linker要求的smiles产物数：',len(product_correct_smi))
        #message = f'第{j_turn+1}轮计算，符合linker要求的SMILES产物数：{len(product_correct_smi)}。'    #中英文翻译-中
        message = f'Calculation round {j_turn+1}. Number of SMILES meet the linker requirements: {len(product_correct_smi)}'    #中英文翻译-英
        #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
        #window.text_run.repaint()
        if log_callback:                        # [新增]
            log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
        product_correct_smi_count=product_correct_smi_count+len(product_correct_smi)
        
        if len(product_correct_smi) > 0:
            smiles_descriptor_screened = []
            smiles_descriptor_result = smiles_descriptor(product_correct_smi)
            
            smiles_descriptor_result.insert(0, "Smiles", product_correct_smi, allow_duplicates=False)
            
            mol_sascore_list = []
            for x in product_correct_smi:
                mol_sascore = calculateScore(Chem.MolFromSmiles(x))
                mol_sascore_list.append(mol_sascore)
            smiles_descriptor_result.insert(1, "SAscore", mol_sascore_list, allow_duplicates=False)
            
            smiles_screen = smiles_restriction(smiles_descriptor_result,zip_restriction_fn)
            if len(smiles_screen) > 0:
                #for i in range(len(smiles_screen)):
                    #x = pd.DataFrame(smiles_descriptor_result.iloc[i]).T
                    #smiles_fn = pd.concat([smiles_fn,x], ignore_index=True)
                #smiles_fn.append(smiles_screen, ignore_index=True)
                smiles_fn = pd.concat([smiles_fn,smiles_screen], ignore_index=True)
                #message = f'第{j_turn+1}轮计算，符合产物要求的smiles数：{len(smiles_screen)}。共计符合条件的smiles有：{len(smiles_fn)}条。'    #中英文翻译-中
                message = f'Calculation round {j_turn+1}. Number of SMILES meet the output requirements: {len(smiles_screen)}. Total number of output SMILES: {len(smiles_fn)}.'    #中英文翻译-英
                #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
                #window.text_run.repaint()
                if log_callback:                        # [新增]
                    log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
                smi_1 = ''
                for smi0 in smiles_fn['Smiles']:
                    smi_1= smi_1 + smi0 + '\n'
                #output1 = '输出标准的Smiles为：\n' + smi_1    #中英文翻译-中
                output1 = 'Output SMILES:\n' + smi_1    #中英文翻译-英
                #window.start_output.setText(output1)
                if smi_callback:                        # [新增]
                    smi_callback(output1)               # [修改] 原: window.start_output.setText(output1)
                
            else:
                #message = f'第 {j_turn+1}轮计算，没有SMILES符合产物要求'    #中英文翻译-中
                message = f'Calculation round {j_turn+1}, no SMILES meet the output requirements.'    #中英文翻译-英
                #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
                #window.text_run.repaint()
                if log_callback:                        # [新增]
                    log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
            
        j_turn += 1
        #print('final_smiles_num',final_smiles_num)
        if len(smiles_fn) >= final_smiles_num:
            message = f'共计计算{len(smiles_fn)}个有效Smiles，计算结束。'    #中英文翻译-中
            message = f'Total {len(smiles_fn)} working SMILES been found. Calculation completed. For more functions and higher computing efficiency, please contact the author.'    #中英文翻译-英
            #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
            #window.text_run.repaint()
            if log_callback:                        # [新增]
                log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
            break

        if frag_all > lac:
            print('组合数已超过设计，循环终止。')
            #message = f'共计计算{len(smiles_fn)}个有效Smiles，超过程序设计最大容量，计算结束。更多功能、更高的计算效率，请联系作者。'    #中英文翻译-中
            message = f'Total {len(smiles_fn)} working SMILES been found. The calculation amount exceeds the upper limit of software design, and the calculation is over. For more functions and higher computing efficiency, please contact the author.'    #中英文翻译-英
            #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
            #window.text_run.repaint()
            if log_callback:                        # [新增]
                log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
            break
        if frag_all > Frag_All:
            print('组合数已超过200000，循环终止。\n如需高级权限，请联系购买付费版本：13246490942。\n技术问题请联系作者：江博士 jkk928@163.com')
            #message = '组合数已超过限制',Frag_All,'，计算结束。如需高级权限和技术问题请联系作者：江博士 jkk928@163.com'    #中英文翻译-中
            message = 'The number of random combination calculations has exceeded the upper limit of',Frag_All,'. Calculation completed. For advanced authority and technical questions, please contact the author: Dr. Jiang, jkk928@163.com'    #中英文翻译-英
            #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
            #window.text_run.repaint()
            if log_callback:                        # [新增]
                log_callback(str(message))          # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
            break


    #smiles_final_dsc = smiles_descriptor(smiles_final)   #计算产物rdkit化学描述符
    #smiles_final_dsc.insert(0, "smiles_final", smiles_final, allow_duplicates=False)  # 参数：添加列索引，添加列名，添加数据，是否允许列名重复
    #smiles_final_dsc.insert(1, "smiles_SAscore", mol_sascore_list, allow_duplicates=False)
    #print(smiles_final_dsc.head(3))
    loca=time.strftime('%Y-%m-%d %H-%M-%S')
    smiles_fn.to_excel(f'Final-SMILES-linker-length-{linker_lengh}-{loca}.xlsx')   #数据保存-smiles+rdkit描述符    
    print('结束时间',loca)
    locatime = datetime.strptime(loca, '%Y-%m-%d %H-%M-%S')
    diff = locatime - locatime0
    print(diff)          # 0:06:55
    print('总耗时“秒”', diff.total_seconds())   # 415.0 秒，最常用
    
    #print('共进行',j_turn,'次循环。\n计算fragments组合',frag_all,'对。\n符合linker设计要求的smiles有',
          #product_correct_smi_count,'条。符合产物限制条件的smiles有',smiles_screened_count,'条。输出文件为：',
          #'final-smiles-'+'linker长度-'+str(linker_lengh)+'-'+str(loca)+'.xlsx')
    #message = f'\n\n计算结束。共进行{j_turn}次循环。计算fragments组合{frag_all}对。符合Linker设计要求的Smiles有{product_correct_smi_count}条。符合产物限制条件的smiles有{len(smiles_fn)}条。输出至软件所在目录，文件名为：final-smiles-linker长度-{linker_lengh}-{loca}.xlsx'
        #中英文翻译-中
    message = f'\n\nCalculation completed. A total of {j_turn} calculation cycles were performed. Total fragments combination:{frag_all}. Number of SMILES meet linker requirement:{product_correct_smi_count}. Number of SMILES meet output requirement:{len(smiles_fn)}. The calculation results are output to the directory where the software is located, and the file name is: Final-SMILES-linker-length-{linker_lengh}-{loca}.xlsx'
        #中英文翻译-英
    
    # 结束监控
    max_cpu, max_mem_mb = monitor.stop()
    t_end = time.time()
    cost_time = t_end - t_start
    
    # 输出资源信息（你之前的分行print格式）
    print(f'运行结束资源统计：\n'
          f'总耗时：{cost_time:.2f} s\n'
          f'峰值CPU：{max_cpu:.1f} %\n'
          f'峰值内存(RSS)：{max_mem_mb:.2f} MB')
    print(message, '\n','\n')
    #window.text_run.append(str(message))  # 将输出内容添加到文本输出框并换行
    #window.text_run.repaint()
    if log_callback:                        # [新增]
        log_callback(message)               # [修改] 原: window.text_run.append(str(message)); window.text_run.repaint()
    
    #return smiles_final
    return smiles_fn                        # [修改] 原: return smiles_final（空列表）




#cell 9

def help_print():   #英文说明书
    AA=(
'''                                User manual

    1 The copyright of this software belongs to Zhuhai Haomai Technology Co., Ltd.. This is a free trial version. For business cooperation, please contact mr.wang. E-mail: jeremy.wang@hq-haomai.com.

    2 The free version is only used for academic exchanges and may not be used for commercial purposes. The author and Zhuhai Haomai Technology Co., Ltd. are not responsible for the output results of the free trial version. 

    3 The software is mainly used for Linker design of ProTac molecules and outputs the qualified complete ProTac molecules. Before use, SMILES of E3 target head and ligand molecules of target protein needed for ProTac molecular design should be provided. This software can also be used for molecular design such as molecular glue, which needs to design long-chain connectors.

    4 Input parameter description：
        4.1 E3 Smiles: E3 target smiles need to reserve a connection site with the symbol [Fr], which can be drawn by using chemical molecular drawing software, such as: c1ccncc1[Fr].
        4.2 Target Smiles: Smiles of the ligand molecule of the target protein. A connecting site with the symbol [Cs] should be reserved, which can be drawn by using chemical molecular drawing software, such as C1CCCOC1[Cs].
        4.3 Linker length: design the atomic length of the Linker, that is, the shortest number of atoms between two connecting sites. The length of linkers designed in this software ranges from 3 to 20, and the theoretical maximum number of linkers corresponding to each length is as follows:：
            Linker length = 3 ：704
            Linker length = 4 ：5405
            Linker length = 5 ：53891
            Linker length = 6 ：551902
            Linker length = 7 ：5031843
            Linker length = 8 ：49839456
            Linker length = 9 ：481077675
            Linker length = 10 ：4605229824
            Linker length = 11 ：44768661374
            Linker length = 12 ：431157479647
            Linker length = 13 ：4161169494275
            Linker length = 14 ：40221955675335
            Linker length = 15 ：388029585605208
            Linker length = 16 ：3747205476712534
            Linker length = 17 ：36181920911916859
            Linker length = 18 ：349277299019775247
            Linker length = 19 ：3372506650913179865
            Linker length = 20 ：32560366649179541327
        4.4. Product Quantity: the number of qualified products Smiles to be exported. Due to the limitation of Linker, product, total calculation and theoretical maximum number of linkers, the number of output products may not be reached, and the program automatically outputs a limited number of products.
        4.5. Candidates per Run: the calculation amount of a single cycle of software operation.
        4.6. Total Candidates: the calculation amount of a single operation of software operation. Note: the same parameter can be run repeatedly, and the same output result may appear in different cycle operation results.
        4.7. Conditions of Linker : the setting of this parameter can constrain the calculation of Linker. The format of the parameter is as follows. Adjust the parameters and only modify the number part. There must be no spaces or blank lines in the parameters, otherwise the program will make an error. For more parameters, please refer to "Conditional parameters that can be added", and you can add them by yourself in the same format.
            MolWt:[150,400]
            NHOHCount:[0,4]
            HeavyAtomsCount，[6,15]
            RingCount:[0,4]
            NOCount:[0,5]
            NumHDonors:[0,4]

    5 Cinditions of Product: The setting format is as follows. Adjust the parameters and only modify the number part. There must be no spaces or blank lines in the parameters, otherwise the program will make an error.
        MolWt:[150,400]
        SAscore:[0,6]
        MolLogP:[3,6]
        Maximum molecular weight of Protac: 1500
        Protac maximum LogP:7
        The program automatically calculates the synthesis difficulty of the product: SA_Score. The data is saved in the output Excel file.
        More product constraints: In addition to the following constraints, product constraints also include a number of non-additive chemical descriptors (100+).

    6 After setting the input conditions, click the Start button to start the program operation. 
        The output of the operation process is in the "Program Running Process" box. 
        After running, save the output file in the directory where the program is located. 
        In the output box on the right side of the "Start" button, the qualified products Smiles are displayed.
        Note: When the single calculation amount and output product settings are large, the program needs more time for each step. The program may appear “no response”, please wait patiently for the program to respond accordingly.

    7、Structure Viewer: You can copy a single Smiles to the "Input SMILES" text input box, and click the "Draw" button to draw a molecular structure diagram.

    8、Conditional parameters that can be added (if you need to set the parameter equal to zero: [0,0])(There may be errors in the interpretation of some chemical descriptors)
        MolWt:[150,400]:[molar molecular weight]；
        HeavyAtomsMolWt:[0,5]]: [heavy atomic molar molecular weight];
        HeavyAtomsCount:[0,5]: [number of heavy atoms];
        NHOHCount:[0,5]: [number of amino groups and hydroxyl groups];
        NOCount:[0,5]: [number of nitrogen and oxygen atoms];
        NumHAcceptors:[0,5]: [number of hydrogen atom acceptors];
        NumHDonors:[0,5]: [number of hydrogen atom donors];
        NumHeteroatoms:[0,5]: [number of heteroatoms];
        NumRotatableBonds:[0,5]: [number of rotatable keys];
        NumSaturatedCarbocycles:[0,5]]: [number of saturated carbocycles];
        NumSaturatedHeterocycles:[0,5]: [number of saturated heterocycles];
        NumSaturatedRings:[0,5]: [number of saturated rings];
        NumAliphaticCarbocycles:[0,5]: [number of aliphatic carbocycles];
        NumAliphaticHeterocycles:[0,5]]: [number of aliphatic heterocycles];
        NumAliphaticRings:[0,5]: [number of aliphatic rings];
        NumAromaticCarbocycles: [0,5]: [number of aromatic carbocycles];
        NumAromaticHeterocycles: [0,5]: [number of aromatic heterocycles];
        RingCount:[0,5]: [Total number of rings];
        NumAliphaticRings:[0,5]: [number of aliphatic rings];
        Number of aromatic carbocycles: [0,5]: [number of aromatic carbocycles];
        Number of aromatic heterocycles: [0,5]: [number of aromatic heterocycles];
        NumAromaticRings: [0,5]: [number of aromatic rings];
        [Fr]_bicyclic:[0,5]: [The number of bicyclic parallel rings, such as C12CCCCCC1CCCC2, C12=CC=CC=C1C=CC=C2];
        [Fr]_furan:[0,5]: [furan ring number];
        [Fr]_benzene:[0,5]: [number of benzene rings];
        [Fr]_imidazole:[0,5]: [number of imidazole rings];
        [Fr]_pyridine:[0,5]: [number of pyridine rings];
        [Fr]_piperdine:[0,5]: [number of piperidine rings];
        [Fr]_piperzine:[0,5]: [number of piperazine rings];
        [Fr]_thiazole:[0,5]: [number of thiazole rings];
        [Fr]_thiophene:[0,5]: [number of thiophene rings];
        [Fr]_Al_COO:[0,5]: [quantity of aliphatic carboxylic acids];
        [Fr]_Al_OH:[0,5]: [number of aliphatic hydroxyl groups];
        [Fr]_Al_OH_noTert:[0,5]: [Number of fatty hydroxyl groups except tertiary hydroxyl groups];
        [Fr]_ArN:[0,5]: [Number of amino functional groups on aromatic hydrocarbon, such as c1cnccc1CC];
        [Fr]_Ar_N:[0,5]: [number of aromatic nitrogen, such as c1ccccc1N, c1ccccc1NCC, c1ccccc1N(CC)C,];
        [Fr]_Ar_NH:[0,5]: [number of aromatic imines, such as c1ccccc1NCC];
        [Fr]_Ar_OH:[0,5]: [Number of hydroxyl groups on aromatic ring, number of phenolic hydroxyl groups, such as c1cc(CC)ccc1O];
        [Fr]_COO:[0,5]: [number of carboxylic acids];
        [Fr]_C_O:[0,5]:[The number of carbonyl carbon-oxygen double bonds, including ester groups, carboxyl groups, ketones, aldehydes, amides, etc.];
        [Fr]_C_O_noCOO:[0,5]:[Number of carbonyl O, including ester group, excluding carboxyl group]；
        [Fr]_C_S:[0,5]:[Number of carbonyl O, including ester group, excluding carboxyl group];
        [Fr]_NH0:[0,5]:[The number of thiocarbonyl groups, such as c1ccccc1CC(=S)(CCC)];
        [Fr]_NH1:[0,5]:[The number of tertiary amines, the one at the end of the Linker does not contain tertiary amines, and the tertiary amines in the middle of the Linker (including nitrogen atoms on the pyridine ring, etc.) are calculated here (this parameter can be limited in the product)];
        [Fr]_NH2:[0,5]:[Number of primary amines, secondary amines at the end of Linker will be converted into tertiary amines after synthesizing ProTac molecules (this parameter can be limited in the product)];
        [Fr]_Nhpyrrole:[0,5]:[The number of H-pyrrole nitrogen, such as c1cc[nH]c1CC(=S)(CCC), the substituted structure without pyrrole nitrogen];
        [Fr]_SH:[0,5]:[number of sulfhydryl groups]；
        [Fr]_aldehyde:[0,5]:[number of aldehydes]；
        [Fr]_alkyl_halide:[0,5]:[Number of alkyl halide]；
        [Fr]_amide:[0,5]:[amide number]；
        [Fr]_aniline:[0,5]:[Number of alkyl groups of carbamate (hydrolyzable), such as CCCCC(N)(=N)]；
        [Fr]_aryl_methyl:[0,5]:[The number of Amidines, amidine is a kind of nitrogen-containing organic compound and a nitrogen-containing derivative of carboxylic acid, such as c1ccccc1CC]；
        [Fr]_ether:[0,5]:[number of esters]；
        [Fr]_halogen:[0,5]:[number of halogens]；
        [Fr]_hdrzine:[0,5]:[Number of hydrazine groups, excluding amino substitution on pyrrole nitrogen atom, such as CCNNCCC]；
        [Fr]_imide:[0,5]:[number of imide groups]；
        [Fr]_ketone:[0,5]:[Number of ketones, excluding aldehydes, esters and amides, such as CC(=O)CNN1C(CCC)=CC=C1]；
        [Fr]_ketone_Topliss:[0,5]:[Number of ketones, excluding diaryl, α β-unsaturated ketone, dienone and heteroatom on C-alpha]；
        [Fr]_morpholine:[0,5]:[Number of morpholine rings, such asN1CCOCC1]；
        [Fr]_para_hydroxylation:[0,5]:[Number of hydroxylation sites, such as c1ccc(O)cc1O]；
        [Fr]_phenol:[0,5]:[quantity of phenol]；
        [Fr]_phenol_noOrthoHbond:[0,5]:[The number of phenolic hydroxyl groups excluding intramolecular bond substituents in ortho-position, such as c1(CC(=O)O)ccccc1O,1; c1(C(=O)O)ccccc1O,0 (six-membered ring forming intramolecular hydrogen bond)]；
        [Fr]_priamide:[0,5]:[number of propionamide]；
        [Fr]_sulfonamd:[0,5]:[number of sulfonamides];
        [Fr]_sulfone:[0,5]:[sulfone radix];
        [Fr]_term_acetylene:[0,5]:[number of terminal acetylene];
        [Fr]_Alkynyl_group:[0,5]:[number of Alkynyl group];
        [Fr]_unbrch_alkane:[0,5]:[Number of unbranched alkanes with at least 4 carbon atoms (excluding halogenated alkanes)

    9 For software bugs, experience discussion and technical exchange, please save software screenshots and descriptions and contact Dr. Jiang, E-mail: jkk928@163.com
        If the software is helpful to your work, cite our paper. Thanks.
''')
    
    return AA




#cell 10

def frag_calculate(frag_onetime, Frag_All):
    import time
    
    if frag_onetime == 928928929 and Frag_All == 928928929:
        frag_onetime = 2000
        Frag_All = 10000000
        #message = '#### 彩 蛋 加 倍 精 彩 ####'    #中英文翻译-中
        message = '#### Double Surprise ####'
        window.text_run.append(str(message))
        window.text_run.repaint()
        #message = '#### 来自可爱的软件作者：江博士，E-mail：jkk928@163.com ####'    #中英文翻译-中
        message = '#### From lovely software author: Dr. Jiang, E-mail：jkk928@163.com ####'
        window.text_run.append(str(message))
        window.text_run.repaint()
        #message = '#### 突破数量限制，等待时间更长 ####'    #中英文翻译-中
        message = '#### Break through the quantitative limit. Much more time is needed. ####'
        window.text_run.append(str(message)) 
        window.text_run.repaint()
        #message = '#### 单次计算量：2000，总计算量：10000000 ####'    #中英文翻译-中
        message = '#### Single-Round Calculation: 2,000  Total calculation: 10,000,000 ####'
        window.text_run.append(str(message))
        #print('frag_onetime, Frag_All',frag_onetime, Frag_All)
        time.sleep(1)
    if Frag_All == 928928928 and frag_onetime == 928928928:
        frag_onetime = 1000
        Frag_All = 2000000
        #message = '#### 彩 蛋 ####'    #中英文翻译-中
        message = '#### Surprise ####'
        window.text_run.append(str(message))
        window.text_run.repaint()
        #message = '#### 来自可爱的软件作者：江博士，E-mail：jkk928@163.com ####'    #中英文翻译-中
        message = '#### From lovely software author: Dr. Jiang, E-mail：jkk928@163.com ####'
        window.text_run.append(str(message))
        window.text_run.repaint()
        #message = '#### 突破数量限制，等待时间更长 ####'    #中英文翻译-中
        message = '#### Break through the quantitative limit. Much more time is needed. ####'
        window.text_run.append(str(message)) 
        window.text_run.repaint()
        #message = '#### 单次计算量：1000，总计算量：2 000 000 ####'    #中英文翻译-中
        message = '#### Single-Round Calculation: 1,000  Total calculation: 2,000,000 ####'           
        window.text_run.append(str(message)) 
        window.text_run.repaint()
        #print('frag_onetime, Frag_All',frag_onetime, Frag_All)
        time.sleep(1)
    else:
        if frag_onetime > 1000:
            frag_onetime = 1000
        if Frag_All > 1000000:
            Frag_All = 1000000
    
    #window.text_run.append("倒计时3秒后开始！计算过程可能出现卡顿，请勿关闭软件！...")
    window.text_run.append("The countdown starts in three seconds! There may be a jam in the calculation process. Please do not close the software!...")
    window.text_run.repaint()
    for t in range(3, 0, -1):
        #msg = f"倒计时 {t} 秒"    #中英文翻译-中
        msg = f"Countdown {t} seconds"
        window.text_run.append(msg)
        window.text_run.repaint()
        time.sleep(1)
    window.text_run.repaint()
    print('frag_onetime, Frag_All-end',frag_onetime, Frag_All)
    
    return frag_onetime, Frag_All




#cell 11

###新代码，待调试



import sys
import ast
from PyQt5.QtCore import Qt, QThread, pyqtSignal  # 导入QThread pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QPlainTextEdit, QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
import cairosvg
import io
from PIL import Image
from PyQt5.QtGui import QPixmap, QFont
import pandas as pd


def smi_img(text_smi):   ##画图
    mol = Chem.MolFromSmiles(text_smi)
    img1 = rdMolDraw2D.MolDraw2DSVG(1000,600)
    img1.drawOptions().addAtomIndices=True
    img1.drawOptions().addStereoAnnotation=True
    img1.DrawMolecule(mol)
    img1.FinishDrawing()
    svg_code = img1.GetDrawingText()
    png_bytes = cairosvg.svg2png(bytestring=svg_code)
    img2 = Image.open(io.BytesIO(png_bytes))
    return img2


# ====================== Worker 线程类新增 ======================
class Worker(QThread):
    log_signal = pyqtSignal(str)
    smi_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self, E3, Target, linker_lengh, final_smiles_num, zip_restriction,
                 zip_restriction_fn, frag_onetime, Frag_All):
        super().__init__()
        self.E3 = E3
        self.Target = Target
        self.linker_lengh = linker_lengh
        self.final_smiles_num = final_smiles_num
        self.zip_restriction = zip_restriction
        self.zip_restriction_fn = zip_restriction_fn
        self.frag_onetime = frag_onetime
        self.Frag_All = Frag_All

    def run(self):
        # 回调函数，子线程收到消息发射信号
        def log_cb(msg):
            self.log_signal.emit(msg)
        def smi_cb(msg):
            self.smi_signal.emit(msg)

        # 调用独立的Linker_Design函数
        Linker_Design(
            E3=self.E3,
            Target=self.Target,
            linker_lengh=self.linker_lengh,
            final_smiles_num=self.final_smiles_num,
            zip_restriction=self.zip_restriction,
            zip_restriction_fn=self.zip_restriction_fn,
            frag_onetime=self.frag_onetime,
            Frag_All=self.Frag_All,
            log_callback=log_cb,
            smi_callback=smi_cb
        )
        self.finished_signal.emit()
# ==============================================================


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = None  # 保存worker实例
        self.initUI()

    # =========== 修改start函数：只读取参数，启动Worker线程 ===========
    def start(self):
        E3 = self.text_input1.text()
        Target = self.text_input2.text()
        linker_lengh = self.text_input3.value()
        final_smiles_num = int(self.text_input4.text())

        # 解析linker限制条件
        rtt1 = self.text_input5.toPlainText().split('\n')
        zip_restriction = []
        for x in rtt1:
            x = x.strip()
            if not x:
                continue
            rtt1_0 = []
            sp = x.split(':')
            rtt1_0.append(sp[0])
            rtt1_0.append(ast.literal_eval(sp[1]))
            zip_restriction.append(rtt1_0)

        # 解析产物限制条件
        rtt2 = self.text_input10.toPlainText().split('\n')
        zip_restriction_fn = []
        for x in rtt2:
            x = x.strip()
            if not x:
                continue
            rtt1_0 = []
            sp = x.split(':')
            rtt1_0.append(sp[0])
            rtt1_0.append(ast.literal_eval(sp[1]))
            zip_restriction_fn.append(rtt1_0)

        frag_onetime = int(self.text_input6.text())
        Frag_All = int(self.text_input7.text())
        frag_onetime, Frag_All = frag_calculate(frag_onetime, Frag_All)

        # 实例化工作线程
        self.worker = Worker(
            E3=E3,
            Target=Target,
            linker_lengh=linker_lengh,
            final_smiles_num=final_smiles_num,
            zip_restriction=zip_restriction,
            zip_restriction_fn=zip_restriction_fn,
            frag_onetime=frag_onetime,
            Frag_All=Frag_All
        )
        # 绑定信号槽
        self.worker.log_signal.connect(self.append_log)
        self.worker.smi_signal.connect(self.update_smi_output)
        self.worker.finished_signal.connect(self.on_task_finish)
        # 启动线程
        self.worker.start()
        self.start_button.setEnabled(False)
        self.text_run.append("==== Task started in background ====")

    # 主线程：追加日志到Run Monitor
    def append_log(self, msg):
        self.text_run.append(msg)
        self.text_run.verticalScrollBar().setValue(self.text_run.verticalScrollBar().maximum())

    # 主线程：更新SMILES输出框
    def update_smi_output(self, msg):
        self.start_output.setText(msg)

    # 主线程：任务结束回调
    def on_task_finish(self):
        self.text_run.append("\n==== Calculation Task Complete ====")
        self.start_button.setEnabled(True)

    def start_multi(self):
        A = 0

    def helps(self):
        output1 = help_print()
        self.start_output.setText(output1)

    def step3(self):  #画图ok
        img = smi_img(self.text_input12.text())   #Smiles 输入
        byte_stream = io.BytesIO()
        img.save(byte_stream, format='PNG')
        pixmap = QPixmap()
        pixmap.loadFromData(byte_stream.getvalue())
        self.image_label.setPixmap(pixmap)

    def initUI(self):
        # 第一组：两个垂直分布，共4个文本输入框
        vbox0 = QVBoxLayout()
        HBOX1 = QHBoxLayout()   #第一个大框
        container_widget = QWidget()
        container_widget.setLayout(HBOX1)
        vbox0.addWidget(container_widget)
        vbox1 = QVBoxLayout()
        #label_1 = QLabel('参数输入部分')    #中英文翻译-中
        label_1 = QLabel('Parameter Input')    #中英文翻译-英
        font1 = QFont()
        font1.setPointSize(16)
        #font1.setFamily('KaiTi')    #中英文翻译-中
        font1.setFamily('Times New Roman')   # 修改字体    #中英文翻译-英
        font1.setBold(True)
        font2 = QFont()
        font2.setPointSize(14)
        #font2.setFamily('KaiTi')    #中英文翻译-中
        font2.setFamily('Times New Roman')   # 修改字体    #中英文翻译-英
        font2.setBold(True)
        label_1.setFont(font1)
        vbox1.addWidget(label_1)
        vbox1.setObjectName('参数输入')  
        vbox2 = QVBoxLayout()
        vbox2.setObjectName('说明书')   
        vbox3 = QVBoxLayout()
        vbox3.setObjectName('限制条件') 
        self.text_input1 = QLineEdit('c1ccncc1[Fr]')
        self.text_input2 = QLineEdit('C1CCCOC1[Cs]')
        self.text_input3 = QSpinBox()
        self.text_input3.setMinimum(3)
        self.text_input3.setMaximum(20)
        self.text_input3.setValue(6)
        self.text_input4 = QLineEdit('10')
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start)
        self.start_button.setFixedWidth(100)

        #self.start_multi_button = QPushButton('Start\n(多核心)')    #暂缓
        #self.start_multi_button.setFixedWidth(100)
        #self.start_multi_button.clicked.connect(self.start_multi)
        #self.step2_button = QPushButton('多处理')    #中英文翻译-中

        HBOX1.addLayout(vbox1)
        vbox1.addWidget(QLabel('E3 Smiles'))
        vbox1.addWidget(self.text_input1)
        vbox1.addWidget(QLabel('Target Smiles'))
        vbox1.addWidget(self.text_input2)
        vbox1.addWidget(QLabel('Linker Length'))
        vbox1.addWidget(self.text_input3)
        #vbox1.addWidget(QLabel('输出产物数量'))     #中英文翻译-中
        vbox1.addWidget(QLabel('Product Quantity'))     #中英文翻译-英
        vbox1.addWidget(self.text_input4)
        self.text_input6 = QLineEdit("200")
        self.text_input7 = QLineEdit("10000")
        #vbox1.addWidget(QLabel('单次计算量（最大1000）'))    #中英文翻译-中
        vbox1.addWidget(QLabel('Candidates per Run (Max 1000)'))    #中英文翻译-英
        vbox1.addWidget(self.text_input6)
        #vbox1.addWidget(QLabel('总计算量（最大1000000）'))    #中英文翻译-中
        vbox1.addWidget(QLabel('Total Candidates (Max 1000000)'))    #中英文翻译-中
        vbox1.addWidget(self.text_input7)
        #self.help_button = QPushButton('使用说明书')    #中英文翻译-中
        self.help_button = QPushButton("User's Manual")    #中英文翻译-英
        self.help_button.clicked.connect(self.helps)
        vbox1.addWidget(self.help_button)
        HBOX1.addLayout(vbox3)
        self.text_input5 = QPlainTextEdit()
        self.text_input5.setPlainText("MolWt:[150,400]\nNHOHCount:[0,4]\nHeavyAtomsCount:[6,15]\nRingCount:[0,4]\nNumHDonors:[0,4]")     #中英文翻译-英
        #vbox3.addWidget(QLabel('Linker限制条件'))    #中英文翻译-中
        vbox3.addWidget(QLabel('Conditions of Linker'))    #中英文翻译-英
        self.text_input5.setMinimumSize(300,100)
        vbox3.addWidget(self.text_input5)
        self.text_input10 = QPlainTextEdit()    #产物限制条件框
        #self.text_input10.setPlainText("MolWt:[150,400]:【摩尔分子量】\nSAscore:[0,6]:【合成难度系数】\nMolLogP:[3,6]:【分子脂水分配系数】")    #中英文翻译-中
        self.text_input10.setPlainText("MolWt:[150,400]\nSAscore:[0,6]\nMolLogP:[3,6]")    #中英文翻译-英
        self.text_input10.setMinimumSize(300,100)
        #vbox3.addWidget(QLabel('产物限制条件'))    #中英文翻译-中
        vbox3.addWidget(QLabel('Conditions of Product'))    #中英文翻译-英
        vbox3.addWidget(self.text_input10)
        HBOX2 = QHBoxLayout()
        vbox0.addLayout(HBOX2)   #第三个大框
        # 将处理2的按钮和输出框添加到水平布局2中
        self.start_output = QTextEdit('Output SMILES:')
        self.start_output.setMinimumSize(600,120)
        #self.start_output.setMaximumSize(600,200)
        vbox2_1 = QVBoxLayout()
        vbox2_1.addWidget(self.start_button)
        '''vbox2_1.addWidget(self.start_multi_button)
        vbox2_1.addWidget(QLabel('CPU核心数'))    #多核心计算
        self.text_cpu = QSpinBox()
        self.text_cpu.setMinimum(2)
        self.text_cpu.setMaximum(128)
        self.text_cpu.setValue(4)
        self.text_cpu.setFixedWidth(100)
        vbox2_1.addWidget(self.text_cpu)'''
        HBOX2.addLayout(vbox2_1)
        HBOX2.addWidget(self.start_output)
        HBOX3 = QHBoxLayout()  #输出框和绘图框#############################
        vbox0.addLayout(HBOX3)   #第三个大框
        vbox3_1 = QVBoxLayout()
        #label_2 = QLabel('程序运行过程')    #中英文翻译-中
        label_2 = QLabel('Run Monitor')    #中英文翻译-英
        label_2.setFont(font2)
        vbox3_1.addWidget(label_2)
        self.text_run = QTextEdit(self)
        self.text_run.setReadOnly(True)
       # self.text_run.resize(400,300)
        self.text_run.setMinimumSize(300,300)    #(self, minw: int, minh: int)
        vbox3_1.addWidget(self.text_run)
        vbox3_2 = QVBoxLayout()
        #label_3 = QLabel('SMILES绘图')    #中英文翻译-中
        label_3 = QLabel('Structure Viewer')    #中英文翻译-英
        label_3.setFont(font2)
        vbox3_2.addWidget(label_3)
        #self.text_input12 = QLineEdit("输入SMILES")    #中英文翻译-中
        self.text_input12 = QLineEdit("Input SMILES")    #中英文翻译-英
        vbox3_2.addWidget(self.text_input12)
        #self.fig_button = QPushButton('绘图')    #中英文翻译-中
        self.fig_button = QPushButton('Draw')    #中英文翻译-英
        self.fig_button.clicked.connect(self.step3)
        vbox3_2.addWidget(self.fig_button)
        self.image_label = QLabel(self)
        #self.image_label.setFixedSize(500, 300)  #固定大小
        self.image_label.setMinimumSize(500, 300)
        self.image_label.setStyleSheet("background-color: white;")
        vbox3_2.addWidget(self.image_label, 4)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_label.setScaledContents(True)   # 图片随标签尺寸缩放
        HBOX3.addLayout(vbox3_1)
        HBOX3.addLayout(vbox3_2)
        #self.setMinimumSize(800, 600)        # 最小尺寸（防止缩太小布局乱）
        self.setMaximumSize(1500, 1500)      # 最大尺寸（按您屏幕分辨率设定）
        self.setLayout(vbox0)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("LiMIt_4.1")
    window.show()
    sys.exit(app.exec_())





#cell 













