rc_files = [
  'main.rc',
  'apps' / 'chrome.rc',
  'apps' / 'gimp.rc',
  'apps' / 'libreoffice.rc',
  'apps' / 'terminal.rc',
  'apps' / 'thunar.rc',
  'apps' / 'xfce.rc'
]

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

################################################################################
#### Assets ####################################################################

assets = [
  ## Focus
  ['focus-all', 'focus'],
  ## Notebook
  ['tabframe-all', 'frame-notebook'],
  ['tabframe-normal-bottom-junct-all', 'tab-bottom-gap'],
  ['tabframe-normal-right-junct-all', 'tab-right-gap'],
  ['tabframe-normal-top-junct-all', 'tab-top-gap'],
  ['tabframe-normal-left-junct-all', 'tab-left-gap'],
  ['tab-normal-all', 'tab-top'],
  ['tab-toggled-all', 'tab-top-active'],
  ['tab-normal-all', 'tab-bottom', 'transform-rotate:180'],
  ['tab-toggled-all', 'tab-bottom-active', 'transform-rotate:180'],
  ['tab-normal-all', 'tab-right', 'transform-rotate:90'],
  ['tab-toggled-all', 'tab-right-active', 'transform-rotate:90'],
  ['tab-normal-all', 'tab-left', 'transform-rotate:270'],
  ['tab-toggled-all', 'tab-left-active', 'transform-rotate:270'],
  ## Button
  ['button-normal-all', 'button'],
  ['button-focused-all', 'button-hover'],
  ['button-pressed-all', 'button-active'],
  ['button-disabled-all', 'button-insensitive'],
  ## Entry
  ['lineedit-normal-frame', 'entry-frame-normal'],
  ['lineedit-normal', 'entry-background-normal'],
  ['lineedit-focused-frame', 'entry-frame-active'],
  ['lineedit-focused', 'entry-background-active'],
  ['lineedit-disabled-frame', 'entry-frame-insensitive'],
  ['lineedit-disabled', 'entry-background-insensitive'],
  ## Checkbox
  ['checkbox-normal', 'checkbox-unchecked'],
  ['checkbox-focused', 'checkbox-unchecked-active'],
  ['checkbox-focused', 'checkbox-unchecked-hover'],
  ['checkbox-disabled', 'checkbox-unchecked-insensitive'],
  ['checkbox-checked-normal', 'checkbox-checked'],
  ['checkbox-checked-focused', 'checkbox-checked-active'],
  ['checkbox-checked-focused', 'checkbox-checked-hover'],
  ['checkbox-checked-disabled', 'checkbox-checked-insensitive'],
  ['checkbox-tristate-normal', 'checkbox-mixed'],
  ['checkbox-tristate-focused', 'checkbox-mixed-active'],
  ['checkbox-tristate-focused', 'checkbox-mixed-hover'],
  ['checkbox-tristate-disabled', 'checkbox-mixed-insensitive'],
  ## Menu Checkbox
  ['checkbox-normal', 'menu-checkbox-unchecked', 'transform-scale:0.875'],
  ['checkbox-focused', 'menu-checkbox-unchecked-active', 'transform-scale:0.875'],
  ['checkbox-focused', 'menu-checkbox-unchecked-hover', 'transform-scale:0.875'],
  ['checkbox-disabled', 'menu-checkbox-unchecked-insensitive', 'transform-scale:0.875'],
  ['checkbox-checked-normal', 'menu-checkbox-checked', 'transform-scale:0.875'],
  ['checkbox-checked-focused', 'menu-checkbox-checked-active', 'transform-scale:0.875'],
  ['checkbox-checked-focused', 'menu-checkbox-checked-hover', 'transform-scale:0.875'],
  ['checkbox-checked-disabled', 'menu-checkbox-checked-insensitive', 'transform-scale:0.875'],
  ['checkbox-tristate-normal', 'menu-checkbox-mixed', 'transform-scale:0.875'],
  ['checkbox-tristate-focused', 'menu-checkbox-mixed-active', 'transform-scale:0.875'],
  ['checkbox-tristate-focused', 'menu-checkbox-mixed-hover', 'transform-scale:0.875'],
  ['checkbox-tristate-disabled', 'menu-checkbox-mixed-insensitive', 'transform-scale:0.875'],
  ## Radio
  ['radio-normal', 'radio-unchecked'],
  ['radio-focused', 'radio-unchecked-active'],
  ['radio-focused', 'radio-unchecked-hover'],
  ['radio-disabled', 'radio-unchecked-insensitive'],
  ['radio-checked-normal', 'radio-checked'],
  ['radio-checked-focused', 'radio-checked-active'],
  ['radio-checked-focused', 'radio-checked-hover'],
  ['radio-checked-disabled', 'radio-checked-insensitive'],
  ['radio-tristate-normal', 'radio-mixed'],
  ['radio-tristate-focused', 'radio-mixed-active'],
  ['radio-tristate-focused', 'radio-mixed-hover'],
  ['radio-tristate-disabled', 'radio-mixed-insensitive'],
  ## Menu Radio
  ['radio-normal', 'menu-radio-unchecked', 'transform-scale:0.875'],
  ['radio-focused', 'menu-radio-unchecked-active', 'transform-scale:0.875'],
  ['radio-focused', 'menu-radio-unchecked-hover', 'transform-scale:0.875'],
  ['radio-disabled', 'menu-radio-unchecked-insensitive', 'transform-scale:0.875'],
  ['radio-checked-normal', 'menu-radio-checked', 'transform-scale:0.875'],
  ['radio-checked-focused', 'menu-radio-checked-active', 'transform-scale:0.875'],
  ['radio-checked-focused', 'menu-radio-checked-hover', 'transform-scale:0.875'],
  ['radio-checked-disabled', 'menu-radio-checked-insensitive', 'transform-scale:0.875'],
  ['radio-tristate-normal', 'menu-radio-mixed', 'transform-scale:0.875'],
  ['radio-tristate-focused', 'menu-radio-mixed-active', 'transform-scale:0.875'],
  ['radio-tristate-focused', 'menu-radio-mixed-hover', 'transform-scale:0.875'],
  ['radio-tristate-disabled', 'menu-radio-mixed-insensitive', 'transform-scale:0.875'],
  ## Progressbar Pettern
  ['progress-pattern-normal-all', 'progressbar'],
  ## Progressbar
  ['progress-normal-all', 'progressbar-horz-trough'],
  ['progress-normal-all', 'progressbar-vert-trough'],
  ## Spin
  ['arrow-up-normal', 'spin-up-normal', 'transform-scale: 1.125'],
  ['arrow-up-focused', 'spin-up-hover', 'transform-scale: 1.125'],
  ['arrow-up-pressed', 'spin-up-active', 'transform-scale: 1.125'],
  ['arrow-up-disabled', 'spin-up-insensitive', 'transform-scale: 1.125'],
  ['arrow-down-normal', 'spin-down-normal', 'transform-scale: 1.125'],
  ['arrow-down-focused', 'spin-down-hover', 'transform-scale: 1.125'],
  ['arrow-down-pressed', 'spin-down-active', 'transform-scale: 1.125'],
  ['arrow-down-disabled', 'spin-down-insensitive', 'transform-scale: 1.125'],
  ## Pan
  ['arrow-up-normal',      'pan-up-normal',         'transform-scale: 1.25'],
  ['arrow-up-focused',     'pan-up-hover',          'transform-scale: 1.25'],
  ['arrow-up-pressed',     'pan-up-active',         'transform-scale: 1.25'],
  ['arrow-up-disabled',    'pan-up-insensitive',    'transform-scale: 1.25'],
  ['arrow-down-normal',    'pan-down-normal',       'transform-scale: 1.25'],
  ['arrow-down-focused',   'pan-down-hover',        'transform-scale: 1.25'],
  ['arrow-down-pressed',   'pan-down-active',       'transform-scale: 1.25'],
  ['arrow-down-disabled',  'pan-down-insensitive',  'transform-scale: 1.25'],
  ['arrow-right-normal',   'pan-right-normal',      'transform-scale: 1.25'],
  ['arrow-right-focused',  'pan-right-hover',       'transform-scale: 1.25'],
  ['arrow-right-pressed',  'pan-right-active',      'transform-scale: 1.25'],
  ['arrow-right-disabled', 'pan-right-insensitive', 'transform-scale: 1.25'],
  ['arrow-right-normal',   'pan-right-semi-normal', 'transform-rotate: 45; transform-scale: 1.25'],
  ['arrow-left-normal',    'pan-left-normal',       'transform-scale: 1.25'],
  ['arrow-left-focused',   'pan-left-hover',        'transform-scale: 1.25'],
  ['arrow-left-pressed',   'pan-left-active',       'transform-scale: 1.25'],
  ['arrow-left-disabled',  'pan-left-insensitive',  'transform-scale: 1.25'],
  ['arrow-left-normal',    'pan-left-semi-normal',  'transform-rotate: -45; transform-scale: 1.25'],
  ## Frame
  ['common-normal-all', 'frame'],
  ['common-normal-topleft', 'border'],
  ## Treeview Header
  ['header-corner-normal',  'treeview-header-corner-ltr-normal'],
  ['header-corner-normal',  'treeview-header-corner-rtl-normal', 'object-flip-horizontal'],
  ['header-corner-focused', 'treeview-header-corner-ltr-hover'],
  ['header-corner-focused', 'treeview-header-corner-rtl-hover', 'object-flip-horizontal'],
  ['header-corner-pressed', 'treeview-header-corner-ltr-active'],
  ['header-corner-pressed', 'treeview-header-corner-rtl-active', 'object-flip-horizontal'],
  ## Spin Frame LTR
  ['spinbutton-normal-frame-all', 'spin-frame-ltr-normal'],
  ['spinbutton-focused-frame-all', 'spin-frame-ltr-active'],
  ['spinbutton-disabled-frame-all', 'spin-frame-ltr-insensitive'],
  ## Spin Up LTR
  ['spinbutton-up-normal-all', 'spin-ltr-up'],
  ['spinbutton-up-focused-all', 'spin-ltr-up-hover'],
  ['spinbutton-up-pressed-all', 'spin-ltr-up-active'],
  ['spinbutton-up-disabled-all', 'spin-ltr-up-insensitive'],
  ## Spin Down LTR
  ['spinbutton-down-normal-all', 'spin-ltr-down'],
  ['spinbutton-down-focused-all', 'spin-ltr-down-hover'],
  ['spinbutton-down-pressed-all', 'spin-ltr-down-active'],
  ['spinbutton-down-disabled-all', 'spin-ltr-down-insensitive'],
  ## Spin Frame RTL
  ['spinbutton-normal-frame-all', 'spin-frame-rtl-normal', 'object-flip-horizontal'],
  ['spinbutton-focused-frame-all', 'spin-frame-rtl-active', 'object-flip-horizontal'],
  ['spinbutton-disabled-frame-all', 'spin-frame-rtl-insensitive', 'object-flip-horizontal'],
  ## Spin Up RTL
  ['spinbutton-up-normal-all', 'spin-rtl-up', 'object-flip-horizontal'],
  ['spinbutton-up-focused-all', 'spin-rtl-up-hover', 'object-flip-horizontal'],
  ['spinbutton-up-pressed-all', 'spin-rtl-up-active', 'object-flip-horizontal'],
  ['spinbutton-up-disabled-all', 'spin-rtl-up-insensitive', 'object-flip-horizontal'],
  ## Spin Down RTL
  ['spinbutton-down-normal-all', 'spin-rtl-down', 'object-flip-horizontal'],
  ['spinbutton-down-focused-all', 'spin-rtl-down-hover', 'object-flip-horizontal'],
  ['spinbutton-down-pressed-all', 'spin-rtl-down-active', 'object-flip-horizontal'],
  ['spinbutton-down-disabled-all', 'spin-rtl-down-insensitive', 'object-flip-horizontal'],
  ## Slider Horizontal
  ['slider-normal-all', 'scale-horz-trough', 'transform-rotate:90'],
  ['slider-toggled-all', 'scale-horz-trough-active', 'transform-rotate:90'],
  ## Slider Vertical
  ['slider-normal-all', 'scale-vert-trough'],
  ['slider-toggled-all', 'scale-vert-trough-active'],
  ## Slider Cursor
  ['slidercursor-normal-all', 'scale-slider'],
  ['slidercursor-focused-all', 'scale-slider-hover'],
  ['slidercursor-pressed-all', 'scale-slider-active'],
  ['slidercursor-disabled-all', 'scale-slider-insensitive'],
  ## Scrollbar Slider Vectical
  ['scrollbarslider-normal-all', 'scrollbar-vert-slider'],
  ['scrollbarslider-focused-all', 'scrollbar-vert-slider-hover'],
  ['scrollbarslider-pressed-all', 'scrollbar-vert-slider-active'],
  ## Scrollbar Slider Vectical
  ['scrollbarslider-normal-all', 'scrollbar-horz-slider', 'transform-rotate:90'],
  ['scrollbarslider-focused-all', 'scrollbar-horz-slider-hover', 'transform-rotate:90'],
  ['scrollbarslider-pressed-all', 'scrollbar-horz-slider-active', 'transform-rotate:90'],
  ## Splitter
  ['splitter-grip-normal', 'handle-vert'],
  ['splitter-grip-normal', 'handle-horz', 'transform-rotate:90'],
  ## Menubar
  ['menubar-normal-all', 'menubar'],
  ## Menubar Item
  ['menubaritem-pressed-all', 'menubar-item-active'],
  ## Menu
  # ['menu-normal-all', 'menu'],
  ## Line
  ['line', 'line'],
  ## Handle
  ['handle', 'handle'],
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
    install_dir : prefix / 'share' / 'themes' / 'Nordic-Darker' / 'gtk-2.0' / 'assets'
  )
endforeach
