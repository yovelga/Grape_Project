import torch


def check_gpu():
    if torch.cuda.is_available():
        print(f"✅ GPU is available: {torch.cuda.get_device_name(0)}")
        print(f"Number of CUDA devices: {torch.cuda.device_count()}")
        print(f"GPU in use: {torch.cuda.current_device()}")
    else:
        print("❌ No GPU found. Ensure your server connection is correct.")

check_gpu()
print("check changes on SSH server again C")
