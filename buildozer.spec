[app]
title = Змейка
package.name = snakegame
package.domain = com.yourcompany
version = 1.0.0
requirements = python3,kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
android.permissions = INTERNET
android.api = 35
android.minapi = 21
android.sdk = 35
android.ndk = 25b
android.release_artifact = aab
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1