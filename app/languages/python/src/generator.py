"""
A simple Android project structure generator to
streamline the setting up process of your host system for Android application development from command line (without Android Studio)
"""
import os
import sys

class Generator():
    """
    Main Android Project Generator class
    """
    def __init__(self):
        self.reset_defaults()

    def set_android_Environment(self, setting_key, new_Value):
        """
        Set and overwrite Android environment settings

        :: Params
        - setting_key : Specify the setting you want to change
            + ANDROID_HOME : Set the Android SDK root directory
            + ANDROID_USER_HOME : Set the Android SDK user home directory
            + ANDROID_EMULATOR_HOME : Set the home path of the Android SDK official Emulator
            + ANDROID_AVD_HOME : Set the home path of the Android SDK Virtual Device

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["env"][setting_key] = new_Value

    def set_android_Tools(self, setting_key, new_Value):
        """
        Set and overwrite Android environment settings

        :: Params
        - setting_key : Specify the setting you want to change
            + android_Tools : Set the path of Android SDK tools
            + android_platform_Tools : Set the path of Android SDK platform tools (i.e. Operating System SDK)
            + android_cmdline_tools_Bin : Set the path containing the Android SDK cmdlinetools Binary files
            + DEPENDENCIES : Set list of all dependencies
            - project_primary_Language : Specify the primary langage of the project to use
                - Supported Languages
                    + java
                    + kotlin

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["android_tools_Info"][setting_key] = new_Value

    def set_project_structure(self, setting_key, new_Value):
        """
        Set and overwrite template project filesystem structure

        :: Params
        - setting_key : Specify the setting you want to change
            + application-source : Set a new project application source directory - Contains backend and frontend resource files
            + resources : Set a new application resources (res) directory
            + res-layout : Set a new layouts and Frontend Design (res/layouts) directory
            + res-drawables : Set a new Drawables (res/drawable) directory
            + res-mipmap : Set a new Mipmap Drawables (res/mipmap) directory
            + res-values : Set a new Value specification XML files (res/values) directory

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["project_Info"][setting_key] = new_Value

    def set_project_Settings(self, setting_key, new_Value):
        """
        Set and overwrite project configuration/settings

        :: Params
        - setting_key : Specify the setting you want to change
            + project_root_Dir : Set a new project root directory path
            + root_dir_Name : Set a new project root directory name
            + organization name : Set a new organization name
            + project_Name : Set a new project name
            + application_Name : Set a new application name
            + android_sdk_Packages : Specify list of all Android SDK package dependencies to download and install using sdkmanager
            + target_directories : Specify key-value (dictionary) mappings of names to the path of the target directories to create
            + target_files : Specify key-value (dictionary) mappings of names to the path of the target files to create

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["project_Info"][setting_key] = new_Value

    def update_Settings(self, setting_key, setting_subkey, new_Value):
        """
        Set and overwrite an existing project configuration/settings key and subkeys

        :: Params
        - setting_key : Specify the setting you want to change (Layer 1)
            + Type: String

        - setting_subkey : Specify the setting options you want to change (Layer 2)
            + Type: String

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings[setting_subkey][setting_key] = new_Value

    def reset_defaults(self):
        self.settings = {
            # Settings and Configurations
            "env" : {
                ## Environment Variables
                "ANDROID_HOME" : "/usr/lib/android-sdk",
                "ANDROID_USER_HOME" : "{}/.config/android".format(os.environ.get("HOME")),
                "ANDROID_EMULATOR_HOME" : "{}/emulator".format(self.settings["env"]["ANDROID_USER_HOME"]),
                "ANDROID_AVD_HOME" : "{}/avd".format(self.settings["env"]["ANDROID_USER_HOME"]),
            },
            "android_tools_Info" : {
                ## Custom
                "android_Tools" : "{}/tools".format(self.settings["env"]["ANDROID_HOME"]),
                "android_platform_Tools" : "{}/platform-tools".format(self.settings["env"]["ANDROID_HOME"]),
                "android_cmdline_tools_Bin" : "{}/cmdline-tools/latest/bin".format(self.settings["env"]["ANDROID_HOME"]),
                "DEPENDENCIES" : ["android-sdk", "gradle"],
                "project_primary_Language" : "java", # Specify main backend language (java | kotlin)
            },
            "project_structure" : {
                # Alias names for the project structurem folders
                "application-source" : "{}/app/src/{}".format("main", self.settings["project_Info"]["project_root_Dir"]), # Project application source directory - Contains backend and frontend resource files
                "backend" : "{}/{}/{}/{}/{}".format(
                    # Project application backend source files - i.e. Java/Kotlin
                    self.settings["project_structure"]["application-source"],
                    self.settings["android_tools_Info"]["project_primary_Language"],
                    self.settings["project_Info"]["organization_Name"],
                    self.settings["project_Info"]["project_Name"],
                    self.settings["project_Info"]["application_Name"]
                ),
                "resources" : "{}/res".format(self.settings["project_structure"]["application-source"]), # Project Resource Files
                "res-layout" : "{}/layout".format(self.settings["project_structure"]["resources"]), # Project Resources - Layouts and Frontend Design
                "res-drawables" : "{}/drawable".format(self.settings["project_structure"]["resources"]), # Project Resources - Drawable files
                "res-mipmap" : "{}/mipmap".format(self.settings["project_structure"]["resources"]), # Project Resources - Mipmap Drawables
                "res-values" : "{}/values".format(self.settings["project_structure"]["resources"]), # Project Resources - Value specification XML files
            },
            "project_Info" : {
                ## Project
                "root_dir_Name"  : "test-project",
                "organization_Name" : "com",
                "project_Name" : "example",
                "application_Name" : "test_app",
                "project_root_Dir" : "{}/{}".format(os.getcwd(), self.settings["project_Info"]["root_dir_Name"]),
                "ANDROID_SDK_COMMAND_LINE_TOOLS" : "https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip",
                "android_sdk_Packages" : [
                    # Place your Android SDK packages and components here
                    "platform-tools",
                    "cmdline-tools;latest",
                    "platforms;android-32",
                    "build-tools;31.0.0",
                    "system-images;android-31;google_apis;x86_64",
                ],
                "target_directories" : {
                    # "directory-name" : "directory-path",
                    "backend" : self.settings["project_structure"]["backend"],
                    "frontend-layout" : self.settings["project_structure"]["res-layout"],
                    "frontend-drawable" : self.settings["project_structure"]["res-drawables"],
                    "frontend-mipmap" : self.settings["project_structure"]["res-mipmap"],
                    "frontend-values" : self.settings["project_structure"]["res-values"],
                },
                "target_files" : {
                    # [file-name]="file-path"
                    "AndroidManifest.xml" : self.settings["project_structure"]["application-source"],
                    "MainActivity.java" : self.settings["project_structure"]["backend"],
                    "activity_main.xml" : self.settings["project_structure"]["res-layout"],
                    "colors.xml" : self.settings["project_structure"]["res-values"],
                    "styles.xml" : self.settings["project_structure"]["res-values"],
                    "strings.xml" : self.settings["project_structure"]["res-values"],
                },
            }
        }

    def setup_Env(self):
        """
        Setup Environment Variables
        """
        # Initialize Variables
        env_to_Write = [
            "ANDROID_HOME=\"/usr/lib/android-sdk\"",
            "ANDROID_USER_HOME=\"\$HOME/.config/android\"",
            "ANDROID_EMULATOR_HOME=\$ANDROID_USER_HOME/emulator",
            "ANDROID_AVD_HOME=\$ANDROID_USER_HOME/avd",
            "PATH+=\"\$ANDROID_HOME/emulator:\$ANDROID_HOME/tools:\$ANDROID_HOME/platform-tools:\$ANDROID_HOME/cmdline-tools/latest/bin:\"",
        ]
        config_file = "~/.bashrc"
        line = ""
        shell_Contents = []

        # Read shell resource (config) file
        with open(config_file, "r") as read_Config:
            # Go through each line

            # Read next line
            line = read_Config.readline()

            while line != "":
                # Process line
                # Append line into shell contents
                shell_Contents.append(line)

                # Read next line
                line = read_Config.readline()

            # Close file after usage
            read_Config.close()

        # Read shell resource (config) file
        with open(config_file, "a+") as append_Config:
            # Loop through all environment variables
            for env in env_to_Write:
                # Check if environment variable in shell
                print("Checking [{}] in [{}]...".format(env, config_file))
                if not (env in shell_Contents):
                    # Is not in line
                    print("[{}] not found, writing...".format(config_file))
                    # Append Environment Variables and system paths into bashrc file
                    append_Config.write(env + "\n")
                else:
                    print("[{}] found.".format(config_file))

            # Close file after usage
            append_Config.close()

def display_help():
    """
    Display help message
    """
    msg="""
{}

