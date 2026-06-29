[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
# Bu hissəni dəyişdik (arm64-v8a yerinə armeabi-v7a):
android.archs = armeabi-v7a
android.accept_sdk_license = True
