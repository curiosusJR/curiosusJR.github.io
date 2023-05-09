---
title: ZMK keyboard firmware usage
tags:
  - zmk
  - keyboard
categories:
  - blogs
date: 09-05-2023
---
I have purchased an open source split keyboard with zmk firmware. Unlike those using qmk, the keymaps of this one cannot be changed simply and directly using via/vial software, it have to build firmware myself. I do not have t experience with this and after my first successful attempt, I decided to document it here.

# Normal usage
1. This keyboard can be connected to PC in two ways. USB connection or Blue-tooth connection.
2. If you want to connect to PC with cables, just connect the left hand keyboard to PC with USB C cable. 
3. If you want to connect device with Blue-tooth, press layer 2 button (which is on the bottom of right hand) and click number 1 to 5 (which means you can connect 5 different device with blue tooth), and then your device can found the keyboard by blue tooth name 'Sofle'.
4. If the blue tooth connect failed, try clearing the blue tooth message in both keyboard and your PC. Delete the 'Sofle' device in PC blue tooth setting and press `layer 2 + ESC` on the keyboard. The location of `ESC` in layer 2 is `BT_CLR` button.
5. The location of 'TAB' in layer 3 is the power button, which means you can turn on/off with pressing `layer 1 + layer 2 + tab` at the same time.

# Check and set the keymap in Github
1. Fork this repo (<https://github.com/curiosusJR/YoungMan_DIY_SOFLE_CFG>) to your own github.
2. Open <https://nickcoutsos.github.io/keymap-editor/> with web-browser.
3. Select the source in Github and login your account. Select the repo you just forked only, not all the repo you have, for the keymap-editor.
4. It will be shown my keymap setting in the website.
5. Change the setting as you will.
6. Select the layer first, then select the key you want to change. Click the `&kp` can change the group of keys. Different groups shows different keys. The normal keyboard press group is `&kp`. You can select any key you want at any location. The knob can be click or rotation. The rotation function setting is on the bottom of keyboards.
	**Tips**: The layer 0 is the default and the main layer you will use. Use `&mo` for changing layer during pressing the button, use `&lt` for short tapping in normal type and pressing in layer changing type or use `&to` for turning into new layer when tap the button.
7. After finishing the setting, click `Save changes` button on the top of website and commit your changing to your repo.
8. Check the commit exists.

# Build the firmware file in Github
1. Click `Actions` on your own Github repo.
2. Enable the actions and run the 'Build' workflow.Wait for a second till it's done.
3. When it shows a green check mark, click the 'Build' and download the firmware file at the bottom.
4. Unzip it and delete the `setting_reset-nrfmicro_13-zmk.uf2` file. Keep the right hand and the left hand firmware file for use.

# Reset the firmware in the keyboard

1. First, connect keyboard to PC with USB C cable. The right hand keyboard and the left one should be reset separately, so connect the right one first. 
2. Press the reset button (the small white one under the screen) twice quickly and the computer will recognize a flash drive which is the keyboard itself.
3. There should be three files in the flash drive just detected. Copy [this file](settings_reset-nrfmicro_13-zmk.uf2) into the root directory of that flash drive. Now there are four files in it.
4. Eject that flash drive.
5. Unplug the USB cable and reconnect it. Repeat step 2 and check the drive. There should be still **three** files in it.
6. Copy the right hand `.uf2` file into the right hand keyboard and eject the drive.
7. Up to now, the firmware of right hand has been update completed. Do it same to the left one. Just remember that copy [this file](settings_reset-nrfmicro_13-zmk.uf2), not the file downloaded from github, to **both left and right** hand keyboard before copying the `solfe_*.uf2` file.
8. After updating the firmware of both left and right hands, press `BT_CLR` button you set to clear the blue-tooth message. 
9. Press the reset button of both right and left hand keyboard in the same time. 
10. Check the connection between two hands and connection to PC. Enjoy your new keymaps! 😄
