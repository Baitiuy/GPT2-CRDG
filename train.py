import torch
import argparse
import json
import random
import numpy as np



def main():
    parser = argparse.ArgumentParser(description = 'test')
    parser.add_argument('--input_path',default="input", type=str,help ='input files')
    parser.add_argument('--output_path',default = "output", type=str,help='result dir.') 
    parser.add_argument('--raw',action='store_true', help='是否先做tokenize') 
    parser.add_argument('--pretrained_model', default='', type=str, required=False, help='模型训练起点路径')
    # 解析参数
    args = parser.parse_args()
    print ('args:\n' + args.__repr__())


    raw = args.raw

    if raw:
        print('building files' )

    if not args.pretrained_model:
        print('training finished')



if __name__ == '__main__' :
    main()