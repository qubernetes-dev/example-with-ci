from functools import wraps
import logging

logger = logging.getLogger(__name__)


def cuda_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            import pynvml
        except ImportError:
            print("pynvml is not installed. Please install it to use this decorator.")
            return func(*args, **kwargs)

        pynvml.nvmlInit()
        logger.info(f"Driver Version: {pynvml.nvmlSystemGetDriverVersion()}")
        logger.info(f"CUDA Version: {pynvml.nvmlSystemGetCudaDriverVersion()}")
        deviceCount = pynvml.nvmlDeviceGetCount()
        logger.info(f"Number of GPUs: {deviceCount}")

        result = func(*args, **kwargs)

        for i in range(deviceCount):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            name = pynvml.nvmlDeviceGetName(handle)
            logger.info(f"GPU {i}: {name}")
            info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            logger.info(f"  Total memory: {info.total / 1024 ** 2} MB")
            logger.info(f"  Used memory: {info.used / 1024 ** 2} MB")
            logger.info(f"  Free memory: {info.free / 1024 ** 2} MB")
            logger.info(
                f"  Utilization: {pynvml.nvmlDeviceGetUtilizationRates(handle).gpu} %"
            )
        pynvml.nvmlShutdown()

        return result

    return wrapper
