#!/bin/env bash
export ANDROID_HOME=/path/to/android-sdk
export ANDROID_USER_HOME=/path/to/user/home/.config/android
export ANDROID_EMULATOR_HOME="$ANDROID_USER_HOME/emulator"
export ANDROID_AVD_HOME="$ANDROID_USER_HOME/avd"
export PATH+="$ANDROID_EMULATOR_HOME:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:"

