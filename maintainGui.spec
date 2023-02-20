# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['maintainGui.py'],
    pathex=[],
    binaries=[],
    datas=[('MainWindow.ui', '.'), ('dictionaryMaintain.py', '.'),
    ('default_theme.xml', '.'), ('my_theme.xml', '.'),
    ('dialogs.py', '.'), ('joukahainenDialog.ui', '.'),
    ('settingsDialog.ui', '.'), ('sizeDialog.ui', '.'),
    ('sanitizeDictionary.ui', '.'), ('settings.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='maintainGui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='maintainGui',
)
