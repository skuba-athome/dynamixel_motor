#author: fptrainnie
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
from termcolor.termcolor import colored

if __name__ == '__main__':
    env = os.environ
    env['PYTHONIOENCODING'] = 'utf-8' 
    pan = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','10'], stdout=subprocess.PIPE, env=env)
    out, err =  pan.communicate() 
    if out.split()[4] == 'done':
        print 'Neck: Pan\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Neck: Pan\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    tilt = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','11'], stdout=subprocess.PIPE, env=env)
    out, err = tilt.communicate()
    if out.split()[4] == 'done':
        print 'Neck: Tilt\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Neck: Tilt\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print 

    shd_in_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','20'], stdout=subprocess.PIPE, env=env)
    out, err = shd_in_r.communicate()
    if out.split()[4] == 'done':
        print 'Sholder1_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Sholder1_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    shd_out_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','21'], stdout=subprocess.PIPE, env=env)
    out, err = shd_out_r.communicate()
    if out.split()[4] == 'done':
        print 'Sholder2_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Sholder2_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    elb_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','22'], stdout=subprocess.PIPE, env=env)
    out, err = elb_r.communicate()
    if out.split()[4] == 'done':
        print 'Elbow_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Elbow_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst1_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','40'], stdout=subprocess.PIPE, env=env)
    out, err = wst1_r.communicate()
    if out.split()[4] == 'done':
        print 'Wrist1_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist1_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst2_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','41'], stdout=subprocess.PIPE, env=env)
    out, err = wst2_r.communicate()
    if out.split()[4] == 'done':
        print 'Wrist2_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist2_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst3_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','42'], stdout=subprocess.PIPE, env=env)
    out, err = wst3_r.communicate()
    if out.split()[4] == 'done':
        print 'Wrist3_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist3_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    grp_r = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','43'], stdout=subprocess.PIPE, env=env)
    out, err = grp_r.communicate()
    if out.split()[4] == 'done':
        print 'Gripper_right\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Gripper_right\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    shd_in_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','25'], stdout=subprocess.PIPE, env=env)
    out, err = shd_in_l.communicate()
    if out.split()[4] == 'done':
        print 'Sholder1_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Sholder1_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    shd_out_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','26'], stdout=subprocess.PIPE, env=env)
    out, err = shd_out_l.communicate()
    if out.split()[4] == 'done':
        print 'Sholder2_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Sholder2_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    elb_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','27'], stdout=subprocess.PIPE, env=env)
    out, err = elb_l.communicate()
    if out.split()[4] == 'done':
        print 'Elbow_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Elbow_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst1_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','45'], stdout=subprocess.PIPE, env=env)
    out, err = wst1_l.communicate()
    if out.split()[4] == 'done':
        print 'Wrist1_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist1_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst2_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','46'], stdout=subprocess.PIPE, env=env)
    out, err = wst2_l.communicate()
    if out.split()[4] == 'done':
        print 'Wrist2_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist2_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    wst3_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','47'], stdout=subprocess.PIPE, env=env)
    out, err = wst3_l.communicate()
    if out.split()[4] == 'done':
        print 'Wrist3_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Wrist3_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    grp_l = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','48'], stdout=subprocess.PIPE, env=env)
    out, err = grp_l.communicate()
    if out.split()[4] == 'done':
        print 'Gripper_left\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Gripper_left\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print

    prism = subprocess.Popen(['python','info_dump.py','--port=/dev/ttyUSB1','--baud=57600','50'], stdout=subprocess.PIPE, env=env)
    out, err = prism.communicate()
    if out.split()[4] == 'done':
        print 'Prismetics\t' + out.split()[1] + colored(out.split()[2],'yellow') + out.split()[3] + colored(out.split()[4],'green')
        print '\t' + out.split()[25] + out.split()[26] + out.split()[27] + colored(out.split()[28],'cyan')
    else:
        print 'Prismetics\t' + out.split()[1] + colored(out.split()[2],'red') + out.split()[3] + colored(out.split()[4],'red')
    print
