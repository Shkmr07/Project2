from sketchpy import  canvas
obj = canvas.sketch_from_image("tree.jpg")
obj.draw(threshold=127)