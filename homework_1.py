
import pexpect
import re


#open old primates file with mcmc
oldprimates = open('primates.nex').read()

#open black newprimates file 
newprimates = open('newprimates.nex', 'w')

#replace the mcmc with mcmcp in the oldprimates file and write to newprimates
newprimates.write(oldprimates.replace('mcmc', 'mcmcp'))

#close the newprimates file
newprimates.close()

#spawn the newprimates file in mrbayes
child = pexpect.spawn('mb -i newprimates.nex')

#wait for mrbayes prompt
child.expect('MrBayes >')

#tell mrbayes to stop the stop the analysis
child.sendline(r"mcmc")

#wait for mrbayes prompt
child.expect('Continue with analysis?', timeout = 60)

#tell mr bayes no
child.sendline("no")

#wait for mrbayes prompt
child.expect('MrBayes >')

#print screen output
print child.before

#quit mrbayes
child.sendline('quit')


