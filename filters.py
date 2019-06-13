from Cimpl import *
import random

def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x, y, (r, g, b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = (range(x-10,x+11),range(y-10,y+11)
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
                rand1 = (-5-15)
                rand2 = (-5,15) 
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = x+rand1
            random_row = y + rand2  
            
            # Determine if the random coordinates are in bounds.

            if ({random_column,random_row})>issubset(row_and_column_are_in_bounds)==True:
                row_and_column_are_in_bounds = a
                    
        # Get the color of the randomly-selected pixel.
        
        new_col = get_color(image,random_column,random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x,y,new_col)
                    
    # Return the scattered image.
    ______
def greyscale(image):
    new_image = copy(image)


    for x, y, (r, g, b) in image:
        brightness= (r + g+ b) //3
        grey = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, grey)
      
        show(new_image)
   
def weighted_greyscale(image):
    new_image = copy(image)


    for x, y, (r, g, b) in image:
        brightness= (r * 0.299 + g * 0.587 + b * 0.114) //3
        grey = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, grey)
      
        show(new_image)
   
def extreme_contrast(image):
    new_image = copy(image)


    for x, y, (r, g, b) in image:
        brightness= (r + g+ b) //3
        low_contrast= create_color(0 , 0 , 0 )
        high_contrast= create_color(255, 255, 255)
        if brightness<128:
            set_color(new_image, x, y, low_contrast)
        else:
            set_color(new_image, x, y, high_contrast)
      
            show(new_image)

def sepia_tint(image):
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r * 0.299) + (g * 0.587) + (b * 0.114)
        dark_grey = create_color(brightness*1.1, brightness, brightness*0.9)
        medium_grey = create_color(brightness*1.15, brightness, brightness*0.85)
        light_grey = create_color(brightness*1.08, brightness, brightness*0.93)
        if brightness<63:
            set_color(new_image, x, y, dark_grey)
        elif brightness<192:
            set_color(new_image, x, y, medium_grey)
        else:
            set_color(new_image, x, y, light_grey)
        
            show(new_image)
   
def _adjust_component(amount):
    if amount<64:
        return 31
    elif amount<128:
        return 95
    elif amount<192:
        return 159
    else:
        return 223
   
def posterize(image):
    new_image = copy(image)
    for x,y, (r, g, b) in image:
        new_r=_adjust_component(r)
        new_g=_adjust_component(g)
        new_b=_adjust_component(b)
        new_color = create_color(new_r, new_g, new_b)
        set_color(new_image, x, y, new_color)
        show(new_image)
def detect_edges(image, threshold): 
    """ (Cimpl.Image, float) -> Cimpl.Image 
    Return a new image that contains a copy of the original image 
    that has been modified using edge detection. 

    >>> image = load_image(choose_file()) 
    >>> filtered = detect_edges(image, 10.0) 
    >>> show(filtered) 
    """ 

    target = copy(image) 

    for y in range(1, get_height(image) - 1): 
        for x in range(1, get_width(image) - 1): 

            top_red, top_green, top_blue = get_color(image, x, y) 
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1) 

            if (top_red + top_green + top_blue)/3 - ( bottom_red + bottom_green + bottom_blue)/3 >10: 
                col = create_color(0,0,0) 
            set_color(image,x,y,col) 

        elif (top_red + top_green + top_blue)/3 - ( bottom_red + bottom_green + bottom_blue)/3 <10: 
            col = create_color(255,255,255) 
            set_color(image,x,y,col) 
            show(target) 


def detect_edges_better(image, threshold): 
    """ (Cimpl.Image, float) -> Cimpl.Image 
   
   Return a new image that contains a copy of the original image 
   that has been modified using edge detection. 

   >>> image = load_image(choose_file()) 
   >>> filtered = detect_edges_better(image, 10.0) 
   >>> show(filtered) 
   """ 

    target = copy(image) 

    for y in range(1, get_height(image) - 1): 
        for x in range(1, get_width(image) - 1): 

            top_red, top_green, top_blue = get_color(image, x, y) 
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1) 
            right_red, right_green, right_blue = get_color(image, x + 1, y) 


            if (top_red + top_green + top_blue)/3 - ( bottom_red + bottom_green + bottom_blue)/3 >10: 
                col = create_color(0,0,0) 
            set_color(image,x,y,col) 

        elif (top_red + top_green + top_blue)/3 - ( bottom_red + bottom_green + bottom_blue)/3 <10: 
            col = create_color(255,255,255) 
            set_color(image,x,y,col) 
            show(target) 


def blur(image): 
    """ (Cimpl.Image) -> Cimpl.Image 

   Return a new image that is a blurred copy of image. 

   original = load_image(choose_file()) 
   blurred = blur(original) 
   show(original) 
   show(blurred) 
   """ 
    target = copy(image) 
   
    for y in range(1, get_height(image) - 1): 
        for x in range(1, get_width(image) - 1): 
          
            sum_red = 0 
            sum_green = 0 
            sum_blue = 0 

            for m in range (y-1,y+2): 
                for n in range(x-1,x+2): 
               
                    color_inside = get_color(image, n , m) 
                new_red, new_green, new_blue = color_inside 

                sum_red = sum_red + new_red 
                sum_green = sum_green + new_green 
                sum_blue = sum_blue + new_blue 
               
                final_red = sum_red//9 
                final_green = sum_green//9 
                final_blue = sum_blue//9 
               
                new_color = create_color(final_red , final_green , final_blue) 
                set_color(target , x , y , new_color) 

                show(target)   
def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    
    for y in range(1, get_height(image)-1):  
        for x in range(1,  get_width(image)-1):

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def test_blur():
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)
    
    
def make_very_blurry(number_of_blurs):
    image = load_image(choose_file())
    
    for i in range(number_of_blurs):
        image = blur(image) 

    show(image)  
    
