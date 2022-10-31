# WarpLinuxConnector

a GUI app base on [warp](https://developers.cloudflare.com/warp-client/get-started/linux) on Windows for linux users

## Installation

Read [warp-cli install doc](https://developers.cloudflare.com/warp-client/get-started/linux). install `warp-cli` and
register with `$ warp-cli register`.

and then:

    $ git clone https://github.com/0xb4dc0d3x/WarpLinuxConnector
    $ cd WarpLinuxConnector
    $ python3 install.py
    $ sudo chmod +x ~/.local/share/applications/WARP-Linux.desktop

now search for `WARP-Linux` app in your desktop menu.

> ⚠️ IMPORTANT: After the installation please make sure you do not remove the repository dir. It is required for the desktop shortcut to work.

## Hide Mode
If you only want to use the tray icon, you can run the program in hide mode
    
    $ python .../main.py --hide

## Uninstall

Just remove `~/.local/share/applications/warp-gui.desktop` file.

## Screenshot

![warp cloudflare gui](icons/ss.png)
