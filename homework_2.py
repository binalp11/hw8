import pexpect
import re


#start interactive MrBayes with newprimates.nex
child = pexpect.spawn('mb -i newprimates.nex')

child.expect('MrBayes >')


#run the sumt analysis
child.sendline(r'sumt')

#wiat for Mr.Bayes prompt
child.expect('MrBayes >')



#print everything before mrbayes prompt
print child.before


#run the sump compand
child.sendline(r'sump')

#wiat for Mr.Bayes prompt
child.expect('MrBayes >')



#print everything before mrbayes prompt
print child.before


#quit
child.sendline('quit')