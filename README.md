# Blackwatch
## _Dev tool for file system event handling_

Blackwatch is a file system even handler built on top of python watchdog and using cleo for cli.

Currently, a basic file system event handler and command runner is implemented (`watch` command). watchdog's own cli does this better for now but blackwatch will grow into a complete (idk what) solution.

## Features

- `watch` command watches for file system events
    - Monitor file system events in a folder
    - Handle file system events by running a shell command / script when it happens
    - Options to control what to watch (files, folders or both), what events to watch for (create, modify, delete or move)
    - file/ folder exclusion and inclusion from monitoring scope (TODO)

## External dependencies

At its core, Blackwatch uses a number of open source projects to work properly:

- [Cleo](https://github.com/sdispater/cleo) - Create beautiful and testable command-line interfaces.
- [Watchdog](https://github.com/gorakhargosh/watchdog) - Python API and shell utilities to monitor file system events.

And of course Blackwatch itself is open source with a [public repository](https://github.com/nvn-nil/blackwatch) on GitHub.

## Installation
Install the dependencies.

```sh
pip install blackwatch==0.1.0
```

## Usage

Watch for `file` `create` file system events in folder `<folder_to_watch>` and run `<command_to_run>`
```sh
blackwatch watch <folder_to_watch> <command_to_run> --event create --kind files
```

## License

MIT
