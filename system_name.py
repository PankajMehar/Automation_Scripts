import platform, subprocess
print(platform.node())
print(platform.system())



def get_processor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl',"-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        return subprocess.check_output(command, shell=True).strip()
    return ""
cpustr = get_processor_info()
print(cpustr)


