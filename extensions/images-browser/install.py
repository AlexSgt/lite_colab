import launch
import os

if not launch.is_installed("send2trash"):
    launch.run_pip("install Send2Trash", "Send2Trash requirement for image browser")

try:
    import ImageReward
    import datasets
    import dill
    import diffusers
    import multiprocessing
    import pyarrow
    import xxhash
except (ImportError, ModuleNotFoundError) as e:
    #print(e)
    req_IR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "req_IR.txt")
    launch.run_pip(f'install -r "{req_IR}" --no-deps image-reward', 'ImageReward requirement for image browser')
