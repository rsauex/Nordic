sass_depend_files = run_command(
  'find',
  meson.current_source_dir(),
  '-name', '_*.scss',
  check : true
).stdout().split()

gtk3_stylesheet = custom_target(
  'gtk.css',
  input : 'gtk.scss',
  output : 'gtk.css',
  command : [sassc, sassc_options, '@INPUT@', '@OUTPUT@'],
  build_by_default : true,
  depend_files : sass_depend_files,
  install : true,
  install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-3.0'
)

gtk3_dark_stylesheet = custom_target(
  'gtk-dark.css',
  input : 'gtk-dark.scss',
  output : 'gtk-dark.css',
  command : [sassc, sassc_options, '@INPUT@', '@OUTPUT@'],
  build_by_default : true,
  depend_files : sass_depend_files,
  install : true,
  install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-3.0'
)

install_data(
  'thumbnail.png',
  install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-3.0'
)
