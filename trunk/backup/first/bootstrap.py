#!/usr/bin/env python
"""
A bootstrap script to automatically install FusionCatcher <https://code.google.com/p/fusioncatcher/>.
It only needs to have pre-installed:
- Python version >=2.6.0 and < 3.0
- NumPy <https://pypi.python.org/pypi/numpy>



Author: Daniel Nicorici, Daniel.Nicorici@gmail.com

Copyright (c) 2009-2014 Daniel Nicorici

This file is part of FusionCatcher.

FusionCatcher is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

FusionCatcher is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FusionCatcher (see file 'COPYING.txt').  If not, see
<http://www.gnu.org/licenses/>.

By default, FusionCatcher is running BLAT aligner
<http://users.soe.ucsc.edu/~kent/src/> but it offers also the option to disable
all its scripts which make use of BLAT aligner if you choose explicitly to do so.
BLAT's license does not allow to be used for commercial activities. If BLAT
license does not allow to be used in your case then you may still use
FusionCatcher by forcing not use the BLAT aligner by specifying the option
'--skip-blat'. Fore more information regarding BLAT please see its license.

Please, note that FusionCatcher does not require BLAT in order to find
candidate fusion genes!

This file is running/executing/using BLAT.
"""



import os
import sys
import optparse
import shutil
import subprocess
import time
import tempfile
import ftplib


################################################################################
################################################################################
################################################################################

def PATHS(exe = None, prefix = None, installdir = None):
    global PYTHON_EXE
    global FUSIONCATCHER_PREFIX
    global FUSIONCATCHER_PATH
    global FUSIONCATCHER_BIN
    global FUSIONCATCHER_URL
    global FUSIONCATCHER_DATA
    global FUSIONCATCHER_CURRENT
    global FUSIONCATCHER_ORGANISM
    global FUSIONCATCHER_TOOLS
    global FUSIONCATCHER_CONFIGURATION
    global NUMPY_PATH
    global NUMPY_URL
    global BIOPYTHON_PATH
    global BIOPYTHON_URL
    global XLRD_PATH
    global XLRD_URL
    global OPENPYXL_PATH
    global OPENPYXL_URL
    global SETUPTOOLS_PATH
    global SETUPTOOLS_URL
    global BOWTIE_PATH
    global BOWTIE_URL
    global BLAT_PATH
    global BLAT_URL
    global FATOTWOBIT_PATH
    global FATOTWOBIT_URL
    global SRATOOLKIT_PATH
    global SRATOOLKIT_URL
    global VELVET_PATH
    global VELVET_URL
    global LZO_PATH
    global LZO_URL
    global LZOP_PATH
    global LZOP_URL
    global COREUTILS_PATH
    global COREUTILS_URL
    global PIGZ_PATH
    global PIGZ_URL
    global ENSEMBL_VERSION
    # python
    if exe:
        PYTHON_EXE = expand(exe)
    else:
        PYTHON_EXE = '/usr/bin/python'
    # fusioncatcher

    if prefix:
        FUSIONCATCHER_PREFIX = expand(prefix)
    else:
        FUSIONCATCHER_PREFIX = expand('.')
        if os.getuid() == 0:
            FUSIONCATCHER_PREFIX = expand('/opt')

    if installdir:
        FUSIONCATCHER_PATH = expand(installdir)
        FUSIONCATCHER_PREFIX = expand(os.path.dirname(installdir.rstrip(os.sep)))
    else:
        FUSIONCATCHER_PATH = expand(FUSIONCATCHER_PREFIX,'fusioncatcher')

    FUSIONCATCHER_BIN = expand(FUSIONCATCHER_PATH,'bin')
    FUSIONCATCHER_URL = 'https://sourceforge.net/projects/fusioncatcher/files/fusioncatcher_v0.99.2.zip'
    FUSIONCATCHER_DATA = expand(FUSIONCATCHER_PATH,'data')
    FUSIONCATCHER_CURRENT = expand(FUSIONCATCHER_DATA,'current')
    FUSIONCATCHER_ORGANISM = 'homo_sapiens'
    FUSIONCATCHER_TOOLS = expand(FUSIONCATCHER_PATH,'tools')
    FUSIONCATCHER_CONFIGURATION = expand(FUSIONCATCHER_BIN,'configuration.cfg')
    # numpy
    NUMPY_PATH = os.path.join(FUSIONCATCHER_TOOLS,'numpy')
    NUMPY_URL = 'https://pypi.python.org/packages/source/n/numpy/numpy-1.7.1.tar.gz'
    # biopython
    BIOPYTHON_PATH = os.path.join(FUSIONCATCHER_TOOLS,'biopython')
    BIOPYTHON_URL = 'https://pypi.python.org/packages/source/b/biopython/biopython-1.62.tar.gz'
    # xlrd python
    XLRD_PATH = os.path.join(FUSIONCATCHER_TOOLS,'xlrd')
    XLRD_URL = 'https://pypi.python.org/packages/source/x/xlrd/xlrd-0.9.2.tar.gz'
    # openpyxl python
    OPENPYXL_PATH = os.path.join(FUSIONCATCHER_TOOLS,'openpyxl')
    OPENPYXL_URL = 'https://pypi.python.org/packages/source/o/openpyxl/openpyxl-1.6.2.tar.gz'
    # setuptools python
    SETUPTOOLS_PATH = os.path.join(FUSIONCATCHER_TOOLS,'setuptools')
    SETUPTOOLS_URL = 'https://pypi.python.org/packages/source/s/setuptools/setuptools-1.3.1.tar.gz'
    # BOWTIE
    BOWTIE_PATH = os.path.join(FUSIONCATCHER_TOOLS,'bowtie')
    BOWTIE_URL = 'https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.0.0/bowtie-1.0.0-linux-x86_64.zip'
    # BLAT
    BLAT_PATH = os.path.join(FUSIONCATCHER_TOOLS,'blat')
    BLAT_URL = 'http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/blat/blat'
    # faToTwoBit
    FATOTWOBIT_PATH = os.path.join(FUSIONCATCHER_TOOLS,'fatotwobit')
    FATOTWOBIT_URL = 'http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64.v287/faToTwoBit'
    # SRATOOLKIT
    SRATOOLKIT_PATH = os.path.join(FUSIONCATCHER_TOOLS,'sratoolkit')
    SRATOOLKIT_URL = 'http://ftp-private.ncbi.nlm.nih.gov/sra/sdk/2.3.3-4/sratoolkit.2.3.3-4-centos_linux64.tar.gz'
    # VELVET
    VELVET_PATH = os.path.join(FUSIONCATCHER_TOOLS,'velvet')
    VELVET_URL = 'http://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz'
    # ENSEMBL version
    ENSEMBL_VERSION = ensembl_version()
    # LZO
    LZO_PATH = os.path.join(FUSIONCATCHER_TOOLS,'lzo')
    LZO_URL = 'http://www.oberhumer.com/opensource/lzo/download/lzo-2.06.tar.gz'
    # LZOP
    LZOP_PATH = os.path.join(FUSIONCATCHER_TOOLS,'lzop')
    LZOP_URL = 'http://www.lzop.org/download/lzop-1.03.tar.gz'
    # COREUTILS (for SORT parallel)
    COREUTILS_PATH = os.path.join(FUSIONCATCHER_TOOLS,'coreutils')
    COREUTILS_URL = 'http://ftp.gnu.org/gnu/coreutils/coreutils-8.22.tar.xz'
    # PIGZ (GZIP parallel)
    PIGZ_PATH = os.path.join(FUSIONCATCHER_TOOLS,'pigz')
    PIGZ_URL = 'http://zlib.net/pigz/pigz-2.3.1.tar.gz'



