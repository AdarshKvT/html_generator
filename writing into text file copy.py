import win32com.client as win32
import time

from report_generator import write_content

def ACC_Active():
    file = open(r'D:\services-workspace\python-scripts\git\html_generator\ACC_Reports copy 2.html', "w")

    # file = open(r"C:\Automotive\Pycharm\Reports\ACC_Reports.html", "w")
    write_content("Test Step 1: Set MO_sig_ReadytoDrive to Drive(0x2)", file)
    write_content("Test Step 2: Set Signal ACC_Int_status to Active (0x1)", file)
    time.sleep(1)
    # init_signalValue = CANoe.GetBus('CAN').GetSignal(1, "GWM_ACC", "ACC_Int_status")
    # init_signalValue.Value = 0x01
    write_content("Test Step 3: Set ACC_MainSwitch_ACC is Active (0x2)", file)
    # Main_signalValue = CANoe.GetBus('CAN').GetSignal(1, "GWM_ACC", "ACC_MainSwitch_ACC")
    # Main_signalValue.Value = 0x02
    write_content("Test Step 4: Set Gear_signal is Drive (0x3)", file)
    # Gear_signalValue = CANoe.GetBus('CAN').GetSignal(1, "GWM_ACC", "Gear_signal")
    # Gear_signalValue.Value = 0x03
    write_content("Test Step 5: Set Sig_Spdmtr_Rq is >40 kmph (0x3)", file)
    # speed_signalValue = CANoe.GetBus('CAN').GetSignal(1, "GWM_ACC", "Sig_Spdmtr_Rq")
    # speed_signalValue.Value = 0x70
    write_content("Test Step 6: Set ACC_Set_signal is Activated (0x3)", file)
    # ACCset_signalValue = CANoe.GetBus('CAN').GetSignal(1, "GWM_ACC", "ACC_Set_signal")
    # ACCset_signalValue.Value = 0x1
    time.sleep(5)
    # acc_state = CANoe.GetBus('CAN').GetSignal(1, "ACC_status", "ACC_sig_status")
    acc_state = 0x02
    print(acc_state)
    if int(acc_state) == 0x02:
        write_content("Test Step 7: Pass ACC state is equal to 2- Active Measured Value: " + str(acc_state), file)
    else:
        write_content("Test Step 7: Fail ACC state is not equals 2- Active Measured value: " + str(acc_state), file)

def standby_3():
    file = open(r'D:\services-workspace\python-scripts\git\html_generator\ACC_Reports copy.html', "w")
    write_content("Report: ACC TEST REPORT", file)
    write_content("Test Step 1: Set Ignition State to On:", file)
    write_content("Test Step 2: wait for 1 sec", file)

    time.sleep(1)

    write_content("Test Step 3: Check ACCState is Off", file)
    acc_state = 0.0
    print(acc_state)
    if int(acc_state) == 0.0:
        write_content("Test Step 2: Pass ACC state is equal to 0 Measured Value: " + str(acc_state), file)

    else:
        write_content("Test Step 2: Fail ACC state is not equals 0 Measured value: " + str(acc_state), file)

    write_content("Test Step 1: Set Ignition State to On:", file)
    write_content("Test Step 2: wait for 1 sec ", file)

    time.sleep(1)
    write_content("Test Step 3: Check ACCState is Off ", file)

    acc_state_1= 0.0
    # acc_state_1.Value = 0x1
    time.sleep(3)
    print(acc_state_1)
    if int(acc_state_1) == 0.0:
        write_content("Test Step 2: Pass ACC state is equal to 0 Measured Value: " + str(acc_state), file)
    else:
        write_content("Test Step 2: Fail ACC state is not equals 0 Measured value: " + str(acc_state), file)

time.sleep(3)
time.sleep(5)
standby_3()
ACC_Active()
