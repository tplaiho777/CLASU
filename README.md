Ohessa toistaiseksi vielä suomenkielinen NURBS makro Rhinoceros 7.0 ja 8.0 ohjelmistoon. Ohjelma on siirtynyt alpha - asteelta Beta - vaiheeseen. 

The CLASU NURBS surfacing macro tool for Rhinoceros 7.0 and 8.0 is a concise code for Class-A level NURBS surfacing. It is an easy-to-use macro tool for Rhino users to create G1, G2, and G3 level NURBS surface continuity between NURBS surfaces. The tool is currently in a beta level and functions solely as a macro tool. While there is potential for additional functionality, it is already operational, at least for developers' use. Extensive testing is required, but the code is only 50 lines long and can be used for such testing. It is too early to claim that it is a production-ready macro. The code is written in Rhino Python.

The concept involves combining the control points of the NURBS surface between the patches and creating a linear NURBS curve between these control points. This NURBS curve should then be extrapolated and linearly extended to a length required to manually determine the missing tangents between the NURBS patches. You can refer to the images, which clarify this process significantly.

This tool enables the creation of full-scale Class-A NURBS surfaces, for instance, for an entire car. The fundamental method of finding continuity in this manual manner is surprisingly simple. The tool is available for free use under the MIT license.



![CLASU IMAGE](https://github.com/tplaiho777/CLASU/assets/81896612/83521456-a774-4d5c-aef5-8a6f31ed49dd)
