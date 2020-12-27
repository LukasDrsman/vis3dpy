# vis3dpy
![preview image](https://github.com/LukasDrsman/vis3dpy/blob/main/assets/coil.png)

## Installation
#### Requirements:
 * python3 with pip

#### Install:
```sh
pip install vis3dpy
```

## Usage
### *class* *vis3d.plot.* Figure *(window width, window height, grid color, mode)*
 * ***window width*** - x size of the window in pixels
 * ***window height*** - y size of the window in pixels
 * ***grid color*** - color of the generated grid (for now just the cube)
 * ***mode*** (*default* : 0) - 0 for orthographic, 1 for perspective

| method | parameters | description |
|--------|------------|-------------|
| scatter | points, color  | creates a scatter plot |
| plot | points, color | creates a line plot |
| show | none | displays plots |

## To Do
 - [x] upload to pypi
 - [ ] clean the code
 - [ ] fix UI control bugs
 - [ ] add grid
 - [ ] add axis labels
