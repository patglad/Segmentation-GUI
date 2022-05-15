import subprocess


def yolact_video_segmentation(video, model, score_threshold, topk, video_multiframe):
    print("Yolact video segmentation")
    video = "125_16s.avi"
    command = r'conda activate yolact && ' \
              r'python eval.py --config=yolact_icsi_config --dataset=my_icsi_dataset ' \
              r'--trained_model={} --score_threshold={} --top_k={} --video_multiframe={} --video={}'\
        .format(model, score_threshold, topk, video_multiframe, video)
    print("Command: ", command)
    p = subprocess.Popen(["start", "cmd", "/k", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True, cwd=r'D:/yolact')
    ret_code = p.wait()
    print("ret_code ", ret_code)
    if ret_code != 0:
        print("Something went wrong...")
    return ret_code
