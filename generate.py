import torch
import os
import argparse



os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='0,1,2,3', type=str, required=False, help='设置使用哪些显卡')
    parser.add_argument('--length', default=-1, type=int, required=False, help='生成长度')
    parser.add_argument('--temperature', default=1, type=float, required=False, help='生成温度，越高越随机')
    parser.add_argument('--topk', default=8, type=int, required=False, help='生成的时候最高几选一')
    parser.add_argument('--topp', default=0, type=float, required=False, help='生成的时候积累概率最高多少')
    parser.add_argument('--repetition_penalty', default=1.0, type=float, required=False)

    args = parser.parse_args()
    print('args:\n' + args.__repr__())

    os.environ["CUDA_VISIBLE_DEVICES"] = args.device  # 此处设置程序使用哪些显卡
    length = args.length
    temperature = args.temperature
    topk = args.topk
    topp = args.topp
    repetition_penalty = args.repetition_penalty

if __name__ == '__main__':
    main()