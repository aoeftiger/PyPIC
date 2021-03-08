import numpy as np
from pathlib import Path
thisfolder = Path(__file__).parent.absolute()
pkg_root = thisfolder.parent.absolute()

shared_kernel_descriptions = {
    'p2m_rectmesh3d':{
        'args':(
            (np.int32, 'nparticles',),
            ('Array', 'x',),
            ('Array', 'y',),
            ('Array', 'z',),
            ('Array', 'part_weights'),
            (np.float64, 'x0',),
            (np.float64, 'y0',),
            (np.float64, 'z0',),
            (np.float64, 'dx',),
            (np.float64, 'dy',),
            (np.float64, 'dz',),
            (np.int32, 'nx',),
            (np.int32, 'ny',),
            (np.int32, 'nz',),
            ('Array', 'grid1d'),),
        'num_threads_from_arg': 'nparticles'
        }
    }



pocl_default_kernels = {
    'kernel_descriptions': shared_kernel_descriptions,
    'src_files': [
        pkg_root.joinpath('src_c/atomicadd.clh'),
        pkg_root.joinpath('src_autogenerated/linear_interpolators_pocl.clh')
        ]
    }

