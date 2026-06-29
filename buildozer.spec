[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Android parametrləri
orientation = portrait
fullscreen = 0
android.presplash_color = #FFFFFF
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
# Bu hissəni boş saxlayırıq ki, Buildozer avtomatik ən stabil versiyanı seçsin
