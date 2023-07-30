assets = [
  ## Checkbox Unchecked
  ['checkbox-normal',   'checkbox-unchecked'],
  ['checkbox-normal',   'checkbox-unchecked-dark'],
  ['checkbox-focused',  'checkbox-unchecked-hover'],
  ['checkbox-focused',  'checkbox-unchecked-hover-dark'],
  ['checkbox-focused',  'checkbox-unchecked-active'],
  ['checkbox-focused',  'checkbox-unchecked-active-dark'],
  ['checkbox-disabled', 'checkbox-unchecked-insensitive'],
  ['checkbox-disabled', 'checkbox-unchecked-insensitive-dark'],
  ['checkbox-focused',  'selected-checkbox-unchecked'],
  ['checkbox-focused',  'selected-checkbox-unchecked-dark'],
  ## Checkbox Checked
  ['checkbox-checked-normal',   'checkbox-checked'],
  ['checkbox-checked-normal',   'checkbox-checked-dark'],
  ['checkbox-checked-focused',  'checkbox-checked-hover'],
  ['checkbox-checked-focused',  'checkbox-checked-hover-dark'],
  ['checkbox-checked-focused',  'checkbox-checked-active'],
  ['checkbox-checked-focused',  'checkbox-checked-active-dark'],
  ['checkbox-checked-disabled', 'checkbox-checked-insensitive'],
  ['checkbox-checked-disabled', 'checkbox-checked-insensitive-dark'],
  ['checkbox-checked-focused',  'selected-checkbox-checked'],
  ['checkbox-checked-focused',  'selected-checkbox-checked-dark'],
  ## Checkbox Mixed
  ['checkbox-tristate-normal',   'checkbox-mixed'],
  ['checkbox-tristate-normal',   'checkbox-mixed-dark'],
  ['checkbox-tristate-focused',  'checkbox-mixed-hover'],
  ['checkbox-tristate-focused',  'checkbox-mixed-hover-dark'],
  ['checkbox-tristate-focused',  'checkbox-mixed-active'],
  ['checkbox-tristate-focused',  'checkbox-mixed-active-dark'],
  ['checkbox-tristate-disabled', 'checkbox-mixed-insensitive'],
  ['checkbox-tristate-disabled', 'checkbox-mixed-insensitive-dark'],
  ['checkbox-tristate-focused',  'selected-checkbox-mixed'],
  ['checkbox-tristate-focused',  'selected-checkbox-mixed-dark'],
  ## Radio Unchecked
  ['radio-normal',   'radio-unchecked'],
  ['radio-normal',   'radio-unchecked-dark'],
  ['radio-focused',  'radio-unchecked-hover'],
  ['radio-focused',  'radio-unchecked-hover-dark'],
  ['radio-focused',  'radio-unchecked-active'],
  ['radio-focused',  'radio-unchecked-active-dark'],
  ['radio-disabled', 'radio-unchecked-insensitive'],
  ['radio-disabled', 'radio-unchecked-insensitive-dark'],
  ['radio-focused',  'selected-radio-unchecked'],
  ['radio-focused',  'selected-radio-unchecked-dark'],
  ## Radio Checked
  ['radio-checked-normal',   'radio-checked'],
  ['radio-checked-normal',   'radio-checked-dark'],
  ['radio-checked-focused',  'radio-checked-hover'],
  ['radio-checked-focused',  'radio-checked-hover-dark'],
  ['radio-checked-focused',  'radio-checked-active'],
  ['radio-checked-focused',  'radio-checked-active-dark'],
  ['radio-checked-disabled', 'radio-checked-insensitive'],
  ['radio-checked-disabled', 'radio-checked-insensitive-dark'],
  ['radio-checked-focused',  'selected-radio-checked'],
  ['radio-checked-focused',  'selected-radio-checked-dark'],
  ## Radio Mixed
  ['radio-tristate-normal',   'radio-mixed'],
  ['radio-tristate-normal',   'radio-mixed-dark'],
  ['radio-tristate-focused',  'radio-mixed-hover'],
  ['radio-tristate-focused',  'radio-mixed-hover-dark'],
  ['radio-tristate-focused',  'radio-mixed-active'],
  ['radio-tristate-focused',  'radio-mixed-active-dark'],
  ['radio-tristate-disabled', 'radio-mixed-insensitive'],
  ['radio-tristate-disabled', 'radio-mixed-insensitive-dark'],
  ['radio-tristate-focused',  'selected-radio-mixed'],
  ['radio-tristate-focused',  'selected-radio-mixed-dark'],
]

foreach asset : assets
  input_file    = assets_svg
  asset_id      = asset[0]
  asset_name    = asset[1]
  asset_actions = asset.length() > 2 ? ';' + asset[2] : ''

  gtk_asset_targets += custom_target(
    'test-asset-' + asset_name + '.png',
    input : input_file,
    output : asset_name + '.png',
    command : [inkscape,
               '--actions=select-by-id:' + asset_id + asset_actions,
               '--export-id=' + asset_id,
               '--export-id-only',
               '--export-background-opacity=0',
               '--export-dpi=96',
               '--export-filename=@OUTPUT@',
               '@INPUT@'],
    build_by_default : true,
    install : true,
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'assets'
  )

  gtk_asset_targets += custom_target(
    'test-asset-' + asset_name + '@2.png',
    input : input_file,
    output : asset_name + '@2.png',
    command : [inkscape,
               '--actions=select-by-id:' + asset_id + asset_actions,
               '--export-id=' + asset_id,
               '--export-id-only',
               '--export-background-opacity=0',
               '--export-dpi=192',
               '--export-filename=@OUTPUT@',
               '@INPUT@'],
    build_by_default : true,
    install : true,
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'assets'
  )
endforeach
