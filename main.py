#A script that speeds up the react native environment setup.
import asyncio
import os
run = os.system

async def setup_react_native_cli():
    run('wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash')
    run('''
    echo '
    export ANDROID_HOME=$HOME/Android/Sdk
    export PATH=$PATH:$ANDROID_HOME/emulator
    export PATH=$PATH:$ANDROID_HOME/tools
    export PATH=$PATH:$ANDROID_HOME/tools/bin
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm' >> ~/.bashrc
    ''')
    run('nvm install 12')
    run('nvm use 12')
    run('npm i -g yarn react-native-cli')
    print('react-native-cli and NVM setup is done!')

async def setup_java():
    run('wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -')
    run('sudo add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/')
    run('sudo apt-get install adoptopenjdk-8-hotspot -y')
    print('Java 8 SDK setup is done!')
    run('java --version')

async def setup_android_studio():
    run('wget https://redirector.gvt1.com/edgedl/android/studio/ide-zips/4.0.1.0/android-studio-ide-193.6626763-linux.tar.gz -O android-studio4.0.1.0')
    run('tar xf android-studio4.0.1.0')
    run('bash android-studio/bin/studio.sh')
    run('yes | sdkmanager --licenses')
    print('Android Studio setup is done!')


async def main():
    await asyncio.gather(setup_java(), setup_react_native_cli(), setup_android_studio())

asyncio.run(main())