################################################################################
################################################################################
################################################################################

#############################################
# expand path
#############################################
def expand(*p):
    return os.path.abspath(os.path.expanduser(os.path.join(*p)))

#############################################
# get ensembl version
#############################################
def ensembl_version():
    print "Checking latest version of Ensembl database that is available..."
    list_files = []
    last_version = "unknown"
    try:
        ftp = ftplib.FTP("ftp.ensembl.org",timeout=10)
        if ftp:
            ftp.login()
            ftp.cwd("pub")
            list_files = [int(el.lstrip('release').lstrip('-')) for el in ftp.nlst() if el.lower().startswith('release-') and el.lstrip('release').lstrip('-').isdigit()]
    except:
        pass

    if list_files:
        last_version = "v"+str(max(list_files))
    else:
        # try again!
        try:
            import subprocess
            p = subprocess.Popen("wget -nv ftp://ftp.ensembl.org/pub/ -O -", stdout=subprocess.PIPE, stderr=None, shell=True)
            result = p.communicate()[0].split()
            result = [el.split('>release-')[1].split('<')[0] for el in result if el.lower().find('>release-')!=-1]
            result = [int(el) for el in result]
            if result:
                last_version = "v"+str(max(result))
        except:
            pass
    if last_version == 'unknown':
        print "   * Not found! (WARNING: Is the internet connection working?)"
    else:
        print "   * Version %s found!" % (last_version,)
    return last_version




#############################################
# test Python modules
#############################################
def test_module(module, name = "", package = "", web = "", verbose = False, exit = False):
    """ Test is a given module is installed
        Example:
            module = 'Bio'
            name = 'BioPython'
            package = 'python-biopython'
            description = '<https://pypi.python.org/pypi/biopython>'
    """
    if verbose:
        print "Checking if the Python module named '%s' is installed..." % (name,)
    flag = True
    try:
        __import__(module)
    except:
        flag = False
        if verbose:
            if os.getuid() == 0:
                print >>sys.stderr, "  * WARNING: The Python module '%s' is not installed!\n" % (name,)
                print >>sys.stderr, "             Please, install the Python module: %s (see %s for more info)," % (name,web)
                print >>sys.stderr, "             like for example using the commands: "
                print >>sys.stderr, "               sudo apt-get install %s" % (package,)
                print >>sys.stderr, "             or"
                print >>sys.stderr, "               sudo yum install %s" % (package,)
                print >>sys.stderr, "             or"
                print >>sys.stderr, "               sudo easy_install %s" % (package.lstrip('python').lstrip('-'),)
                print >>sys.stderr, ""
            else:
                print >>sys.stderr, "  * WARNING: The Python module '%s' is not installed!\n" % (name,)
                print >>sys.stderr, "             Please, install the Python module: %s (see %s for more info). It is recommended" % (name,web)
                print >>sys.stderr, "             that the admin/root install this module, like for example using the commands: "
                print >>sys.stderr, "               sudo apt-get install %s" % (package,)
                print >>sys.stderr, "             or"
                print >>sys.stderr, "               yum install %s" % (package,)
                print >>sys.stderr, "             or"
                print >>sys.stderr, "               easy_install %s" % (package.lstrip('python').lstrip('-'),)
                print >>sys.stderr, ""
        if exit:
            sys.exit(1)
    module_path = None
    try:
        module_path = getattr(__import__(module),'__path__')[0]
    except:
        if verbose:
            print >>sys.stderr, "  * WARNING: Cannot find the path of the Python module '%s'!" % (name,)

    if verbose:
        if flag:
            if module_path:
                print "  * Ok! Python module '%s' found at '%s'!" % (name,module_path)
            else:
                print "  * Ok! Python module '%s' found!" % (name,)
        else:
            print >>sys.stderr,"  * WARNING! Python module '%s' not found!" % (name,)
    return (flag,module_path)


#############################################
# test a given program/tools/software
#############################################
def test_tool(name = "",
              exe = "",
              web = "",
              param = "",
              verbose = False,
              versions = None,
              version_word = 'version',
              exit = False):
    """ Test if a given tools/program is installed
    """
    flag = False
    if verbose:
        print "Checking if '%s' is installed..." % (name,)

    p = which(exe)
    if p and versions:
        p = os.path.dirname(expand(p))
        if verbose:
            print "  * Found at '%s'!" % (p,)
        flag,r = cmd([[[exe,param],False]], exit = False, verbose = False)
        r = [line for line in r if line.lower().find(version_word.lower()) != -1]
        f = False
        v = None
        for el in versions:
            for line in r:
                if line.lower().find(el.lower()) != -1:
                    f = True
                    v = el
                    break
        if f:
            flag = True
            if verbose:
                print "  * Found supported version '%s'!" % (v,)
        elif verbose:
            print >>sys.stderr,"  * WARNING: Unsupported version found!"
            p = None
            flag = False
    elif verbose:
        print >>sys.stderr,"  * WARNING: Not found!"

    return (flag,p)

#############################################
# temp file
#############################################
def give_me_temp_filename(tmp_dir = None):
    (ft,ft_name) = tempfile.mkstemp(dir = tmp_dir)
    os.close(ft)
    return ft_name

#############################################
# simulates which
#############################################
def which(program):
    """
    Simulates which from Linux
    """
    if os.path.dirname(program):
        if os.access(program,os.X_OK) and os.path.isfile(program):
            return program
    else:
        paths = os.environ["PATH"].split(os.pathsep)
        paths.append(os.getcwd())
        for path in paths:
            if path:
                p = os.path.join(path.strip('"'),program)
                if os.access(p,os.X_OK) and os.path.isfile(p):
                    return p
    return None

##############################################
# execute command line commands
##############################################
def cmd(cmds = [],
        exit=True,
        verbose = True):
    """
    stderr = os.devnull
    stderr = subprocess.STDOUT
    """
    f = True
    r = []
    rr = []
    for c in cmds:
        if not c:
            continue
        c0 = [el for el in c[0] if el]
        c1 = c[1]
        if verbose:
            print "    # " + ' '.join(c0)

        if c[0][0] == "cd" and len(c[0]) == 2:
            exit = os.chdir(c[0][1])
            if verbose and exit:
                print >>sys.stderr,''
                print >>sys.stderr, "  * ERROR: Unable to change the directory: '%s'!" % (c[0][1],)
            if exit:
                sys.exit(1)
        else:
            p = subprocess.Popen(c0, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = c1)
            r = p.communicate()[0].splitlines()
            if p.returncode != 0:
                f = False
                if verbose:
                    print >>sys.stderr,''
                    print >>sys.stderr, "  * ERROR: Unable to execute: '%s'!" % (' '.join(c0),)
                    for line in r:
                        print >>sys.stderr, line
                if exit:
                    sys.exit(1)
                rr.extend(r)
                break
            rr.extend(r)

    return (f,rr)

