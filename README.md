# POSGame

POSGame is a Chrome Dino Runner-like game written in Python3 tested on Win10 and designed to be rendered on POS Display

For a short demo, see: [https://twitter.com/itzikkotler/status/1290841656489472000](https://twitter.com/itzikkotler/status/1290841656489472000) played on Logic Controls Line Display LD9000

## Tested

POSGame was tested on Windows 10 (Version 1903) with Python 3.8.5 and Logic Controls Line Display LD9000 connected via USB

## Configuration

In order to communicate with the Logic Controls Line Display LD9000, the game is opening & writing to the Device Name: `//./LCLD9/`

This may not always be the case, the best way to find out is to fire up DEVMGMT.MSC (i.e., Device Manager) and see which Device Name is assigned to your display once it's plugged. If it's NOT `//./LCLD9/` then modify the `WIN_DEV` const in `posgame.py` to make sure it points to the right path 

## License
[BSD 3-Clause "New" or "Revised"](https://choosealicense.com/licenses/bsd-3-clause/)
