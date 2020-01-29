class Image(object):
    """Image"""

    def __init__(self, img_id, orientation, num_of_tags, tags):
        super(Image, self).__init__()
        self.img_id = img_id
        self.orientation = orientation
        self.num_of_tags = num_of_tags
        self.tags = set(tags)

    def imprimir(self):
        print(self.orientation)
        print(self.num_of_tags)
        print(self.tags)

class Slide(object):
    """A slide containing one horizontal or vertical image or 2 vertical images"""

    def __init__(self, content, tags):
        super(Slide, self).__init__()
        self.content = content # a list with the image or images contained
        self.tags = tags

    def typesinfo(self):
        print(str(type(self.content)) + " of " + str(type(self.content[0])))
        print(type(self.tags))

    def show_img_id(self):
        img_num = len(self.content)
        if img_num == 1:
            return str(self.content[0])
        elif img_num == 2:
            return str(self.content[0]) + " and image " + str(self.content[1])

    def showSlide(self):
        img_num = len(self.content)
        if img_num == 1:
            print("This slide contains image:\n {0}".format(self.content[0]))
        elif img_num == 2:
            print("This slide contains images:\n {0} \n and \n {1}".format(self.content[0], self.content[1]))
        else:
            print("This slide is empty")
        print("The tags contained in it are:")
        for tag in self.tags:
            print(tag, end=" ")
        print()




def createShow(images):
    """It creates the SlideShow"""
    slides = []
    verticals = []

    for img in images: # horizontal images are always going to be in separate slides
        if img.orientation == "H":
            slides.append(Slide([img.img_id], img.tags))
        else:
            verticals.append(img)

    # Meanwhile, vertical images are the ones that can increase the points a lot
    # so it is important to give coherence to the agrupation or group 2 images
    # that have nothing to do with each other in order to get the minimum loss
    # when changing the topic of the images because 2 images in the same slide
    # having no common tags are not penalized

def ShowValue(slides):
    """Function that given a SlideShow returns the points that it would get"""
    points = 0
    if len(slides) >= 2:
        i = 0
        while i < len(slides)-1:
            common_tags = len(slides[i].tags.intersection(slides[i+1].tags))
            in_S1_not_in_S2 = len(slides[i].tags - slides[i+1].tags)
            in_S2_not_in_S1 = len(slides[i+1].tags - slides[i].tags)
            points += sorted([common_tags, in_S1_not_in_S2, in_S2_not_in_S1])[0]
            i += 1
    return(points)

N = int(input())
images = []

for i in range(N):
    orientation, num_of_tags, *tags = input().split(" ") # input interpreta todo como un string, así que lo divido en una lista unterpretando que cada elemento se separa con un espacio
    images.append(Image(i, orientation, num_of_tags, tags))

slides = []
verticals = []

for img in images:
    if img.orientation == "H":
        slides.append(Slide([img.img_id], img.tags))
    else:
        verticals.append(img)

i = 0
while i < len(verticals):
    if i+1 < len(verticals):
        slides.append(Slide([verticals[i].img_id, verticals[i+1].img_id], verticals[i].tags.union(verticals[i+1].tags)))
        i += 2
    else:
        slides.append(Slide([verticals[i].img_id], verticals[i].tags))
        i += 1

for slide in slides:
    # slide.typesinfo()
    slide.showSlide()

show1 = ShowValue(slides)
print("The value of the show is: {0}".format(show1))
# for image in images:
#     image.imprimir()


# 4
# H 3 cat beach sun
# V 2 selfie smile
# V 2 garden selfie
# H 2 garden cat