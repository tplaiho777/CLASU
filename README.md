Ohessa toistaiseksi vielä suomenkielinen NURBS makro Rhinoceros 7.0 ja 8.0 ohjelmistoon. Ohjelma on siirtynyt alpha - asteelta Beta - vaiheeseen. (There will be you tube video how to use it. )

The CLASU NURBS surfacing macro tool for Rhinoceros 7.0 and 8.0 is a concise code for Class-A level NURBS surfacing. It is an easy-to-use macro tool for Rhino users to create G1, G2, and G3 level NURBS surface continuity between NURBS surfaces. The tool is currently in a beta level and functions solely as a macro tool. While there is potential for additional functionality, it is already operational, at least for developers' use. Extensive testing is required, but the code is only 50 lines long and can be used for such testing. It is too early to claim that it is a production-ready macro. The code is written in Rhino Python.

The concept involves combining the control points of the NURBS surface between the patches and creating a linear NURBS curve between these control points. This NURBS curve should then be extrapolated and linearly extended to a length required to manually determine the missing tangents between the NURBS patches. You can refer to the images, which clarify this process significantly.

This tool enables the creation of full-scale Class-A NURBS surfaces, for instance, for an entire car. The fundamental method of finding continuity in this manual manner is surprisingly simple. The tool is available for free use under the MIT license.

Ohessa suomenkielinen video aiheesta, miten CLASUa käytetään: 

https://www.youtube.com/watch?v=1M1xQi1BPlM

..and here is same with rallyenglish by Tommi P. Laiho: 

https://www.youtube.com/watch?v=nsPk34sJNSs


![CLASU IMAGE](https://github.com/tplaiho777/CLASU/assets/81896612/83521456-a774-4d5c-aef5-8a6f31ed49dd)
![testi8](https://github.com/tplaiho777/CLASU/assets/81896612/f944652b-63f1-4ae7-a2cf-b468343d6ba9)
![testi11](https://github.com/tplaiho777/CLASU/assets/81896612/f96f075d-241d-423d-8c3b-ead39ccc679b)
![testi10](https://github.com/tplaiho777/CLASU/assets/81896612/b14f9cd5-b568-4b0a-b3a1-aebfe0a5c722)
![testi9](https://github.com/tplaiho777/CLASU/assets/81896612/cbf8ded8-fde8-42e6-892d-86f6b7c6fe9f)
![Screenshot 2023-12-03 003224](https://github.com/tplaiho777/CLASU/assets/81896612/fc989c3b-49e1-4b87-9e13-571cc6a2a721)
![Screenshot 2023-12-02 225515](https://github.com/tplaiho777/CLASU/assets/81896612/b2b5fb78-ab52-49c3-8605-0958a24975ff)
![Screenshot 2023-12-02 223439](https://github.com/tplaiho777/CLASU/assets/81896612/5f68c30b-4a9d-486f-bbf8-c4a22a77490e)
![Ferrari F 40 Rhino V8](https://github.com/tplaiho777/CLASU/assets/81896612/d78f4935-c8c8-4426-81fb-baad7dcd0cd5)
