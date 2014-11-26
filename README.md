# SublimeD3R

A sublime package for common components of the D3R Framework.

Add the following repository to Sublime Package Manager to be able to install the D3RSublime plugin trivially:

`https://raw.githubusercontent.com/D3R/sublime-channel/master/packages.json`

## Installing an alternative branch

To do this you need to checkout a local version of the plugin:

* First, if you installed the plugin via Package Control, uninstall it
* In a terminal change to your Packages directory, probably <code>cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages</code> might do it on OSX
* Clone the repository with <code>git clone git@github.com:D3R/SublimeD3R.git</code>
* Change into the fresh checkout and create a tracking branch for the one you're interested in

<code>
cd SublimeD3R && git br --track thebranch origin/thebranch && git co thebranch
</code>

* Restart Sublime

You should now be running the branch version of the plugin

## Commands

* toggle_model
    - Toggle between the php and xml files for a D3R Core model
    - Default keystroke [ ctrl+d, ctrl+t ]

* create_model
    - Given a model name, this command creates the base php class and xml definition files for a new model. The module doesn't have to exist already - directories are created as appropriate.
    - Default keystroke [ ctrl+d, ctrl+m ]