:: Synopsis/Syntax
python {} {global-options} [actions] {internal-options} <arguments>

:: Parameters
- Positionals
    - Actions
        - download [type] : Download the specified category/type
            - Items
                + dependencies : Download specified dependencies
        - setup : Prepare and setup user's shell for Android application development use
        - template : Generate a proper Mobile application project structure
            - Notes
                - The generated template project structure have certain sections populated by keywords that have to be edited by the user
                    + This is for user design
                + Hence, before building, please look through the project structure and edit according to your needs
        - gradle : Setup gradle files within the generated template project structure; To be used after 'template'
- Optionals
    + -h | --help : Display help message

:: Usage
""".format(application_Info["name"], application_Info["executable"])
    print(msg)

def init():
    """
    Perform global variable and class object initialization
    """
    global flags, application_Info, apg

    application_Info = {
        "name" : "APG - Android Project Generator",
        "executable" : "generator.py",
        "version" : "v0.1.0",
    }

    # Global Variables
    flags = {
        "help" : False
    }

    # Initialize Class variables
    apg = Generator()

def setup():
    """
    Perform pre-initialization and project environment setup
    """

def main():
    """
    Run Generator
    """

if __name__ == "__main__":
    init()
    setup()
    main()




dl_Dependencies()
{
    # Download Dependencies

    ## Install Android SDK packages and components
    sdkmanager "${android_sdk_Packages[@]}"
}

generate_template_Project()
{
    : "
    Generate template project structure
    "
    # Initialize Variables

    # Make project root directory
    mkdir -p "$project_root_Dir"

    # Enter project root directory
    cd "$project_root_Dir"

    echo -e ""

    # Initialize Gradle
    ## Switch through language types and initialize project using gradle based on the specified language
    case "$project_primary_Language" in
        "java")
            gradle init --type java-library
            ;;
        "kotlin")
            gradle init --type kotlin-library
            ;;
        *)
            # Invalid language
            echo -e "Invalid language specified: $project_primary_Language"
            ;;
    esac

    echo -e ""

    # Generate template project structure
    for directories_Name in "${!target_directories[@]}"; do
        # Get directory path
        directories_Path="${target_directories[$directories_Name]}"

        # Make directory
        mkdir -p "${directories_Path}" && \
            echo -e "Directory [$directories_Path/$directories_Name] created." || \
            echo -e "Error creating Directory [$directories_Path/$directories_Name]."
    done

    echo -e ""

    # Generate template project source files
    for file_Name in "${!target_files[@]}"; do
        # Get file path
        file_Path="${target_files[$file_Name]}"

        # Create file
        touch "$file_Path/$file_Name" && \
            echo -e "File [$file_Path/$file_Name] created." || \
            echo -e "Error creating File [$file_Path/$file_Name]."
    done

    echo -e ""
}

populate_template_Project()
{
    : "
    Populate project source files with contents
    "

    # Initialize Variables
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
    declare -A content_Mappings=(
        ["AndroidManifest.xml"]="$android_Manifest"
        ["MainActivity.java"]="$activity_main_Java"
        ["activity_main.xml"]="$activity_main_XML"
        ["strings.xml"]="$strings"
        ["styles.xml"]="$styles"
        ["colors.xml"]="$colors"
    )

    for target_fileName in "${!content_Mappings[@]}"; do
        # Get content message
        content_msg="${content_Mappings[$target_fileName]}"

        # Get content filepath
        target_filePath="${target_files[$target_fileName]}"

        # Compile filename and path
        target_File="$target_filePath/$target_fileName"

        # Write content to file
        echo -e "Writing to file: $target_File"
        echo -e "$content_msg" >> $target_File && \
                echo -e "Successfully populated $target_File" || \
                echo -e "Error populating $target_File"

        echo -e ""
    done
}

populate_build_Files()
{
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
    ## Top-level Gradle file
    target_fileName="build.gradle"
    target_filePath="$project_root_Dir"
    target_File="$target_filePath/$target_fileName"
    echo -e "$gradle_build_Top" > $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## Module-level Gradle file
    target_fileName="build.gradle"
    target_filePath="$project_root_Dir/app"
    target_File="$target_filePath/$target_fileName"
    echo -e "$gradle_build_Module" > $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"

    ## Gradle settings
    target_fileName="settings.gradle"
    target_filePath="$project_root_Dir"
    target_File="$target_filePath/$target_fileName"
    echo -e "$gradle_Settings" > $target_File && \
        echo -e "Successfully populated $target_File" || \
        echo -e "Error populating $target_File"
}

main()
{
    argv=("$@")
    argc="${#argv[@]}"

    # Check if arguments are provided
    if [[ "$argc" -gt 0 ]]; then
        # Arguments are provided
        # While there are still arguments
        while [[ "$1" != "" ]]; do
            # Process switch-case the argument and obtain flags
            case "$1" in
                "setup")
                    setup_Env
                    shift 1
                    ;;
                "download")
                    # Check if download type is specified
                    if [[ "$2" != "" ]]; then
                        # Get download category/type
                        category="$2"

                        case "$category" in
                            "dependencies")
                                # Download the specified
                                dl_Dependencies
                                ;;
                            *)
                                echo -e "Invalid argument specified: $category"
                                ;;
                        esac

                        # Shift to the left by 1 argument
                        shift 1
                    else
                        echo -e "No download category/type specified."
                    fi
                    shift 1
                    ;;
                "template")
                    # Check if specified project exists
                    if [[ ! -d "$project_root_Dir" ]]; then
                        # If project does not exist
                       
                        ## Generate template project structure
                        generate_template_Project 

                        ## Populate project source files
                        populate_template_Project
                    else
                        echo -e "Project [$project_root_Dir] exists."
                    fi
                    shift 1
                    ;;
                "gradle")
                    # Create gradle files
                    populate_build_Files
                    shift 1
                    ;;
                "-h" | "--help")
                    # Display Help
                    ## Set flag to true
                    # flags["help"]=true
                    display_help
                    break
                    shift 1
                    ;;
                *)
                    # Invalid Argument
                    echo -e "Invalid Argument provided [$1]"
                    shift 1
                    ;;
            esac
        done
    else
        echo -e "No arguments provided."
    fi

    # Process and execute flags and commands
    ## Flags
}

if [[ "${BASH_SOURCE[@]}" == "${0}" ]]; then
    init_default_Variables
    main "$@"
fi
