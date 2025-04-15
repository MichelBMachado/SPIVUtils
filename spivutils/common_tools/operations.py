#-----------------------------------------------------------------------------------
# CODE DETAILS
#-----------------------------------------------------------------------------------
# Author: Michel Bernardino Machado 
# Date:
# version:

#-----------------------------------------------------------------------------------
# REQUIRED PACKAGES
#-----------------------------------------------------------------------------------
from numpy import sqrt, where, floor

#-----------------------------------------------------------------------------------
# CODE ROUTINES
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def normalization(input_data):
    """
    Normalize the images symply dividing the array by 255
    """
    output_data = input_data/255

    return output_data

#-----------------------------------------------------------------------------------
def thresholding(input_data):
    """
    
    """
    output_data = where(input_data > 127, 255, 0)

    return output_data

#-----------------------------------------------------------------------------------
def vectoraddition(input_data):
    """
    Determines the magnitude of the velocity field using its u and v components
    """
    u_comp = input_data[:, 0]
    v_comp = input_data[:, 1]
    output_data = sqrt(u_comp ** 2 + v_comp ** 2)

    return output_data

#-----------------------------------------------------------------------------------
def imagecropping(input_data):

    Height = input_data.shape[2]
    Width = input_data.shape[3]
    
    if Height == Width:
        return
    
    elif Height < Width:
        x_i = int(floor((Width - Height)/2) - 1)
        x_f = int(x_i + Height)
        output_data = input_data[:, :, :, x_i:x_f]
        return output_data
    
    else:
        y_i = int(floor((Height - Width)/2) - 1)
        y_f = int(y_i + Width)
        output_data = input_data[:, :, y_i:y_f, :]
        return output_data