#############################################
# install a Python modules from source
#############################################
def install_module(package, url, path, exe = '', pythonpath = '', verbose = True, exit = True):
    """
    module = module's name
    url =
    path = where to be installed
    """
    # wget https://pypi.python.org/packages/source/o/openpyxl/openpyxl-1.6.2.tar.gz
    # tar zxvf openpyxl-1.6.2.tar.gz
    # cd openpyxl-1.6.2
    # python setup.py build
    afile = os.path.basename(url)
    path = os.path.abspath(os.path.expanduser(path))
    short_path = os.path.dirname(path.rstrip(os.path.sep))
    adir = afile.rstrip('.tar.gz').rstrip('.tgz')
    apython = exe
    if not exe:
        apython = 'python'
    pypath = ''
    if pythonpath:
        pypath = 'PYTHONPATH=%s' % (pythonpath,)
    cmds = []
    if os.getuid() == 0:
        if verbose:
            print "Installing Python package '%s' as root..." % (package,)
        f,r = cmds([['apt-get']], verbose = False, exit = False)
        if f:
            cmds.append(['apt-get','install',package],False)
        else:
            f,r = cmds([['yum']], verbose = False, exit = False)
            if f:
                cmds.append(['yum','install',package],False)
            else:
                f,r = cmds([['easy_install','--version']], verbose = False, exit = False)
                if f:
                    cmds.append((apython,'easy_install',package.lstrip('python').lstrip('-')),False)
                if verbose:
                    print >>sys.stderr, "  * ERROR: No idea how to install the Python module '%s' using other package " % (module,)
                    print >>sys.stderr, "           managers than 'apt-get', 'yum', or 'easy_install'!"
                if exit:
                    sys.exit(1)
    else:
        if verbose:
            print "Installing Python module '%s' locally '%s'..." % (package,path)
        cmds = [(['mkdir','-p', short_path],False),
                (["rm",'-rf', os.path.join(short_path,afile)],False)]
        if url.startswith('http:') or url.startswith('https:') or url.startswith('ftp:'):
            cmds = cmds + [(['wget', url, '-P', short_path,'--no-check-certificate'],False)]
        else:
            cmds = cmds + [(['cp', url, short_path],False)]
        cmds = cmds + [(["rm",'-rf', path],False),
                (["tar", "-xvzf", os.path.join(short_path,afile), "-C", short_path],False),
                (["ln",'-s',os.path.join(short_path,adir),path],False),
                #(["cd",path,";",pypath,apython,"setup.py","build"],True),
                (["cd",os.path.join(short_path,adir),";",pypath,apython,"setup.py","build"],True)
                #([pypath,apython,os.path.join(short_path,adir,'setup.py'),"build"],True)
             ]
    cmd(cmds,
        verbose = verbose,
        exit = exit
        )
    if verbose:
        print "  * Done!"

#############################################
# install a tool (containing executables)
#############################################
def install_tool(name, url, path, verbose = True, exit = True, env_configure = []):
    """
    url =
    path = where to be installed
    """
    # cd /apps/fusioncatcher/tools
    # wget http://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.08.tgz
    # tar zxvf velvet_1.2.08.tgz
    # cd velvet_1.2.08
    # make
    # cd ..
    # ln -s velvet_1.2.08 velvet
    if verbose:
        print "Installing tool '%s' at '%s' from '%s'" % (name,path,url)
    afile = os.path.basename(url)
    path = os.path.abspath(os.path.expanduser(path))
    short_path = os.path.dirname(path.rstrip(os.path.sep))
    adir = afile.rstrip('.tar.gz').rstrip('.tgz').rstrip('.zip').rstrip('.tar.xz')

    if afile.endswith('.tar.gz') or afile.endswith('.tgz') or afile.endswith('.zip') or afile.endswith('.tar.xz'):
        decompress = [(["tar", "-xvzf", os.path.join(short_path,afile), "-C", short_path],False)]
        if afile.endswith('.zip'):
            decompress = [(["unzip","-o", os.path.join(short_path,afile), "-d", short_path],False)]
        elif afile.endswith('.tar.xz'):
            cwd = os.path.abspath(os.path.expanduser(os.getcwd()))
            decompress = [(["cd",short_path],False),
                          (["unxz","--keep",os.path.join(short_path,afile)],False),
                          (["tar", "xvf", os.path.join(short_path,afile[:-3]), "-C", short_path],False),
                          (["cd",cwd],False),
                          ]
            #unxz -c coreutils-8.22.tar.xz | tar xv


        cmds = [(['mkdir','-p',short_path],False),
                (["rm",'-rf',os.path.join(short_path,afile)],False)]
        if url.startswith('http:') or url.startswith('https:') or url.startswith('ftp:'):
            cmds = cmds + [(['wget', url, '-P', short_path,'--no-check-certificate'],False)]
        else:
            cmds = cmds + [(['cp', url, short_path],False)]
        cmds = cmds + [(["rm",'-rf',path],False),
                       (["rm",'-rf',os.path.join(short_path,adir)],False)
                      ]
        cmd(cmds,
            verbose = verbose,
            exit = exit
            )

        listdir = set([os.path.join(short_path,el) for el in os.listdir(short_path) if (not el.startswith('.')) and os.path.isdir(os.path.join(short_path,el))])
        #cmds = [ decompress  ]
        cmds = decompress
        cmd(cmds,
            verbose = verbose,
            exit = exit
            )
        newdir = [os.path.join(short_path,el) for el in os.listdir(short_path) if ( (not el.startswith('.')) and
                                                                                    os.path.isdir(os.path.join(short_path,el)) and
                                                                                    not os.path.join(short_path,el) in listdir)]

        if newdir and len(newdir) == 1:
            newdir = newdir[0]
        else:
            if verbose:
                print >>sys.stderr, "ERROR: Cannot detect the directory where the archive has been decompressed!"
            if exit:
                sys.exit(1)

        cmds = []
        if not os.path.isdir(os.path.join(short_path,adir)):
            cmds.append((["rm","-rf",os.path.join(short_path,adir)],False))
            cmds.append((["mv",newdir,os.path.join(short_path,adir)],False))
            cmds.append((["ln",'-s',os.path.join(short_path,adir),path],False))
        else:
            cmds.append((["ln",'-s',newdir,path],False))
        if os.path.isfile(os.path.join(newdir,'configure')):
            cwd = os.path.abspath(os.path.expanduser(os.getcwd()))
            cmds.append((["cd",newdir],True))
            if env_configure:
                x = env_configure[:]
                x.insert(0,"env")
                x.append("./configure")
                cmds.append((x,True))
            else:
                cmds.append((["./configure"],False))
            cmds.append((["cd",cwd],False))

            cmd(cmds,
                verbose = verbose,
                exit = exit
                )
            cmds = []

        if os.path.isfile(os.path.join(newdir,'Makefile')):
            cmds.append((["make","-C",newdir],False))
        cmds.append((['chmod','-R','+rx',path],False))

        cmd(cmds,
            verbose = verbose,
            exit = exit
            )
    else:
        # it is just an executable
        cmds = [(['mkdir','-p',path],False),
                (["rm",'-rf',os.path.join(path,afile)],False)]
        if url.startswith('http:') or url.startswith('https:') or url.startswith('ftp:'):
            cmds = cmds + [(['wget', url, '-P',path,'--no-check-certificate'],False)]
        else:
            cmds = cmds + [(['cp', url, path],False)]
        cmds = cmds + [(['chmod','+x',os.path.join(path,afile)],False)
                ]
        cmd(cmds,
            verbose = verbose,
            exit = exit
            )
    if verbose:
        print "  * Done!"

