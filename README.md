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
### Basics
#### *class* *vis3d.plot.* Figure *(window width, window height, grid color, mode)*
 * ***window width*** - x size of the window in pixels
 * ***window height*** - y size of the window in pixels
 * ***grid color*** - color of the generated grid (for now just the cube)
 * ***mode*** (*default* : 0) - 0 for orthographic, 1 for perspective

| method | parameters | description |
|--------|------------|-------------|
| scatter | points, color  | creates a scatter plot |
| plot | points, color | creates a line plot |
| show | none | displays plots |

| parameter | structure | description |
|-----------|--------------------|-------------|
| points    | `[[ x0, y0, z0 ], ..., [ xn, yn, zn ]]` | n-list of 3-lists |
| color     | `( r, g, b )` : `(0-255, 0-255, 0-255)` | RGB colors 3-tuple |

### Creating your own drawable class
A drawable class requires 2 methods:
#### norm *(ndata)*
This method is responsible for centering the object. In case this isn't desired, it's body can be left "empty". It takes 1 parameter, ndata:
 * ***ndata*** - in the form `(-cx, -cy, -cz)`, created from *cpd* of all objects

#### render *()*
This method is responsible for the actual openGL rendering. It takes no parameters.
****
A drawable class also needs a *cpd* and *opd* member variables:
 * ***opd*** - in  the form `[[ x0, y0, z0 ], ..., [ xn, yn, zn ]]`; Original Plotting Data; this is used for "grid" creation and for *ndata* calculation. Can be left as empty list.
 * ***cpd*** -n the form `[[ x0, y0, z0 ], ..., [ xn, yn, zn ]]`; Current Plotting Data; this is used for camera initialization and is the list of "centered" points that actually get drawn in the module's classes. Can be initialized with "anchors" for sake of the camera initialization or be left empty when a module's plotting function's used too.
****
To draw the object, consider this example:
```py
...

figure = Figure(1920, 1080, (0, 0, 0))  # initialize figure
obj = Foo(...)                          # initialize the objec to be drawn
figure.plots(obj)                       # append object to figure's list of plots

...
```
## To Do
 - [x] upload to pypi
 - [ ] clean the code
 - [ ] fix UI control bugs
 - [ ] add grid
 - [ ] add axis labels
 - [ ] fix the aspect ratio problem
