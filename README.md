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

