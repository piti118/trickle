from subprocess import check_output,call,STDOUT
from argparse import ArgumentParser
from time import sleep
import sys
#check the que making sure there are less than
#n jobs enqueued in the que before excute next commnad
def trickle(jobs, n=1000, nsub=100, simulate=False, que=''):
    shouldcheck = True
    njobs = len(jobs)
    for ijob,job in enumerate(jobs):
        nque = n+1
        while shouldcheck:
            nque = getNque(que)
            if nque > n:
                print 'Too many jobs in que(%d) sleep for 1 min %d/%d'%(nque,ijob,njobs)
                sys.stdout.flush()
                sleep(60)
            else:
                break
        print '%d/%d: %s'%(ijob,njobs,job.strip())
        sys.stdout.flush()
        if not simulate: call(job.strip(),shell=True)
        shouldcheck = ijob%10==9


def getNque(que):
    cmd = 'qstat -q %s'%que
    out = check_output(cmd, shell=True)
    tmp = out.split('\n')[-2]
    return int(tmp.split()[1])


def main():
    parser = ArgumentParser()
    parser.add_argument('jobfiles',nargs='+')
    parser.add_argument('--simulate',action="store_true")
    parser.add_argument('-n','--maxque',type=int,default=1000)
    parser.add_argument('-q','--que',default='')
    args = parser.parse_args()
    jobs = []
    for jobfile in args.jobfiles:
        with open(jobfile) as f:
            jobs += f.readlines()
    jobs = [j for j in jobs if not j.strip().startswith('#')]
    trickle(jobs, n=args.maxque, simulate=args.simulate, que=args.que)


if __name__ == "__main__":
    main()
