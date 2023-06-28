project(
  'nordic-theme',
  version : '2.2.1',
  meson_version: '>= 0.61.0',
  license : 'GPL3',
  default_options : [
    'debug=false'
  ]
)

fs = import('fs')

prefix = get_option('prefix')

python3 = find_program('python3')
inkscape = find_program('inkscape')
sassc = find_program('sassc')

if get_option('debug')
  sassc_options = ['--line-numbers', '--style', 'nested']
else
  sassc_options = ['--style', 'compact']
endif

subdir('src')
subdir('gtk-2.0')
subdir('gtk-3.0')
subdir('gtk-4.0')
subdir('metacity-1')
subdir('kde/kvantum')
