python -c 'import pty; pty.spawn("/bin/bash")'
/usr/bin/script -qc /bin/bash /dev/null
perl —e 'exec "/bin/sh";'
perl: exec "/bin/sh";
echo os.system('/bin/bash')
/bin/sh -i
ruby: exec "/bin/sh"
lua: os.execute('/bin/sh')