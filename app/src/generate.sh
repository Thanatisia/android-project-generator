#!/bin/env bash 
<<EOF
A simple Android project structure generator to
streamline the setting up process of your host system for Android application development from command line (without Android Studio)
EOF

main()
{
    # Initialize Variables
    
    ## Environment Variables
    ANDROID_HOME="/usr/lib/android-sdk"
    ANDROID_USER_HOME="$HOME/.config/android"
    ANDROID_EMULATOR_HOME=$ANDROID_USER_HOME/emulator
    ANDROID_AVD_HOME=$ANDROID_USER_HOME/avd
    
    ## Custom
    android_Tools="$ANDROID_HOME/tools"
    android_platform_Tools="$ANDROID_HOME/platform-tools"
    android_cmdline_tools_Bin="$ANDROID_HOME/cmdline-tools/latest/bin"
    DEPENDENCIES=(
        "android-sdk"
        "gradle"
    )
    project_primary_Language="java" # Specify main backend language (java | kotlin)

    ## Project
    root_dir_Name="test-project"
    organization_Name="com"
    project_Name="example"
    application_Name="test_app"
    project_root_Dir="${PWD}/$root_dir_Name"

    android_sdk_Packages=(
        # Place your Android SDK packages and components here
        "platform-tools"
        "cmdline-tools;latest"
        "platforms;android-32"
        "build-tools;31.0.0"
        "system-images;android-31;google_apis;x86_64"
    )
    declare -A target_directories=(
        # [directory-name]="directory-path"
        [backend]="$project_root_Dir/$root_dir_Name/app/src/main/$project_primary_Language/$organization_Name/$project_root_Dir/$application_Name"
        [frontend]="$project_root_Dir/$root_dir_Name/app/src/main/res/{layout,drawable,mipmap,values}"
    )
    declare -A target_files=(
        # [file-name]="file-path"
        [AndroidManifest.xml]="$project_root_Dir/$root_dir_Name/app/src/main/$project_primary_Language/$organization_Name/$project_root_Dir/$application_Name"
        [MainActivity.java]="$project_root_Dir/$root_dir_Name/app/src/main/$project_primary_Language/$organization_Name/$project_root_Dir/$application_Name"
        [activity_main.xml]="$project_root_Dir/$root_dir_Name/app/src/main/res/layout"
        [colors.xml]="$project_root_Dir/$root_dir_Name/app/src/main/res/values"
        [styles.xml]="$project_root_Dir/$root_dir_Name/app/src/main/res/values"
        [strings.xml]="$project_root_Dir/$root_dir_Name/app/src/main/res/values"
    )
    ANDROID_SDK_COMMAND_LINE_TOOLS="https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip"

    # Setup Environment Variables
    # Append Environment Variables and system paths into bashrc file
    msg=$(cat <<EOF 
ANDROID_HOME="/usr/lib/android-sdk"
ANDROID_USER_HOME="$HOME/.config/android"
ANDROID_EMULATOR_HOME=$ANDROID_USER_HOME/emulator
ANDROID_AVD_HOME=$ANDROID_USER_HOME/avd
PATH+="$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:"
EOF
)
    echo -e "$msg" | tee -a $HOME/.bashrc

    # Download Dependencies

    ## Android SDK Command Line Tools
    wget $ANDROID_SDK_COMMAND_LINE_TOOLS
    unzip commandlinetools-linux-*.zip -d $ANDROID_HOME

    ## Install Android SDK packages and components
    sdkmanager "${android_sdk_Packages[@]}"

    # Make project root directory
    mkdir -p "$project_root_Dir"

    # Enter project root directory
    cd "$project_root_Dir"

    # Initialize Gradle
    gradle init --type java-library

    # Generate template project structure
    for directories_Name in "${!target_directories[@]}"; do
        # Get directory path
        directories_Path="${target_directories[$directories_Name]}"

        # Make directory
        mkdir -p "${directories_Path}" && \
            echo -e "Directory [$directories_Path/$directories_Name] created." || \
            echo -e "Error creating Directory [$directories_Path/$directories_Name]."
    done

    # Generate template project source files
    for file_Name in "${!target_files[@]}"; do
        # Get file path
        file_Path="${target_files[$file_Name]}"

        # Create file
        touch "$file_Path/$file_Name" && \
            echo -e "File [$file_Path/$file_Name] created." || \
            echo -e "Error creating File [$file_Path/$file_Name]."
    done

    # Populate project source files with contents

    ## AndroidManifest.xml
    android_Manifest="$(cat <<EOF
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="[organization-name].[project-name].[application.name]">

    <!-- Permissions -->
    <!-- Add any permissions your app requires here -->
    <!-- Example: -->
    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <!-- Activities -->
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- Other components -->
        <!-- Add other components like services, receivers, etc. if needed -->

    </application>

</manifest>
EOF
)"
    target_fileName="AndroidManifest.xml"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$android_Manifest" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## MainActivity.java
    activity_main_Java="$(cat <<EOF
package [organization-name].[project-name].[application-name];

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Your code logic goes here

        TextView textView = findViewById(R.id.textView);
        textView.setText("Hello, Android!");
    }
}
EOF
)"
    target_fileName="MainActivity.java"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$activity_main_Java" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## activity_main.xml
    activity_main_XML="$(cat <<EOF
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, Android!"
        android:textSize="24sp"
        android:layout_centerInParent="true"/>
</RelativeLayout>
EOF
)"
    target_fileName="activity_main.xml"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$activity_main_XML" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## strings.xml
    strings="$(cat <<EOF
