import rhinoscriptsyntax as rs
import scriptcontext
import Rhino.Geometry as rg

def get_start_and_end_points():
    # Ask the user for the starting point
    start_point = rs.GetPoint("Select the starting point of the curve")

    # Check that the user did not cancel the operation
    if start_point is None:
        return None, None

    # Ask the user for the end point
    end_point = rs.GetPoint("Select the end point of the curve")

    # Check that the user did not cancel the operation
    if end_point is None:
        return None, None

    return start_point, end_point

def main():
    # Get the start and end points from the user
    start_point, end_point = get_start_and_end_points()

    if start_point is None or end_point is None:
        return

    desired_length = None

    # Ask the user to input the desired length as a valid number
    while desired_length is None:
        try:
            desired_length = rs.GetReal("Enter the desired length of the curve")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Create a NURBS curve based on a straight line
    curve = rg.LineCurve(end_point, start_point)

    # Calculate the original curve length
    curve_length = curve.GetLength()

    # Calculate how much length is missing to reach the desired length
    extension_length = desired_length - curve_length

    # Extend the curve by the desired length
    extended_curve = curve.Extend(rg.CurveEnd.Start, extension_length, rg.CurveExtensionStyle.Smooth)

    # Check if the curve extension was successful
    if extended_curve:
        # Save the curve GUID
        extended_curve_guid = scriptcontext.doc.Objects.AddCurve(extended_curve)

        # Update the view
        scriptcontext.doc.Views.Redraw()

        # Inform the user
        print("Curve extended successfully to the desired length")
    else:
        print("Failed to extend the curve.")

if __name__ == "__main__":
    main()
