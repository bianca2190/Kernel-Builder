# ChatGPT is pro

import sys
import shutil

base_path = sys.argv[1]

# Replace "/path/to/folder" with the path to your folder
# ksu_folder_path = "drivers/kernelsu"
ksu_folder_path = f"{base_path}/drivers/kernelsu"

# Use the rmtree function to delete the folder and its contents
shutil.rmtree(ksu_folder_path)
print(f"Removed {ksu_folder_path}")

# Replace with the path to your file
# defconfig_filepath = "arch/arm64/configs/vendor/kona-perf_defconfig"
defconfig_filepath = f"{base_path}/arch/arm64/configs/vendor/kona-perf_defconfig"

# Lines to remove
defconfig_lines_to_remove = ["CONFIG_ARM64_MODULE_PLTS=y\n",
                   "CONFIG_KPROBES=y\n",
                   "CONFIG_KRETPROBES=y\n",
                   "CONFIG_HAVE_MOD_ARCH_SPECIFIC=y\n",
                   "CONFIG_STRICT_MODULE_RWX=y\n",
                   "CONFIG_MODULES=y\n",
                   "# CONFIG_MODULE_UNLOAD is not set\n",
                   "# CONFIG_MODVERSIONS is not set\n",
                   "# CONFIG_MODULE_SRCVERSION_ALL is not set\n",
                   "# CONFIG_MODULE_SIG is not set\n",
                   "# CONFIG_MODULE_COMPRESS is not set\n",
                   "# CONFIG_TRIM_UNUSED_KSYMS is not set\n",
                   "# CONFIG_TEST_ASYNC_DRIVER_PROBE is not set\n",
                   "# CONFIG_I2C_STUB is not set\n",
                   "# CONFIG_SPI_LOOPBACK_TEST is not set\n",
                   "CONFIG_MEDIA_ATTACH=y\n",
                   "# CONFIG_RTL8192U is not set\n",
                   "# CONFIG_RTLLIB is not set\n",
                   "# CONFIG_RTL8723BS is not set\n",
                   "# CONFIG_R8188EU is not set\n",
                   "# CONFIG_LTE_GDM724X is not set\n",
                   "# CONFIG_CRYPTO_TEST is not set\n",
                   "CONFIG_KPROBE_EVENTS=y\n",
                   "# CONFIG_PREEMPTIRQ_DELAY_TEST is not set\n",
                   "# CONFIG_KPROBES_SANITY_TEST is not set\n",
                   "# CONFIG_PERCPU_TEST is not set\n",
                   "# CONFIG_TEST_LKM is not set\n",
                   "# CONFIG_TEST_USER_COPY is not set\n",
                   "# CONFIG_TEST_BPF is not set\n",
                   "# CONFIG_TEST_STATIC_KEYS is not set\n",
                   "# CONFIG_TEST_KMOD is not set\n",
                   "# CONFIG_ARM64_RELOC_TEST is not set\n",
                   "CONFIG_MODULE_FORCE_LOAD=y\n"]

with open(defconfig_filepath, "r+") as f:
    lines = f.readlines()
    f.seek(0)  # Move the file pointer to the beginning of the file
    f.truncate()  # Clear the file content
    for line in lines:
        if line not in defconfig_lines_to_remove:
            f.write(line)
    print(f"Processed {defconfig_filepath}")

# Replace with the path to your file
# makefile_filepath = "drivers/Makefile"
makefile_filepath = f"{base_path}/drivers/Makefile"

with open(makefile_filepath, "r+") as f:
    lines = f.readlines()
    f.seek(0)  # Move the file pointer to the beginning of the file
    f.truncate()  # Clear the file content
    f.write(''.join(lines[:-1]).rstrip('\n'))
    print(f"Processed {makefile_filepath}")
