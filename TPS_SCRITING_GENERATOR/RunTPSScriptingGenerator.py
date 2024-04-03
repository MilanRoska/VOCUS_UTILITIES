# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:48:52 2024

@author: m.roska
"""
#%% packages
import csv
import numpy as np
from TPSScriptingGenerator import set_voltages, zero, cal_step, ambient, voltage_scan, calibration_100_minutes

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
tps_script = ambient(tps_script, start_time_seconds = 12*60 + 10, ping = 10)

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

#%%save script to csv file
with open(output_path, 'w') as file:
    csv.writer(file, lineterminator='\r',delimiter='\t').writerows(tps_script)
    csv.list_dialects()
