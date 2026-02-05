# Syntax

# class class_name:
#     def __init__(self,p1,p2):
#         self.p1 = p1
#         self.p2 = p2
       
   
#     def method_name(self):
#         #Implementation of the method


# Object_name=class_name(p1,p2)
# object_name.method_name(self)



# Class and object
class Instagram:
    def __init__(self,title, description):  
        self.title = title
        self.description = description
        self.likes = 0
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1


reel1=Instagram("dancing","dancing with friends")
# 0
reel1.disliked() #0
reel1.liked() #1


reel2=Instagram("finance minister conference","finance minister conference with friends")
reel1.liked() #2
# 0
reel2.liked() #1
reel1.disliked() #1
reel1.display_likes()
reel2.display_likes()

print(id(reel1))
print(id(reel2))
