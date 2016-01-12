import os

open('Script_.tmp', 'w').close()
f = open('Input.txt','r+')
nf = open('Script_.tmp','r+')

print('\n')
print('OLD CFG FILES WILL BE DELETED')

bind = input('Bind to Key: ')
cancel = input('Bind Cancel Key To: ')
delay = input('Delay Between Messages: ')
filename = input('File Name: ')

prepre1 = 'alias '
prepre2 = input('Alias name? ')
prenum = 0
presuf = ' "say '
suffix = '"'
prefix = prepre1+prepre2+str(prenum)

nf.write('bind '+bind+' "'+'exec '+filename+'; '+prepre2+'Set'+str(0)+'"')
nf.write('\n')
nf.write('bind '+cancel+' "'+prepre2+'Cancel'+'"')
nf.write('\n \n')



list = [[]]
setnum = 0
amount = 10
count = 0
listcnt = 0

for i in f:
        if len(i.strip()) > 0:
                prefix = prepre1+prepre2+str(prenum)+presuf
                nf.write('%s%s%s\n' % (prefix, i.rstrip('\n').lstrip(' '), suffix))
                if len(list[setnum]) != amount:
                        list[setnum].append(prepre2+str(prenum))
                elif len(list[setnum]) == amount:
                        setnum += 1
                        list.append([])
                prenum += 1

for i in range(len(list)):
        prefix = prepre1+prepre2+'Set'+str(count)+' "'+'alias '+prepre2+'Cancel'+' '+'"alias '+prepre2+'Set'+str(count+1)+' '+'""";'
        nf.write('\n'+prefix)
        for j in range(len(list[count])):
                if j != 0:
                        nf.write('; ')
                nf.write(list[i][j]+'; wait '+delay)
        count += 1
        prefix = prepre2+'Set'+str(count)
        if i != len(list)-1:
                nf.write('; '+prefix+suffix)
        else:
                nf.write(suffix)

f.close()
nf.close()

for i in os.listdir("."):
        if i.endswith(".cfg"):
                os.remove(i)
        if i.startswith("Script_"):
                os.rename(i, filename+'.cfg')
