import SCons.Scanner.IDL
from SCons.Script import *

def idl2many_emitter(target, source, env):
    newTarget = []
    src = source[0]
    dst = target[0]
    if str(src).endswith('.fbs'):
        for suffix in ['.h']:
            newTarget.append(str(dst) + '_generated' + suffix)
    return (newTarget, source)

def addSlice2cppBuilder(env):
    env['BUILDERS']['Slice2cpp'] = Builder(
        action="slice2cpp -I${SLICE_INCLUDES} -I. ${SLICEFLAGS} --output-dir ${TARGET.dir} ${SOURCE}",
        src_suffix = '.ice',
        emitter = idl2many_emitter,
        source_scanner = SCons.Scanner.IDL.IDLScan(),
        single_source = 1
    )

def MyInstallBld(env, target, source):
    if 'DO_PACKAGE' in env:
        return env.Install(target, source)
    return []

def addMyInstallBuilder(env):
    env['BUILDERS']['MyInstall'] = MyInstallBld
