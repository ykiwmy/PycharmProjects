import  os

print(os.name)
print(os.system('adb shell screencap -p /sdcard/test/1.png'))
print(os.system('adb devices'))