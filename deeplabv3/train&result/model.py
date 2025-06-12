import onnxruntime as ort
import numpy as np
import time

def load_model_onnx(onnx_path):
    providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
    session = ort.InferenceSession(onnx_path, providers=providers)
    print(f"ONNX Runtime providers: {session.get_providers()}")
    return session

def infer_and_measure_onnx(session, input_tensor):
    """
    input_tensor: numpy array (1, 3, H, W), dtype=float32, normalized
    Trả về: output prediction numpy array (1, C, H, W) và thời gian suy luận (ms)
    """
    input_name = session.get_inputs()[0].name
    start = time.time()
    outputs = session.run(None, {input_name: input_tensor})
    end = time.time()
    infer_time_ms = (end - start) * 1000
    return outputs[0], infer_time_ms
