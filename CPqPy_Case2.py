"""
20210104 developped by Yaqiang Wei  yakiwei@yahoo.com
"""


import os
import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod
import numpy as np
import matplotlib.pyplot as plt


# ——————————————————————————————————————————————

def loadDatadet(infile):
    f = open(infile, 'r')
    sourceInLine = f.readlines()[9:]

    dataset = []
    for line in sourceInLine:
        temp3 = line.split()

        dataset.append(temp3)
        # print (dataset)
    k = len(dataset[0])
    for i in range(0, len(dataset)):
        for j in range(0, k):
            dataset[i].append(float(dataset[i][j]))
        del (dataset[i][0:k])
    return dataset


print(__name__)

if __name__ == "__main__":

    # path for .dat files
    datpath = "F:\Pycharm\database"


    def selected_array(db_path, input_string):
        """Load database via linked library object and run input string.
        May be more conventional to use variable name 'phreeqc' instead of 'dbase'.
        """
        dbase = phreeqc_mod.IPhreeqc('F:/Pycharm/dll/IPhreeqc.dll')
        dbase.load_database(db_path)
        dbase.run_string(input_string)
        return dbase.get_selected_output_array()


    # !/usr/bin/python
    # -*- coding: utf-8 -*-
    """
    Created on Wed Aug 12 15:24:15 2020
    @author: Administrator
    phreeqc output unit::: mol/kgw
    """

    # if __name__ == "_main_":

    # —————————————————————————————————————————————————————————————parameters
    import numpy as np
    import time
    import sys
    import os
    import shutil


    def mkdir(path):

        path = path.strip()

        path = path.rstrip("\\")

        isExists = os.path.exists(path)

        if not isExists:

            os.makedirs(path)
            print(path + ' ok')
            return True
        else:
            print(path + ' exist')
            return False



    def wait(path):
        isExists = os.path.exists(path)
        if not isExists:
            return False
        else:
            print(path + ' ok')
            return True


    import psutil
    pids = psutil.pids()
    # print(pids)
    for pid in pids:
        # print(pid)
        p = psutil.Process(pid)
        if p.name() == 'comsolmphserver.exe':
            print("pid-%d,pname-%s" % (pid, p.name()))
            PID = pid


    print(PID)

    def get_cpu_info():
        cpucount = psutil.cpu_count(logical=True)

        process = psutil.Process(int(PID))
        cpupercent = process.cpu_percent(interval=2)

        cpu = int(cpupercent / cpucount)

        start = time.time()
        while cpu > 10:

            time.sleep(0.01)
            cpupercent = process.cpu_percent(interval=2)
            cpu = int(cpupercent / cpucount)
        end1 = time.time()


    class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass


    path = os.path.abspath(os.path.dirname(__file__))
    type = sys.getfilesystemencoding()
    sys.stdout = Logger('runlog.txt')

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('------------------')

    start = time.time()

    import os

    path1 = "F:\Pycharm\COMSOL_phreeqc\Result"
    mkdir(path1)

    timestep = int(0.01 * 864000)

    totaltime = 864000

    steps = int(totaltime / timestep)

    ###————————————————1.prepare comsolrun0.m————————————————————#######################################


    import COMSOLrun0

    incr1 = 'range(0,'
    incr2 = ','
    incr3 = ')'
    incr = incr1 + str(timestep) + incr2 + str(timestep) + incr3
    inputcomsolstr01 = COMSOLrun0.inputcomsolstr0.replace('range(###)', incr)

    print(inputcomsolstr01)

    incr1 = "'t', '"
    incr = incr1 + str(timestep)
    inputcomsolstr02 = inputcomsolstr01.replace("'t', '#", incr)

    incr1 = "outcon"
    incr = incr1 + str(timestep)
    inputcomsolstr03 = inputcomsolstr02.replace("outcono", incr)

    incr1 = "flowh"
    incr = incr1 + str(timestep)
    inputcomsolstr04 = inputcomsolstr03.replace("flowho", incr)

    incr1 = "flowthe"
    incr = incr1 + str(timestep)
    inputcomsolstr05 = inputcomsolstr04.replace("flowtheo", incr)


    fh = open('F:\Pycharm\COMSOL_phreeqc/comsolrun0.m', 'w', encoding='utf-8')
    fh.write(inputcomsolstr05)
    fh.close()


    import win32api

    win32api.ShellExecute(0, 'run', 'F:\\Pycharm\COMSOL_phreeqc/comsolrun0.m', '', '', 1)


    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result\outcon"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！")

    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowthe"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！")

    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowh"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    while wait(infile) == False:
        time.sleep(0.01)
    print(infile,"Find！！")



    ###————————————————   2.obtain outcon,outcon0———————————————————################################################

    infile = 'F:\Pycharm\COMSOL_phreeqc\Result\outcon0.txt'
    infile = np.array(loadDatadet(infile))

    print(infile.shape)


    m = infile.shape[0]

    n = infile.shape[1] - 2  # All reactant numbers

    outn = 10
    phresult = np.zeros((m, outn))

    end1 = time.time()


    ###————————————————   3.input concentration ————############################


    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/outcon"
    incr = str(timestep)
    incr2 = ".txt"
    infile = incr1 + incr + incr2
    print(infile)
    infile = np.array(loadDatadet(infile))

    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowthe"
    incr = str(timestep)
    incr2 = ".txt"
    inthe = incr1 + incr + incr2
    inthe = np.array(loadDatadet(inthe))

    input_string10 = """   """

    for i in range(0, m):
        input_string1 = """
                SOLUTION #
                    temp      25
                    pH        # charge
                    pe        #
                    redox     pe
                    units     mmol/kgw
                    density   1
                    water    ###
                    A         ###
                    B         ###
                    C         ###
                    """

        ph = 7
        pe = 4

        for j in range(2, 5):
            if infile[i, j] < 0:
                infile[i, j] = 0

        # print(ph, pe)

        incr = str(round(ph, 5))
        str1 = 'pH        '
        incr = str1 + incr
        input_string11 = input_string1.replace('pH        #', incr)

        incr = str(round(pe, 5))
        str1 = 'pe        '
        incr = str1 + incr
        input_string12 = input_string11.replace('pe        #', incr)

        # modify A
        incr = str(round(infile[i, 2], 15))
        # print(incr)
        str1 = 'A        '
        incr = str1 + incr
        input_string13 = input_string12.replace('A         ###', incr)

        # modify B
        incr = str(round(infile[i, 3], 10))
        str1 = 'Asn        '
        incr = str1 + incr
        input_string14 = input_string13.replace('B         ###', incr)

        # modify C
        incr = str(round(infile[i, 4], 10))
        str1 = 'Asx        '
        incr = str1 + incr
        input_string15 = input_string14.replace('C         ###', incr)

        # modify water
        incr = str(round(inthe[i, 2], 10))
        # incr = str(0.5)
        str1 = 'water     '
        incr = str1 + incr
        input_string16 = input_string15.replace('water    ###', incr)

        incr = str(i + 1)
        str1 = 'SOLUTION '
        incr = str1 + incr
        input_string17 = input_string16.replace('SOLUTION #', incr)

        # Reaction configuration
        input_string10 = input_string10 + input_string17

    input_string2 = """
            KINETICS #
            R_1
                -formula  A  -1 Asx  1
                -m        100
                -m0       100
                -tol      1e-10
            R_2
                -formula  Asn  1 Asx  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_3
                -formula  A  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_4
                -formula  Asx  -1
                -m        100
                -m0       100
                -tol      1e-10
            R_5
                -formula  Asn  -1
                -m        100
                -m0       100
                -tol      1e-08

            RUN_CELLS
                -cells #
                -time_step    # seconds

            SELECTED_OUTPUT #
                -high_precision       true
                -reset                false
                -solution             true
                -time                 true
                -pH                   true
                -pe                   true
                -water                true
                -charge_balance       true
                -percent_error        true
                -totals               A  Asn Asx

            End
                """
    # modify knite
    incr = str(m)
    str1 = 'KINETICS 1-'
    incr = str1 + incr
    input_string21 = input_string2.replace('KINETICS #', incr)

    # modify cells

    incr = str(m)
    str1 = '-cells 1-'
    incr = str1 + incr
    input_string22 = input_string21.replace('-cells #', incr)

    # modify timesteps
    incr = str(timestep)
    str1 = '-time_step    '
    incr = str1 + incr
    input_string23 = input_string22.replace('-time_step    #', incr)

    # modify out
    incr = str(m)
    str1 = 'SELECTED_OUTPUT 1-'
    incr = str1 + incr
    input_string24 = input_string23.replace('SELECTED_OUTPUT #', incr)

    input_string = input_string10 + input_string24



    phreeqc_result = selected_array(os.path.join(datpath, 'pesti.dat'), input_string)

    ###———————————---------—————   5.new phresult------------————————————————————#############################################

    for jj in range(0, outn):
        for zz in range(m + 2, m + m + 2):
            a = [entry[jj] for entry in phreeqc_result][zz:]
            phresult[zz - m - 2, jj] = float(a[0])



    ### ————————————————————6. new initcon.txt————————————————————————###########################################

    for i in range(0, m):
        for k in range(0, n):
            infile[i, 2 + k] = phresult[i, 7 + k] * 1000


    print(infile)
    print(infile.shape)

    incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/outcon"
    incr =  str(timestep)
    incr2 = ".txt"
    infile11 = incr1 + incr + incr2


    np.savetxt('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', infile)
    # np.savetxt('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', infile, fmt="%10.5f")

    with open('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', 'r', encoding='utf-8') as f:
        dataset = f.read()  # type: str


    fh = open('F:\Pycharm\COMSOL_phreeqc\Result/initcon.txt', 'w')
    for line in open(infile11, 'r'):
        a = line.split(' ')
        if a[0] == '%':
            fh.write(line)
    fh.write(dataset)
    fh.close()


    strint1 = "F:\Pycharm\COMSOL_phreeqc\Result/initcon"
    strint2 = str(int(timestep))
    strint3 = ".txt"
    shutil.copy('F:\Pycharm\COMSOL_phreeqc\Result/initcon.txt', strint1 + strint2 + strint3)


    ###————————————————————————7. input to initcon###################################
    # calculate geochmistry of each reactant in each node

    import COMSOLrun

    for nstep in range(1, steps):

        print(infile.shape)


        incr1 = 'range('
        incr2 = ','
        incr3 = ')'
        incr = incr1 + str(timestep * nstep) + incr2 + str(timestep) + incr2 + str(timestep * (nstep + 1)) + incr3
        inputcomsolstr01 = COMSOLrun.inputcomsolstr0.replace('range(###)', incr)

        incr1 = "initcon"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr02 = inputcomsolstr01.replace("initconi", incr)


        incr1 = "flowh"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr03 = inputcomsolstr02.replace("flowhi", incr)

        incr1 = "flowthe"
        incr = incr1 + str(timestep * nstep)
        inputcomsolstr04 = inputcomsolstr03.replace("flowthei", incr)


        incr1 = "'t', '"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr05 = inputcomsolstr04.replace("'t', '#", incr)

        incr1 = "outcon"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr06 = inputcomsolstr05.replace("outcono", incr)

        incr1 = "flowh"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr07 = inputcomsolstr06.replace("flowho", incr)

        incr1 = "flowthe"
        incr = incr1 + str(timestep * (nstep + 1))
        inputcomsolstr08 = inputcomsolstr07.replace("flowtheo", incr)


        fh = open('F:\Pycharm\COMSOL_phreeqc/comsolrun.m', 'w', encoding='utf-8')
        fh.write(inputcomsolstr08)
        fh.close()


        ###————————————————————————8. new comsolrun.m#########################



        win32api.ShellExecute(0, 'run', 'F:\Pycharm\COMSOL_phreeqc/comsolrun.m', '', '', 1)


        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result\outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        print(infile)
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")

        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowthe"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")

        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowh"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile = incr1 + incr + incr2
        while wait(infile) == False:
            time.sleep(0.01)
        print(infile, "Find！")

        ###———————————————————————9. new outcon文件###################################

        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile=incr1+incr+incr2
        infile = np.array(loadDatadet(infile))

        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/flowthe"
        incr =  str(timestep * (nstep + 1))
        incr2 = ".txt"
        inthe=incr1+incr+incr2
        inthe = np.array(loadDatadet(inthe))

        ###———————————————————————10. new phreeqc input file—————————————————————##############################################

        np.savetxt('F:\Pycharm\COMSOL_phreeqc\Result/result.txt', phresult)


        input_string10 = """   """

        for i in range(0, m):
            input_string1 = """
                    SOLUTION #
                        temp      25
                        pH        # charge
                        pe        #
                        redox     pe
                        units     mmol/kgw
                        density   1
                        water    ###
                        A         ###
                        B         ###
                        C         ###
                        """
            ph = 7
            pe = 4

            for j in range(2, 5):
                if infile[i, j] < 0:
                    infile[i, j] = 0


            incr = str(round(ph, 5))
            str1 = 'pH        '
            incr = str1 + incr
            input_string11 = input_string1.replace('pH        #', incr)

            incr = str(round(pe, 5))
            str1 = 'pe        '
            incr = str1 + incr
            input_string12 = input_string11.replace('pe        #', incr)

            # modify A
            incr = str(round(infile[i, 2], 15))
            # print(incr)
            str1 = 'A        '
            incr = str1 + incr
            input_string13 = input_string12.replace('A         ###', incr)

            # modify B
            incr = str(round(infile[i, 3], 10))
            str1 = 'Asn        '
            incr = str1 + incr
            input_string14 = input_string13.replace('B         ###', incr)

            # modify C
            incr = str(round(infile[i, 4], 10))
            str1 = 'Asx        '
            incr = str1 + incr
            input_string15 = input_string14.replace('C         ###', incr)

            # modify water
            incr = str(round(inthe[i, 2], 10))
            # incr = str(20)
            str1 = 'water     '
            incr = str1 + incr
            input_string16 = input_string15.replace('water    ###', incr)

            incr = str(i + 1)
            str1 = 'SOLUTION '
            incr = str1 + incr
            input_string17 = input_string16.replace('SOLUTION #', incr)

            input_string10 = input_string10 + input_string17

        input_string2 = """
                KINETICS #
                R_1
                    -formula  A  -1 Asx  1
                    -m        100
                    -m0       100
                    -tol      1e-10
                R_2
                    -formula  Asn  1 Asx  -1
                    -m        100
                    -m0       100
                    -tol      1e-10
                R_3
                    -formula  A  -1
                    -m        100
                    -m0       100
                    -tol      1e-10
                R_4
                    -formula  Asx  -1
                    -m        100
                    -m0       100
                    -tol      1e-10
                R_5
                    -formula  Asn  -1
                    -m        100
                    -m0       100
                    -tol      1e-08
    
                RUN_CELLS
                    -cells #
                    -time_step    # seconds
    
                SELECTED_OUTPUT #
                    -high_precision       true
                    -reset                false
                    -solution             true
                    -time                 true
                    -pH                   true
                    -pe                   true
                    -water                true
                    -charge_balance       true
                    -percent_error        true
                    -totals               A  Asn Asx
    
                End
                    """
        # modify knite
        incr = str(m)
        str1 = 'KINETICS 1-'
        incr = str1 + incr
        input_string21 = input_string2.replace('KINETICS #', incr)

        # modify cells

        incr = str(m)
        str1 = '-cells 1-'
        incr = str1 + incr
        input_string22 = input_string21.replace('-cells #', incr)

        # modify timesteps
        incr = str(timestep)
        str1 = '-time_step    '
        incr = str1 + incr
        input_string23 = input_string22.replace('-time_step    #', incr)

        # modify out
        incr = str(m)
        str1 = 'SELECTED_OUTPUT 1-'
        incr = str1 + incr
        input_string24 = input_string23.replace('SELECTED_OUTPUT #', incr)

        input_string = input_string10 + input_string24


        phreeqc_result = selected_array(os.path.join(datpath, 'pesti.dat'), input_string)

        for jj in range(0, outn):
            for zz in range(m + 2, m + m + 2):
                a = [entry[jj] for entry in phreeqc_result][zz:]
                phresult[zz - m - 2, jj] = float(a[0])

        ### ————————————————————11. new initcon.txt——————————————————------------------#####################


        for i in range(0, m):
            for k in range(0, n):
                infile[i, 2 + k] = phresult[i, 7 + k] * 1000


        incr1 = "F:\Pycharm\COMSOL_phreeqc\Result/outcon"
        incr = str(timestep * (nstep + 1))
        incr2 = ".txt"
        infile11=incr1+incr+incr2


        np.savetxt('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', infile)


        with open('F:\Pycharm\COMSOL_phreeqc\Result/infile.txt', 'r', encoding='utf-8') as f:
            dataset = f.read()  # type: str


        fh = open('F:\Pycharm\COMSOL_phreeqc\Result/initcon.txt', 'w')
        for line in open(infile11, 'r'):
            a = line.split(' ')
            if a[0] == '%':
                fh.write(line)
        fh.write(dataset)
        fh.close()

        strint1 = "F:\Pycharm\COMSOL_phreeqc\Result/initcon"
        strint2 = str(int(timestep * (nstep + 1)))
        strint3 = ".txt"
        shutil.copy('F:\Pycharm\COMSOL_phreeqc\Result/initcon.txt', strint1 + strint2 + strint3)



        print('finish %dstep Phreeqc' % (nstep + 1))
        print("-------------------------------------------------")

    # —————————————————————————over————————————————————————————————————————

    # os.system("draw.py")

    end00 = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('Done！')
    print("running:%.2fs" % (end00 - start))
    print('You Win!!!!!!!! ')
