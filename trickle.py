from subprocess import check_output,call,STDOUT
from argparse import ArgumentParser
from time import sleep
#check the que making sure there are less than
#n jobs enqueued in the que before excute next commnad
def trickle(jobs, n=1000, nsub=100):
    shouldcheck = True
    for ijob,job in enumerate(jobs):
        nque = n+1
        while shouldcheck:
            nque = getNque()
            if nque > n:
                print 'Too many jobs in que(%d) sleep for 1 min'%nque
                sleep(60)
            else:
                break
        call(job,shell=True)
        shouldcheck = ijob%10==9


def getNque():
    cmd = 'qstat -q'
    out = check_output(cmd, shell=True)
    tmp = out.split('\n')[-2]
    return int(tmp.split()[1])


def main():
    parser = ArgumentParser()
    parser.add_argument('jobfiles',nargs='+')
    args = parser.parse_args()
    jobs = []
    for jobfile in args.jobfiles:
        with open(jobfile) as f:
            jobs += f.readlines()
    jobs = [j for j in jobs if not j.strip().startswith('#')]
    trickle(jobs)


if __name__ == "__main__":
    main()