#############################################
# User input
#############################################
def accept(question = "", yes = True, no = False, exit = False, force = False):
    """
    force => forces all answers on yes!
    """
    flag = yes
    if not force:
        if yes and no:
            print >>sys.stderr, "ERROR: YES and NO answer cannot be both default answers!"
            sys.exit(1)
        y = 'y'
        if yes: # default is YES
            y = 'Y'
        n = 'n'
        if no: # default is NO
            n = 'N'
        while True:
            text = raw_input("%s [%s/%s]: " % (question, y, n))
            if not text:
                if yes:
                    text = 'y'
                elif no:
                    text = 'n'
                else:
                    continue

            if text.lower() == 'n':
                flag = False
                break
            elif text.lower() == 'y':
                flag = True
                break
            else:
                continue
        if exit and not flag:
            sys.exit(1)
    return flag

#############################################
# test and install Python module
#############################################
def module(module,
           name,
           package,
           web,
           force,
           url,
           path,
           install = False, # forced install
           pythonpath = ''):
    r = False
    thepath = None
    if not install:
        (r, p) = test_module(module = module,
                             name = name,
                             package = package,
                             web = web,
                             verbose = True,
                             exit = False)
    if r:
        thepath = p
    else:
        r = accept(question = "  Do you accept to install the Python module '%s' here '%s'?" % (name,path),
                   yes = True,
                   no = False,
                   exit = False,
                   force = force)
        if not r:
            p = expand(raw_input("  Type new path: "))
            if p:
                path = p
            thepath = path
        install_module(package = package,
                       url = url,
                       path = path,
                       exe = PYTHON_EXE,
                       pythonpath = pythonpath
                      )
    return thepath

#############################################
# test and install software tool module
#############################################
def tool(name,
         exe,
         param,
         web,
         versions,
         force,
         url,
         path,
         install = False,
         version_word = None,
         env_configure = []):

    r = False
    thepath = None
    if not install:
        if version_word:
            (r, p) = test_tool(name = name,
                               exe = exe,
                               param = param,
                               web = web,
                               verbose = True,
                               versions = versions,
                               version_word = version_word,
                               exit = False)
        else:
            (r, p) = test_tool(name = name,
                               exe = exe,
                               param = param,
                               web = web,
                               verbose = True,
                               versions = versions,
                               exit = False)

    if r:
        thepath = p
    else:
        r = accept(question = "  Do you accept to install the %s here: %s ?" % (name,expand(path)),
                   yes = True,
                   no = False,
                   exit = False,
                   force = force)
        if not r:
            p = expand(raw_input("  Type new path: "))
            if p:
                path = p
            thepath = path
        install_tool(name = name,
                     url = url,
                     path = expand(path),
                     verbose = True,
                     env_configure = env_configure
                    )
    return thepath

################################################################################
# MAIN
################################################################################
if __name__ == '__main__':


    # initializing the PATHS
    PATHS()

    #command line parsing

    usage = "%prog [options]"
    description = ("A bootstrap script to automatically install FusionCatcher\n"+
                  "<https://code.google.com/p/fusioncatcher/>. It only needs\n"+
                  "to have pre-installed: (i) Python version >=2.6.0 and < 3.0,\n"+
                  "and (ii) NumPy <https://pypi.python.org/pypi/numpy>.")
    version = "%prog 0.15 beta"

    parser = optparse.OptionParser(usage = usage,
                                   description = description,
                                   version = version)

    parser.add_option("-d","--instal-dir",
                      action = "store",
                      type = "string",
                      dest = "installation_directory",
                      default = FUSIONCATCHER_PATH,
                      help = """The directory where FusionCatcher will be installed. Default is '%default'.""")

    parser.add_option("-p","--prefix",
                      action = "store",
                      type = "string",
                      dest = "prefix_directory",
                      help = """The FusionCatcher will be installed in 'prefix_directory/fusioncatcher'.""")

    parser.add_option("-a","--install-all",
                      action = "store_true",
                      default = False,
                      dest = "install_all",
                      help = """It forcibly installs all the software tools and Python modules needed even if they are already installed.""")

    parser.add_option("-m","--install-all-py",
                      action = "store_true",
                      default = False,
                      dest = "install_all_py",
                      help = """It forcibly installs all the Python modules needed even if they are already installed.""")

    parser.add_option("-t","--install-all-tools",
                      action = "store_true",
                      default = False,
                      dest = "install_all_tools",
                      help = """It forcibly installs all the software tools needed even if they are already installed.""")

    parser.add_option("-s","--skip-dependencies",
                      action = "store_true",
                      default = False,
                      dest = "skip_install_all",
                      help = """It skips installing and testing all the dependencies (i.e. software tools and Python modules). Only the FusionCatcher scripts will be installed. Use this when there the internet connection is broken or not availble.""")

    parser.add_option("-y","--yes",
                      action = "store_true",
                      default = False,
                      dest = "force_yes",
                      help = """It answers automatically all questions with yes.""")

    parser.add_option("--list-dependencies",
                      action = "store_true",
                      default = False,
                      dest = "list_dependencies",
                      help = """It lists all the needed dependencies. No installation is done!""")

    parser.add_option("-b","--build",
                      action = "store_true",
                      default = False,
                      dest = "build",
                      help = """It builds (and also some download is required) the build files for human organism, which are needed to run FusionCatcher. Default value is '%default'.""")

    parser.add_option("-n","--download",
                      action = "store_true",
                      default = False,
                      dest = "download",
                      help = """It downloads from <http://sf.net> the build files for human organism, which are needed to run FusionCatcher. Default value is '%default'.""")


    parser.add_option("-x","--extra",
                      action = "store_true",
                      default = False,
                      dest = "extra",
                      help = """It installs the last version of SORT (which allows several CPUs to be used and compression of temporary files) and LZOP compression. Default value is '%default'.""")

    parser.add_option("-l","--local",
                      action = "store",
                      type = "string",
                      dest = "local",
                      help = """By default all the software tools and Python modules are downloaded using internet. In case that one wishes to proceed with the install by using all the locally pre-downloaded software tools and Python modules this option should be used. It specifies the local path where all the software tools and Python modules are available and no internet connection will be used.""")

    parser.add_option("-f","--local-fusioncatcher",
                      action = "store",
                      type = "string",
                      dest = "local_fusioncatcher",
                      help = """By default scripts belonging to FusionCatcher are downloaded using internet. In case that one wishes to proceed with the installation by using the FusionCatcher ZIP archive this option should be used. It specifies the local path where FusionCatcher archive is available and no internet connection will be used.""")

    (options, args) = parser.parse_args()