<resources>
    <!-- App Name -->
    <string name="app_name">MyAndroidApp</string>

    <!-- Example Strings -->
    <string name="hello_text">Hello, Android!</string>
    <string name="welcome_message">Welcome to My Android App</string>

    <!-- Other Strings -->
    <!-- Add other strings used in your app here -->
</resources>
EOF
)"
    target_fileName="strings.xml"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$strings" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## styles.xml
    styles="$(cat <<EOF
<resources>

    <!-- Base application theme -->
    <style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <!-- Customize your theme here -->
        <item name="colorPrimary">@color/colorPrimary</item> <!-- Primary branding color -->
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item> <!-- Darker variant of primary color -->
        <item name="colorAccent">@color/colorAccent</item> <!-- Accent color for UI elements -->
        <!-- Other theme attributes -->

        <!-- ActionBar styles -->
        <!-- Customize ActionBar styles here -->

        <!-- App-wide text appearance -->
        <item name="android:textAppearance">@style/AppTextAppearance</item>

        <!-- Add any other customizations or overrides here -->
    </style>

    <!-- Text Appearance for the entire app -->
    <style name="AppTextAppearance" parent="TextAppearance.AppCompat">
        <!-- Customize text appearance here -->
        <item name="android:textColor">@color/textColor</item> <!-- Default text color -->
        <!-- Other text attributes -->
    </style>

</resources>
EOF
)"
    target_fileName="styles.xml"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$styles" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## colors.xml
    colors="$(cat <<EOF
<resources>
    <!-- Primary branding color -->
    <color name="colorPrimary">#3F51B5</color>

    <!-- Darker variant of primary color -->
    <color name="colorPrimaryDark">#303F9F</color>

    <!-- Accent color for UI elements -->
    <color name="colorAccent">#FF4081</color>

    <!-- Text color -->
    <color name="textColor">#000000</color>
    
    <!-- Additional colors -->
    <!-- <color name="secondaryColor">#2196F3</color> -->
    <!-- <color name="highlightColor">#FFC107</color> -->
    <!-- Add more colors as needed -->
</resources>
EOF
)"
    target_fileName="colors.xml"
    target_filePath="${target_files[$target_fileName]}"
    target_File="$target_filePath/$target_fileName"
    echo -e "$colors" >> $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    # Create gradle files

    ## Module-level Gradle file
    gradle_build_Module="$(cat <<EOF
apply plugin: '[plugin-id]'

android {
    compileSdkVersion [android-sdk-version]
    namespace = "[organization-name].[project-name].[application-name]"
    defaultConfig {
        applicationId "organization-name.project-name.application-name"
        minSdkVersion [android-minimum-sdk-version]
        targetSdkVersion [android-target-sdk-version]
        versionCode [your-codes-current-version-number]
        versionName "your-codes-current-version-name"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            // Customize your release build settings if needed
        }
    }
}

dependencies {
    implementation 'com.android.support:appcompat-v7:28.0.0'
    implementation 'com.android.support.constraint:constraint-layout:1.1.3'
    
    // Other dependencies as needed for your project
}
EOF
)"
    target_fileName="build.gradle"
    target_filePath="$project_root_Dir/$root_dir_Name/app"
    target_File="$target_filePath/$target_fileName"
    # Check if file exists
    if [[ ! -f "$target_File" ]]; then
        # File doesnt exist
        echo -e "$gradle_build_Module" >> $target_File && \
            echo -e "Successfully populated $target_File" || \
            echo -e "Error populating $target_File"
    fi

    ## Top-level gradle file
    gradle_build_Top="$(cat <<EOF
// Top-level build file where you can add configuration options common to all sub-projects/modules.

// Declare buildscript repositories
buildscript {
    repositories {
        google() // Google's Maven repository
        jcenter() // JCenter repository
        // Add any other repositories here if needed
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:[gradle-plugin-version]' // Android Gradle Plugin version
        // Add other build dependencies here if needed
    }
}

// All projects in the root project
allprojects {
    repositories {
        google() // Google's Maven repository
        jcenter() // JCenter repository
        // Add any other repositories here if needed
    }
}

// Configuration specific to the root project
task clean(type: Delete) {
    delete rootProject.buildDir
}
EOF
)"
    target_fileName="build.gradle"
    target_filePath="$project_root_Dir/$root_dir_Name"
    target_File="$target_filePath/$target_fileName"
    # Check if file exists
    if [[ ! -f "$target_File" ]]; then
        # File doesnt exist
        echo -e "$gradle_build_Top" >> $target_File && \
            echo -e "Successfully populated $target_File" || \
            echo -e "Error populating $target_File"
    fi

    ## Gradle settings
    gradle_Settings="$(cat <<EOF
// Configure the modules included in the project

// Include the app module
include ':app'

// Include other modules if present
// For example:
// include ':library_module'

// Set the root project
rootProject.name = "your-root-application-name"
EOF
)"
    target_fileName="settings.gradle"
    target_filePath="$project_root_Dir/$root_dir_Name"
    target_File="$target_filePath/$target_fileName"
    # Check if file exists
    if [[ ! -f "$target_File" ]]; then
        # File doesnt exist
        echo -e "$gradle_Settings" >> $target_File && \
            echo -e "Successfully populated $target_File" || \
            echo -e "Error populating $target_File"
    fi
}

if [[ "${BASH_SOURCE[@]}" == "${0}" ]]; then
    main "$@"
fi
