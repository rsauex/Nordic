gtk_assets = run_command(
  python3,
  meson.current_source_dir() / 'list-assets.py',
  meson.current_source_dir() / 'wm' / 'wm-assets.svg',
  check : true
).stdout().strip().split('\n')

gtk_asset_targets = []
gtk_asset_hidpi_targets = []

foreach asset : gtk_assets
  asset_parts = asset.split()
  input_file  = asset_parts[0]
  asset_id    = asset_parts[1]
  asset_name  = asset_parts[2]

  gtk_asset_targets += custom_target(
    'gtk-asset-' + asset_name + '.png',
    input : input_file,
    output : asset_name + '.png',
    command : [inkscape,
               '--export-id=' + asset_id,
               '--export-filename=@OUTPUT@',
               '@INPUT@'],
    build_by_default : true,
    install : true,
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'assets'
  )

  gtk_asset_hidpi_targets += custom_target(
    'gtk-asset-' + asset_name + '@2.png',
    input : input_file,
    output : asset_name + '@2.png',
    command : [inkscape,
               '--export-dpi=180',
               '--export-id=' + asset_id,
               '--export-filename=@OUTPUT@',
               '@INPUT@'],
    build_by_default : true,
    install : true,
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'assets'
  )
endforeach