################################################################################
################################################################################
################################################################################

    ############################################################################
    # List all dependencies
    ############################################################################
    if options.list_dependencies:
        print "FusionCatcher: ",FUSIONCATCHER_URL
        print "NumPy: ",NUMPY_URL
        print "BioPython: ",BIOPYTHON_URL
        print "Python module XLRD: ",XLRD_URL
        print "Python module OpenPyXL: ",OPENPYXL_URL
        print "Python SETUPTOOLS: ",SETUPTOOLS_URL
        print "Bowtie: ",BOWTIE_URL
        print "Blat: ",BLAT_URL
        print "FaToTwoBit (from Blat toolbox): ",FATOTWOBIT_URL
        print "SRAToolKit (from NCBI): ",SRATOOLKIT_URL
        print "Velvet (de novo assembler): ",VELVET_URL
        sys.exit(0)

    ############################################################################
    # Python version
    ############################################################################
    print "Checking Python version..."
    version = sys.version_info
    if version >= (2,6) and version < (3,0):
        print "  * Ok! Found Python version: %s.%s" % (version[0],version[1])
    else:
        print >>sys.stderr, "  * ERROR: Found Python version: %s.%s !\n" % (version[0],version[1])
        print >>sys.stderr, "           The Python version should be >=2.6.0 and < 3.0 . If there is another"
        print >>sys.stderr, "           Python version installed you could run again this script using that"
        print >>sys.stderr, "           Python version, for example: '/some/other/pythonXYZ bootstrap.py' !"
        sys.exit(1)

    ############################################################################
    # Test 64-bit environment
    ############################################################################
    print "Checking if this environment is a 64-bit environment..."
    import struct
    if struct.calcsize("P") * 8 >= 64:
        print "  * Ok! 64-bit environment found."
    else:
        print >>sys.stderr, "  * ERROR: Not a 64-bit environment! 64-bit environment is needed!"
        sys.exit(1)

    ############################################################################
    # Check if WGET is available
    ############################################################################
    r = os.system('wget --help > /dev/null 2>&1')
    if r != 0:
        print >>sys.stderr, "  * ERROR: 'wget' is not available! Please, install 'wget'!"
        sys.exit(1)

    print ""
    print "Installing FusionCatcher from <https://code.google.com/p/fusioncatcher/>"
    print "------------------------------------------------------------------------"
    print ""

    # validate options
    if options.skip_install_all and (options.install_all_tools or
       options.install_all_py or options.install_all):
        parser.error("Incompatible command line options (which cannot be used simultaneously)!")

    # validate options
    if options.local and options.local_fusioncatcher:
        parser.error("Incompatible command line options (which cannot be used simultaneously)!")

    if options.prefix_directory:
        options.installation_directory = expand(options.prefix_directory,'fusioncatcher')
        PATHS(installdir = options.installation_directory)


    ############################################################################
    # Download using URL or copy from a local path?
    ############################################################################
    if options.local:
        if os.path.isdir(options.local):
            # modify all URLS
            FUSIONCATCHER_URL = os.path.join(options.local, os.path.basename(FUSIONCATCHER_URL))
            NUMPY_URL = os.path.join(options.local, os.path.basename(NUMPY_URL))
            BIOPYTHON_URL = os.path.join(options.local, os.path.basename(BIOPYTHON_URL))
            XLRD_URL = os.path.join(options.local, os.path.basename(XLRD_URL))
            OPENPYXL_URL = os.path.join(options.local, os.path.basename(OPENPYXL_URL))
            SETUPTOOLS_URL = os.path.join(options.local, os.path.basename(SETUPTOOLS_URL))
            BOWTIE_URL = os.path.join(options.local, os.path.basename(BOWTIE_URL))
            BLAT_URL = os.path.join(options.local, os.path.basename(BLAT_URL))
            FATOTWOBIT_URL = os.path.join(options.local, os.path.basename(FATOTWOBIT_URL))
            SRATOOLKIT_URL = os.path.join(options.local, os.path.basename(SRATOOLKIT_URL))
            VELVET_URL = os.path.join(options.local, os.path.basename(VELVET_URL))
        else:
            print >> sys.stderr,"ERROR: '%s' should be a directory!" % (options.local,)
            sys.exit(0)
    elif options.local_fusioncatcher:
        FUSIONCATCHER_URL = options.local_fusioncatcher

    ############################################################################
    # Installation path of FusionCatcher
    ############################################################################
    print "Path for installation of FusionCatcher: '%s'" % (options.installation_directory,)
    r = accept(question = "  Do you accept this path (WARNING: some files/directories within this path may be deleted/replaced/updated without warning)?",
               yes = True,
               no = False,
               exit = False,
               force = options.force_yes)
    if r:
        FUSIONCATCHER_PATH = options.installation_directory
    else:
        p = expand(raw_input("  Type new path:"))
        PATHS(installdir = p)

    ############################################################################
    # Absolute path to the Python executable
    ############################################################################
    print "Obtaining the absolute path of the Python executable..."
    PYTHON_EXE = expand(sys.executable)
    print "  * Ok! '%s' found!" % (PYTHON_EXE,)


    ############################################################################
    # FusionCatcher
    ############################################################################
    install_tool(name = 'FusionCatcher (fusion genes finder in RNA-seq data)',
                 url = FUSIONCATCHER_URL,
                 path = FUSIONCATCHER_BIN,
                 verbose = True
                )
    if os.getuid() == 0: # root
        cmd([
             [["rm","-rf","/usr/bin/fusioncatcher"],False],
             [["ln","-s",os.path.join(FUSIONCATCHER_BIN,'fusioncatcher'),"/usr/bin/fusioncatcher"],False],
             [["rm","-rf","/usr/bin/fusioncatcher-build"],False],
             [["ln","-s",os.path.join(FUSIONCATCHER_BIN,'fusioncatcher-build'),"/usr/bin/fusioncatcher-build"],False]
            ],
            exit=True,
            verbose = True)

    if not options.skip_install_all:
        ############################################################################
        # NumPy
        ############################################################################
        (r, p) = test_module(module = "numpy",
                             name = "NumPy",
                             package = "python-numpy",
                             web = "<https://pypi.python.org/pypi/numpy>",
                             verbose = True,
                             exit = True)
        if r:
            NUMPY_PATH = p

        ############################################################################
        # BioPython
        ############################################################################
        r = module(module = "Bio",
                   name = "BioPython",
                   package = "python-biopython",
                   web = "<https://pypi.python.org/pypi/biopython>",
                   force = options.force_yes,
                   url = BIOPYTHON_URL,
                   path = BIOPYTHON_PATH,
                   install = options.install_all or options.install_all_py
                   )
        if r:
            BIOPYTHON_PATH = r

        ############################################################################
        # Python module: XLRD
        ############################################################################
        r = module(module = "xlrd",
                   name = "Xlrd",
                   package = "python-xlrd",
                   web = "<https://pypi.python.org/pypi/xlrd>",
                   force = options.force_yes,
                   url = XLRD_URL,
                   path = XLRD_PATH,
                   install = options.install_all or options.install_all_py
                   )
        if r:
            XLRD_PATH = r

        ############################################################################
        # Python module: OPENPYXL & SETUPTOOLS
        ############################################################################
        r = False
        if (not options.install_all) and (not options.install_all_py):
            (r, p) = test_module(module = "openpyxl",
                                 name = "OpenPyXL",
                                 package = "python-openpyxl",
                                 web = "<https://pypi.python.org/pypi/openpyxl>",
                                 verbose = False,
                                 exit = False)
        if r:
            OPENPYXL_PATH = p
        else:
            r = module(module = "setuptools",
                       name = "SetupTools",
                       package = "python-setuptools",
                       web = "<https://pypi.python.org/pypi/setuptools>",
                       force = options.force_yes,
                       url = SETUPTOOLS_URL,
                       path = SETUPTOOLS_PATH,
                       install = options.install_all or options.install_all_py
                      )
            if r:
                SETUPTOOLS_PATH = r

            r = module(module = "openpyxl",
                       name = "OpenPyXL",
                       package = "python-openpyxl",
                       web = "<https://pypi.python.org/pypi/openpyxl>",
                       force = options.force_yes,
                       url = OPENPYXL_URL,
                       path = OPENPYXL_PATH,
                       install = options.install_all or options.install_all_py,
                       pythonpath = SETUPTOOLS_PATH)
            if r:
                OPENPYXL_PATH = r


        ############################################################################
        # BOWTIE
        ############################################################################
        r = tool(name = "BOWTIE (short read aligner)",
                 exe = "bowtie",
                 param = "--version",
                 web = "<https://bowtie-bio.sourceforge.net/index.shtml>",
                 versions = ('1.0.0',),
                 force = options.force_yes,
                 url = BOWTIE_URL,
                 path = BOWTIE_PATH,
                 install = options.install_all or options.install_all_tools)
        if r:
            BOWTIE_PATH = r

        ############################################################################
        # SRATOOLKIT
        ############################################################################
        r = tool(name = "NCBI SRA Toolkit (sequence assembler for short reads)",
                 exe = "fastq-dump",
                 param = "",
                 web = "<http://www.ncbi.nlm.nih.gov/Traces/sra/?view=software>",
                 versions = ('2.3.2','2.3.3','2.3.3-4'),
                 version_word = 'fastq-dump',
                 force = options.force_yes,
                 url = SRATOOLKIT_URL,
                 path = SRATOOLKIT_PATH,
                 install = options.install_all or options.install_all_tools)
        if r:
            SRATOOLKIT_PATH = r

        ############################################################################
        # BLAT
        ############################################################################
        blat = False
        if (not options.install_all) and (not options.install_all_py):
            (b,p) = test_tool(name = "BLAT (alignment tool)",
                              exe = "blat",
                              web = "<http://www.ncbi.nlm.nih.gov/Traces/sra/?view=software>",
                              param = "",
                              versions = ('35x1',),
                              version_word = 'blat v.',
                              verbose = False,
                              exit = False)
            if not b:
                blat = True
        r = tool(name = "BLAT (alignment tool)",
                 exe = "blat",
                 param = "",
                 web = "<http://www.ncbi.nlm.nih.gov/Traces/sra/?view=software>",
                 versions = ('35x1',),
                 version_word = 'blat v.',
                 force = options.force_yes,
                 url = BLAT_URL,
                 path = BLAT_PATH,
                 install = options.install_all or options.install_all_tools)
        if r:
            BLAT_PATH = r

        r = tool(name = "FaToTwoBit (companion of BLAT alignment tool)",
                 exe = "faToTwoBit",
                 param = "",
                 web = "<http://www.ncbi.nlm.nih.gov/Traces/sra/?view=software>",
                 versions = ('in.fa',),
                 version_word = "faToTwoBit",
                 force = options.force_yes,
                 url = FATOTWOBIT_URL,
                 path = FATOTWOBIT_PATH,
                 install = options.install_all or options.install_all_tools or blat)
        if r:
            FATOTWOBIT_PATH = r

        ############################################################################
        # VELVET
        ############################################################################
        r = tool(name = "VELVET (sequence assembler for short reads)",
                 exe = "velveth",
                 param = "--version",
                 web = "<http://www.ebi.ac.uk/~zerbino/velvet/>",
                 versions = ('1.2.09','1.2.10'),
                 force = options.force_yes,
                 url = VELVET_URL,
                 path = VELVET_PATH,
                 install = options.install_all or options.install_all_tools)
        if r:
            VELVET_PATH = r

        ############################################################################
        # EXTRA (SORT and LZOP)
        ############################################################################
        if options.extra:
            # LZO library
            r = tool(name = "LZO (LZO library for LZOP compression)",
                     exe = "lzop",
                     param = "-V",
                     web = "<http://www.oberhumer.com/opensource/lzo/>",
                     versions = ('v1.03',),
                     version_word = 'lzop',
                     force = options.force_yes,
                     url = LZO_URL,
                     path = LZO_PATH,
                     install = options.install_all or options.install_all_tools)
            if r:
                LZO_PATH = r

            # LZOP executable
            r = tool(name = "LZOP compression",
                     exe = "lzop",
                     param = "-V",
                     web = "<http://www.lzop.org/>",
                     versions = ('v1.03',),
                     version_word = 'lzop',
                     force = options.force_yes,
                     url = LZOP_URL,
                     path = LZOP_PATH,
                     install = options.install_all or options.install_all_tools,
                     env_configure = ['CPPFLAGS="-I%s"' % (expand(LZO_PATH,'include','lzo'),),
                                      'LDFLAGS="-L%s"' % (expand(LZO_PATH,'src','.libs'),)])
            if r:
                LZOP_PATH = r

            # COREUTILS (for new SORT)
            r = tool(name = "COREUTILS (for latest SORT)",
                     exe = "sort",
                     param = "--version",
                     web = "<http://ftp.gnu.org/gnu/coreutils>",
                     versions = ('v8.22',),
                     version_word = 'coreutils',
                     force = options.force_yes,
                     url = COREUTILS_URL,
                     path = COREUTILS_PATH,
                     install = options.install_all or options.install_all_tools)
            if r:
                COREUTILS_PATH = r

            # PIGZ (GZIP parallel)
            r = tool(name = "PIGZ (GZIP parallel)",
                     exe = "pigz",
                     param = "--version",
                     web = "<http://zlib.net/pigz/>",
                     versions = ('2.3.1',),
                     version_word = 'pigz',
                     force = options.force_yes,
                     url = PIGZ_URL,
                     path = PIGZ_PATH,
                     install = options.install_all or options.install_all_tools)
            if r:
                PIGZ_PATH = r

    ############################################################################
    # PYTHON SHEBANG
    ############################################################################
    print "Checking the shebang of FusionCatcher Python scripts..."
    if which('python') != PYTHON_EXE:
        print "  * Updating the SHEBANG of Python scripts with '%s'" % (PYTHON_EXE,)
        pies = [os.path.join(FUSIONCATCHER_BIN,f) for f in os.listdir(FUSIONCATCHER_BIN) if f.endswith('.py') and os.path.isfile(os.path.join(FUSIONCATCHER_BIN,f)) and not f.startswith('.')]
        for f in pies:
            d = file(f,'r').readlines()
            if d:
                d[0] = "#!%s\n" % (PYTHON_EXE,)
            file(f,'w').writelines(d)
        print "  * Done!"
    else:
        print "  * Ok!"

    ############################################################################
    # FUSIONCATCHER CONFIGURATION
    ############################################################################
    print "Updating the configuration file of FusionCatcher..."
    print "  * configuration file '%s'" % (FUSIONCATCHER_CONFIGURATION,)
    # update the SRATOOLKIT with 'bin'
    sra = os.path.join(SRATOOLKIT_PATH,'bin')
    if (SRATOOLKIT_PATH and
        (not os.path.isfile(os.path.join(SRATOOLKIT_PATH,'bin','fastq-dump'))) and
        os.path.isfile(os.path.join(SRATOOLKIT_PATH,'fastq-dump'))
       ):
        sra = SRATOOLKIT_PATH
    # update the COREUTILS with 'src'
    coreutils = os.path.join(COREUTILS_PATH,'src')
    if (COREUTILS_PATH and
        (not os.path.isfile(os.path.join(COREUTILS_PATH,'src','sort'))) and
        os.path.isfile(os.path.join(COREUTILS_PATH,'sort'))
       ):
        coreutils = COREUTILS_PATH
    # update the LZOP with 'src'
    lzop = os.path.join(LZOP_PATH,'src')
    if (LZOP_PATH and
        (not os.path.isfile(os.path.join(LZOP_PATH,'src','lzop'))) and
        os.path.isfile(os.path.join(LZOP_PATH,'lzop'))
       ):
        lzop = LZOP_PATH
    config_file = FUSIONCATCHER_CONFIGURATION
    data = []
    data.append("[paths]\n")
    data.append("python = %s\n" %(os.path.dirname(PYTHON_EXE),))
    data.append("data = %s\n"%(FUSIONCATCHER_CURRENT,))
    data.append("scripts = %s\n"%(FUSIONCATCHER_BIN,))
    data.append("bowtie = %s\n"%(BOWTIE_PATH,))
    data.append("blat = %s\n"%(BLAT_PATH,))
    data.append("velvet = %s\n"%(VELVET_PATH,))
    data.append("fatotwobit = %s\n"%(FATOTWOBIT_PATH,))
    data.append("sratoolkit = %s\n"%(sra,))
    data.append("numpy = %s\n"%(NUMPY_PATH,))
    data.append("biopython = %s\n"%(BIOPYTHON_PATH,))
    data.append("xlrd = %s\n"%(XLRD_PATH,))
    data.append("openpyxl = %s\n"%(OPENPYXL_PATH,))

    data.append("lzo = %s\n"%(LZO_PATH,))
    data.append("lzop = %s\n"%(lzop,))
    data.append("coreutils = %s\n"%(coreutils,))
    data.append("pigz = %s\n"%(PIGZ_PATH,))

    file(config_file,'w').writelines(data)

    ############################################################################
    ############################################################################
    print "-------------------------------------------------------------------------------"
    print "FusionCatcher is installed here:\n  %s" % (FUSIONCATCHER_PATH,)
    print "FusionCatcher's scripts are here:\n  %s" % (os.path.join(FUSIONCATCHER_BIN),)
    print "FusionCatcher's dependencies and tools are installed here:\n  %s" % (os.path.join(FUSIONCATCHER_TOOLS),)
    print "FusionCatcher's organism data is here:\n  %s" % (os.path.join(FUSIONCATCHER_DATA),)
    print "Run FusionCatcher as following:\n  %s" % (os.path.join(FUSIONCATCHER_BIN,'fusioncatcher'),)
    print "In order to download and build the files for FusionCatcher run the following:\n  %s" % (os.path.join(FUSIONCATCHER_PATH,FUSIONCATCHER_BIN,'fusioncatcher-build'),)
    print ""
    print "=== Installed successfully! ==="
    print ""
    if options.build:
        time.sleep(5)
        cmd([
             [["rm","-rf",os.path.join(FUSIONCATCHER_CURRENT)],False],
             [["rm","-rf",os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION)],False],
             [["ln","-s",os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION),os.path.join(FUSIONCATCHER_CURRENT)],False]
            ],
            exit=True,
            verbose = True)
        c = [os.path.join(FUSIONCATCHER_BIN,'fusioncatcher-build'),"-g",FUSIONCATCHER_ORGANISM,"-o",os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION)]
        print "  # %s" % (' '.join([el.replace(' ','\\ ') for el in c]))
        time.sleep(5)
        subprocess.call(c)
    else:
        print "*****************************************************************"
        print "*  DON'T FORGET to download (or build) the organism's data needed by FusionCatcher to run!"
        print "*****************************************************************"
        print ""
        print "Several options to get the data needed by FusionCatcher are shown below (please try them in this order)!"
        ########################################################################
        print ""
        print "---------------------------------------------------------------------------"
        print "*  OPTION 1: Download the data needed by FusionCatcher from SOURCEFORGE!"
        print "             THIS IS HIGHLY RECOMMENDED"
        print "---------------------------------------------------------------------------"
        print "In order to download the latest human data files needed by FusionCatcher, please run these (it will take hours):"
        print ""
        txt = []
        v = "ensembl_v74b"
        txt.append("rm  -rf  %s" % (FUSIONCATCHER_CURRENT.replace(" ","\\ "),))
        txt.append("rm %s.tar.gz.*" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),))
        txt.append("rm -rf %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),))
        txt.append("mkdir  -p  %s" % (FUSIONCATCHER_DATA.replace(" ","\\ "),))
        txt.append("ln  -s  %s  %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),FUSIONCATCHER_CURRENT.replace(" ","\\ ")))
        txt.append("wget --no-check-certificate https://sourceforge.net/projects/fusioncatcher/files/data/%s.tar.gz.aa -P %s" % (v,FUSIONCATCHER_DATA.replace(" ","\\ ")))
        txt.append("wget --no-check-certificate https://sourceforge.net/projects/fusioncatcher/files/data/%s.tar.gz.ab -P %s" % (v,FUSIONCATCHER_DATA.replace(" ","\\ ")))
        txt.append("wget --no-check-certificate https://sourceforge.net/projects/fusioncatcher/files/data/%s.tar.gz.ac -P %s" % (v,FUSIONCATCHER_DATA.replace(" ","\\ ")))
        txt.append("wget --no-check-certificate https://sourceforge.net/projects/fusioncatcher/files/data/%s.tar.gz.ad -P %s" % (v,FUSIONCATCHER_DATA.replace(" ","\\ ")))
        #txt.append("tar  zxvf  %s -C %s" % (v,FUSIONCATCHER_DATA.replace(" ","\\ ")))
        txt.append("cat %s.tar.gz.* | tar xz -C %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),FUSIONCATCHER_DATA.replace(" ","\\ ")))
        for t in txt:
            print t
        print ""
        f = os.path.join(FUSIONCATCHER_BIN,"download.sh")
        print "All these commands are saved in '%s' file! You may execute '%s' shell script or copy/paste all the previous commands and run them manually in the terminal!" % (f,f)
        print ""
        txt.insert(0,'#!/usr/bin/env bash')
        file(f,'w').writelines([el+'\n' for el in txt])
        os.system('chmod +rx "%s"' % (f,))
        file_download = f
        print ""
        print "---------------------------------------------------------------------------"
        print "*  OPTION 2: Download the data needed by FusionCatcher from MEGA.CO.NZ!"
        print "             TRY THIS ONLY IF OPTION 1 DID NOT WORK!"
        print "---------------------------------------------------------------------------"
        print "In order to download the latest human data files needed by FusionCatcher, please run these (it will take hours):"
        print ""
        txt = []
        v = "ensembl_v74b"
        txt.append("rm  -rf  %s" % (FUSIONCATCHER_CURRENT.replace(" ","\\ "),))
        txt.append("rm %s.tar.gz.*" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),))
        txt.append("rm -rf %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),))
        txt.append("mkdir  -p  %s" % (FUSIONCATCHER_DATA.replace(" ","\\ "),))
        txt.append("ln  -s  %s  %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),FUSIONCATCHER_CURRENT.replace(" ","\\ ")))
        txt.append("  ====>>> 1. Download manually the file '%s.tar.gz.aa' to here '%s' using your favourite Internet browser from here:" % (v,FUSIONCATCHER_DATA))
        txt.append("  ====>>>            https://mega.co.nz/#!OddwzDaT!ydwFOxRajG8vs_v-xr0yWkqaSCsNOqaT3qkY7qIraIo")
        txt.append("  ====>>> 2. Download manually the file '%s.tar.gz.ab' to here '%s' using your favourite Internet browser from here:" % (v,FUSIONCATCHER_DATA))
        txt.append("  ====>>>            https://mega.co.nz/#!qVUBwJ5Y!EW9zxm1b5XZ58TAAAqQ9X68LPf220t1ez-booR_PKtc")
        txt.append("  ====>>> 3. Download manually the file '%s.tar.gz.ac' to here '%s' using your favourite Internet browser from here:" % (v,FUSIONCATCHER_DATA))
        txt.append("  ====>>>            https://mega.co.nz/#!WAkg3DAK!pcvuX8x68PDChb9SZs7kTvwABllj3cdz5KbIGD8svu8")
        txt.append("  ====>>> 4. Download manually the file '%s.tar.gz.ad' to here '%s' using your favourite Internet browser from here:" % (v,FUSIONCATCHER_DATA))
        txt.append("  ====>>>            https://mega.co.nz/#!HJtyBCwB!ZjiURH-Ee_OgIWc7w-xT7hFhHVoY04lAXCLImJG960E")
        txt.append("cat %s.tar.gz.* | tar xz -C %s" % (os.path.join(FUSIONCATCHER_DATA,v).replace(" ","\\ "),FUSIONCATCHER_DATA.replace(" ","\\ ")))
#        print "  wget  https://dl.dropboxusercontent.com/u/3870630/%s  --no-check-certificate  &&  tar  zxvf  %s -C %s" % (v,v,FUSIONCATCHER_DATA.replace(" ","\\ "))
        for t in txt:
            print t
        #txt.insert(0,'#!/usr/bin/env bash')
        f = os.path.join(FUSIONCATCHER_BIN,"mega.sh")
        print ""
        print "All these commands are saved in '%s' file! You shall copy/paste all the previous commands (except the URLS which need to be downloaded manually) and run them manually in the terminal!" % (f,)
        print ""
        file(f,'w').writelines([el+'\n' for el in txt])
        os.system('chmod +rx "%s"' % (f,))
        ########################################################################
        print ""
        print "---------------------------------------------------------------------------"
        print "*  OPTION 3: Build yourself the data needed by FusionCatcher!"
        print "             TRY THIS ONLY IF OPTION 1 and OPTION 2 DID NOT WORK!"
        print "---------------------------------------------------------------------------"
        print "In order to build yourself the latest human data files needed by FusionCatcher, please run these (it will take hours):"
        print ""
        txt = []
        txt.append("rm  -rf  %s" % (FUSIONCATCHER_CURRENT.replace(" ","\\ "),))
        txt.append("rm  -rf  %s" % (os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION).replace(" ","\\ "),))
        txt.append("mkdir  -p  %s" % (os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION).replace(" ","\\ "),))
        txt.append("ln  -s  %s  %s" % (os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION).replace(" ","\\ "),FUSIONCATCHER_CURRENT.replace(" ","\\ ")))
        txt.append("%s  -g  homo_sapiens  -o %s" % (os.path.join(FUSIONCATCHER_BIN,'fusioncatcher-build').replace(" ","\\ "),os.path.join(FUSIONCATCHER_DATA,ENSEMBL_VERSION).replace(" ","\\ ")))
        for t in txt:
            print t
        txt.insert(0,'#!/usr/bin/env bash')
        f = os.path.join(FUSIONCATCHER_BIN,"build.sh")
        print ""
        print "All these commands are saved in '%s' file! You may execute '%s' shell script or copy/paste all the previous commands and run them manually in the terminal!" % (f,f)
        print ""
        file(f,'w').writelines([el+'\n' for el in txt])
        os.system('chmod +rx "%s"' % (f,))
        file_build = f
        ########################################################################
        print "-----------------------------------------------------------------"

        if options.download:
            r = os.system(file_download)
            if not r:
                print >>sys.stderr,"ERROR: Something wrong appeared during the execution of '%s'." % (file_download,)
                sys.exit(1)
        elif options.build:
            r = os.system(file_build)
            if not r:
                print >>sys.stderr,"ERROR: Something wrong appeared during the execution of '%s'." % (file_build,)
                sys.exit(1)
        print "--------------> THE END (everything looks good)!"
    #time.sleep(1)

####
# to add LZOP (for sort???)
# wget http://www.oberhumer.com/opensource/lzo/download/lzo-2.06.tar.gz
# tar zxvf lzo-2.06.tar.gz
# ./configure
# make
#
# wget http://www.lzop.org/download/lzop-1.03.tar.gz
# tar zxvf lzop-1.03.tar.gz
# env CPPFLAGS="-I/apps/fusioncatcher/tools/lzo/include/lzo" LDFLAGS="-L/apps/fusioncatcher/tools/lzo/src/.libs" ./configure
# make

####
# install newer version of SORT
# wget http://ftp.gnu.org/gnu/coreutils/coreutils-8.22.tar.xz
# unxz -c coreutils-8.22.tar.xz | tar xv
# ./configure
# make

####
# zlib from source for PIGZ (GZIP parallel)
# CFLAGS=-O3 -Wall -Wextra -I../zlib-1.2.5/ -L../zlib-1.2.5/ (in Makefile of pigz)
#
# wget http://zlib.net/pigz/pigz-2.3.1.tar.gz
# tar zxvf pigz-2.3.1.tar.gz
# make
#
