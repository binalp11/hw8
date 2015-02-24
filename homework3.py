

import pexpect
import glob
import re



def domcmc(nexusfile, XX=1000 ):
    child = pexpect.spawn('mb -i nexusfile')
    child.expect('MrBayes >')
    child.sendline('set nowarn = yes')
    child.expect('MrBayes >')
    child.sendline('mcmcp ngen = XX')
    child.expect('MrBayes >')
    child.sendline(r'mcmc')
    child.expect('Continue with analysis?', timeout = 60)
    child.sendline('no')
    child.expect('MrBayes >')
    print child.before
    child.sendline('quit')


def dosumtsump(nexusfile):
    child = pexpect.spawn('mb -i nexusfile') 
    child.expect('MrBayes >')
    child.sendline('set nowarn = yes')
    child.expect('MrBayes >')
    child.sendline(r'sumt')
    child.expect('MrBayes >')
    print child.before
    child.sendline('set nowarn = yes')
    child.sendline(r'sump')
    child.expect('MrBayes >')
    print child.before
    child.sendline('quit')




all_files = glob.glob('*')
allcount = len(all_files)

t_files = glob.glob('*.t')
tcount = len(t_files)

print "there are " + str(allcount) + " in the current directory and " + str(tcount) + " files that end in 't'" 


domcmc(newprimates.nex)

dosumtsump(newprimates.nex)

all_files = glob.glob('*')
allcount = len(all_files)

t_files = glob.glob('*.t')
tcount = len(t_files)


print "there are " + str(allcount) + " in the current directory and " + str(tcount) + " files that end in 't'" 

print "these files end in '.t:" + str(all_files)

