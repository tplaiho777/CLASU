Ohessa toistaiseksi vielä suomenkielinen NURBS makro Rhinoceros 7.0 ja 8.0 ohjelmistoon. 

The CLASU NURBS surfacing macro tool for Rhinoceros 7.0 and 8.0 is a concise code for Class-A level NURBS surfacing. It is an easy-to-use macro tool for Rhino users to identify G1, G2, and G3 level NURBS surface continuity between NURBS surfaces. The tool is currently in an alpha level and functions solely as a macro tool. While there is potential for additional functionality, it is already operational, at least for developers' use. Extensive testing is required, but the code is only 50 lines long and can be used for such testing. It is too early to claim that it is a production-ready macro. The code is written in Rhino Python.

The concept involves combining the control points of the NURBS surface between the patches and creating a linear NURBS curve between these control points. This NURBS curve should then be extrapolated and linearly extended to a length required to manually determine the missing tangents between the NURBS patches. You can refer to the images, which clarify this process significantly.

This tool enables the creation of full-scale Class-A NURBS surfaces, for instance, for an entire car. The fundamental method of finding continuity in this manual manner is surprisingly simple. The tool is available for free use under the MIT license.

# CLASU
# A class - A  NURBS surfacing tools for Rhinoceros 7.0 and 8.0

import rhinoscriptsyntax as rs
import scriptcontext
import Rhino.Geometry as rg

# Kysy kayttajalta aloituspiste
start_point = rs.GetPoint("Valitse kayran aloituspiste")

# Tarkista, etta kayttaja ei perunut toimintoa
if start_point is None:
    exit()

# Kysy kayttajalta loppupiste
end_point = rs.GetPoint("Valitse kayran loppupiste")

# Tarkista, etta kayttaja ei perunut toimintoa
if end_point is None:
    exit()

# Kysy kayttajalta haluttu pituus
desired_length = rs.GetReal("Syota haluttu kayran pituus")

# Luo NURBS-kayra suoran pohjalta
curve = rg.LineCurve(start_point, end_point)

# Laske alkuperaisen kayran pituus
curve_length = curve.GetLength()

# Laske, kuinka paljon pituutta puuttuu halutusta pituudesta
extension_length = desired_length - curve_length

# Jatka kayra halutulla pituudella
extended_curve = curve.Extend(rg.CurveEnd.Start, extension_length, rg.CurveExtensionStyle.Smooth)

# Tarkista, onnistuiko kayran jatkaminen
if extended_curve:
    # Tallenna kayra GUID
    extended_curve_guid = scriptcontext.doc.Objects.AddCurve(extended_curve)

    # Paivita nakyma
    scriptcontext.doc.Views.Redraw()

    # Ilmoita kayttajalle
    print("Kayra jatkettu halutulla pituudella onnistuneesti")
else:
    print("Kayran jatkaminen epaonnistui.")

