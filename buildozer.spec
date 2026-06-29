[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Bura əlavə etdiyin tələblərdir:
requirements = python3,kivy,openssl,sqlite3

orientation = portrait
android.archs = armeabi-v7a
android.accept_sdk_license = True
android.ndk = 25b
android.ndk_api = 24
android.api = 33
