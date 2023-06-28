assets = run_command(
  'cat',
  meson.current_source_dir() / 'assets.txt',
  check : true
).stdout().strip().split('\n')

rc_files = [
  'main.rc',
  'apps' / 'chrome.rc',
  'apps' / 'gimp.rc',
  'apps' / 'libreoffice.rc',
  'apps' / 'terminal.rc',
  'apps' / 'thunar.rc',
  'apps' / 'xfce.rc'
]

asset_targets = []

foreach asset : assets
  asset_targets += custom_target(
    asset + '.png',
    input : meson.current_source_dir() / 'assets.svg',
    output : asset + '.png',
    command : [inkscape,
               '--export-id=' + asset,
               '--export-id-only',
               '--export-background-opacity=0',
               '--export-filename=@OUTPUT@',
               '@INPUT@'],
    build_by_default : true,
    install : true,
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0' / 'assets'
  )
endforeach

foreach element : ['checkbox', 'radio']
  foreach state : ['unchecked', 'checked', 'mixed']
    install_symlink(
      element + '-' + state + '.png',
      install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0' / 'assets',
      pointing_to : '..' / '..' / 'assets' / (element + '-' + state + '-dark.png')
    )
    foreach substate : ['active', 'hover', 'insensitive']
      install_symlink(
        element + '-' + state + '-' + substate + '.png',
        install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0' / 'assets',
        pointing_to : '..' / '..' / 'assets' / (element + '-' + state + '-' + substate + '-dark.png')
      )
    endforeach
  endforeach
endforeach

install_data(
  'gtkrc',
  install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0'
)

foreach rc_file : rc_files
  install_data(
    meson.current_source_dir() / rc_file,
    install_dir : fs.parent(prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0' / rc_file)
  )
endforeach
