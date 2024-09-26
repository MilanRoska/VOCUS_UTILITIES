# -*- coding: utf-8 -*-
"""
Created on Wed Apr 03 10:02:48 2024

@author: m.roska
"""

#%%Packages
import numpy as np
import sys

#%%Functions
#Set Voltages
def check_times(tps_script, start_time_seconds):
    #test if last time in script is after start_time_seconds
    if len(tps_script) > 0:
        last_time_seconds = tps_script[-1][0]
        # Comparing start_time_seconds with the value from the array
        if start_time_seconds < last_time_seconds:
            error_message = f"Error: set start time is smaller then last time in script! ({start_time_seconds}) < ({last_time_seconds})"
            print(error_message)
            sys.exit(1)
        return

def via_turn_off(tps_script, start_time_seconds, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds)    
    #initilize an empy array 
    via_turn_off_arr = np.zeros((1*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        via_turn_off_arr[1*i,:] = [float(start_time_seconds+i), int(XXXX), 'A', float(0)]
    #append lines to final script
    tps_script = np.vstack((tps_script, via_turn_off_arr))
    return tps_script

def via_turn_on(tps_script, start_time_seconds, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds)    
    #initilize an empy array 
    via_turn_on_arr = np.zeros((1*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        via_turn_on_arr[1*i,:] = [float(start_time_seconds+i), int(XXXX), 'A', float(1)]
    #append lines to final script
    tps_script = np.vstack((tps_script, via_turn_on_arr))
    return tps_script

def set_voltages(tps_script, start_time_seconds, imr_front_voltage, imr_back_voltage, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds)    
    #initilize an empy array 
    set_voltages_arr = np.zeros((2*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        set_voltages_arr[2*i,:] = [float(start_time_seconds+i), int(3710), 'A', float(imr_front_voltage)]
        set_voltages_arr[2*i+1,:] = [float(start_time_seconds+i), int(3711), 'A', float(imr_back_voltage)]
    #append lines to final script
    tps_script = np.vstack((tps_script, set_voltages_arr))
    return tps_script

def zero(tps_script, start_time_seconds, zero_flow_sccm = 1000, cal_flow_sccm = 1, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds) 
    #initilize an empy array
    zero_arr = np.zeros((4*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        #set zero flow to set sccm level
        zero_arr[4*i,:] = [float(start_time_seconds+i), int(3310), 'A', float(zero_flow_sccm/1000)]
        #open zero gas valve
        zero_arr[4*i+1,:] = [float(start_time_seconds+i), int(3702), 'A', float(1)]
        #close calibration gas valve
        zero_arr[4*i+2,:] = [float(start_time_seconds+i), int(3703), 'A', float(0)]
        #set calibration gas flow to set sccm
        zero_arr[4*i+3,:] = [float(start_time_seconds+i), int(3320), 'A', float(cal_flow_sccm/1000)]
    #append lines to final script
    tps_script = np.vstack((tps_script, zero_arr))
    return tps_script

def cal_step(tps_script, start_time_seconds, cal_flow_sccm , zero_flow_sccm = 1000, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds) 
    #initilize an empy array
    cal_arr = np.zeros((4*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        #set zero flow to set sccm level
        cal_arr[4*i,:] = [float(start_time_seconds+i), int(3310), 'A', float(zero_flow_sccm/1000)]
        #open zero gas valve
        cal_arr[4*i+1,:] = [float(start_time_seconds+i), int(3702), 'A', float(1)]
        #open calibration gas valve
        cal_arr[4*i+2,:] = [float(start_time_seconds+i), int(3703), 'A', float(1)]
        #set calibration gas flow to set sccm
        cal_arr[4*i+3,:] = [float(start_time_seconds+i), int(3320), 'A', float(cal_flow_sccm/1000)]
    #append lines to final script
    tps_script = np.vstack((tps_script, cal_arr))
    return tps_script

def ambient(tps_script, start_time_seconds, cal_flow_sccm = 1, zero_flow_sccm = 1000, ping = 10):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds) 
    #initilize an empy array
    ambient_arr = np.zeros((4*ping,4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(ping):
        #set zero flow to set sccm
        ambient_arr[4*i,:] = [float(start_time_seconds+i), int(3310), 'A', float(zero_flow_sccm/1000)]
        #close zero gas valve
        ambient_arr[4*i+1,:] = [float(start_time_seconds+i), int(3702), 'A', float(0)]
        #close calibration gas valve
        ambient_arr[4*i+2,:] = [float(start_time_seconds+i), int(3703), 'A', float(0)]
        #set calibration gas flow to 1 sccm
        ambient_arr[4*i+3,:] = [float(start_time_seconds+i), int(3320), 'A', float(cal_flow_sccm/1000)]
    #append lines to final script
    tps_script = np.vstack((tps_script, ambient_arr))
    return tps_script

def voltage_scan(tps_script, start_time_seconds, tuning_frequency_hz, total_voltage, step_size_voltage):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, start_time_seconds)
    #calculate number of steps needed
    steps = total_voltage/step_size_voltage
    #initilize an empy array
    vs_arr = np.zeros((int(2*steps),4), dtype=object)
    #fill array with Time, Parameter Code, 'A'bsolute/'R'elative change of value, value
    #iterate over ping (several pings ensure that parameter changes are read out, pings every second)
    for i in range(int(steps)):
        vs_arr[i*2,:] = [float(start_time_seconds+i*1/tuning_frequency_hz), int(3710), 'R', float(step_size_voltage)]
        vs_arr[i*2+1,:] = [float(start_time_seconds+i*1/tuning_frequency_hz), int(3711), 'R', float(step_size_voltage)]
    #append lines to final script
    tps_script = np.vstack((tps_script, vs_arr))
    return tps_script 

#preset 100 minutes calibration
def calibration_100_minutes(tps_script, total_start_time_seconds):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, total_start_time_seconds)
    #zero
    tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds)
    #normilization step (cal 10 sccm)
    tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 5*60, cal_flow_sccm = 10)
    #zero
    tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds + 10*60)
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
    #normilization step (cal 10 sccm)
    tps_script = cal_step(tps_script, start_time_seconds = total_start_time_seconds + 90*60, cal_flow_sccm = 10)
    #zero
    tps_script = zero(tps_script, start_time_seconds = total_start_time_seconds + 95*60)
    
    return tps_script

#preset 100 minutes calibration with cal and  zero VS
def calibration_100_minutes_vs(tps_script, total_start_time_seconds, tuning_frequency_hz, total_voltage, step_size_voltage, imr_front_voltage = 450, imr_back_voltage = 0):
    #check if set start time is smaller then last entry of the script
    check_times(tps_script, total_start_time_seconds)
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
    
    return tps_script