import os
import mlflow
import argparse

def evalu(a,b):
    return a+b

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--first','-f',type=int, default=2,)
    parser.add_argument('--second','-s',type=int, default=5,)
    args=parser.parse_args()

    with mlflow.start_run():
        mlflow.log_param('first_parameter', args.first)
        mlflow.log_param('sec_parameter', args.second)
        mlflow.log_metric('result',evalu(args.first,args.second))
        # mlflow.log(key,value)
        #mlflow.log_artifact(dir)

    
    