{
  'configurations': {
    'Debug': {
      'xcode_settings': {
        'GCC_OPTIMIZATION_LEVEL': '0',
        'ONLY_ACTIVE_ARCH': 'YES',
      },
    },
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'cflags': [
      '-Wall',
      '-Werror',
      '-Wno-deprecated',
      '-fvisibility=hidden',
    ],
    'cflags_cc': [
      '<@(_cflags)',
      '-std=c++1y',
      '-fexceptions',
    ],
    'xcode_settings': {
      'OTHER_CFLAGS' : [ '<@(_cflags)' ],
      'OTHER_CPLUSPLUSFLAGS' : [ '<@(_cflags_cc)' ],
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++1y',
      'CLANG_CXX_LIBRARY': 'libc++',
      'CLANG_ENABLE_OBJC_ARC': 'YES',
    },
    'conditions': [
      [ 'OS=="ios"',
        {
          'xcode_settings+' : {
            'SDKROOT': 'iphoneos',
            'SUPPORTED_PLATFORMS': 'iphonesimulator iphoneos',
          },
        }
      ],
      [ 'OS=="mac"',
        {
          'xcode_settings+' : {
            'SDKROOT': 'macosx',
          },
        }
      ],
    ],
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG' ],
        'cflags' : [ '-g', '-O0' ],
      },
      'Release': {
        'defines': [ 'RELEASE' ],
        'cflags': [
          '-Os',
          '-fomit-frame-pointer',
          '-fdata-sections',
          '-ffunction-sections',
        ],
        'xcode_settings': {
          'DEAD_CODE_STRIPPING': 'YES',
        },
      },
    },
  },
}
