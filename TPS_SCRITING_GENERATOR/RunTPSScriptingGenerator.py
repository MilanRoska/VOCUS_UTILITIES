# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:48:52 2024

@author: m.roska
"""
#%% packages
import csv
import numpy as np
from TPSScriptingGenerator import set_voltages, zero, cal_step, ambient, voltage_scan, calibration_100_minutes, calibration_100_minutes_vs, via_turn_off, via_turn_on

#%%input
#path to where the txt file of the script is saved
output_path = 'C://Users/m.roska/OneDrive - Forschungszentrum Jülich GmbH/Desktop/VOCUS/TPS Scripting/TPSScriptingGenerator/TPSScript.txt'

#vs setup
set_tuning_frequency_hz = 1
set_total_voltage = 120
set_step_size_voltage = 2

#%%initilize array
tps_script = np.zeros((0,4), dtype=object)

#%% EVA Plants spring
#Setvolt
tps_script = set_voltages(tps_script, start_time_seconds = 0, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#cal step
tps_script = cal_step(tps_script, start_time_seconds = 10, cal_flow_sccm = 10 , zero_flow_sccm = 1000, ping = 10)
#cal vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 5*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 6*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#zero
tps_script =  zero(tps_script, start_time_seconds = 6*60 + 10, zero_flow_sccm = 1000, cal_flow_sccm = 1, ping = 10)
#zer vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 11*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 12*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#ambient
tps_script = ambient(tps_script, start_time_seconds = 12*60 + 10, cal_flow_sccm = 1, zero_flow_sccm = 1000, ping = 10)

#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 45*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 46*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 90*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 91*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#%% EVA Plants spring (condensed code formating)
#Setvolt
tps_script = set_voltages(tps_script, 0, 450, 0)

#cal step
tps_script = cal_step(tps_script, 10, 10 , 1000)
#cal vscan
tps_script = voltage_scan(tps_script, 5*60 , set_tuning_frequency_hz, set_total_voltage, set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, 6*60, 450, 0)

#zero
tps_script =  zero(tps_script, 6*60 + 10)
#zer vscan
tps_script = voltage_scan(tps_script, 11*60 , set_tuning_frequency_hz, set_total_voltage, set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, 12*60, 450, 0)

#ambient
tps_script = ambient(tps_script, 12*60 + 10)

#amb vscan
tps_script = voltage_scan(tps_script, 45*60 , set_tuning_frequency_hz, set_total_voltage, set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, 46*60, 450, 0)

#amb vscan
tps_script = voltage_scan(tps_script, 90*60 , set_tuning_frequency_hz, set_total_voltage, set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, 91*60, 450, 0)

#%% test VS script
for i in range(10):
    start_time = (1+i*5)*60
    end_time = (1+1+i*5)*60
    #cal vscan
    tps_script = voltage_scan(tps_script, start_time_seconds = start_time , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
    #reset votlages
    tps_script = set_voltages(tps_script, start_time_seconds = end_time, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

# %% DEHLI campaign NH4
# 3h total
#Setvolt
tps_script = set_voltages(tps_script, start_time_seconds = 0, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
# 9 min cal
#cal step
tps_script = cal_step(tps_script, start_time_seconds = 10, cal_flow_sccm = 5 , zero_flow_sccm = 1000, ping = 10)
# 1 min cal vs
#cal vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 9*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 10*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

# 9 min zero
#zero
tps_script =  zero(tps_script, start_time_seconds = 10*60 + 10, zero_flow_sccm = 1000, cal_flow_sccm = 1, ping = 10)
# 1 min zero vs
#zer vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 19*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 20*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

# rest amb with VS every 15 min
#ambient
tps_script = ambient(tps_script, start_time_seconds = 20*60 + 10, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 35*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 36*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 50*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 51*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 65*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 66*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 80*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 81*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 95*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 96*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 110*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 111*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 125*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 126*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 140*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 141*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 155*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 156*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)
#amb vscan
tps_script = voltage_scan(tps_script, start_time_seconds = 170*60 , tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage)
#reset votlages
tps_script = set_voltages(tps_script, start_time_seconds = 171*60, imr_front_voltage = 450, imr_back_voltage = 0, ping = 10)

#%% cal with vs
#tps_script = calibration_100_minutes_vs(tps_script, total_start_time_seconds = 0, tuning_frequency_hz = set_tuning_frequency_hz, total_voltage = set_total_voltage, step_size_voltage = set_step_size_voltage, imr_front_voltage = 450, imr_back_voltage = 0)
total_start_time_seconds = 0
tuning_frequency_hz = set_tuning_frequency_hz
total_voltage = set_total_voltage
step_size_voltage = set_step_size_voltage
imr_front_voltage = 450
imr_back_voltage = 0
#zero
tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds)
#normilization step (cal 10 sccm)
tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 5*60, cal_flow_sccm = 10)
#cal vs
tps_script = voltage_scan(tps_script, start_time_seconds = total_start_time_seconds + 8*60, tuning_frequency_hz = tuning_frequency_hz, total_voltage = total_voltage, step_size_voltage = step_size_voltage)
tps_script = set_voltages(tps_script, start_time_seconds = total_start_time_seconds + 9*60, imr_front_voltage = imr_front_voltage, imr_back_voltage = imr_back_voltage, ping = 10)
#zero
tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds + 10*60)
#zero vs
tps_script = voltage_scan(tps_script, start_time_seconds = total_start_time_seconds + 18*60, tuning_frequency_hz = tuning_frequency_hz, total_voltage = total_voltage, step_size_voltage = step_size_voltage)
tps_script = set_voltages(tps_script, start_time_seconds = total_start_time_seconds + 19*60, imr_front_voltage = imr_front_voltage, imr_back_voltage = imr_back_voltage, ping = 10)
#cal 20 sccm
tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 20*60, cal_flow_sccm = 20)
#cal 10 sccm
tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 35*60, cal_flow_sccm = 10)
#cal 5 sccm
tps_script = cal_step(tps_script, start_time_seconds =  total_start_time_seconds + 50*60, cal_flow_sccm = 5)
#cal 2 sccm
tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 65*60, cal_flow_sccm = 2)
#zero
tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds + 80*60)
#zero vs
tps_script = voltage_scan(tps_script, start_time_seconds = total_start_time_seconds + 88*60, tuning_frequency_hz = tuning_frequency_hz, total_voltage = total_voltage, step_size_voltage = step_size_voltage)
tps_script = set_voltages(tps_script, start_time_seconds = total_start_time_seconds + 89*60, imr_front_voltage = imr_front_voltage, imr_back_voltage = imr_back_voltage, ping = 10)
#normilization step (cal 10 sccm)
tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 90*60, cal_flow_sccm = 10)
#cal vs
tps_script = voltage_scan(tps_script, start_time_seconds = total_start_time_seconds + 93*60, tuning_frequency_hz = tuning_frequency_hz, total_voltage = total_voltage, step_size_voltage = step_size_voltage)
tps_script = set_voltages(tps_script, start_time_seconds = total_start_time_seconds + 94*60, imr_front_voltage = imr_front_voltage, imr_back_voltage = imr_back_voltage, ping = 10)
#zero
tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds + 95*60)


# %% via example
tps_script = via_turn_on(tps_script, start_time_seconds = 60 , ping = 10)
tps_script = via_turn_off(tps_script, start_time_seconds = 120, ping = 10)
#%%save script to csv file
with open(output_path, 'w') as file:
    csv.writer(file, lineterminator='\r',delimiter='\t').writerows(tps_script)
    csv.list_dialects()
