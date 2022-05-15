import os
import subprocess


def yolact_video_segmentation(video, video_output, model, score_threshold, topk, video_multiframe):
    print("YOLACT video segmentation")
    command = r'conda activate yolact && ' \
              r'python eval.py --config=yolact_icsi_config --dataset=my_icsi_dataset ' \
              r'--trained_model={} --score_threshold={} --top_k={} --video_multiframe={} --video={}:{}'\
        .format(model, score_threshold, topk, video_multiframe, video, video_output)
    print("Command: ", command)
    print("Results will be saved in: ", video_output)

    p = subprocess.Popen(["start", "cmd", "/k", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True, cwd=r'D:/yolact')
    ret_code = p.wait()
    print("ret_code ", ret_code)
    if ret_code != 0:
        print("Something went wrong...")
    return ret_code


def yolact_single_image_segmentation(input_image, output_image, model, score_threshold, topk):
    print("YOLACT single image segmentation")
    command = r'conda activate yolact && ' \
              r'python eval.py --config=yolact_icsi_config --dataset=my_icsi_dataset ' \
              r'--trained_model={} --score_threshold={} --top_k={} --image={}:{}'\
        .format(model, score_threshold, topk, input_image, output_image)
    print("Command: ", command)
    print("Results will be saved in: ", output_image)

    p = subprocess.Popen(["start", "cmd", "/k", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True, cwd=r'D:/yolact')
    ret_code = p.wait()
    print("ret_code ", ret_code)
    if ret_code != 0:
        print("Something went wrong...")
    return ret_code


def yolact_images_segmentation(images_input_path, images_output_path, model, score_threshold, topk):
    print("YOLACT images segmentation")
    command = r'conda activate yolact && ' \
              r'python eval.py --config=yolact_icsi_config --dataset=my_icsi_dataset ' \
              r'--trained_model={} --score_threshold={} --top_k={} --images={}:{}'\
        .format(model, score_threshold, topk, images_input_path, images_output_path)
    print("Command: ", command)
    print("Results will be saved in: ", images_output_path)

    p = subprocess.Popen(["start", "cmd", "/k", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True, cwd=r'D:/yolact')
    ret_code = p.wait()
    print("ret_code ", ret_code)
    if ret_code != 0:
        print("Something went wrong...")
    return ret_code

